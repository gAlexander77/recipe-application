from flask import Blueprint, jsonify, redirect


def send(data, ok=True, location=None):
    if location is not None:
        return redirect(location)
    return jsonify({"ok": ok, "data": data})


def log_in(user, session):
    if user is None:
        return None
    session["id"] = user["id"]
    session["logged_in"] = True
    return session["id"]


def logged_in(session):
    return session.get("id") and session.get("logged_in")


def must_log_in():
    return send("must log in", ok=False)


blueprint = Blueprint("api", __name__, url_prefix="/api")


from api.routes import accounts, comments, ratings, recipes, users
for route in [accounts, comments, ratings, recipes, users]:
    blueprint.register_blueprint(route.blueprint)
