from api import models


def insert(db, userid, recipeid, comment):
    return models.insert(db, "comments", {
        "userid": userid,
        "recipeid": recipeid,
        "comment": comment
    })


def delete(db, rowid):
    return models.delete(db, "comments", rowid, "recipeid")


def select(db, rowid):
    return models.select(db, "comments", {"rowid": rowid})


def from_recipe(db, recipeid):
    return models.query(db, "recipe_comments", {"recipeid": recipeid})


def from_user(db, userid):
    return models.query(db, "user_comments", {"userid": userid})