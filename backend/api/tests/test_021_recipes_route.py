def test_010_create(client):
    client.post("/api/account/login", data={
        "username": "admin",
        "password": "admin"
    })
    response = client.post("/api/recipes/create", data={
        "name": "test recipe 02",
        "ingredients": ["milk", "eggs", "cheese"],
        "description": "just a test recipe",
        "instructions": "go with your gut"
    })
    assert response.json["ok"] and response.json["data"] == 3
