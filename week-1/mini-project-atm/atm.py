# ============================================
# Simple ATM Simulator
# Skill Nexis - Week 1 Mini Project
# ============================================

# Initial account details
CORRECT_PIN = "1234"
balance = 10000.0


def login():
    """Authenticate the user using a 4-digit PIN."""

    attempts = 3

    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")

        if pin == CORRECT_PIN:
            print("\nLogin successful!")
            return True

        attempts -= 1

        if attempts > 0:
            print(f"Incorrect PIN. {attempts} attempt(s) remaining.\n")
        else:
            print("Too many incorrect attempts. Account locked.")

    return False


def check_balance():
    """Display the current account balance."""

    print(f"\nCurrent Balance: ₹{balance:.2f}")


def deposit():
    """Deposit money into the account."""

    global balance

    try:
        amount = float(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("Deposit amount must be greater than ₹0.")
            return

        balance += amount

        print(f"₹{amount:.2f} deposited successfully.")
        print(f"Updated Balance: ₹{balance:.2f}")

    except ValueError:
        print("Invalid amount. Please enter a numeric value.")


def withdraw():
    """Withdraw money from the account."""

    global balance

    try:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Withdrawal amount must be greater than ₹0.")
            return

        if amount > balance:
            print("Insufficient balance.")
            return

        balance -= amount

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Remaining Balance: ₹{balance:.2f}")

    except ValueError:
        print("Invalid amount. Please enter a numeric value.")


def display_menu():
    """Display the ATM menu."""

    print("\n" + "=" * 40)
    print("             ATM MENU")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=" * 40)


def atm():
    """Run the ATM application."""

    if not login():
        return

    while True:
        display_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using our ATM.")
            print("Have a great day!")
            break

        else:
            print("\nInvalid choice. Please select an option from 1 to 4.")


# ============================================
# Program Entry Point
# ============================================

if __name__ == "__main__":
    print("=" * 40)
    print("       WELCOME TO PYTHON ATM")
    print("=" * 40)

    atm()