#  List Based Transaction System With Date & Time 

from datetime import datetime

CORRECT_USERNAME = "add"
CORRECT_PASSWORD = "pass112"
MAX_LOGIN_ATTEMPTS = 3

def login():
    attempts = 0
    
    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("\nLogin Successful!")
            print("Login Time:", login_time)
            return True, login_time
        else:
            attempts += 1
            remaining = MAX_LOGIN_ATTEMPTS - attempts
            print(f"Invalid credentials. {remaining} attempts remaining.\n")
    
    print("Too many failed attempts. System exiting.")
    return False, None

def deposit(balance, transactions):
    amount = int(input("Enter deposit amount: "))
    balance += amount
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transactions.append(f"{current_time} | Deposited: {amount}")
    
    print("Amount Deposited Successfully.")
    return balance

def withdraw(balance, transactions):
    amount = int(input("Enter withdrawal amount: "))
    
    if amount <= balance:
        balance -= amount
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transactions.append(f"{current_time} | Withdrawn: {amount}")
        
        print("Amount Withdrawn Successfully.")
    else:
        print("Insufficient Balance.")
    
    return balance

def check_balance(balance):
    print(f"Current Balance: {balance}")


def show_transactions(transactions):
    print("\n--- Transaction History ---")
    
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)


def show_menu():
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")


def main():
    balance = 0
    transactions = []

    print("--- Welcome to Puppala Bank ---")
    
    success, login_time = login()
    
    if not success:
        return
    
    print(f"\nWelcome back, {CORRECT_USERNAME}!")

    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            balance = deposit(balance, transactions)
        elif choice == 2:
            balance = withdraw(balance, transactions)
        elif choice == 3:
            check_balance(balance)
        elif choice == 4:
            show_transactions(transactions)
        elif choice == 5:
            print("Thank you for banking with us.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
