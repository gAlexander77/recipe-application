from api.models import ingredients
from api import db


def test_010_insert(app):
    with app.app_context():
        ingredientid, error = ingredients.insert(db.load(), 1, "zuccini")
    assert error is None and ingredientid == 4


def test_020_from_recipe(app):
    with app.app_context():
        rows, error = ingredients.from_recipe(db.load(), 1)
    assert error is None and len(rows) == 4 and rows[0]["name"] == "bread"
