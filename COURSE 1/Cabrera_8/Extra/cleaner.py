


import random

# Global List
# Kept having issues with attributes being changed in instances that were not the same; went with global list to minimize
ACCOUNTS = []

# Change sorting class
class CoinCollector:

    # Change sorting function
    def parseChange(coins):
        
        # Money total
        totalCent = 0

        for i in coins:

            # Pennies
            if i == "P":
                totalCent = totalCent + .01
            
            # Nickels
            elif i == "N":
                totalCent = totalCent + .05

            # Dimes
            elif i == "D":
                totalCent = totalCent + .10

            # Quarters
            elif i == "Q":
                totalCent = totalCent + .25

            # Half-Dollars
            elif i == "H":
                totalCent = totalCent + .50

            # Whole Dollars
            elif i == "W":
                totalCent = totalCent + 1

            # Exception for invalid inputs
            else:
                print ("Invalid Coin: ", i)

        return float(totalCent)
             
# Account info storage class
class Account:
    # Defining attributes
    def __init__(self, accnum, first, last, ssn, pin, balance):
        self.accnum = accnum
        self.first = first
        self.last = last
        self.ssn = ssn
        self.pin = pin
        self.balance = balance

    # Deposit function to change balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # Withdraw function to change balance  
    def withdraw(self, amount):
        if self.balance < amount:
            return self.balance - amount
        self.balance -= amount
        return self.balance

    #  Function to check if PIN is correct
    def isPinValid(self, input_pin):
        if input_pin == self.pin:
            return True
        else:
            return False
            

    # Change PIN function
    def changePIN(self, newpin):
        self.pin = newpin

# Bank Class to hold Account list
class Bank():
  
    def addAccountToBank(self, account):
        # Number of Accounts/Users Supported by the Bank:
        u = 5

        #  Adding new accounts to banklist
        if len(ACCOUNTS) < u:

            ACCOUNTS.append(account)
            return True
        
        # Account creation cut off
        else:

            print("\n\nNo more accounts available.")
            return False

    # Remove account function
    def removeAccountFromBank(self, account):
 
            print("\nRemoving Account...")

            ACCOUNTS[account] = "Null"

            print("\nAccount Successfully Removed.")

    # Find account function
    def findAccount(self, account_number):
        
        index = 0
        found = False

        # Cycle through list to find account with correct account number attribute
        for i in ACCOUNTS:
            try:
                g = getattr(i, "accnum")
                if g == account_number:
                    found = True
                    break

            # Case if account does not exist
            except:
                print("Account not found for account: ", account_number)
                

        if found:
            print("\nAccount found!\n")
            return index

    # ----------------------------------------------------------------------
    # Extra credit func (Unfortunately does not work )
    # def addMonthlyInterest(self, annual_interest):
    #     monthly_interest = annual_interest //100

    #     for i in ACCOUNTS:
    #         amount = getattr(i, "balance")
    #         Iamount = amount * monthly_interest
    #     for i in ACCOUNTS:
    #         ACCOUNTS[i].deposit(Iamount)
    #         print("\nNew Balance:", getattr(ACCOUNTS[i], "balance"))
    # ----------------------------------------------------------------------

# Function to print menu screen
def displayO():

    print("\n============================================================\n")
    print("1. Open an account\n")
    print("2. Get account information and balance\n")
    print("3. Change PIN\n")
    print("4. Deposit money in account\n")
    print("5. Transfer money between accounts\n")
    print("6. Withdraw money from an account\n")
    print("7. ATM withdrawal\n")
    print("8. Deposit change\n")
    print("9. Close an account\n")
    print("10. Add monthly interest to all accounts\n")
    print("11. End program\n")
    print("============================================================\n")

