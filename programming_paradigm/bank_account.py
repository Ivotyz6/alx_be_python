# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        # Private attribute for encapsulation
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if funds are sufficient.
        Returns True if the withdrawal is successful, False otherwise.
        """
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")

