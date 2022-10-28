from flask import Blueprint, current_app, request, session

from api.models import recipes, ingredients
from api.routes import json
from api import db

import os


DEFAULT_IMG = "/uploads/default.jpeg"


views = Blueprint("recipes", __name__, url_prefix="/recipes")


@views.route("/")
def index():
    rows, error = recipes.all(db.load())
    return json.exception(error) if error else json.ok(rows)


@views.route("/<int:rowid>")
def query(rowid):
    recipe, error = recipes.get(db.load(), rowid)
    return json.exception(error) if error else json.ok(recipe)


@views.route("/create", methods=["POST"])
def create():

    database = db.load()

    userid = session.get("id")
    if userid is None:
        return json.exception("must be logged in to create a recipe")

    fields = request.form
    values = tuple(fields.get(field) for field in ("name", "description", "instructions"))
    ingredient_list = fields.getlist("ingredients")
    if None in values or ingredients is None:
        return json.exception("must have name, ingredients, description, and instructions")

    image = request.files.get("image")
    path = f"{userid}/{image.filename}" if image and image.filename else DEFAULT_IMG
    if path != DEFAULT_IMG:
        upload_full = current_app.config["UPLOADS"]
        upload_base = os.path.basename(upload_full)
        syspath = os.path.join(upload_full, path)
        webpath = os.path.join(upload_base, path) 
        if not os.path.isdir(f"{upload_full}/{userid}"):
            os.makedirs(f"{upload_full}/{userid}")
        image.save(syspath)
    else:
        webpath = path
    
    name, description, instructions = values
    recipeid, error = recipes.create(
        database, userid, name, description, instructions, webpath)
    if error:
        return json.exception(error)

    for ingredient in ingredient_list:
        _, error = ingredients.create(database, recipeid, ingredient)
        if error:
            return json.exception(error)

    return json.ok(recipeid)


@views.route("/delete/<int:rowid>", methods=["POST"])
def delete(rowid):
    name, error = recipes.delete(db.load(), rowid)
    return json.exception(error) if error else json.ok(f"deleted {name}")
