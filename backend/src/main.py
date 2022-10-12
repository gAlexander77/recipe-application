import sys; sys.path.append("./src")

from flask import Flask, g
from api import views


app = Flask(__name__)
with app.app_context():
    app.register_blueprint(views, url_prefix="/api")


# closing each database object after the connection closes
@app.teardown_appcontext
def close_connection(exception):
    if (db := getattr(g, "_db", None)) is not None:
        db.close()
