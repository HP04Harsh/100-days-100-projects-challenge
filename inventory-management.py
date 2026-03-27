class Product:
    total_products = 0  # class variable

    def __init__(self, name, price, quantity):
        if not self.validate_price(price):
            raise ValueError("Invalid price")

        self.name = name
        self.price = price
        self.quantity = quantity
        Product.total_products += 1

    def add_stock(self, amount):
        self.quantity += amount
        print(f"{amount} items added. Total: {self.quantity}")

    def sell(self, amount):
        if amount > self.quantity:
            print("Not enough stock!")
        else:
            self.quantity -= amount
            print(f"{amount} sold. Remaining: {self.quantity}")

    @classmethod
    def show_total_products(cls):
        print(f"Total products: {cls.total_products}")

    @staticmethod
    def validate_price(price):
        return price > 0


# 🔹 Usage
p1 = Product("Laptop", 50000, 10)
p2 = Product("Mouse", 500, 50)

p1.add_stock(5)
p1.sell(3)

Product.show_total_products()