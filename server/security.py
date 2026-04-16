import hashlib

def encrypt_weights(coef, intercept):
    data = str(coef) + str(intercept)
    hash_value = hashlib.sha256(data.encode()).hexdigest()
    return hash_value
