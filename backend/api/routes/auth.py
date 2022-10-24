from flask import Blueprint, request, session
from api.models import users
from api.routes import json
from api import db


views = Blueprint("auth", __name__, url_prefix="/auth")


@views.route("/")
def index():
    if "id" in session:
        user, error = users.get(db.load(), rowid=session["id"])
        if error:
            return json.exception(error)
        return json.ok(user)
    return json.ok("not logged in")


@views.route("/login", methods=["POST"])
def login():
    if "id" in session:
        return json.exception("already logged in")

    fields = request.get_json(force=True)
    values = tuple(fields.get(field) for field in ("username", "password"))
    if None in values:
        return json.exception("username and password required")

    username, password = values
    user, error = users.get(db.load(), username=username)
    if error:
        return json.exception(error)

    if user["password"] == users.md5sum(password):
        session["id"] = user["id"]
        return json.ok("logged in successfully")

    return json.exception("password does not match")


@views.route("/logout")
def logout():
    if "id" in session:
        return json.ok(session.pop("id"))
    return json.exception("not logged in")
