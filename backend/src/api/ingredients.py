from flask import Blueprint, request
from .util import send, fail, params, open_database
import sql


views = Blueprint("ingredients", __name__)


@views.route("/")
def index():

    name = request.args.get("name")
    ingredients, error = sql.select.ingredients(open_database(), name=name)

    return send(ingredients) if not error else fail(error)


@views.route("/<id>")
def select(id):

    db = open_database()

    ingredient, error = sql.select.ingredient(db, id=id)
    if error:
        return fail(error)

    recipes, error = sql.select.ingredient_recipes(db, id)
    ingredient["recipes"] = recipes

    return send(ingredient) if not error else fail(ingredient)
