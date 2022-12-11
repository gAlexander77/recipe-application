from flask import Blueprint, request, session
from api import routes, models, db

blueprint = Blueprint("accounts", __name__, url_prefix="/accounts")


@blueprint.route("/")
def index():

    if not routes.logged_in(session):
        return routes.must_log_in()

    database = db.load()

    recipes = models.recipes.select_set(
        database,
        columns="id, name, ingredients, description,\
                instructions, created, image",
        filters={"userid": session["id"]}
    )

    for recipe in recipes:
        recipe["rating"] = models.ratings.avg(database, recipe["id"])

    return routes.send({
        "user": models.users.select_one(
            database,
            columns="id, username", 
            filters={"id": session["id"]}),
        "recipes": recipes
    })


@blueprint.route("/session")
def info():
    return routes.send(routes.logged_in(session))


@blueprint.route("/login", methods=["POST"])
def login():

    user = models.users.select_one(db.load(), columns="id", filters={
        "username": request.form["username"],
        "password": db.sha3(request.form["password"])
    })

    id = routes.log_in(user, session)

    return routes.send(
        id,
        ok=False if id is None else True,
        location=request.headers["Origin"]
    )


@blueprint.route("/logout", methods=["POST"])
def logout():
    return routes.send(
        session.pop("id") if "id" in session else None,
        location=request.headers["Origin"]
    )
