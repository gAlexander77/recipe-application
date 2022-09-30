import sqlite3

from uuid import uuid4
from hashlib import sha256
from os.path import isfile


DATABASE = "./db/db.sqlite3"
SCHEMA = "./db/schema.sql"


# function to initialize and create the
# database tables if needed, returning a handle
# to the database object
def load_database(database: str=DATABASE, schema: str=SCHEMA) -> sqlite3.Connection:

    # crash if theres no schema
    assert isfile(schema)

    # if the database exists already we dont
    # need to worry about creating the tables
    if isfile(database):
        return sqlite3.connect(database)

    # create a new database
    db: sqlite3.Connection = sqlite3.connect(database)
    
    # open the schema file and execute it against the database
    with open(schema, "rt") as file:
        db.executescript(file.read())
    
    db.commit() # save
    return db   # give the database to the higher scope


# insert fields into a database. will return json serializable data
def insert(db: sqlite3.Connection, table: str, fields: dict) -> tuple:
    
    # extract the keys and values from the supplied request parameters
    uuid: str = uuid4().hex
    keys: str = ', '.join(fields.keys())
    # extend the values tuple and add a unique ID to the front
    values: tuple = (uuid, *tuple(fields.values())) # * <- expands list into values

    try:
        # try inserting values at key indicies in the table
        db.execute(f"insert into {table} (id, {keys}) values {values}")
        db.commit()
    except Exception as error:
        return False, str(error)
    
    return True, uuid


# insert a user row into the database
def insert_user(db: sqlite3.Connection, username: str, password: str) -> tuple:
    try:
        if len(username) < 3:
            return False, "username must be > 3 characters"
        # attempt to load a dict with the required values
        fields: dict = { "username": username,
            "password": sha256(password.encode("utf-8")).digest().hex() }
        return insert(db, "users", fields) # try inserting
    except Exception as error:
        return False, error


# query and filter users based on username
def select_users(db: sqlite3.Connection, uuid: str=None, username: str=None) -> dict:
    users = {}
    uuid = '' if uuid is None else uuid
    username = '' if username is None else username
    try:
        user_rows = db.execute(
                "select id, username from users where username like ? and id like ?",
                ('%'+username+'%', '%'+uuid+'%', ))
        for uuid, username in user_rows.fetchall():
            recipe_rows = db.execute(
                    "select id, title, rating from recipes where user = ?",
                    (uuid, ))
            users[uuid] = {"username": username, "recipes": dict((i, {"title": t, "rating": r}) for i, t, r in recipe_rows.fetchall())}
        return True, users
    except Exception as error:
        return False, error


# function to delete user from database, requires id string
# as a path variable
def delete_user(db: sqlite3.Connection, uuid: str) -> dict:
    try:
        db.execute("delete from users where id = ?", (uuid, ))
        db.commit()
        return True
    except Exception as error:
        return False


# specific function for login
def select_user_password(db: sqlite3.Connection, username: str) -> tuple:
    try:
        row = db.execute(
                "select id, password from users where username = ?",
                (username,))
        return True, row.fetchall()[0] if len(row) > 0 else []
    except Exception as error:
        return False, error


def select_ingredients(db: sqlite3.Connection, name: str=None):
    name = '' if name is None else name
    try:
        rows = db.execute(
                "select * from ingredients where name like ?",
                ('%'+name+'%', ))
        return True, dict((i, (n, r)) for i, n, r in rows.fetchall())
    except Exception as error:
        return False, error


def select_recipes(db: sqlite3.Connection, title: str=None):
    title = '' if title is None else title
    try:
        rows = db.execute(
                "select * from recipes where title like ?",
                ('%'+title+'%', ))
        return True, dict((i, {"user": u, "title": t, "steps": s, "rating": r}) for i, u, t, s, r in rows.fetchall())
    except Exception as error:
        return False, error


def insert_ingredient(db: sqlite3.Connection, name: str):
    return insert(db, "ingredients", {"name": name, "rating": 5})

def insert_recipe_ingredient(db: sqlite3.Connection, recipe: str, ingredient: str, units: str, count: int):
    return insert(db, "recipes_ingredients", {"recipe": recipe, "ingredient": ingredient, "units": units, "count": count})

def insert_recipe(db: sqlite3.Connection, user: str, title: str, steps: str, ingredients: dict):
    
    ok, uuid = insert(db, "recipes", {
            "user": user,
            "title": title,
            "steps": steps,
            "rating": 5 # out of 10? we'll talk about it
        })

    for name, (units, count) in ingredients.items():
        
        ok, data = select_ingredients(db, name=name)
        if not ok:
            return False, data
        
        if len(data) > 0:
            ingredient = list(data.keys())[0]
        else:
            ok, ingredient = insert_ingredient(db, name)
            if not ok:
                return False, ingredient
        
        ok, error = insert_recipe_ingredient(db, uuid, ingredient, units, count)
        if not ok:
            return False, error
    return True, uuid


# returns the recipe + ingredients + authors name
def recipe_details(db: sqlite3.Connection, uuid: str):
    try:
        row = db.execute(
                "select title, steps, rating from recipes where id = ?", 
                (uuid, )).fetchone()
        if not row:
            return False, "not a valid uuid"
        title, steps, rating = row
        rows = db.execute(
                "select ingredient, name, units, count from recipes_ingredients right join ingredients on recipes_ingredients.ingredient = ingredients.id where recipes_ingredients.recipe = ?", (uuid, ))
        ingredients = dict((i, {"name": n, "units": u, "count": c}) for i, n, u, c in rows.fetchall())
    except Exception as error:
        return False, error
    return True, { "title": title, "steps:": steps, "rating": rating, "ingredients": ingredients }
