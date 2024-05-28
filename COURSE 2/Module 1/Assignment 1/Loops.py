

import random

# Defining swap function
def swap(list):
    
    x = 0
    
    while x != len(list):

        y = 0
        z = 1
        
        list[y], list[z] = list[z], list[y]

        x += 1
        y += 2
        z += 2


    else:
        return list

# Defining main function
def main():

    # Prompt for input
    check = False

    while not check:
        
        try:

            urange = int(input("Please enter an integer between 9 and 21: "))

        except ValueError: 
            print("\nThe input was not a valid integer, please try again: \n")
            continue
        
        else:

            check = True

    # Create random list
    ulist = random.sample(range(30), urange)

    print(ulist)

    swap(ulist)

    print(ulist)

if __name__ == "__main__":
    main()







    

    



































