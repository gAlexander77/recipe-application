def test_010_index(client):
    response = client.get("/api/recipes/")
    print(response.json.get("data"))
    assert response.json["ok"] and response.json["data"][0]["rating"] == 4.0

def test_020_create(admin):
    response = admin.post("/api/recipes/create", data={
        "name": "test recipe 02",
        "ingredients": ["milk", "eggs", "cheese"],
        "description": "just a test recipe",
        "instructions": "go with your gut",
        "upload": (open("./README.md", 'rb'), "./README.md")
    })
    assert response.json["ok"] and response.json["data"] == 3


def test_030_delete(admin):
    response = admin.post("/api/recipes/delete/2")
    assert response.json["ok"] and response.json["data"] == "deleted other recipe"


def test_040_rate(admin):
    response = admin.post("/api/recipes/rate/1", data={"rating": 4})
    assert response.json["ok"] and response.json["data"] == 3


def test_050_comment(admin):
    response = admin.post("/api/recipes/comment/1", data={"comment": "nice job"})
    assert response.json["ok"] and response.json["data"] == 2
