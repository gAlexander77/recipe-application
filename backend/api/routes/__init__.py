from flask import Blueprint, jsonify


def cors(response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    return response


def send(data, ok=True):
    return cors(jsonify({"ok": ok, "data": data}))


def logged_in(session):
    return "id" in session


def must_log_in():
    return send("must log in", ok=False)


blueprint = Blueprint("api", __name__, url_prefix="/api")


from api.routes import accounts, comments, ratings, recipes, users
for route in [accounts, comments, ratings, recipes, users]:
    blueprint.register_blueprint(route.blueprint)
