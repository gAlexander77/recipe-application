from flask import Blueprint, request, redirect, session
from api.routes import json
from api import models
from api import db

views = Blueprint("account", __name__, url_prefix="/account")

@views.route("/")
def index():

    if "id" not in session:
        return redirect("/login")

    database = db.load()

    user, error = models.users.select(database, rowid=session["id"])
    if error:
        return json.exception(error)

    recipes, error = models.recipes.query(database, userid=user["rowid"])
    if error:
        return json.exception(error)

    ratings, error = models.ratings.query(database, userid=user["rowid"])
    if error:
        return json.exception(error)

    comments, error = models.comments.query(database, userid=user["rowid"])
    if error:
        return json.exception(error)

    clear_userids = lambda row: dict(filter(lambda i: i[0] != "userid", row.items()))

    del user["password"]
    user["recipes"] = list(map(clear_userids, recipes))
    user["ratings"] = ratings
    user["comments"] = comments

    return json.ok(user)


@views.route("/login", methods=["POST"])
def login():

    if "id" in session:
        return redirect('/')

    username = request.form.get("username")
    password = request.form.get("password")
    if username is None and password is None:
        return json.exception("username and password required")

    user, error = models.users.select(db.load(), username=username)
    if error:
        return json.exception(error)
    
    if user["password"] == models.md5sum(password):
        session["id"] = user["rowid"]
        return json.ok(dict(session))

    return json.exception("invalid password")


@views.route("/logout", methods=["POST"])
def logout():
    if "id" in session:
        return json.ok(session.pop("id"))
    return redirect('/login')
