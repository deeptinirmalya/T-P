import time

accounts = {
    101: 5000,
    102: 3000,
    103: 7000
}

def view_accounts():
    print("\nAccount Details:")
    for acc, balance in accounts.items():
        print("Account:", acc, "Balance:", balance)


def transfer_money():
    try:
        sender = int(input("Enter Sender Account Number: "))
        receiver = int(input("Enter Receiver Account Number: "))

        if sender not in accounts or receiver not in accounts:
            raise KeyError("Incorrect account number!")

        amount = float(input("Enter Amount to Transfer: "))

        if amount <= 0:
            raise ValueError("Amount must be positive!")

        if accounts[sender] < amount:
            raise Exception("Overdraft! Insufficient balance.")

        print("Processing transaction...")
        time.sleep(2)   # simulate delay

        # simulate timeout
        if amount > 10000:
            raise TimeoutError("Transaction timeout!")

        accounts[sender] -= amount
        accounts[receiver] += amount

        print("Transaction successful!")

    except ValueError as e:
        print("Error:", e)
    except KeyError as e:
        print("Error:", e)
    except TimeoutError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)


while True:
    print("\n--- Banking System ---")
    print("1. View Accounts")
    print("2. Transfer Money")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_accounts()
        elif choice == 2:
            transfer_money()
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")