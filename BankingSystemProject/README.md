# Banking System Project

## Project Overview

The **Banking System Project** is a console-based Python application that simulates a simple banking system. It allows users to:
1. Create a new account.
2. Login to an existing account.
3. Perform banking operations such as:
   - Check Balance
   - Deposit Money
   - Withdraw Money
   - View Mini Statement
4. Securely handle user data using password hashing.
5. Log transactions for user accounts.

## Project Structure

BankingSystemProject/ 
├── data/ 
│   ├── accounts.txt # Stores account details 
│   ├── transactions.txt # Logs user transactions 
├── src/ 
│   ├── init.py # Package initializer 
│   ├── banking_system.py # Main application logic 
│   ├── config.py # Configuration settings 
├── utils/ 
│   ├── init.py # Package initializer 
│   ├── file_operations.py # File operations for data storage and retrieval 
│   ├── hashing.py # Password hashing utilities 
├── tests/ 
│ └── # Placeholder for unit tests 
├── venv/ # Virtual environment 
├── main.py # Entry point for the application 
├── requirements.txt # Project dependencies 
├── README.md # Project documentation



## Features

1. **Account Management**:
   - Create accounts with a unique account number.
   - Login with secure password verification.
2. **Banking Operations**:
   - Deposit and withdraw money.
   - View a mini statement of recent transactions.
3. **Secure Storage**:
   - Passwords are hashed using the `bcrypt` library.
   - Account details and transactions are stored in text files for simplicity.
4. **File-Based Data Storage**:
   - `accounts.txt`: Stores user account details.
   - `transactions.txt`: Logs all user transactions.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd BankingSystemProject   

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   
3. Install dependencies:
    ```bash
   pip install -r requirements.txt
   
4. Run the application:
   ```bash
   python main.py
