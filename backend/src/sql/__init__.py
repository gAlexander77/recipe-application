from sqlite3 import connect
from os.path import isfile
from hashlib import sha256

from . import insert
from . import select
from . import delete
from . import util

DATABASE_PATH = "./db/db.sqlite3"
DBSCHEMA_PATH = "./db/schema.sql"


def open_database(database=DATABASE_PATH, dbschema=DBSCHEMA_PATH):

    if isfile(database):
        return connect(database)

    db = connect(database)
    with open(dbschema, "rt") as file:
        db.executescript(file.read())
    db.commit()

    return db


def validate_password(db, username, password):
    try:
        user = db.execute(
                "select id, password from users where username = ?",
                (username, )).fetchone()
    except Exception as error:
        return util.db_fail(error)

    if not user:
        return util.db_fail(f"username: {username} does not exist")

    if user["password"] == sha256(password.encode("utf-8")).digest().hex():
        return util.db_pass(user["id"])
    return util.db_fail("invalid password")
