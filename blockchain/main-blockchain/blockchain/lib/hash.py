import hashlib

def encrypt_string(hash_string: str | list | dict) -> str:
    """ sha256 encryption """
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
