from api import models


def insert(db, userid, name, description, instructions, image):
    return models.insert(db, "recipes", {
        "userid": userid,
        "name": name,
        "description": description,
        "instructions": instructions,
        "image": image
    })


def delete(db, rowid):
    return models.delete(db, "recipes", rowid, "name")


def select(db, rowid):
    return models.select(db, "recipes", {"rowid": rowid})


def dump(db):
   return models.dump(db, "recipes_info")


def from_user(db, userid):
    return models.query(db, "recipes", {"userid": userid})