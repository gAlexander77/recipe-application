from flask import Blueprint, request
from .util import send, fail, params, open_database
import sql


views = Blueprint("users", __name__)


@views.route("/")
def index():

    username = request.args.get("username")
    users, error = sql.select.users(open_database(), username=username)

    return send(users) if not error else fail(error)


@views.route("/<id>")
def select(id):
    
    db = open_database()

    user, error = sql.select.user(db, id=id)
    if error:
        return fail(error)

    recipes, error = sql.select.recipes(db, userid=user["id"])
    user["recipes"] = recipes

    return send(user) if not error else fail(error)
