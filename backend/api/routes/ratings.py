from flask import Blueprint, request, session
from api import routes, models, db


blueprint = Blueprint("ratings", __name__, url_prefix="/ratings")


@blueprint.route("/create", methods=["POST"])
def create():

    if not routes.logged_in(session):
        return routes.must_log_in()

    return routes.send(models.ratings.insert(
        db.load(),
        session["id"], 
        request.json["recipeid"],
        request.json["rating"]
    ))


@blueprint.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    return routes.send(models.ratings.delete(db.load(), id))
