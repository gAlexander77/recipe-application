from flask.cli import with_appcontext
from flask import Blueprint, request
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
    return routes.send(models.users.insert(
        db.load(), 
        request.json["username"], 
        request.json["password"]
    ))


@blueprint.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    return routes.send(models.users.delete(db.load(), id))
