from api.models import users
from api import db


def test_010_insert(app):
    with app.app_context():
        userid, error = users.insert(db.load(), "hello", "world")
    assert error is None and userid == 4


def test_020_delete(app):
    with app.app_context():
        username, error = users.delete(db.load(), 1)
    assert error is None and username == "admin"


def test_030_select(app):
    with app.app_context():
        user, error = users.select(db.load(), 2)
    assert error is None and user["username"] == "user1"


def test_031_select_by_username(app):
    with app.app_context():
        user, error = users.select_by_username(db.load(), "admin")
    assert error is None and user["rowid"] == 1
