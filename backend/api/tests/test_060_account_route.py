def test_010_index(admin):
    response = admin.get("/api/account/")
    assert response.json["ok"] and response.json["data"]["username"] == "admin"


def test_020_login(client):
    response = client.post("/api/account/login", data={
        "username": "admin",
        "password": "admin"
    })
    print(response)
    assert response.json["ok"] and response.json["data"] == 1


def test_030_logout(admin):
    response = admin.post("/api/account/logout")
    assert response.json["ok"] and response.json["data"] == 1


