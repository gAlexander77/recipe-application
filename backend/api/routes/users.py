from flask.cli import with_appcontext
from flask import Blueprint, request, session
from api import routes, models, db

import click

blueprint = Blueprint("users", __name__, cli_group="users", url_prefix="/users")


@blueprint.cli.command("create")
@click.argument("username")
@click.argument("password")
@with_appcontext
def cli_create(username, password):
    print(
        "added new user:", 
        models.users.insert(db.load(), username, password)
    )


@blueprint.route("/create", methods=["POST"])
def create():
    userid = models.users.insert(
        db.load(), 
        request.form["username"], 
        request.form["password"]
    ) 
    session["id"] = userid
    return routes.send(userid, location=request.headers["Origin"])


@blueprint.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    return routes.send(models.users.delete(db.load(), id),
                       location=request.headers["Origin"])
