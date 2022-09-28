#!/usr/bin/env python3

# *** SETUP ***
# import and setup the flask runtime
from flask import Flask, g, cli, request
api = Flask(__name__)
cli.show_server_banner = lambda _, n: print(f"serving {n}...")

# import project files
import src.sql as sql
import src.log as log

# let's build our own logger so we can have more control
import logging; logging.getLogger('werkzeug').disabled = True

# almost done with setup, we just need a way for flask to handle the
# database, we need to use the 'teardown_appcontext' decorator
# to close the database after each request if needed
# https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/
@api.teardown_appcontext
def close_connection(exception):
    if (db := getattr(g, "_database", None)) is not None:
        db.close()


# *** API FUNCTIONS ***
# the @ below is called a decorator. 
# it tells the flask object 'api' to add this function as a handler 
# for when a user requests the home page. its essentially a fancy callback
@api.route('/') # by convention, API's should start with endpoint /api, we'll update this later
def index():
    log.msg("GET /")
    db = sql.load_database()
    # flask will automatically send collections as JSON
    return sql.select_users(db)


# how to handle POST request parameters, works the same with GET
@api.route('/post', methods=["POST"])
def post_user():
    log.msg("POST /post")
    db = sql.load_database()
    username = request.form.get("username")
    password = request.form.get("password")
    if username is not None and password is not None: # check to see if either one is None
        log.msg("inserted user into user table")
        return sql.insert_user(db, username, password)
    else:
        log.err("failed to insert user, username and password required")
        return {"ok": False, "error": "username and password required"}


# __main__ here lets us run the file through python3
# instead of python3 -m flask --app api run
if __name__ == "__main__": api.run()
