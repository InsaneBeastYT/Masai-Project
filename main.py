import os
import hashlib
from datetime import datetime

ACCOUNTS_FILE = 'accounts.txt'
TRANSACTIONS_FILE = 'transactions.txt'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_account(account_number, name, hashed_password, balance):
    with open(ACCOUNTS_FILE, 'a') as file:
        file.write(f"{account_number},{name},{hashed_password},{balance}\n")

def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as file:
            for line in file:
                account_number, name, hashed_password, balance = line.strip().split(',')
                accounts[account_number] = {
                    'name': name,
                    'password': hashed_password,
                    'balance': float(balance)
                }
    return accounts

def save_transaction(account_number, transaction_type, amount):
    with open(TRANSACTIONS_FILE, 'a') as file:
        date = datetime.now().strftime('%Y-%m-%d')
        file.write(f"{account_number},{transaction_type},{amount},{date}\n")

def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    account_number = str(hash(name + str(initial_deposit) + str(datetime.now())) % 10**6)
    password = input("Enter a password: ")
    hashed_password = hash_password(password)
    save_account(account_number, name, hashed_password, initial_deposit)
    print(f"Your account number: {account_number} (Save this for login)")
    print("Account created successfully!")

def login():
    accounts = load_accounts()
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    if account_number in accounts and accounts[account_number]['password'] == hashed_password:
        print("Login successful!")
        return account_number, accounts[account_number]
    else:
        print("Invalid account number or password.")
        return None, None

def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account['balance'] += amount
    save_transaction(account['account_number'], 'Deposit', amount)
    update_account(account)
    print(f"Deposit successful! Current balance: {account['balance']}")

def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if amount > account['balance']:
        print("Insufficient balance.")
    else:
        account['balance'] -= amount
        save_transaction(account['account_number'], 'Withdrawal', amount)
        update_account(account)
        print(f"Withdrawal successful! Current balance: {account['balance']}")

def update_account(account):
    accounts = load_accounts()
    accounts[account['account_number']]['balance'] = account['balance']
    with open(ACCOUNTS_FILE, 'w') as file:
        for acc_number, details in accounts.items():
            file.write(f"{acc_number},{details['name']},{details['password']},{details['balance']}\n")

def main():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            account_number, account = login()
            if account:
                account['account_number'] = account_number
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        deposit(account)
                    elif sub_choice == '2':
                        withdraw(account)
                    elif sub_choice == '3':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
