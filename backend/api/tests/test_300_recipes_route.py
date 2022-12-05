def test_000_create(admin):
    response = admin.post("api/recipes/create", data={
        "name": "test recipe",
        "ingredients": ["hello", "world"],
        "description": "hi there",
        "instructions": "first you take your leg\nand you stick it in the air\n",
        "upload": (open("requirements.txt", "rb"), "photo.jpg")
    })
    assert response.json["data"] == 3


def test_010_index(client):
    response = client.get("api/recipes/")
    assert len(response.json["data"]) == 3


def test_020_recipe(client):
    response = client.get("api/recipes/1")
    assert response.json["data"]["id"] == 1


def test_030_delete(admin):
    response = admin.post("api/recipes/delete/1")
    assert response.json["data"] == "hello world"
