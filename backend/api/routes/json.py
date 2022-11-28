from flask import jsonify

def send(status=True, data=[], error=None, redirect=None):
    payload = { "ok": status, "data": data }
    if error is not None:
        payload["error"] = str(error)
    response = jsonify(payload)
    if redirect is not None:
        response.headers["Location"] = redirect
    response.headers["Access-Control-Allow-Origin"] = '*'
    return response

def ok(data, redirect=None):
    return send(data=data, redirect=redirect)

def exception(error, data=[]):
    return send(status=False, data=data, error=error)
