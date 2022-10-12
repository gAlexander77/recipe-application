from flask import Blueprint, request
from .util import send, fail, params, open_database
import sql


views = Blueprint("users", __name__, url_prefix="/users")


@views.route("/")
def index():

    # optional filter parameters
    username = params(request.args, ("username", ))

    # retrieve users
    users, error = sql.select.users(open_database(), username=username)

    return send(users) if not error else fail(error)


@views.route("/create", methods=["GET","POST"])
def create():

    # let frontend know what's going on
    if request.method == "GET":
        return fail("POST method required to create user")

    # not optional parameters for creating a new user where
    #  username = username
    #  password = sha256(password)
    username, password = params(
            request.get_json(force=True), 
            ("username", "password") )

    # attempt to create the user with supplied parameters
    id, error = sql.insert.user(
            open_database(),
            username=username, 
            password=password )

    return send(id) if not error else fail(error)
    

@views.route("/<id>")
def select(id):
    user, error = sql.select.user(open_database(), id=id)
    return send(user) if not error else fail(error)
