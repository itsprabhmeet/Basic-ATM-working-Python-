class ATM:
    def __init__(self, initial_balance=0, pin="1234"):
        """Initialize the ATM with an initial balance and a PIN."""
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def check_balance(self):
        """Return the current account balance."""
        return self.balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return f"Successfully deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient balance exists."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew: ${amount}")
                return f"Successfully withdrew ${amount}. New balance: ${self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def change_pin(self, old_pin, new_pin):
        """Change the account PIN if the old PIN is correct."""
        if old_pin == self.pin:
            self.pin = new_pin
            return "PIN changed successfully."
        else:
            return "Old PIN is incorrect."

    def get_transaction_history(self):
        """Return the transaction history."""
        return self.transaction_history if self.transaction_history else "No transactions yet."

def main():
    """Main function to simulate ATM operations."""
    atm = ATM(initial_balance=1000)  # Initialize ATM with $1000 balance
    print("Welcome to the ATM!")

    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print(f"Your current balance is: ${atm.check_balance()}")

        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))

        elif choice == '4':
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter your new PIN: ")
            print(atm.change_pin(old_pin, new_pin))

        elif choice == '5':
            print("Transaction History:")
            for transaction in atm.get_transaction_history():
                print(transaction)

        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()