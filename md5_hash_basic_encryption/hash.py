import hashlib

def hash_MD5(data):
    return hashlib.md5(data.encode()).hexdigest()



