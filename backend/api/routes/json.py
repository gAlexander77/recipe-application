from flask import jsonify

def send(status=True, data=[], error=None):
    payload = { "ok": status, "data": data }
    if error is not None:
        payload["error"] = str(error)
    response = jsonify(payload)
    response.headers["Access-Control-Allow-Origin"] = '*'
    return response

def ok(data):
    return send(data=data)

def exception(error, data=[]):
    return send(status=False, data=data, error=error)
