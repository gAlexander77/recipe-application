from api import models


def insert(db, username, password):
    return models.insert(db, "users", {
        "username": username,
        "password": models.md5sum(password)
    })


def delete(db, rowid):
    return models.delete(db, "users", rowid, "username")


def select(db, rowid):
    return models.select(db, "users", {"rowid": rowid})


def select_by_username(db, username):
    return models.select(db, "users", {"username": username})
