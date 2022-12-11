from . import users, recipes, ratings, comments

INSERT_SQL = "INSERT INTO %s (%s) values (%s) returning %s"
UPDATE_SQL = "UPDATE %s SET %s = %s%s"
SELECT_SQL = "SELECT %s FROM %s%s"
DELETE_SQL = "DELETE FROM %s WHERE id = %s returning %s"


def __sql_filter(filters):
    sql = " AND ".join("%s = '%s'" % (k, v) for k,v in filters.items())
    return " WHERE %s" % sql if sql else ''


def __prep_insert(fields):
    ks = ','.join(fields.keys())
    qs = ','.join('?' * len(fields))
    return ks, tuple(fields.values()), qs


# puts a new row into the table, using the fields dict as values
def insert(db, table, fields, returning="id"):
    ks, vs, qs = __prep_insert(fields)
    row = db.execute(INSERT_SQL % (table, ks, qs, returning), vs).fetchone()
    db.commit()
    return row[returning]


# updates a single field, im too tired to write logic for multiple...
# filter is not optional, we dont want to update every single row
def update(db, table, field, value, filters):
    sql_filter = __sql_filter(filters)
    row = db.execute(UPDATE_SQL % (table, field, value, sql_filter)).fetchone()
    db.commit()
    return row[field]


# gets all rows from the table, optionally select columns, and filter 
def select(db, table, columns='*', filters={}):
    sql_filter = __sql_filter(filters)
    return db.execute(SELECT_SQL % (columns, table, sql_filter))

def select_set(db, table, columns='*', filters={}):
    return select(db, table, columns, filters).fetchall()

def select_one(db, table, columns='*', filters={}):
    return select(db, table, columns, filters).fetchone()


# deletes a row from the table by id
def delete(db, table, id, returning="id"):
    row = db.execute(DELETE_SQL % (table, id, returning)).fetchone()
    db.commit()
    return row[returning]
