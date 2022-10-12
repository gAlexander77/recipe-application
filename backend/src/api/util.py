from flask import g, jsonify
import sql

def open_database():
    if "_db" not in g:
        db = g._db = sql.open_database()
    db.row_factory = sql.util.dicts
    return db


def params(data, keys):
    values = tuple(data.get(k) for k in keys)
    return values[0] if len(values) == 1 else values


def json_response(data=[], error=None):
    payload = { "ok": True if not error else False, "data": data }
    if error:
        payload["error"] = str(error)
    response = jsonify(payload)
    response.headers["Access-Control-Allow-Origin"] = '*'
    return response


def send(data):
    return json_response(data)


def fail(error, data=[]):
    return json_response(data, error)
