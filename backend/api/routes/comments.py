from flask import Blueprint, session, request
from api import routes, models, db


blueprint = Blueprint("comments", __name__, url_prefix="/comments")

@blueprint.route("/")
def index():
    
    if not routes.logged_in(session):
        return routes.must_log_in()

    return routes.send(models.comments.select_set(
        db.load(), 
        columns="id, recipe_username as username, comment",
        filters={"userid": session["id"]}
    ))


@blueprint.route("/<int:recipeid>")
def recipe(recipeid):
    return routes.send(models.comments.select_set(
        db.load(),
        columns="id, username, comment",
        filters={"recipeid": recipeid}
    ))


@blueprint.route("/create", methods=["POST"])
def create():

    if not routes.logged_in(session):
        routes.must_log_in()

    return routes.send(models.comments.insert(
        db.load(),
        session["id"],
        request.json["recipeid"], 
        request.json["comment"]
    ))


@blueprint.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    return routes.send(models.comments.delete(db.load(), id))
