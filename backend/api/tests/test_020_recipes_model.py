from api.models import recipes
from api import db


def test_010_insert(app):
    with app.app_context():
        recipeid, error = recipes.insert(db.load(), 
            1, "hello", "world", "goodbye", "all")
    assert error is None and recipeid == 3


def test_020_delete(app):
    with app.app_context():
        name, error = recipes.delete(db.load(), 1)
    assert error is None and name == "Sandwich"


def test_030_select(app):
    with app.app_context():
        recipe, error = recipes.select(db.load(), 1)
    assert error is None and recipe["name"] == "Sandwich"


def test_040_from_user(app):
    with app.app_context():
        rows, error = recipes.from_user(db.load(), 1)
    assert error is None and len(rows) == 2 and rows[0]["rowid"] == 1


def test_050_dump(app):
    with app.app_context():
        rows, error = recipes.dump(db.load())
    assert error is None and len(rows) == 3 and rows[0]["rowid"] == 1
