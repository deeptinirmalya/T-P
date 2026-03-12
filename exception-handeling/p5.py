class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass


# Inventory Data
inventory = {
    1: {"name": "Laptop", "stock": 5},
    2: {"name": "Mouse", "stock": 10},
    3: {"name": "Keyboard", "stock": 7}
}


def view_inventory():
    print("\nInventory List:")
    for pid, details in inventory.items():
        print("Product ID:", pid, "| Name:", details["name"], "| Stock:", details["stock"])


def buy_product():
    try:
        pid = int(input("Enter Product ID: "))

        if pid not in inventory:
            raise InvalidProductIDError("Invalid Product ID!")

        quantity = int(input("Enter quantity: "))

        if quantity > inventory[pid]["stock"]:
            raise OutOfStockError("Product is out of stock!")

        inventory[pid]["stock"] -= quantity
        print("Product purchased successfully!")

    except InvalidProductIDError as e:
        print("Error:", e)

    except OutOfStockError as e:
        print("Error:", e)

    except ValueError:
        print("Please enter numbers only!")


while True:
    print("\n--- Inventory Management System ---")
    print("1. View Inventory")
    print("2. Buy Product")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_inventory()
        elif choice == 2:
            buy_product()
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")