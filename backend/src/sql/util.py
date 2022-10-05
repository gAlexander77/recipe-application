def db_pass(data, message=None):
    return data, None


def db_fail(data, message=None):
    return None, data


def dump_tables(db):
    rows = db.execute("select name from sqlite_master where type = 'table'")
    return [row["name"] for row in rows.fetchall()]


def valid_table(db, table):
    return table in dump_tables(db)


def dicts(cursor, row):
    return dict((cursor.description[i][0], v) for i, v in enumerate(row))
