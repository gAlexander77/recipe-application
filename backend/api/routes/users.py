from flask import Blueprint, request
from api.models import users
from api.routes import json
from api import db


views = Blueprint("users", __name__, url_prefix="/users")


@views.route("/create", methods=["POST"])
def create():
    
    username = request.form.get("username")
    password = request.form.get("password")
    if username is None or password is None:
        return json.exception("username and password required")

    userid, error = users.create(db.load(), username, password)
    return json.exception(error) if error else json.ok(userid)


@views.route("/delete/<int:rowid>", methods=["POST"])
def delete(rowid):
    username, error = users.delete(db.load(), rowid)
    return json.exception(error) if error else json.ok(f"deleted {username}")
