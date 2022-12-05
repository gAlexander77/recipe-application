from flask import Flask
from werkzeug.exceptions import HTTPException

from api import uploads, routes, db

import secrets
import click
import json
import os

CONF_PATH = os.path.join(os.getcwd(), "etc/config.json")


def create_app():

    app = Flask(__name__)
    app.config.from_file(CONF_PATH, load=json.load)
    app.secret_key = secrets.token_hex()
    db_path, schema_path, uploads_dir = (app.config["DB_PATH"], 
                                         app.config["SCHEMA_PATH"],
                                         app.config["UPLOADS_DIR"])
    
    if not os.path.isfile(schema_path):
        raise FileNotFoundError("schema file not found")

    if app.config["SERVE_UPLOADS"]: 
        print("+ serving uploads from flask")
        app.register_blueprint(uploads.blueprint)
    
    if not os.path.isdir(uploads_dir):
        print(f"+ created uploads directory {uploads_dir}")
        os.makedirs(uploads_dir)

    if not os.path.isfile(db_path):
        db_dir = os.path.dirname(db_path)
        if not os.path.isdir(db_dir):
            print("+ creating directory for database")
            os.makedirs(db_dir)
        print(f"+ initializing database {db_path}")
        db.init(db_path, schema_path)

    app.register_blueprint(routes.blueprint)
    app.teardown_appcontext(db.close)
    
    @click.command("initdb")
    def initdb():
        print("+ initializing database for you")
        os.remove(db_path)
        db.init(db_path, schema_path)

    @app.errorhandler(HTTPException)
    def http_exception(exception):
        response = exception.get_response()
        response.data = json.dumps({
            "ok": False, 
            "data": f"{exception.code} - {exception.name}"
        })
        response.content_type = "application/json"
        return routes.cors(response)

    return app
