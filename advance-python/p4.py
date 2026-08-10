cart = {}

def add_item(name, price, quantity):
    cart[name] = {
        "price": price,
        "quantity": quantity
    }
    print(f"{name} added to cart.")

def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    
    total = 0
    print("\nYour Cart:")
    for name, details in cart.items():
        item_total = details["price"] * details["quantity"]
        total += item_total
        print(f"{name} - ₹{details['price']} x {details['quantity']} = ₹{item_total}")
    
    print("Total Amount: ₹", total)

def remove_item(name):
    if name in cart:
        del cart[name]
        print(f"{name} removed from cart.")
    else:
        print("Item not found.")

def menu():
    while True:
        print("\n1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            add_item(name, price, quantity)

        elif choice == "2":
            view_cart()

        elif choice == "3":
            name = input("Enter item name to remove: ")
            remove_item(name)

        elif choice == "4":
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice.")

menu()