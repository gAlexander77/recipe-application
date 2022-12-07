from api import db, create_app

import pytest
import os

TEST_DB = os.path.join(os.getcwd(), "db/tests.db")

@pytest.fixture(scope="module")
def app():

    app = create_app()
    app.config["DB_PATH"] = TEST_DB

    if os.path.isfile(TEST_DB):
        os.remove(TEST_DB)

    with app.app_context():
        db.init(TEST_DB, app.config["SCHEMA_PATH"])
        db.init(TEST_DB, os.path.join(os.getcwd(), "db/tests-samples.sql"))

    return app


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()

@pytest.fixture
def admin(client):
    client.post("api/accounts/login", json={
        "username": "admin",
        "password": "admin"
    })
    return client
