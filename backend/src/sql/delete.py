from .util import dump_tables, db_pass, db_fail

def recipe(db, id):
    try:
        query = db.execute("select title from recipes where id = ?", (id, ))
        db.execute("delete from recipes where id = ?", (id, ))
        db.commit()
    except Exception as error:
        return db_fail(error)

    return db_pass(query.fetchone()["title"])
