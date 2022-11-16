import pytest

from api import create_app


@pytest.fixture()
def app():
    yield create_app()

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
