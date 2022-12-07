def test_000_create(admin):
    response = admin.post("api/ratings/create", json={
        "recipeid": 2,
        "rating": 2
    })
    assert response.json["data"] == 2


def test_010_delete(admin):
    response = admin.post("api/ratings/delete/2")
    assert response.json["data"] == 2
