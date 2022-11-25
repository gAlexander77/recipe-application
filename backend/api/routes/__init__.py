from flask import Blueprint, current_app
import os

def save_file(files, user):
    
    file = files.get("upload")

    if file is None or file.filename == '':
        return "default.jpg"

    with current_app.app_context():
        basedir = os.path.join(current_app.config["UPLOADS"], str(user))
        if not os.path.isdir(basedir):
            os.makedirs(basedir)
        file.save(os.path.join(basedir, file.filename))
    
    return os.path.join(str(user), file.filename)

from api.routes import users, account, recipes

views = Blueprint("api", __name__, url_prefix="/api")

for route in [users, account, recipes]:
    views.register_blueprint(route.views)
