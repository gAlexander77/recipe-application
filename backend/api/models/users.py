from api import models


def insert(db, username, password):
    return models.insert(db, "users", {
        "username": username,
        "password": models.md5sum(password)
    })


def delete(db, rowid):
    return models.delete(db, "users", rowid, "username")


def select(db, rowid=None, username=None):
    assert rowid is not None or username is not None
    return models.select(db, "users", {
        "rowid": rowid,
        "username": username
    })
