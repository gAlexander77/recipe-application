from flask import Blueprint, current_app
import os

def save_file(files, user):
    
    file = files.get("upload")

    if file is None or file.filename == '':
        return "default.jpg"

    filename = os.path.join(user, file.filename)
    with current_app.app_context():
        file.save(os.path.join(current_app.config["UPLOADS"], filename))
    
    return filename

from api.routes import users, account, recipes

views = Blueprint("api", __name__, url_prefix="/api")

for route in [users, account, recipes]:
    views.register_blueprint(route.views)
