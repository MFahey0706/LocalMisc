import hashlib

def generate_dict():
    keys = ["hello", "there", "hello_there", "hello there", "dictionaries are cool"]
    return {key: hashlib.sha224(key).hexdigest() for key in keys}
