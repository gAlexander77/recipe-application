from flask import Blueprint, jsonify
from . import ingredients
from . import recipes
from . import users
from . import util


views = Blueprint("api", __name__, url_prefix="/api")
views.register_blueprint(ingredients.views)
views.register_blueprint(recipes.views)
views.register_blueprint(users.views)
