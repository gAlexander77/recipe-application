from flask import Blueprint, current_app, request, redirect, session
from api.routes import json
from api import models
from api import db

import os


views = Blueprint("recipes", __name__, url_prefix="/recipes")


@views.route("/")
def index():
    recipes, error = models.recipecards.dump(db.load())
    return json.exception(error) if error else json.ok(recipes)


@views.route("/<int:rowid>")
def get(rowid):
    return json.ok([])


@views.route("/comment/<int:rowid>", methods=["POST"])
def post_comment(rowid):

    if "id" not in session:
        return redirect("/login")

    comment = request.form.get("comment")

    if comment is None:
        return json.exception("missing comment")

    commentid, error = models.comments.insert(db.load(), 
        session["id"], rowid, comment)

    if error:
        return json.exception(error)

    return json.ok(commentid)

@views.route("/create", methods=["POST"])
def create():

    if "id" not in session:
        return redirect("/login")

    database = db.load()

    name = request.form.get("name")
    ingredients = request.form.getlist("ingredients")
    description = request.form.get("description")
    instructions = request.form.get("instructions")

    if None in (name, ingredients, description, instructions):
        return json.exception("must have the name, ingredients list, description, and instructions")

    recipeid, error = models.recipes.insert(database, session["id"], 
        name, description, instructions, "bigfile.png")
    if error:
        return json.exception(error)

    for ingredient in ingredients:
        _, error = models.ingredients.insert(database, recipeid, ingredient)
        if error:
            return json.exception(error)

    return json.ok(recipeid)


@views.route("/delete/<int:rowid>", methods=["POST"])
def delete(rowid):
    name, error = models.recipes.delete(db.load(), rowid)
    return json.exception(error) if error else json.ok(f"deleted {name}")
