from api import models
from api.db import timestamp


def insert(db, userid, name, ingredients, description, instructions, image):
    return models.insert(db, "recipes", {
        "userid": userid,
        "name": name,
        "ingredients": '\n'.join(ingredients),
        "description": description,
        "instructions": instructions,
        "image": image,
        "created": timestamp()
    })


def delete(db, id):
    return models.delete(db, "recipes", id, "name")


def select_set(db, columns='*', filters={}):
    return models.select_set(db, "full_recipes", columns, filters)


def select_one(db, columns='*', filters={}):
    return models.select_one(db, "full_recipes", columns, filters)
