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
        g.db = sqlite3.connect(current_app.config["SQLITE"])
        g.db.execute("PRAGMA foreign_keys=ON")
        # change the default row type make it easier to use
        g.db.row_factory = lambda c, r: dict((c.description[i][0], v) for i, v in enumerate(r))
    return g.db # return the database, it should exist now


@click.command("initdb")
def init():
    db = load()
    path = current_app.config["SCHEMA"]
    db.execute("PRAGMA foreign_keys=OFF")
    with current_app.open_resource(path) as file:
        db.executescript(file.read().decode("utf-8"))
    click.echo(f"- created database using schema file {path}")
    db.execute("PRAGMA foreign_keys=ON")
    _, error = users.insert(db, "admin", "admin")
    if not error:
        click.echo("- created admin user")
    db.close()


# this function will close the database whenever the app context is destroyed
def free(exception): # takes optional exception
    # check if the db is in the global hash table (a.k.a. 'g'). if it is, close it
    if (db := g.pop("db", None)) is not None:
        db.close() # close the database if its not None
