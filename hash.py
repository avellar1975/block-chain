from hashlib import sha256

def calcula_hash(string):
    return sha256(string.encode()).hexdigest()
