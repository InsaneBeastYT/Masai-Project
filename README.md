Banking System

Description
The Banking System is a console-based Python application that allows users to create accounts,
perform banking transactions, and manage their finances. The system uses secure login
functionality,
transaction logging, and persistent storage for user and transaction data using file handling.
Features

- Account Creation:
Users can create a new account by providing their name, initial deposit, and password.
Account details (Account Number, Name, Password, Balance) are stored securely in accounts.txt.

- Login:
Users can log in with their account number and password.
Passwords are stored securely using hashing.

- Transactions:
- Deposit: Add funds to the account.
- Withdrawal: Withdraw funds from the account (checks for sufficient balance).
- Transactions are logged in transactions.txt in the format:
Account Number, Transaction Type, Amount, Date.

- Error Handling:
Handles invalid inputs, incorrect credentials, and insufficient balance gracefully.

Files Used
- accounts.txt: Stores user account details in the format:
Account Number, Name, Password (hashed), Balance
- transactions.txt: Logs all transactions in the format:
Account Number, Transaction Type (Deposit/Withdrawal), Amount, Date


How to Use
- Main Menu
When the application starts, the main menu is displayed:
Welcome to the Banking System!
1. Create Account
2. Login
3. Exit
