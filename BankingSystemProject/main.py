import logging
from src.banking_system import BankingSystem
from src.config import ACCOUNTS_FILE, TRANSACTIONS_FILE

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main_menu():
    banking_system = BankingSystem(ACCOUNTS_FILE, TRANSACTIONS_FILE)

    while True:
        try:
            print("\nWelcome to the Banking System!")
            print("1. Create Account\n2. Login\n3. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                banking_system.create_account()
            elif choice == "2":
                user = banking_system.login()
                if user:
                    user_menu(banking_system, user)
            elif choice == "3":
                print("Thank you for using our banking system!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")


def user_menu(banking_system, user_details):
    account_number = user_details["account_number"]
    name = user_details["name"]
    balance = user_details["balance"]

    while True:
        print(f"\nHello, {name}!")
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Mini-Statement\n5. Logout")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(f"Your current balance is: {balance}")
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: ").strip())
                if amount <= 0:
                    print("Deposit amount must be positive.")
                    continue
                balance += amount
                print(f"Deposit successful! New balance is {balance}.")
                banking_system.log_transaction(account_number, "Deposit", amount, balance)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: ").strip())
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                    continue
                if amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    print(f"Withdrawal successful! New balance is {balance}.")
                    banking_system.log_transaction(account_number, "Withdrawal", amount, balance)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '4':
            banking_system.get_mini_statement()
        elif choice == '5':
            print("Logging out...")
            banking_system.update_account_balance(account_number, balance)
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main_menu()

    # from src.config import ACCOUNTS_FILE, TRANSACTIONS_FILE
    # import os
    #
    # # Print paths
    # print("Accounts file path:", ACCOUNTS_FILE)
    # print("Transactions file path:", TRANSACTIONS_FILE)
    #
    # # Verify if the files exist
    # print("Does accounts.txt exist?", os.path.exists(ACCOUNTS_FILE))
    # print("Does transactions.txt exist?", os.path.exists(TRANSACTIONS_FILE))
    #
    # # Check if directories exist
    # print("Does data directory exist?", os.path.exists(os.path.dirname(ACCOUNTS_FILE)))
