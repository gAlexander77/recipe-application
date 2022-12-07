import click

from api.db import sha3, timestamp
from api import models

def insert(db, username, password):
    return models.insert(db, "users", {
        "username": username, 
        "password": sha3(password),
        "created": timestamp()
    })


def delete(db, id):
    return models.delete(db, "users", id, "username")


def select_set(db, columns='*', filters={}):
    return models.select_set(db, "users", columns, filters)


def select_one(db, columns='*', filters={}):
    return models.select_one(db, "users", columns, filters)
