from flask import g, current_app
from api.models import users
import sqlite3
import click

# this function is responsible for loading the database into the current app context if
# it does not currently exist. the app context will initialize and close as needed
def load():
    # checking to see if the key "db" exists in the global hash table for flask (a.k.a. 'g')
    if "db" not in g:
        # this line is responsible for opening the database file and loading it into memory
        g.db = sqlite3.connect(
                current_app.config["SQLITE"],
                detect_types=sqlite3.PARSE_DECLTYPES)
        # change the default row type make it easier to use
        g.db.execute("PRAGMA foreign_keys=ON")
        g.db.row_factory = sqlite3.Row
    return g.db # return the database, it should exist now


@click.command("initdb")
def init():
    db = load()
    path = current_app.config["SCHEMA"]
    with current_app.open_resource(path) as file:
        db.executescript(file.read().decode("utf-8"))
    users.create(db, "admin", "admin")
    click.echo(f"- created database using schema file {path}")


# this function will close the database whenever the app context is destroyed
def free(exception): # takes optional exception
    # check if the db is in the global hash table (a.k.a. 'g'). if it is, close it
    if (db := g.pop("db", None)) is not None:
        db.close() # close the database if its not None
