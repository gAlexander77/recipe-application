from flask import Blueprint
from api.routes import auth, users, recipes


views = Blueprint("api", __name__, url_prefix="/api")


for route in [auth, users, recipes]:
    views.register_blueprint(route.views)
