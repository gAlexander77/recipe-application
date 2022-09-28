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
def insert(db: sqlite3.Connection, table: str, fields: dict) -> dict:
    
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
        return {"ok": False, "error": str(error)}
    return {"ok": True, "data": str(uuid)}


# insert a user row into the database
def insert_user(db: sqlite3.Connection, username: str, password: str) -> dict:
    try:
        if len(username) < 3:
            return {"ok": False, "error": "username must be > 3 characters"}
        # attempt to load a dict with the required values
        fields: dict = { "username": username,
            "password": sha256(password.encode("utf-8")).digest().hex() }
        return insert(db, "users", fields) # try inserting
    except Exception as error:
        return {"ok": False, "error": str(error)}


# temporary function, will most likely change
# what do you think works best? I might add a filter parameter
# to this function, or have a specific funciton for querying a specific
# user
def select_users(db: sqlite3.Connection) -> dict:
    return dict(db.execute("select id, username from users"))

# TODO: insert function wrapper for recipies
