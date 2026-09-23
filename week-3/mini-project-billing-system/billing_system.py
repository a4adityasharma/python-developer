# Mini Project: Billing System (OOP-based)
# Skill Nexis Python Programming Internship - Week 3

from datetime import datetime


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    TAX_RATE = 0.18

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(product.get_total() for product in self.products)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.TAX_RATE

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        if not self.products:
            print("No products in the bill.")
            return

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print("\n" + "=" * 65)
        print("                         BILL")
        print("=" * 65)
        print(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
        print("-" * 65)
        print(f"{'Product':<25}{'Price':>12}{'Qty':>8}{'Amount':>15}")
        print("-" * 65)

        for product in self.products:
            print(
                f"{product.name:<25}"
                f"₹{product.price:>10.2f}"
                f"{product.quantity:>8}"
                f"₹{product.get_total():>13.2f}"
            )

        print("-" * 65)
        print(f"{'Subtotal':<50}₹{subtotal:>12.2f}")
        print(f"{'Tax (18%)':<50}₹{tax:>12.2f}")
        print(f"{'Grand Total':<50}₹{total:>12.2f}")
        print("=" * 65)


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Quantity must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number.")


def main():
    bill = Bill()

    print("=" * 45)
    print("        OOP BILLING SYSTEM")
    print("=" * 45)

    while True:
        name = input("\nEnter product name (or 'done' to finish): ").strip()

        if name.lower() == "done":
            break

        if not name:
            print("Product name cannot be empty.")
            continue

        price = get_positive_number("Enter product price: ₹")
        quantity = get_positive_integer("Enter quantity: ")

        product = Product(name, price, quantity)
        bill.add_product(product)

        print("Product added successfully.")

    bill.display_bill()


if __name__ == "__main__":
    main()
