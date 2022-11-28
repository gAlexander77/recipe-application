from flask import Flask, send_from_directory

from . import routes
from . import db

import secrets
import os


PROC_ROOTDIR = os.getcwd()


def create_app():

    app = Flask(__name__)

    app.secret_key = secrets.token_bytes()
    app.config.from_mapping(
            DATABASE=os.path.join(PROC_ROOTDIR, "db"),
            UPLOADS=os.path.join(PROC_ROOTDIR, "uploads"))

    app.config["SQLITE"] = os.path.join(app.config["DATABASE"], "db.sqlite3")
    app.config["SCHEMA"] = os.path.join(app.config["DATABASE"], "schema.sql")
    
    if not os.path.isdir(app.config["DATABASE"]):
        os.mkdir(app.config["DATABASE"])
    
    if not os.path.isdir(app.config["UPLOADS"]):
        os.mkdir(app.config["UPLOADS"])

    app.cli.add_command(db.initdb)

    app.teardown_appcontext(db.free)
    app.register_blueprint(routes.views)

    return app
