import hashlib
import sys

def fingerprint(text):
    """creates a hash fingerprint with len=10"""
    encoded = text.encode("utf-8")
    hash = hashlib.md5(encoded)

    return hash.hexdigest()[:10]

class Auth_Tools:
    """Basic auth functions."""
    def authenticateUser(self, password,stored_hash): # noqa: N802
        return fingerprint(password) ==stored_hash



assert Auth_Tools().authenticateUser("s3cur3", "876a5b350b") == True
assert not Auth_Tools().authenticateUser("p4zzword", "876a5b350b")
