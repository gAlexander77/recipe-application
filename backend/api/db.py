from flask import current_app as app
from flask import g

import sqlite3
import os


def timestamp():
    from datetime import datetime
    return int(datetime.now().timestamp())


def sha3(string):
    from hashlib import sha3_256
    return sha3_256(string.encode("utf-8")).hexdigest()


def init(db_path, schema_path):
    database = sqlite3.connect(db_path)
    with open(schema_path) as stream:
        schema = stream.read()
    if len(schema) > 0:
        database.executescript(schema)
    database.close()


def load():
    if (db := getattr(g, "_database", None)) is None:
        db = g._database = sqlite3.connect(app.config.get("DB_PATH"))
        db.row_factory = lambda c, r: dict((c.description[i][0], v) for i, v in enumerate(r))
    return db


def close(execption):
    if (db := getattr(g, "_database", None)) is not None:
        db.close()
