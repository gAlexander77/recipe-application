from api.models import comments
from api import db


def test_010_insert(app):
    with app.app_context():
        commentid, error = comments.insert(db.load(), 1, 2, "hello world")
    assert error is None and commentid == 2


def test_020_delete(app):
    with app.app_context():
        recipeid, error = comments.delete(db.load(), 1)
    assert error is None and recipeid == 1


def test_030_from_user(app):
    with app.app_context():
        rows, error = comments.from_user(db.load(), 2)
    assert error is None and len(rows) == 1 and rows[0]["comment"] == "nice sandwich"


def test_040_from_recipe(app):
    with app.app_context():
        rows, error = comments.from_recipe(db.load(), 1)
    assert error is None and len(rows) == 1 and rows[0]["comment"] == "nice sandwich"
