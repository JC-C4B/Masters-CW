

# Creating Person class
class Person:

    def __init__(self, name, familyName, age):
        self.name = name
        self.famN = familyName
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, {self.famN}, {self.age}"

    def getname(self):
        return self.name
    
    def getfamN(self):
        return self.famN
    
    def getage(self):
        return self.age

# Creating our stack
stack = []

# Getting data from our csv file to put in the stack
with open("People.csv", "r") as data:
    for line in data.readlines():
        words = line.split(",")
        stack.append(Person(words[0], words[1], words[2]))

# Function to pop people from stack
def pstack():

    check = False

    while not check:    
        
        # Ask user for input
        print("\n+-------------------------------------------------------------------------+")
        x = int(input("\nPlease enter an amount, 1 - 4, of people you'd like to pop out of the stack\n"))

        L = len(stack)

        # Checking if input is valid
        if 0 < x < 5:
            
            # If input is less than length of list
            if x < L:
                
                # Remove last person added to the last
                for i in range(x):
                    
                    print("\nRemoving last person added to the list: ", stack.pop())
                
                # Print person currently at the top of the list
                try:
                    
                    print("\nThe current person at the top of the list is: ", stack[-1])

                except IndexError:
                    print("\nThe list has been emptied.\n")
                
                # Stop loop
                check = True    
            
            # If input is greater than the length of the list
            elif x > L:

                # Remove remaining people in the list
                for i in range(L):
                    
                    print("\nRemoving last person added to the list: ", stack.pop())

                # Inform user that amount was greater than length of list
                print("\nAmount entered was greater than remaining list.")    

                # Print person currently at the top of the list
                print("\nThere is currently no one at the top of the list.")

                # Inform user that the list is empty
                print("\nThe list has been emptied.\n")

                # Stop loop
                check = True 

            # If input is equal to length of list
            elif x == L:

                # Remove remaining people in the list
                for i in range(x):
                    
                    print("\nRemoving last person added to the list: ", stack.pop())

                # Inform user that amount was greater than length of list
                print("\nAmount entered was equal to remaining list.")    

                # Print person currently at the top of the list
                print("\nThere is currently no one at the top of the list.")

                # Inform user that the list is empty
                print("\nThe list has been emptied.\n")

                # Stop loop
                check = True
                
        # If not a number between 1 - 4
        else:
            print("\nPlease enter a number 1 - 4 only.")
            continue

# Function to check if stack is empty
def isEmpty():

    if len(stack) == 0:
        return True
    
    else:
        return False

# Defining main function
def main():

    # Loop while list not empty
    while isEmpty() == False:
        pstack()

    # End program if list is empty
    else:
        print("No one is left to pop from the list.\n") 
        print("Now closing the program ... Goodbye!")    

# Calling main function
if __name__ == "__main__":
    main()




    
































