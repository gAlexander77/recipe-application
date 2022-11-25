import pytest
import os

from api import db, create_app, PROC_ROOTDIR


@pytest.fixture
def app():

    testdb_path = os.path.join(PROC_ROOTDIR, "db/test_db.sqlite3")

    app = create_app()
    app.config["SQLITE"] = testdb_path

    with app.app_context():
        db.init()
        d = db.load()
        with open("./api/tests/sample.sql", "rt") as file:
            d.executescript(file.read())
        d.close()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
