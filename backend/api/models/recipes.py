def create(db, userid, name, description, instructions, image):
    from api.models import insert
    return insert(db, "recipes", {
        "userid": userid,
        "name": name,
        "description": description,
        "instructions": instructions,
        "image": image
    })


def delete(db, rowid):
    from api.models import delete
    return delete(db, "recipes", rowid, "name")
