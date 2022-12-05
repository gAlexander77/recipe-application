from flask import Blueprint, send_from_directory
from flask import current_app as app

import os


blueprint = Blueprint("uploads", __name__, url_prefix="/uploads")


@blueprint.route("/<path:name>")
def download(name):
    uploads_dir = os.path.join(os.getcwd(), app.config["UPLOADS_DIR"])
    return send_from_directory(uploads_dir, name)
