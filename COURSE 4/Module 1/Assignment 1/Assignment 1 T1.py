
# Create a program that randomizes a vector of 1000 positive and negative integers, then finds the maximum contiguous subsequence sum value
# and prints out the maximum value

# Import random to create list/vector of positive and negative numbers
import random

# Create vector
# num = random.sample(range(-500,500), 1000)
num = [-2, 34, -16, 9, -32, 12, 38, -1, 81, -76, 9, 34, -4, 12]

# Using the most efficient function from the class presentation
def MCSS(a):

    # Defining largest value, accumulation, and starting index(i)
    largest, acc, i = 0, 0, 0
    
    # Loop to advance through subsequence window
    for j in range(len(a)):
        acc += a[j]

        # Noting the largest contiguous subsequences sum as we progress
        if (acc > largest):
            largest = acc
        
        # Resetting the starting index if a value in the window is negative
        elif (acc < 0):
            i = j + 1
            acc = 0
    
    # Returning the MCSS
    return largest

# Defining main function
def main():

    # Calling MCSS function and printing largest value
    print("The MCSS of the array inputted is: ", MCSS(num))

# Calling main function
if __name__ == "__main__":
    main()

































