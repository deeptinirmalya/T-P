class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class BillingSystem:
    def __init__(self):
        self.cart = []
        self.total = 0

    def scan_product(self, name, price):
        p = Product(name, price)
        self.cart.append(p)
        self.total += price
        print(name, "added")

    def apply_discount(self, percent):
        discount = (self.total * percent) / 100
        self.total = self.total - discount
        print("Discount Applied")

    def generate_bill(self):
        print("Bill")
        for p in self.cart:
            print(p.name, p.price)
        print("Total:", self.total)

    def record_transaction(self):
        print("Transaction Recorded")


b = BillingSystem()

b.scan_product("Milk", 50)
b.scan_product("Bread", 30)
b.scan_product("Eggs", 60)

b.apply_discount(10)

b.generate_bill()

b.record_transaction()