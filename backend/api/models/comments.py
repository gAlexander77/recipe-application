from api import models


def insert(db, userid, recipeid, comment):
    return models.insert(db, "comments", {
        "userid": userid,
        "recipeid": recipeid,
        "comment": comment
    })


def delete(db, rowid):
    return models.delete(db, "comments", rowid, "content")


def select(db, rowid):
    return models.select(db, "comments", {"rowid": rowid})


def query(db, userid=None, recipeid=None):
    return models.query(db, "comments", {
        "userid": userid,
        "recipeid": recipeid
    })


def dump(db):
    return models.dump(db, "comments")
