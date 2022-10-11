from datetime import datetime
from hashlib import sha256
from uuid import uuid4

from .util import db_pass, db_fail


# base insert function
def insert(db, table, fields): # base insert function

    # extract the keys and values from the supplied request parameters
    uuid, keys = uuid4().hex, ', '.join(fields.keys())
    
    # extend the values tuple and add a unique ID to the front
    values = (uuid, *tuple(fields.values())) # * <- expands list into values
    inputs = ','.join(['?'] * len(values))

    try:
        # try inserting values at key indicies in the table
        db.execute(f"insert into {table} (id, {keys}) values ({inputs})", values)
        db.commit() # save changes
    except Exception as error:
        return db_fail(error, uuid)
    
    return db_pass(uuid)


# INSERT USER
# db:       database object
# username: username of new user (length must be > 3)
# password: plaintext password of new user to be hashed
def user(db, username, password):
   
    if len(username) < 3:
        return db_fail("username must be greater or equal to 3 characters")
    
    timestamp = int(datetime.now().timestamp())
    return insert(db, "users", {
        "username": username,
        "password": sha256(password.encode("utf-8")).digest().hex(),
        "created": timestamp,
        "updated": timestamp
    })


# INSERT INGREDIENT
# db:    database object
# name:  name of ingredient
def ingredient(db, name):

    if len(name) < 3:
        return db_fail("name must be greater than or equal to 3 characters")

    return insert(db, "ingredients", { "name": name.capitalize().strip() })


# INSERT RECIPE
# db:    database object
# user:  uuid of user who posted recipe
# title: title of recipe (length must be > 3)
# description: instructions for recipe
def recipe(db, user, title, description):
    
    if len(title) < 3:
        return db_fail("title must be greater than or equal to 3 characters")

    timestamp = int(datetime.now().timestamp())
    return insert(db, "recipes", {
        "user": user,
        "title": title.capitalize().strip(),
        "description": description.strip(),
        "created": timestamp,
        "updated": timestamp,
    })


# INSERT RECIPE INGREDIENT
# db:         database object
# recipe:     recipe uuid
# ingredient: ingredient uuid
# units:      what the ingredient is measured in (cups, oz, gal, etc)
# count:      how many of those units are present
def recipe_ingredient(db, recipe, ingredient, units, count):

    if not isinstance(count, (int, float)):
        try:
            count = int(count)
        except:
            count = 0

    return insert(db, "recipes_ingredients", {
        "recipe": recipe,
        "ingredient": ingredient,
        "units": units.strip(),
        "count": count
    })


def user_recipe(db, user, recipe, rating, pinned):

    if not isinstance(rating, int):
        try:
            rating = int(rating)
        except:
            rating = 0

    return insert(db, "users_recipes", {
        "user": user,
        "recipe": recipe,
        "rating": rating,
        "pinned": pinned
    })
