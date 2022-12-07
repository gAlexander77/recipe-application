def test_000_create(admin):
    response = admin.post("api/comments/create", json={
        "recipeid": 2,
        "comment": "hey there"
    })
    assert response.json["data"] == 1

def test_010_user_index(admin):
    response = admin.get("api/comments/")
    assert response.json == {
        "ok": True,
        "data": [{"id": 1, "comment": "hey there"}]
    }


def test_020_recipe_index(admin):
    response = admin.get("api/comments/2")
    assert response.json == {
        "ok": True,
        "data": [{"id": 1, "comment": "hey there", "username": "admin"}]
    }


def test_030_delete(admin):
    response = admin.post("api/comments/delete/1")
    assert response.json["data"] == "hey there"


