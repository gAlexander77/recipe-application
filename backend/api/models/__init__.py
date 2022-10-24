
def success(value):
    return value, None

def failure(value):
    return None, value

def md5sum(text):
    import hashlib; return hashlib.md5(text.encode("utf-8")).digest().hex()
