from flask import Blueprint, request, redirect, session
from api.routes import json
from api import models
from api import db


views = Blueprint("account", __name__, url_prefix="/account")


@views.route("/")
def index():

    if "id" not in session:
        return redirect("/login")

    rowid = session["id"]
    database = db.load()

    user, error = models.users.select(database, rowid)
    if error:
        return json.exception(error)

    recipes, recipes_error = models.recipes.query(database, userid=rowid)
    if error:
        return json.exception(error)

    ratings, ratings_error = models.ratings.from_user(database, rowid)
    if error:
        return json.exception(error)

    comments, comments_error = models.comments.from_user(database, rowid)
    if error:
        return json.exception(error)

    clear_userids = lambda row: dict(filter(lambda i: i[0] != "userid", row.items()))

    del user["password"]
    user["recipes"] = recipes_error or list(map(clear_userids, recipes))
    user["ratings"] = ratings_error or ratings
    user["comments"] = comments_error or comments

    return json.ok(user)


@views.route("/login", methods=["POST"])
def login():

    if "id" in session:
        return redirect('/')

    username = request.form.get("username")
    password = request.form.get("password")
    if username is None and password is None:
        return json.exception("username and password required")

    user, error = models.users.select_by_username(db.load(), username)
    if error:
        return json.exception(error)
    
    if user["password"] == models.md5sum(password):
        session["id"] = user["rowid"]
        return json.ok(user["rowid"], redirect="/")

    return json.exception("invalid password")


@views.route("/logout", methods=["POST"])
def logout():
    if "id" in session:
        return json.ok(session.pop("id"))
    return redirect('/login')
