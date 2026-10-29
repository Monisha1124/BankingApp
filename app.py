class BankingApp:
    def __init__(self, balance=0.0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    # ADDED FOR PUSH 2
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        return self.balance

def main():
    app = BankingApp(100.0)
    print("--- Simple Banking Application (Push 2) ---")
    print(f"Initial Balance: ${app.check_balance()}")
    try:
        print("Withdrawing $40...")
        app.withdraw(40.0)
        print(f"Balance after withdrawal: ${app.check_balance()}")
        print("Attempting to overdraw $200...")
        app.withdraw(200.0)
    except ValueError as e:
        print(f"Transaction Denied: {e}")

if __name__ == '__main__':
    main()