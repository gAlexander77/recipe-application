from flask import Blueprint, request
from api.models import users
from api.routes import json
from api import db


views = Blueprint("users", __name__, url_prefix="/users")


@views.route("/")
def index():
    rows, error = users.all(db.load())
    return json.exception(error) if error else json.ok(rows)


@views.route("/<int:rowid>")
def query(rowid):
    user, error = users.get(db.load(), rowid)
    return json.exception(error) if error else json.ok(user)


@views.route("/create", methods=["POST"])
def create():
    
    fields = request.form
    values = [fields.get(field) for field in ("username", "password")]
    if None in values:
        return json.exception("username and password required")

    username, password = values
    result, error = users.create(db.load(), username, password)
    return json.exception(error) if error else json.ok(result)


@views.route("/delete/<int:rowid>", methods=["POST"])
def delete(rowid):
    username, error = users.delete(db.load(), rowid)
    return json.exception(error) if error else json.ok(f"deleted {username}")
