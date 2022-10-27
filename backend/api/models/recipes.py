from api.models import ingredients, success, failure


def create(db, userid, name, description, instructions, image):
    try:
        row = db.execute(
            """insert into recipes 
            (userid, name, description, instructions, image) 
            values (?, ?, ?, ?, ?)
            returning rowid""",
            (userid, name, description, instructions, image)).fetchone()
        db.commit()
    except Exception as error:
        return failure(str(error))

    return success(row["rowid"])


def delete(db, rowid):
    try:
        row = db.execute(
                "delete from recipes where rowid = ? returning name", 
                (rowid, )).fetchone()
        if row is None:
            return failure("rowid does not exist")
        db.commit()
    except Exception as error:
        return failure(str(error))

    return success(row["name"])


def get(db, rowid):

    try:
        row = db.execute("""select recipes.rowid as rowid, * from recipes 
            left join users on recipes.userid = users.rowid 
            where recipes.rowid = ?""", (rowid, ))
    except Exception as error:
        return failure(str(error))

    recipe = row.fetchone()
    if not recipe:
        return failure("recipe not found")

    ingredients_list, error = ingredients.all(db, recipeid=recipe["rowid"])
    if error:
        return failure(str(error))

    return success({
        "id": recipe["rowid"],
        "name": recipe["name"],
        "description": recipe["description"],
        "ingredients": list(ingredients_list),
        "instructions": recipe["instructions"],
        "image": recipe["image"],
        "user": {
            "id": recipe["userid"],
            "username": recipe["username"]
        }
    })


def all(db):

    try:
        rows = db.execute("""select recipes.rowid, * from recipes left join users on 
            recipes.userid = users.rowid""")
    except Exception as error:
        return failure(str(error))

    return success([ {
        "id": row["rowid"],
        "name": row["name"],
        "description": row["description"],
        "instructions": row["instructions"],
        "image": row["image"],
        "user": {
            "id": row["userid"],
            "username": row["username"]
        }
    } for row in rows.fetchall() ])
