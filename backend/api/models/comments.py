from api import models


def insert(db, userid, recipeid, comment):
    return models.insert(db, "comments", {
        "userid": userid,
        "recipeid": recipeid,
        "comment": comment
    })


def delete(db, id):
    return models.delete(db, "comments", id, "comment")


def select_set(db, columns='*', filters={}):
    return models.select_set(db, "full_comments", columns, filters)


def select_one(db, columns='*', filters={}):
    return models.select_one(db, "full_comments", columns, filters)
