import unittest
from app import BankingApp

class TestBankingApp(unittest.TestCase):
    def test_check_balance(self):
        app = BankingApp(100.0)
        self.assertEqual(app.check_balance(), 100.0)

    def test_deposit_success(self):
        app = BankingApp(100.0)
        app.deposit(50.0)
        self.assertEqual(app.check_balance(), 150.0)

    
    def test_withdraw_success(self):
        app = BankingApp(100.0)
        app.withdraw(40.0)
        self.assertEqual(app.check_balance(), 60.0)

    def test_withdraw_insufficient_funds(self):
        app = BankingApp(100.0)
        with self.assertRaises(ValueError):
            app.withdraw(150.0)