# Bank Manager class / main function
class BankManager:
    
    def __init__(self):
        self.ACCOUNTS = ACCOUNTS

    def main():  #KEEP AN EYE ON THE B PARAMETER

        # Instance bank class
        b = Bank()

        # Welcome to bank
        print("\nWelcome to your personal banking interface!")
        print("\nPlease select an option below: ")
        
        # Display choice interface
        displayO() 
        
        # Transaction number variable
        tnum = 0

        # Start option loop
        while tnum != 11:
            
            # Loop to get a valid input
            user_input = False
            
            while user_input == False:
                
                try:
                    tnum = int(input("\nPlease enter an option number: "))
                    
                    if 0 < tnum < 12:
                        user_input = True

                    else:
                        print("\nPlease enter a valid option number.")
                        displayO()
                
                except:
                    print("\nPlease enter only valid option numbers.")
                    displayO()

        # Defining what to do with each option:

            # Create Account Option
            if tnum == 1:
                
                print("\nCreating new account...\n ")

                # List of used account numbers
                usedlist = []

                # Creating random account number
                accnum = random.randint(11111111,99999999)
                
                # Checking if random account number already exists
                if accnum not in usedlist:
                    usedlist.append(accnum)
                else: 
                     accnum = random.randint(11111111,99999999)

                print("\nYour account number is:", accnum)    

                # Prompt for First Name
                first = input("\nPlease input your first name:\n\n")
                
                # Prompt for Last Name
                last = input("\nPlease input your last name:\n\n")
                
                # Create a random SSN
                ssn = f"000-{random.randint(10,99)}-{random.randint(1000,9999)}"
                print("\nOwner SSN: ", ssn)

                # Create a random PIN
                pin = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
                print("\nYour Account PIN is: ", pin)

                # Set starting balance to 0
                balance = 0.0
                print("\nBalance: $", balance)

                # Use input to create an instance of account class
                a = Account(accnum, first, last, ssn, pin, balance)
                
                print("\nYour account has been created!\n")

                # Add account to bank list
                b.addAccountToBank(a)

                displayO()
            
            # Display Account Information
            elif tnum == 2:
                
                info = BankManager.promptForAccountNumberAndPIN(b)


                try:
                
                    #Print contents of account object returned from finding
                    print("\n============================================================")
                    print("Account information: ")
                    print("============================================================\n")
                    print("Account Number: ", getattr(ACCOUNTS[info], "accnum"))
                    print("\nUser First Name: ", getattr(ACCOUNTS[info], "first"))
                    print("\nUser Last Name: ", getattr(ACCOUNTS[info], "last"))
                    print("\nUser SSN: ", getattr(ACCOUNTS[info], "ssn"))
                    print("\nUser PIN: ", getattr(ACCOUNTS[info], "pin"))
                    print("\nUser Balance: $", getattr(ACCOUNTS[info], "balance"))
                    print("\n============================================================\n")
                
                    displayO()

                except:
                    print("Account does not exist.")

                    displayO()  

            # Change PIN
            elif tnum == 3:
            
                # Returns list index of account that matches accnum and pin
                info = BankManager.promptForAccountNumberAndPIN(b)

                match = False

                while match == False:

                    # Input for new pin
                    newpin = int(input("\nEnter desired new PIN: \n"))
                    
                    #  Input to check if new pin matches
                    cnewpin = int(input("\nPlease confirm new PIN: \n"))

                    if 0 < newpin < 9999:
                        if 0 < cnewpin < 9999:
                            if newpin == cnewpin:
                                
                                # Changing pin attribute of account w/ previously matching account number
                                ACCOUNTS[info].changePIN(newpin)

                                print("\nPIN Updated!\n")
                                match = True

                            # Checking if new pin matches confirmation
                            elif newpin != cnewpin:
                                print("\nInputs don't match, please try again\n")
                                continue
                    
                    # Making sure pin is only 4 digits
                    elif len(newpin) > 4:
                        print("Please enter only 4 numbers.")
                        continue
                    
                    # Making sure only numbers are entered
                    else:
                        print("Please enter only numbers.")
                        continue
                
                else:
                    
                    displayO()

            # Deposit Money
            elif tnum == 4:
                
                # Account to Deposit into
                info = BankManager.promptForAccountNumberAndPIN(b)

                # Amount to deposit
                amount = float(input("\nEnter amount to deposit in dollars and cents (e.g. 2.57): \n"))
                
                # Exception if amount is less than 0
                while amount < 0:
                    print("\nDeposit unsuccessful: cannot be a negative number\n")
                    amount = float(input("\nEnter amount to deposit in dollars and cents (e.g. 2.57): \n"))

                else:
                    # Deposit amount in target account
                    ACCOUNTS[info].deposit(amount)
                    print("\nNew Balance:", getattr(ACCOUNTS[info], "balance"))
                    displayO()
                
           
            # Transfer money between accounts
            elif tnum == 5:
                
                print("\nEnter account number of Account to transfer from: \n")
                
                # Account to transfer from
                tfrom = BankManager.promptForAccountNumberAndPIN(b)

                # Transfer amount
                tamount = float(input("\nEnter amount to transfer in dollars and cents (e.g. 2.57): \n"))
                
                while tamount < 0:
                    print("\nWithdrawal unsuccessful: cannot use negative numbers\n")
                    tamount = float(input("\nEnter amount to deposit in dollars and cents (e.g. 2.57): \n"))

                else:
                    # Withdraw amount from transfer account
                    if ACCOUNTS[tfrom].withdraw(tamount) < 0:
                        print("\nCould not process transfer. Insufficient funds.\n")
                        displayO()
                    else:
                        print("\nNew Balance of account",getattr(ACCOUNTS[tfrom], "accnum"), ": ", getattr(ACCOUNTS[tfrom], "balance"))
                
                print("\nEnter account number of Account to transfer to: \n")

                # Account to transfer to
                tto = BankManager.promptForAccountNumberAndPIN(b)

                while tamount > 0:

                    # Deposit in target account
                    ACCOUNTS[tto].deposit(tamount)
                    print("\nNew Balance of account",getattr(ACCOUNTS[tto], "accnum"), ": ", getattr(ACCOUNTS[tto], "balance"))
                    displayO()
                
                else:
                    print("\nDeposit unsuccessful: Insufficient funds\n")
                    displayO()


            # Withdraw Money
            elif tnum == 6:
                
                # Account to withdraw from
                info = BankManager.promptForAccountNumberAndPIN(b)

                # Amount to withdraw
                amount = float(input("\nEnter amount to withdraw in dollars and cents (e.g. 2.57): \n"))

                while amount < 0:
                    print("\nWithdrawal unsuccessful: cannot use negative numbers\n")
                    amount = float(input("\nEnter amount to deposit in dollars and cents (e.g. 2.57): \n"))

                else:
                    # Exception for account not having enough money
                    if ACCOUNTS[info].withdraw(amount) < 0:
                        print("\nCould not process withdrawal. Insufficient funds.\n")
                        displayO()

                    else:
                        print("\nNew Balance:", getattr(ACCOUNTS[info], "balance"))
                        displayO()
            
            # ATM Withdrawal
            elif tnum == 7:

                info = BankManager.promptForAccountNumberAndPIN(b)

                amount = int(input("\nEnter amount to withdraw in multiples of $5 (e.g. $5, $10, $15): \n"))
                
                # Making sure amount is divisible by 5 and less than 1000
                if 5 >= amount >= 1000 and amount %5 != 0:
                    
                    print("Invalid amount. Try again.")

                    amount = int(input("\nEnter amount to withdraw in multiples of $5 (e.g. $5, $10, $15): \n"))

                else:

                    if ACCOUNTS[info].withdraw(amount) < 0:
                        
                        print("\nCould not process withdrawal. Insufficient funds.\n")
                        
                        displayO()
                    
                    else:                      

                        print("\n")

                        # Amount of $20 bills
                        if amount >= 20:
                            print(amount // 20, "$20 Bills")
                            amount = amount % 20
                        
                        
                        # Amount of $10 bills
                        if amount >= 10:
                            print(amount // 10, "$10 Bills")
                            amount = amount % 10                            
                        

                        # Amount of $5
                        if amount >= 5:
                            print(amount // 5, "$5 Bills")
                            amount = amount % 5
                        

                        print("\nNew Balance:", getattr(ACCOUNTS[info], "balance"))
                    
                        displayO()
                    
            
            # Deposit Change
            elif tnum == 8:

                print("\nWelcome, please log into your account: \n")

                info = BankManager.promptForAccountNumberAndPIN(b)

                # Change Menu
                print("\n===================================================\n")
                print("o P represents a penny (1 cent)")
                print("o N represents a nickel (5 cents)")
                print("o D represents a dime (10 cents)")
                print("o Q represents a quarter (25 cents)")
                print("o H represents a half-dollar (50 cents)")
                print("o W represents a whole dollar (100 cents)")
                print("\n===================================================\n")

                coins = str(input("Please input the coins you'd like to deposit: ").upper())

                # Calling sorting function
                amount = CoinCollector.parseChange(coins)
                
                if amount > 0:

                    # Deposit amount in target account
                    ACCOUNTS[info].deposit(amount)
                    print("\n$", amount, " deposited into account.")
                    print("\nNew Balance:", getattr(ACCOUNTS[info], "balance"))
                    
                    displayO()
                
                else:

                    print("\nDeposit unsuccessful: Insufficient funds\n")
                    
                    displayO()

            
            # Close an Account
            elif tnum == 9:
                
                info = BankManager.promptForAccountNumberAndPIN(b)

                # Set variable to list index
                account = info

                # Call function to set to Null
                b.removeAccountFromBank(account)

                displayO()

            
            # EC: Add monthly extra credit
            elif tnum == 10:

                pass

                # print("\nApplying monthly interest to all accounts...\n")

                # b.addMonthlyInterest(2.5)

                # displayO()
            

            # Quit
            elif tnum == 11:
                print ("\nThank you for using our bank!\n")
                break
 
    # Function to match account number and pin
    def promptForAccountNumberAndPIN(bank_object):

        # Prompt for user input
        account_number = int(input("\nEnter your account number: \n"))
                
        # Check if account exists, returns index number
        info = bank_object.findAccount(account_number)
    
        try:
            if ACCOUNTS[info]:

                # Prompt for user input
                input_pin = (input("\nEnter your PIN number: \n"))
                
                # If user input matches PIN WITHOUT INSTANCING
                if ACCOUNTS[info].isPinValid(input_pin):
                    
                    print("\nCorrect PIN entered...\n")
                    
                    return info

                else:
                    print("Incorrect PIN")
                    
            
        except:
            displayO()

# Calling main function
BankManager.main()
    