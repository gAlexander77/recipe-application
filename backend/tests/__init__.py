import sqlite3

def create_db():
    db = sqlite3.connect(":memory:")
    with open("db/schema.sql", "rt") as file:
        db.executescript(file.read())
    db.row_factory = sqlite3.Row
    return db
