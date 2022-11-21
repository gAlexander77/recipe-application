def test_010_login(client):
    response = client.post("/api/account/login", data={
        "username": "admin",
        "password": "admin"
    })
    assert response.json["ok"] and response.json["data"] == 1

def test_020_logout(client):
    client.post("/api/account/login", data={
        "username": "admin",
        "password": "admin"
    })
    response = client.post("/api/account/logout")
    assert response.json["ok"] and response.json["data"] == 1
