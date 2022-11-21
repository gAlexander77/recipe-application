def test_010_create(client):
    response = client.post("/api/users/create", data={
        "username": "user3",
        "password": "s3cr3t"
    })
    assert response.json["ok"] and response.json["data"] == 4

def test_020_delete(client):
    response = client.post("/api/users/delete/2")
    assert response.json["ok"] and response.json["data"] == "user1"
