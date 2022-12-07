from api import routes


def test_000_login(client):
    response = client.post("api/accounts/login", json={
        "username": "admin",
        "password": "admin"
    })
    assert response.json["data"] == 1


def test_010_index(client):
    response = client.get("api/accounts/")
    assert response.json["data"]["user"]["id"] == 1
    assert len(response.json["data"]["recipes"]) == 2


def test_030_logout(client):
    response = client.post("api/accounts/logout")
    assert response.json["data"] == 1
