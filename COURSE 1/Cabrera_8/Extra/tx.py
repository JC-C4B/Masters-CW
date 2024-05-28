            elif tnum == 2:
                
                info = BankManager.promptForAccountNumberAndPIN(b)
                
                print(ACCOUNTS)

                # print_me = [getattr(information, "accnum"), getattr(information, "first"), 
                # getattr(information, "last"), getattr(information, "ssn"), getattr(information, "pin"), getattr(information, "balance")]

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




    def findAccount(self, account_number):
        
        index = 0
        found = False
        null = False

        for i in ACCOUNTS:
            g = getattr(i, "accnum")
            if g == account_number:
                found = True
                break
            # OPTION FOR NULL not sure if nec. KEEP AN EYE ON -------------------------------------------------------*******
            elif i == "Null":
                null = True
                break
            index = index + 1
        
        if found:
            print("Account found!")
            return index
        
        elif null:
            return index

        else:
            print("Account not found for account: ", account_number)







def promptForAccountNumberAndPIN(bank_object):

        # Prompt for user input
        account_number = int(input("\nEnter your account number: \n"))
                
        # Check if account exists, returns index number
        info = bank_object.findAccount(account_number)
    

        # If Null condition WITHOUT INSTANCING
        if ACCOUNTS[info] == "Null":

            # What to print if account is Null:
            print("\nNull: This account was previously removed.\n")
                        
            displayO()   

        # Prompt for user input
        input_pin = (input("\nEnter your PIN number: \n"))
        
        # If user input matches PIN WITHOUT INSTANCING
        if input_pin == getattr(ACCOUNTS[info], "pin"):
            
            print("\nCorrect PIN entered...\n")
            
            return info

        else:
            print("Incorrect PIN")

    def removeAccountFromBank(self, account):
        
        account_number = input("\nEnter your account number: \n")
        index = 0
        found = False
        
        for account in ACCOUNTS:
            if account == account_number:
                found = True
                break
            index = index + 1

        if found: 
            print("\nRemoving Account...")
            ACCOUNTS[index] = "Null"
            print("\nAccount Successfully Removed.")