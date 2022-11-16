import json


def test_recipes(client):
    response = client.get("/api/recipes/")
    assert json.loads(response.text).get("ok")
