from api import models


def insert(db, recipeid, name):
    return models.insert(db, "ingredients", {
        "recipeid": recipeid,
        "name": name
    })


def from_recipe(db, recipeid):
    return models.query(db, "ingredients", {"recipeid": recipeid})
