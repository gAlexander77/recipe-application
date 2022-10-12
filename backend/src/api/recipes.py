from flask import Blueprint, request
from .util import send, fail, params, open_database
import sql


views = Blueprint("recipes", __name__)


@views.route("/")
def index():

    username, title, rating, sort_by = params(
            request.args,
            ("username", "title", "rating", "sort") )

    recipes, error = sql.select.recipes(
            open_database(),
            username=username,
            title=title,
            rating=rating,
            sort_by=sort_by )

    return send(recipes) if not error else fail(error)


@views.route("/<id>")
def select(id):

    db = open_database()

    recipe, error = sql.select.recipe(db, id=id)
    if error:
        return fail(error)

    ingredients, error = sql.select.recipe_ingredients(db, recipe["id"])
    recipe["ingredients"] = ingredients

    return send(recipe)
