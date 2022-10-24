from flask import Blueprint, request, session

from api.models import recipes, ingredients
from api.routes import json
from api import db


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

    user_id = session.get("id")
    if user_id is None:
        return json.exception("must be logged in to create a recipe")

    fields = request.get_json(force=True)
    values = tuple(fields.get(field) for field in ("name", "ingredients", "description", "instructions"))
    if None in values:
        return json.exception("must have name, ingredients, description, and instructions")

    name, ingredient_list, description, instructions = values
    recipe_id, error = recipes.create(database, user_id, name, description, instructions)
    if error:
        return json.exception(error)

    for ingredient in ingredient_list:
        _, error = ingredients.create(database, recipe_id, ingredient)
        if error:
            return json.exception(error)

    return json.ok(recipe_id)


@views.route("/delete/<int:rowid>", methods=["POST"])
def delete(rowid):
    name, error = recipes.delete(db.load(), rowid)
    return json.exception(error) if error else json.ok(f"deleted {name}")
