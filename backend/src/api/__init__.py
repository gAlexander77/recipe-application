from flask import Blueprint

from . import ingredients
from . import recipes
from . import users
from . import util

include = [users, recipes, ingredients]

views = Blueprint("api", __name__, url_prefix="/api")
for module in include:
    views.register_blueprint(
            module.views,
            url_prefix='/'+module.views.name )
