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


@app.route("/api/login", methods=["POST"])
def login():
    
    username, password = api.values(
            request.get_json(force=True), ("username", "password"))

    id, error = sql.validate_password(open_database(), username, password)

    if error:
        return api.fail(error)

    return api.send(id)


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
 
    id, title, description, rating, sort_by = api.values(
            request.args, ("id", "title", "description", "rating", "sort"))

    recipes, error = sql.select.recipes(
            open_database(), id=id, title=title, description=description, rating=rating, sort_by=sort_by)
    if error:
        return api.fail(error)

    for recipe in recipes:
        recipe["user"] = {
            "id": recipe["userid"],
            "name": recipe["username"]
        }
        del recipe["userid"]
        del recipe["username"]

    return api.send(recipes)


@app.route("/api/users")
def query_users():
 
    id, username = api.values(request.args, ("id", "username"))

    users, error = sql.select.users(open_database(), id=id, username=username)
    if error:
        return api.fail(error)

    return api.send(users)


@app.route("/api/users/<id>")
def user_details(id):

    db = open_database()

    user, error = sql.select.user(db, id=id)
    if not user:
        return api.fail("user does not exist" if not error else error)

    recipes, error = sql.select.recipes(db, user=user["id"])
    if error:
        return api.fail(error)

    user["recipes"] = recipes
    return api.send(user)


@app.route("/api/recipes/<id>")
def recipe_details(id):
    
    db = open_database()

    recipe, error = sql.select.recipe(db, id=id)
    if error:
        return api.fail(error)
    
    if not recipe:
        return api.fail("no recipe matches")

    ingredients, error = sql.select.recipe_ingredients(db, id)
    if error:
        return api.fail(error)

    recipe["ingredients"] = ingredients
    return api.send(recipe)


@app.route("/api/ingredients")
def query_ingredients():
    
    id, name = api.values(request.args, ("id", "name"))
    ingredients, error = sql.select.ingredients(
            open_database(), id=id, name=name)

    if error:
        return api.fail(error)

    return api.send(ingredients)


# D
@app.route("/api/delete/recipe/<id>", methods=["POST"])
def delete_recipe(id):
    # attempt to delete user with matching uuid
    sql.delete.recipe(open_database(), id) 
    return api.send(f"deleted {title}")
