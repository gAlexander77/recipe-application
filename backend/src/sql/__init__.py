from sqlite3 import connect
from os.path import isfile

from . import insert
from . import select
from . import update
from . import delete

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
