from api import models
from api import db


def test_000_insert(app):
    with app.app_context():
        assert models.ratings.insert(db.load(), 2, 1, 5) == 2


def test_001_insert_other(app):
    with app.app_context():
        assert models.ratings.insert(db.load(), 2, 2, 2) == 3


def test_010_delete(app):
    with app.app_context():
        assert models.ratings.delete(db.load(), 1) == 5


def test_020_avg(app):
    with app.app_context():
        assert models.ratings.avg(db.load(), 1) == 5
