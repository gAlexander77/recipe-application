from flask import g, current_app
from api.models import users
import sqlite3
import click
import os

# this function is responsible for loading the database into the current app context if
# it does not currently exist. the app context will initialize and close as needed
def load(path=None):
    if path is None:
        path = current_app.config["SQLITE"]
    # checking to see if the key "db" exists in the global hash table for flask (a.k.a. 'g')
    if "db" not in g:
        # this line is responsible for opening the database file and loading it into memory
        db = sqlite3.connect(path)
        db.execute("PRAGMA foreign_keys=ON")
        # change the default row type make it easier to use
        db.row_factory = lambda c, r: dict((c.description[i][0], v) for i, v in enumerate(r))
        g.db = db
        return db # return the database, it should exist now
    return sqlite3.connect(path)


def init(path=None):
    
    if path is None:
        path = current_app.config["SQLITE"]

    db = load(path=path)
    schema = current_app.config["SCHEMA"]
    
    db.execute("PRAGMA foreign_keys=OFF")
    with current_app.open_resource(schema) as file:
        db.executescript(file.read().decode("utf-8"))
    
    click.echo(f"- created database @ {os.path.basename(path)}")
    click.echo(f"- created using schema @ {os.path.basename(schema)}")
    
    db.execute("PRAGMA foreign_keys=ON")
    
    _, error = users.insert(db, "admin", "admin")
    if not error:
        click.echo("- created admin user")
    
    db.close()


@click.command("initdb")
def initdb():
    init()


# this function will close the database whenever the app context is destroyed
def free(exception): # takes optional exception
    # check if the db is in the global hash table (a.k.a. 'g'). if it is, close it
    if (db := g.pop("db", None)) is not None:
        db.close() # close the database if its not None
