from .util import dump_tables, db_pass, db_fail

SQL_DELETE = "DELETE FROM %s WHERE id = ?"

def recipe(db, id):
    db.execute("delete from recipes where id = ?", (id, ))
    db.commit()
    return db_pass(query.fetchone()["title"])

def ingredient(db, id):
    db.execute(SQL_DELETE % "ingredients", (id, ))
