def values(data, keys):
    return ( data[k] if k in data else None for k in keys )

def send(data):
    return { "ok": True, "data": data }

def fail(error, data=None):
    if not isinstance(error, str):
        error = str(error)
    return { "ok": False, "data": data, "error": error }
