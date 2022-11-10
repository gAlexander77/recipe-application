from flask import Blueprint
from api.routes import users, account, recipes


views = Blueprint("api", __name__, url_prefix="/api")


for route in [users, account, recipes]:
    views.register_blueprint(route.views)
