products = {
    "Laptop": {"price": 50000, "stock": 5},
    "Phone": {"price": 20000, "stock": 10},
    "Headphones": {"price": 2000, "stock": 8}
}

valid_coupon = "SAVE10"
orders = []

def view_products():
    print("\nAvailable Products:")
    for name, details in products.items():
        print(name, "- Price:", details["price"], "Stock:", details["stock"])


def place_order():
    try:
        product = input("Enter product name: ")

        if product not in products:
            raise KeyError("Product not found!")

        if products[product]["stock"] <= 0:
            raise Exception("Out of stock!")

        quantity = int(input("Enter quantity: "))

        total = products[product]["price"] * quantity

        coupon = input("Enter coupon code (or press Enter to skip): ")
        if coupon != "":
            if coupon != valid_coupon:
                raise ValueError("Invalid coupon code!")
            total = total * 0.9   # 10% discount

        payment = input("Enter payment method (UPI/Card/Cash): ")
        if payment not in ["UPI", "Card", "Cash"]:
            raise ValueError("Invalid payment method!")

        products[product]["stock"] -= quantity
        orders.append(product)

        print("Order placed successfully!")
        print("Total amount:", total)

    except KeyError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)


def return_order():
    try:
        product = input("Enter product to return: ")

        if product not in orders:
            raise Exception("Order not found!")

        products[product]["stock"] += 1
        orders.remove(product)

        print("Product returned successfully!")
        print("Refund processed.")

    except Exception as e:
        print("Error:", e)


while True:
    print("\n--- E-Commerce Order System ---")
    print("1. View Products")
    print("2. Place Order")
    print("3. Return Order")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_products()
        elif choice == 2:
            place_order()
        elif choice == 3:
            return_order()
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")