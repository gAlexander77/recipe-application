from flask import Blueprint

views = Blueprint("ingredients", __name__, url_prefix="/ingredients")

@views.route("/")
def index():
    return "<center>index for ingredients</center>"
