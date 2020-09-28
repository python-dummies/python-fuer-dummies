"""Provide basic password authentication."""
import hashlib


def fingerprint(text):
    """Create a hash fingerprint with len=10."""
    encoded = text.encode("utf-8")
    hash_ = hashlib.sha3_256(encoded)

    return hash_.hexdigest()[:10]


def authenticate(password, stored_hash):
    """Authenticate a user.

    Compares a provided a password against the hash stored in a database.
    """
    return fingerprint(password) == stored_hash
