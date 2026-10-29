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

def main():
    app = BankingApp(100.0)
    print("--- Simple Banking Application (Push 1) ---")
    print(f"Initial Balance: ${app.check_balance()}")
    print("Depositing $50...")
    app.deposit(50.0)
    print(f"Updated Balance: ${app.check_balance()}")

if __name__ == '__main__':
    main()