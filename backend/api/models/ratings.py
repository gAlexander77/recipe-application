from api import models


def insert(db, userid, recipeid, value):
    return models.insert(db, "ratings", {
        "userid": userid,
        "recipeid": recipeid,
        "value": float(value)
    })


def delete(db, rowid):
    return models.delete(db, "ratings", rowid, "content")


def select(db, rowid):
    return models.select(db, "ratings", {"rowid": rowid})


def query(db, userid=None, recipeid=None, value=None):
    assert userid is not None or recipeid is not None
    return models.query(db, "ratings", {
        "userid": userid,
        "recipeid": recipeid,
        "value": value
    })


def dump(db):
    return models.dump(db, "ratings")
