from api import models, db


def test_000_insert(app):
    with app.app_context():
        assert models.comments.insert(db.load(), 1, 1, "hello") == 1


def test_010_delete(app):
    with app.app_context():
        assert models.comments.delete(db.load(), 1) == "hello"
