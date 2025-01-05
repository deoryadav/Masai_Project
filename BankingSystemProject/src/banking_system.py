import getpass
import logging
import random
from datetime import datetime
from decimal import Decimal

from utils.file_operations import write_file, read_file, initialize_file_with_headers
from utils.hashing import hash_password, verify_password

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class BankingSystem:
    def __init__(self, accounts_file, transactions_file):
        self.accounts_file = accounts_file
        self.transactions_file = transactions_file
        self.logged_in_user = None

        # Ensure files exist with appropriate headers
        initialize_file_with_headers(self.accounts_file, "Account Number,Name,Password,Balance,Date Created")
        initialize_file_with_headers(self.transactions_file, "Account Number,Transaction Type,Amount,New Balance,Date")


    @staticmethod
    def generate_account_number(existing_account_numbers):
        """
        Generate a unique 6-digit account number.
        """
        while True:
            account_number = random.randint(100000, 999999)
            if str(account_number) not in existing_account_numbers:
                return account_number

    @staticmethod
    def get_current_datetime():
        """
        Get the current date and time in a readable format.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_account(self):
        """
        Create a new bank account with a unique account number.
        """
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        try:
            initial_deposit = Decimal(input("Enter your initial deposit: ").strip())
            if initial_deposit < 0:
                print("Deposit amount cannot be negative.")
                return
        except ValueError:
            print("Invalid deposit amount. Please try again.")
            return

        password = getpass.getpass("Enter a password: ").strip()
        if not password:
            print("Password cannot be empty.")
            return

        accounts = read_file(self.accounts_file) or []
        existing_account_numbers = set(
            line.split(',')[0].strip() for line in accounts if line.strip()
        )

        account_number = self.generate_account_number(existing_account_numbers)
        hashed_password = hash_password(password)
        created_at = self.get_current_datetime()

        # Save account details
        try:
            write_file(self.accounts_file, f"{account_number},{name},{hashed_password},{initial_deposit},{created_at}")
            logging.info(f"Account created successfully for {name}. Account Number: {account_number}")
            print(f"Account created successfully! Your account number is {account_number}. Save it for login.")
        except Exception as e:
            logging.error(f"Failed to create account: {e}")
            print("An error occurred while creating the account. Please try again.")

    def login(self):
        """
        Login to an existing bank account.
        """
        account_number = input("Enter your account number: ").strip()
        password = getpass.getpass("Enter your password: ").strip()

        accounts = read_file(self.accounts_file)

        for account in accounts:
            if not account.strip() or account.count(",") != 4:
                continue

            acc_no, name, hashed_password, balance, created_at = account.strip().split(",")
            if acc_no == account_number and verify_password(password, hashed_password):
                print(f"Login successful! Welcome, {name}.")
                print(f"Account created on: {created_at}")
                print(f"Your current balance is: {balance}")

                # Store the logged-in user details
                self.logged_in_user = {
                    "account_number": acc_no,
                    "name": name,
                    "balance": float(balance)
                }

                return {"account_number": acc_no, "name": name, "balance": float(balance)}


        print("Invalid account number or password. Please try again.")
        self.logged_in_user = None
        return None

    def update_account_balance(self, account_number, balance):
        """
        Update the balance for a specific account number in accounts.txt.
        """
        accounts = read_file(self.accounts_file)
        if not accounts:
            print("Accounts file is empty or missing.")
            return

        # Extract the header and existing accounts
        header = accounts[0].strip() if accounts else "Account Number,Name,Password,Balance,Date Created"
        account_dict = {}

        for account in accounts[1:]:  # Skip the header
            if not account.strip() or account.count(",") != 4:
                continue

            acc_no, name, hashed_password, current_balance, created_at = account.strip().split(",")
            account_dict[acc_no] = f"{acc_no},{name},{hashed_password},{current_balance},{created_at}"

        # Update the specific account's balance
        if account_number in account_dict:
            name, hashed_password, created_at = account_dict[account_number].split(",")[1:]
            account_dict[account_number] = f"{account_number},{name},{hashed_password},{balance},{created_at}"
        else:
            logging.error("Account number not found.")
            return

        # Write back all updated accounts including the header
        write_file(self.accounts_file, header, mode="w")  # Write header first
        for account_data in account_dict.values():
            write_file(self.accounts_file, account_data)
            print("Account balance updated successfully!")

    def log_transaction(self, account_number, transaction_type, amount, new_balance):
        """
        Log a transaction (deposit or withdrawal) in the transactions file.
        """
        headers = "Account Number,Transaction Type,Amount,New Balance,Date"
        initialize_file_with_headers(self.transactions_file, headers)

        transaction_time = self.get_current_datetime()
        transaction_entry = f"{account_number},{transaction_type},{amount},{new_balance},{transaction_time}"
        write_file(self.transactions_file, transaction_entry)
        print("Transaction logged successfully!")

    def get_mini_statement(self):
        """
        Fetch and display the mini-statement for the logged-in user's account.
        """
        if not self.logged_in_user:
            print("Error: No user is logged in. Please log in first.")
            return

        account_number = self.logged_in_user["account_number"]

        try:
            # Read transactions file
            with open(self.transactions_file, "r") as file:
                lines = file.readlines()

            # Extract headers and filter transactions
            headers = lines[0].strip().split(",")
            transactions = lines[1:]
            user_transactions = [
                txn.strip().split(",") for txn in transactions if txn.startswith(account_number)
            ]

            if not user_transactions:
                print("\nNo transactions found for your account.\n")
                return

            # Display mini-statement
            print("\n---------------------- Mini-Statement ----------------------")
            print(f"{'Date':<20} {'Transaction Type':<15} {'Amount':<10} {'New Balance':<10}")
            print("-" * 60)
            for txn in user_transactions:
                txn_date, txn_type, txn_amount, txn_balance = txn[4], txn[1], txn[2], txn[3]
                print(f"{txn_date:<20} {txn_type:<15} {txn_amount:<10} {txn_balance:<10}")
            print("-" * 60)

        except FileNotFoundError:
            print("Transactions file not found. Please check the system configuration.")
        except Exception as e:
            print(f"An error occurred while fetching the mini-statement: {e}")







