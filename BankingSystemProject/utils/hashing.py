import hashlib

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password, hashed_password):
    """Verify input password by comparing its hash with the stored hashed password."""
    return hash_password(input_password) == hashed_password
