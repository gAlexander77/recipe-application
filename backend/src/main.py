import api, sql
from flask import Flask, g, request


app = Flask(__name__)


# opening the database object
def open_database():
    if (db := getattr(g, "_db", None)) is None:
        db = g._db = sql.open_database()
    db.row_factory = sql.util.dicts
    return db


# closing the database object after the connection closes
@app.teardown_appcontext
def close_connection(exception):
    if (db := getattr(g, "_db", None)) is not None:
        db.close()


# C
@app.route("/api/create/user", methods=["POST"])
def create_user():
    
    # extract username and password from json payload
    username, password = api.values(
            request.get_json(force=True), ("username", "password"))

    # make sure user supplied both
    if not username or not password:
        return api.fail("username and password required")

    # attempt to insert
    uuid, error = sql.insert.user(open_database(), username, password)
    if error:
        return api.fail(error)

    # return the uuid
    return api.send(uuid)


@app.route("/api/create/recipe", methods=["POST"])
def create_recipe():

    user, title, steps, ingredients = api.values(
            request.get_json(force=True), ("user", "title", "steps", "ingredients"))

    if not user or not title:
        return api.fail("user id and title are required")

    if not ingredients:
        return api.fail("ingredients are required")

    db = open_database()

    recipe, error = sql.insert.recipe(db, user, title, steps, 0)
    if error:
        return api.fail(f"insert recipe error: {error}") 

    for name, (units, count) in ingredients.items():

        # adds unadded ingredient
        # TODO, turn this into a function in api.py
        ingredient, error = sql.select.ingredient(db, name=name)
        if ingredient:
            ingredient = ingredient["name"]
        if error or not ingredient:
            ingredient, error = sql.insert.ingredient(db, name)
            if error:
                sql.delete.recipe(db, recipe)
                return api.fail(f"insert ingredient error: {error}")

        _, error = sql.insert.recipe_ingredient(db, recipe, ingredient, units, count)
        if error:
            sql.delete.recipe(db, recipe)
            return api.fail(f"insert recipe ingredient error: {error}")

    return api.send(recipe)


# R
@app.route("/api/recipes")
def query_recipes():
 
    id, title, steps, rating = api.values(
            request.args, ("id", "title", "steps", "rating"))

    recipes, error = sql.select.recipes(
            open_database(), id=id, title=title, steps=steps, rating=rating)
    if error:
        return api.fail(error)

    return api.send(recipes)


# D
@app.route("/api/delete/recipe/<id>", methods=["POST"])
def delete_recipe(id):
    
    # attempt to delete user with matching uuid
    title, error = sql.delete.recipe(open_database(), id)
    if error:
        return api.fail(error)
    
    return api.send(f"deleted {title}")
