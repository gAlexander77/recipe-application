from api.models import success, failure
from api import db


def create(db, recipeid, name):

    try:
        db.execute("insert into ingredients (recipeid, name) values (?, ?)", 
            (recipeid, name))
        db.commit()
    except Exception as error:
        return failure(error)

    return success(f"created ingredient {name} successfully")


def delete(db, rowid):

    try:
        db.execute("delete from ingredients where rowid = ?", (rowid, ))
        db.commit()
    except Exception as error:
        return failure(error)

    return success(f"deleted ingredient where rowid = {rowid}")


def all(db, recipeid=None):

    recipe_filter = '' if recipeid is None else f" where recipes.rowid = {recipeid}"
    query = f"""select ingredients.rowid as rowid, * from ingredients
    left join recipes on ingredients.recipeid = recipes.rowid{recipe_filter}"""
    try:
        rows = db.execute(query)
    except Exception as error:
        return failure(error)

    return success( {
        "id": row["rowid"], 
        "name": row["name"] 
    } if recipeid is not None else {
        "id": row["rowid"],
        "name": row["name"],
        "recipe": {
            "id": row["recipe.rowid"],
            "name": row["recipe.name"]
        }
    } for row in rows.fetchall() )


def get(db, rowid):
    pass
