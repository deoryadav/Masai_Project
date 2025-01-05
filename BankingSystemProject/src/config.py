import os

# Define base directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Define absolute paths for data files
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)  # Ensure data directory exists

ACCOUNTS_FILE = os.path.join(DATA_DIR, 'accounts.txt')
TRANSACTIONS_FILE = os.path.join(DATA_DIR, 'transactions.txt')
