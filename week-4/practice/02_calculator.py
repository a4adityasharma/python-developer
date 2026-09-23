def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Choose an operation: ")

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result:g}")

    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError as error:
        print(error)


if __name__ == "__main__":
    main()
