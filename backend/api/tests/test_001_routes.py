from api import routes


def test_000_handle_404_error(client):
    response = client.get("/does/not/exist")
    assert response.json["data"].startswith("404")
