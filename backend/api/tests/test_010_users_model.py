from api import models, db
import pytest


def test_000_insert(app):
    with app.app_context():
        assert models.users.insert(db.load(), "user", "pass") == 2


def test_010_delete(app):
    with app.app_context():
        assert models.users.delete(db.load(), '2') == "user"


def test_020_select_set(app):
    with app.app_context():
        assert models.users.select_set(db.load(), columns="id") == [{"id": 1}]


def test_030_select_one(app):
    with app.app_context():
        assert models.users.select_one(db.load(), columns="id", filters={
            "username":"admin"
        }) == {"id": 1}
