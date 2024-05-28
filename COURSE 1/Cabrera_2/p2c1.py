
# Introduction to code, specifying parameters.
print("\nHello!")
print("\nPlease enter positive integers for a & b to test whether either can evenly divide the other:")

#Create main function
def main():
    
    #Start a loop;
        while True:
            
            try:
            
            #Ask user for positive integers through input, make input into variables
                a = eval(input("\nEnter a: "))
                b = eval(input("Enter b: "))
            
            #Restart loop if there is an issue with the value given
            except ValueError:    
                print("\nSomething went wrong, let's try again:")
                continue
            #Restart loop if characters are entered instead of numbers
            except NameError:
                print("\nPlease only use positive integers; letters and characters will not work.")
                continue
            #Fail safe in case of unexpected failure.
            except:
                print("\nSomething went wrong. Please only use positive integers.")   
                continue
            
            #Restart loop if the integer is not positive
            if a < 0:
                print("\nPlease only use positive integers.")
                continue
            elif b < 0:
                print("\nPlease only use positive integers.")
                continue
            #Restart loop if a number is being divided by 0
            elif b == 0:
                print("\nUnfortunately, we cannot divide by 0. Please only use positive integers.")
                continue
            #Find remainders of correct integers to see if they can be divided evenly;
            elif a % b == 0:
                print("\nTrue, a,", a, ",is evenly divided by b,", b)
                return True
            elif b % a == 0:
                print("\nTrue, b,", b, ",is evenly divided by a,", a)
                return True
            #Prep for scenario in which they do not divide evenly
            elif a % b and b % a != 0:
                print("\n", a, "and", b, "are not evenly divisble by one another.")
                print("\nRestarting loop...")

#Taking return from function to choose what happens next
while main() == True:
    print("The inputted integers are evenly divisible!")
    continue

#Execute function 
if __name__ == "__main__":
    main()
































