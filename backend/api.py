#!/usr/bin/env python3

# *** SETUP ***
# import and setup the flask runtime
# dont worry about anything up here until
# after all setup is done, i can explain better in
# person i think
from flask import Flask, g, cli, request
api = Flask(__name__)
cli.show_server_banner = lambda _, n: print(f"serving {n}...")

# import project files
import src.sql as sql
import src.log as log

# let's build our own logger so we can have more control
import logging; logging.getLogger('werkzeug').disabled = True

# wrapper function to add database to flask globals
def get_db() -> sql.sqlite3.Connection:
    if (db := getattr(g, "_database", None)) is None:
        db = g._database = sql.load_database()
    return db

# almost done with setup, we just need a way for flask to handle the
# database, we need to use the 'teardown_appcontext' decorator
# to close the database after each request if needed
# https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/
@api.teardown_appcontext
def close_connection(exception: Exception):
    if (db := getattr(g, "_database", None)) is not None:
        db.close()

# now the important stuff

# first we want to create functions to handle success and error
# this is saying each api response should have a dict with at least 2 keys,
# with the first key always being 'ok', and the second being 'data'
# the first key indicates if an error was detected on the backend

# flask will automatically send collections as JSON
# use these functions as the returns of the functions below.
# they will keep the api responses consistent
def api_ok(data: any, context: str='') -> dict:
    if context:
        log.msg(context)
    return {"ok": True, "data": data}


def api_error(error: str, context: str='') -> dict:
    if context:
        log.err(context)
    return {"ok": False, "data": error}

# *** API FUNCTIONS ***
# the @ below is called a decorator. 
# it tells the flask object 'api' to add this function as a handler 
# for when a user requests the home page. its essentially a fancy callback
@api.route("/api") # here is a simple example
def index():
    return api_ok("this is the index page", "GET / 200")


# heres a simple example of how to use the database
@api.route("/api/users")
def users():

    uuid = request.args.get("uuid")
    username = request.args.get("username")

    # this function gets all the users
    # there will be several more database functions 
    # documented as the project grows
    ok, data = sql.select_users(get_db(), uuid=uuid, username=username)

    # if the database ran into an error, tell the frontend
    if not ok:
        return api_error(str(data), f"database error {str(data)}")
    
    # otherwise, return as successful
    return api_ok(data, f"GET /users: {uuid or username} 200")


@api.route("/api/users/create", methods=["POST"])
def create_user():
    
    username = request.json.get("username")
    password = request.json.get("password")
    
    if username is None or password is None:
        return api_error("username and password required", "POST /api/users/create 401")
    
    ok, data = sql.insert_user(get_db(), username, password)
    
    if not ok:
        return api_error(str(data), f"database error {str(data)}")

    return api_ok(data, f"POST /users/create 200 - created user: {username}")


@api.route("/api/users/delete/<uuid>", methods=["POST"])
def delete_user(uuid: str):
    if not sql.delete_user(get_db(), uuid):
        return api_error(f"could not delete user with id: {uuid}", f"warn: error deleting {uuid}")
    return api_ok(f"user id: {uuid} deleted", f"user id: {uuid} deleted")


@api.route("/api/users/login", methods=["POST"])
def login_user():

    username = request.json.get("username")
    password = request.json.get("password")

    if username is None or password is None:
        return api_error("username and password required", "POST /api/users/login 401")

    ok, data = sql.select_user_password(get_db(), username)
    if not ok or len(data) != 2:
        return api_error(str(data), f"database error {str(data)}")

    uuid, hashword = data
    if hashword == sql.sha256(password.encode("utf-8")).digest().hex():
        return api_ok(uuid, "POST /users/login 200 - %s logged in successfully" % username)

    return api_error("passwords do not match", "warn: unsuccessful login attempt from %s" % username)


@api.route("/api/recipes")
def recipes():

    title = request.args.get("title")

    ok, data = sql.select_recipes(get_db(), title=title)
    if not ok:
        return api_error(str(data))

    return api_ok(data)


@api.route("/api/recipes/create", methods=["POST"])
def create_recipe():
    
    user = request.json.get("user")
    title = request.json.get("title")
    steps = request.json.get("steps")
    ingredients = request.json.get("ingredients")
    
    ok, data = sql.insert_recipe(get_db(), user, title, steps, ingredients)
    if not ok:
        return api_error(str(data))

    return api_ok(data)

@api.route("/api/recipes/select/<uuid>")
def select_recipe(uuid: str):

    ok, data = sql.recipe_details(get_db(), uuid)
    if not ok:
        return api_error(str(data))

    return api_ok(data)


# __main__ here lets us run the file through python3
# instead of python3 -m flask --app api run
if __name__ == "__main__": api.run()
