def ok(value):
    return str(value) if value else "ok", None


def error(value):
    return None, str(value) if value else "error"


# wrapper function to abstract the action
# of adding a row to an existing database
# table
# DO NOT USE IN API ENDPOINTS
def insert(db, table, fields): 
    
    columns = ','.join(fields.keys())
    values = ','.join(('?' * len(fields)))
    
    try:
        row = db.execute(f"""insert into {table} 
            ({columns}) values ({values})
            returning rowid""", fields.values()).fetchone()
        db.commit()
    except Exception as e:
        return error(str(e))
    
    return ok(row["rowid"])


# wrapper function to abstract the action
# of deleting an existing row from a
# table
# DO NOT USE IN API ENDPOINTS
def delete(db, table, rowid, returning):
    
    try:
        row = db.execute(f"""delete from {table} where rowid = ?
                         returning {returning}""").fetchone()
        if len(row) == 0:
            return error("id does not match")
    except Exception as e:
        return error(str(e))

    return ok(row[returning])
