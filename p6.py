# Multiple User ATM System

users = {
    "1001": {"pin": "1234", "balance": 5000},
    "1002": {"pin": "5678", "balance": 3000}
}


def login():
    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")
    
    if acc_no in users and users[acc_no]["pin"] == pin:
        print("Login Successful ")
        return acc_no
    else:
        print("Invalid Account or PIN ")
        return None


def check_balance(acc_no):
    print("Current Balance: ", users[acc_no]["balance"])


def deposit(acc_no):
    amount = float(input("Enter amount to deposit: "))
    users[acc_no]["balance"] += amount
    print("Deposit Successful")


def withdraw(acc_no):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= users[acc_no]["balance"]:
        users[acc_no]["balance"] -= amount
        print("Withdraw Successful ")
    else:
        print("Insufficient Balance ")


def atm_menu(acc_no):
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            check_balance(acc_no)
        elif choice == "2":
            deposit(acc_no)
        elif choice == "3":
            withdraw(acc_no)
        elif choice == "4":
            print("Logged Out ")
            break
        else:
            print("Invalid Choice ")
account = login()
if account:
    atm_menu(account)