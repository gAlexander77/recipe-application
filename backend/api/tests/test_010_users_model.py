from api.models import users
from api import db


def test_010_user_insert(app):
    with app.app_context():
        userid, error = users.insert(db.load(), "hello", "world")
    assert error is None and userid == 3


def test_020_user_delete(app):
    with app.app_context():
        username, error = users.delete(db.load(), 1)
    assert error is None and username == "admin"


def test_030_user_select_by_rowid(app):
    with app.app_context():
        user, error = users.select(db.load(), rowid=2)
    assert error is None and user["username"] == "username"


def test_031_user_select_by_username(app):
    with app.app_context():
        user, error = users.select(db.load(), username="admin")
    assert error is None and user["rowid"] == 1
