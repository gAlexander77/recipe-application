from flask import Blueprint, request, session
from api import routes, models, db


blueprint = Blueprint("ratings", __name__, url_prefix="/ratings")


@blueprint.route("/create", methods=["POST"])
def create():

    if not routes.logged_in(session):
        return routes.must_log_in()

    database = db.load()
    userid = session["id"]
    recipeid = request.json["recipeid"]
    rating = request.json["rating"]

    if models.ratings.exists(database, userid, recipeid):
        return routes.send(models.ratings.update(
            database, userid, recipeid, rating))

    return routes.send(models.ratings.insert(
        database, userid, recipeid, rating))


@blueprint.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    return routes.send(models.ratings.delete(db.load(), id))
