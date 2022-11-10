from hashlib import md5

from . import users
from . import recipes, recipecards
from . import ingredients
from . import comments, ratings

ok = lambda value: (value, None)
error = lambda value: (None, value)
md5sum = lambda text: md5(text.encode("utf-8")).digest().hex()


# parses a dictionary into SQLite3 parameters
def parse_params(fields):

    exists = dict(filter(lambda i: i[1] is not None, fields.items()))
    sql = " and".join(f" where {k} = ?" for k in exists.keys())
    
    return tuple(exists.values()), sql


# wrapper function to abstract the action
# of adding a row to an existing database
# table
def insert(db, table, fields): 
    
    cols, qs = ','.join(fields.keys()), ','.join(('?') * len(fields))

    try:
        row = db.execute(f"""insert into {table} ({cols}) values ({qs})
            returning rowid""", tuple(fields.values())).fetchone()
        db.commit()
    except Exception as e:
        return error(str(e))
    
    return ok(row["rowid"])


# wrapper function to abstract the action
# of deleting an existing row from a
# table
def delete(db, table, rowid, returning):
    
    try:
        row = db.execute(f"""delete from {table} where rowid = ?
            returning {returning}""").fetchone()
        if len(row) == 0:
            return error("id does not match")
    except Exception as e:
        return error(str(e))

    return ok(row[returning])


# wrapper function to get one row from the table based on some filter
def select(db, table, fields):

    values, sql = parse_params(fields)
        
    try:
        row = db.execute(f"select * from {table}{sql}", values).fetchone()
    except Exception as e:
        return error(str(e))

    return ok(row) if row is not None else error(f"{'/'.join(values)} does not exist")


# wrapper function to get one all rows from the table based on a filter
def query(db, table, fields):
 
    values, sql = parse_params(fields)
    
    try:
        rows = db.execute(f"select * from {table}{sql}", values).fetchall()
    except Exception as e:
        return error(str(e))

    return ok(rows)


# wrapper function to get all rows from a table (or view)
def dump(db, table):

    try:
        rows = db.execute(f"select * from {table}").fetchall()
    except Exception as e:
        return error(str(e))
    
    return ok(rows)
