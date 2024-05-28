
# Extend the program of Task #1 to output not only the maximum value, 
# but also the initial and final index of the elements to compute the maximum value

# Import random to create list/vector of positive and negative numbers
import random

# Create vector
num = random.sample(range(-500,500), 1000)

# Using the most efficient function from the class presentation
def MCSS(a):

    # Defining largest value, accumulation, and starting index(i)
    largest, acc, i, end = 0, 0, 0, 0
    
    # Loop to advance through subsequence window
    for j in range(len(a)):
        acc += a[j]

        # Noting the largest contiguous subsequences sum as we progress
        if (acc > largest):
            largest = acc

            # Setting the last j value used as the end index
            end = j
        
        # Resetting the starting index if a value in the window is negative
        elif (acc < 0):
            i = j + 1
            acc = 0
    
    # Printing the start index
    print("\nThe intial index used to find the maximum value was: ", i)

    # Printing the end index
    print("The final index used to find the maximum value was: ", end)

    # Returning the MCSS
    return largest

# Defining main function
def main():

    # Calling MCSS function and printing largest value
    print("The MCSS of the array inputted is: ", MCSS(num))

# Calling main function
if __name__ == "__main__":
    main()
