import os

def write_file(filepath, content, mode="a"):
    try:
        with open(filepath, mode) as file:
            file.write(content + "\n")
    except Exception as e:
        print(f"Error writing to file {filepath}: {e}")

def read_file(filepath):
    try:
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r") as file:
            return file.readlines()
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return []

def initialize_file_with_headers(filepath, headers):
    try:
        if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:
            write_file(filepath, headers, mode="w")
    except Exception as e:
        print(f"Error initializing file {filepath}: {e}")
