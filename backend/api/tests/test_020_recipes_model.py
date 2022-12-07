from api import models
from api import db


def test_000_insert(app):
    with app.app_context():
        assert models.recipes.insert(db.load(), 1,
            "admins recipe",
            ["butter", "milk"], 
            "hello world","this will not work",
            "imagefile.jpg"
        ) == 3


def test_010_delete(app):
    with app.app_context():
        assert models.recipes.delete(db.load(), 2) == "goodbye world"


def test_020_select_set(app):
    with app.app_context():
        assert models.recipes.select_set(db.load(), columns="name, username") == [
            {"name": "hello world", "username": "admin"},
            {"name": "admins recipe", "username": "admin"}
        ]
