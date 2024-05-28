

# Importing math module for the log 2 function
from math import log2

# Importing random module to pick random values of x
import random

# Defining 'myfunction' and using the code shown in class
def myFunction(x):
    
    if (x == 0):
        return 0
    
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x)) ** 3
    
    elif ((log2(x) * 2) % 23) < (x % 19):
        return (log2(x) * 2) ** 3
    
    else:
        return (log2(x) ** 2) - x

# Defining the hillclimbing function, and using this webpage for reference:
# https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/#
def hc():

    # Setting x to a random integer
    x = random.randint(1,9998)

    # Print the initial search value 
    print("Initial search value: ", x)

    # Starting a loop to find the largest value for the function
    while True:

        # Getting the neighbors of x
        neighbors = [x - 1, x + 1]

        # Getting the values of each neighbor using myFunction, putting in a list
        nv = [myFunction(n) for n in neighbors]

        # Using 'max' to find the maximum value of the neighbors
        maxnv = max(nv)
        
        # Case if the maximum value is found
        if maxnv <= myFunction(x):
            return x
        
        # If the max is not found, try the neighbor with the highest value
        else: 
            x = neighbors[nv.index(maxnv)]


# Defining main function
def main():

    # Printing the results of the Hill Climbing Function
    print("The largest value for 'myFunction' found was: ", hc())
    
    # Testing to check accuracy of answers provided by HC
    # print(myFunction(4533))
    # print(myFunction(4536))

# Calling main function
if __name__ == "__main__":
    main()
    


























