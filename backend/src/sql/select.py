from .util import valid_table, db_pass, db_fail


def recipe_query(table, fields, expression):
    
    items = filter(lambda t: t[1] is not None, fields.items())
    sql = " and ".join(expression % (k, v) for k, v in items)
    
    query = f"""select 
            recipes.id, title, steps, rating,
            recipes.created, recipes.updated, 
            user as userid, username 
            from {table} 
            left join users on recipes.user = users.id"""

    if sql:
        query += f" where {sql}"

    return query


def select(db, query_callback, table, fields, single=False):

    if not valid_table(db, table):
        return db_fail("invalid table")

    expression =  "%s = %s" if single else "%s like '%%%s%%'"
    sql = query_callback(table, fields, expression)

    try:
        rows = db.execute(sql)
    except Exception as error:
        return db_fail(error)

    return db_pass(rows.fetchone() if single else rows.fetchall())


# if user only wants one, only let them use the unique columns
def recipe(db, id=None, title=None, user=None):
    if id is not None or name is not None or user is not None:
        return select(db, recipe_query, "recipes", {
            "id": id, "title": title, "user": user }, single=True)
    return db_fail("id or title or user required")


def recipes(db, id=None, title=None, steps=None, user=None, rating=None):
    return select(db, recipe_query, "recipes", {
        "id": id, "title": title, "steps": steps, "user": user, "rating": rating})
