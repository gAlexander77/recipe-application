from api.models import ratings
from api import db


def test_010_insert(app):
    with app.app_context():
        ratingid, error = ratings.insert(db.load(), 1, 1, 5)
    assert error is None and ratingid == 3


def test_020_delete(app):
    with app.app_context():
        recipeid, error = ratings.delete(db.load(), 1)
    assert error is None and recipeid == 2


def test_030_from_user(app):
    with app.app_context():
        rows, error = ratings.from_user(db.load(), 1)
    assert error is None and len(rows) == 2 and rows[0]["rating"] == 5


def test_040_from_recipe(app):
    with app.app_context():
        rows, error = ratings.from_recipe(db.load(), 1)
    assert error is None and len(rows) == 2 and rows[0]["rating"] == 4


def test_041_from_recipe_avg(app):
    with app.app_context():
        assert ratings.from_recipe_avg(db.load(), 1) == 4.5
