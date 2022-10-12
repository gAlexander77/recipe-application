from flask import Blueprint, request
from .util import send, fail, open_database, params
import sql


views = Blueprint("recipes", __name__, url_prefix="/recipes")


@views.route("/")
def index():

    # optional filter paramters
    username, title, rating, = params(
            request.args
            ("id", "username", "title", "rating") )

    # 
    recipes, error = sql.select.recipes(
            open_database(),
            id=id, 
            username=username,
            title=title,
            rating=rating )
