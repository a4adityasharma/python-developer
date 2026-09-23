class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    calculator = Calculator()

    while True:
        print("\n" + "=" * 35)
        print("         CALCULATOR")
        print("=" * 35)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        print("=" * 35)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Calculator closed.")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice.")
            continue

        first = get_number("Enter first number: ")
        second = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = calculator.add(first, second)
            elif choice == "2":
                result = calculator.subtract(first, second)
            elif choice == "3":
                result = calculator.multiply(first, second)
            else:
                result = calculator.divide(first, second)

            print(f"Result: {result:g}")

        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
