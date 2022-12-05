from api import routes


def test_010_create(client):
    response = client.post("api/users/create", json={
        "username": "user1",
        "password": "user1"
    })
    assert response.json["data"] == 2


def test_020_delete(client):
    response = client.post("api/users/delete/2")
    assert response.json["data"] == "user1"
