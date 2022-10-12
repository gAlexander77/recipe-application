from flask import Blueprint, jsonify

def values(data, keys):
    return ( data[k] if k in data else None for k in keys )

def send(data):
    response = jsonify({ "ok": True, "data": data })
    response.headers["Access-Control-Allow-Origin"] = '*'
    return response

def fail(error, data=None):
    if not isinstance(error, str):
        error = str(error)
    response = jsonify({ "ok": False, "data": data, "error": error })
    response.headers["Access-Control-Allow-Origin"] = '*'
    return response
