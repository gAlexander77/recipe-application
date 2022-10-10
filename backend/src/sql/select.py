from .util import valid_table, db_pass, db_fail

RECIPE_SQL = """select recipes.id, 
title, steps, rating,
recipes.created, recipes.updated, 
user as userid, username 
from recipes
left join users on recipes.user = users.id"""
INGREDIENT_SQL = "select id, name from ingredients"


def query(sql, fields, expression):
    items = filter(lambda t: t[1] is not None, fields.items())
    if items:
        return sql + " where " + " and ".join(expression % (k, v) for k, v in items)
    return sql

def select(db, sql, fields, single=False):

    expression =  "%s = %s" if single else "%s like '%%%s%%'"
    sql = query(sql, fields, expression)

    try:
        rows = db.execute(sql)
    except Exception as error:
        return db_fail(error)

    return db_pass(rows.fetchone() if single else rows.fetchall())


# if user only wants one, only let them use the unique columns
def recipe(db, id=None, title=None, user=None):
    if id is not None or name is not None or user is not None:
        return select(db, RECIPE_SQL, {
            "id": id, 
            "title": title, 
            "user": user 
        }, single=True)
    return db_fail("id or title or user required")


def recipes(db, id=None, title=None, steps=None, user=None, rating=None):
    return select(db, RECIPE_SQL, {
        "id": id, 
        "title": title, 
        "steps": steps, 
        "user": user, 
        "rating": rating
    })

def ingredients(db, id=None, name=None):
    return select(db, INGREDIENT_SQL, {
        "id": id,
        "name": name
    })
