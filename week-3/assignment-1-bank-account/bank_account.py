class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance:.2f}")


def main():
    account = BankAccount("Aditya Sharma", 10000)

    print("Initial Account Details")
    account.display_balance()

    print("\nDepositing ₹2500...")
    account.deposit(2500)

    print("\nWithdrawing ₹1500...")
    account.withdraw(1500)

    print("\nFinal Account Details")
    account.display_balance()


if __name__ == "__main__":
    main()
