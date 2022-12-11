from flask import Blueprint, request, session
from flask import current_app as app
from api import routes, models, db

import secrets
import os

blueprint = Blueprint("recipes", __name__, url_prefix="/recipes")


@blueprint.route("/")
def index():

    database = db.load() 
    recipes = models.recipes.select_set(
        database,
        columns="id, name, username, description, ingredients,\
                instructions, created, image"
    )

    for recipe in recipes:
        recipe["ingredients"] = recipe["ingredients"].strip().split('\n')
        recipe["rating"] = models.ratings.avg(database, recipe["id"])

    return routes.send(recipes)


@blueprint.route("/<int:id>")
def recipe(id):

    database = db.load()
    recipe = models.recipes.select_one(
        database,
        columns="id, name, username, description, ingredients,\
                instructions, created, image",
        filters={"id": id}
    )

    recipe["ingredients"] = recipe["ingredients"].strip().split('\n')
    recipe["rating"] = models.ratings.avg(database, recipe["id"])

    return routes.send(recipe)


@blueprint.route("/create", methods=["POST"])
def create():

    if not routes.logged_in(session):
        return routes.must_log_in()

    uploaded = request.files["upload"]

    _, ext = uploaded.filename.rsplit('.', 1)
    imagepath = os.path.join(
        app.config["UPLOADS_DIR"], 
        secrets.token_hex()
    ) + '.' + ext

    uploaded.save(imagepath)

    return routes.send(models.recipes.insert(
        db.load(), 
        session["id"], 
        request.form["name"], 
        request.form["ingredients"].split(','), 
        request.form["description"], 
        request.form["instructions"],
        imagepath
    ))


@blueprint.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    return routes.send(models.recipes.delete(db.load(), id))
