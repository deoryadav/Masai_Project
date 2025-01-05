import pytest
from utils.hashing import hash_password

def test_hash_password():
    # Test that hash_password returns a hash
    assert hash_password("password123") != "password123"
    # Test that hashes for the same password are consistent
    assert hash_password("password123") == hash_password("password123")
    # Test that hashes for different passwords are different
    assert hash_password("password123") != hash_password("password321")

def test_file_operations():
    from utils.file_operations import write_file, read_file
    # Create a test file
    test_file = "test_file.txt"
    write_file(test_file, "Test line 1", mode="w")
    write_file(test_file, "Test line 2")

    # Read the file
    lines = read_file(test_file)
    assert lines == ["Test line 1\n", "Test line 2\n"]

    # Cleanup
    import os
    os.remove(test_file)
