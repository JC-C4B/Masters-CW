
import unittest
import PEight
from PEight import *


class TestparseChange(unittest.TestCase):

    def test_total(self):
        coins = "PNDQHW"
        self.assertEqual(CoinCollector.parseChange(coins), 1.91)
      
    def test_pennies(self):
        coins = "PPPP"
        self.assertEqual(CoinCollector.parseChange(coins), .04)

    def test_Quarters(self):
        coins = "QQQQ"
        self.assertEqual(CoinCollector.parseChange(coins), 1)

class TestAccount(unittest.TestCase):

    def test_depo1(self):
        a = Account()
        a2 = Account()
        a.deposit(200)
        self.assertGreater(a.balance, a2.balance)
        
    def test_depo2(self):
        a = Account()
        a2 = Account()
        a.deposit(200)
        a2.deposit(200)
        self.assertEqual(a, a2)

    def test_withdraw1(self):
        a = Account()
        a2 = Account()
        a.deposit(200)
        a2.deposit(200)
        a2.withdraw(100)
        self.assertGreater(a, a2)

    def test_withdraw2(self):
        a = Account()
        a.deposit(200) 
        a.withdraw(100)
        self.assertGreater(200, a.balance)

    def test_isValidPIN1(self):
        a = Account(444, "J", "C", 444, 1111, 0)
        if a.isPinValid(1111) == True:
            self.assertTrue

    def test_isValidPIN1(self):
        a = Account(444, "J", "C", 444, 1111, 0)
        if a.isPinValid(2323) == False:
            self.assertTrue

class TestBank(unittest.TestCase):

    def test_addacc1(self):
        b = Bank()
        ACCOUNTS = ACCOUNTS
        a = Account(444, "J", "C", 444, 1111, 0)
        b.addAccountToBank(a)
        if ACCOUNTS[0] == a:
            self.assertTrue    

    def test_addacc1(self):
        b = Bank()
        ACCOUNTS = ACCOUNTS
        a = Account(444, "J", "C", 444, 1111, 0)
        a2 = Account(444, "w", "x", 444, 1111, 0)
        b.addAccountToBank(a)
        b.addAccountToBank(a2)
        if Account in ACCOUNTS == 2:
            self.assertTrue  

    def test_remacc1(self):
        b = Bank()
        ACCOUNTS = ACCOUNTS
        a = Account(444, "J", "C", 444, 1111, 0)
        a2 = Account(444, "w", "x", 444, 1111, 0)
        b.addAccountToBank(a)
        b.addAccountToBank(a2)
        b.removeAccountFromBank(a)
        if Account in ACCOUNTS == 1:
                self.assertTrue

    def test_remacc1(self):
        b = Bank()
        ACCOUNTS = ACCOUNTS
        a = Account(444, "J", "C", 444, 1111, 0)
        a2 = Account(444, "w", "x", 444, 1111, 0)
        b.addAccountToBank(a)
        b.addAccountToBank(a2)
        b.removeAccountFromBank(a)
        b.removeAccountFromBank(a2)
        if "Null" in ACCOUNTS == 2:
                self.assertTrue








unittest.main()








