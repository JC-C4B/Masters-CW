


# Importing random to create random unique dataset
import random

# Creating random array
num = []
length = 100
for i in range(length):
    num.append(random.randint(0,1000))

# Defining a function to sort and find the mode of an array
def mode(a):
    
    # Sorting the array
    a.sort()

    # Defining placeholder values
    maxValue, maxCount = 0, 0
    count = 1

    # Setting our fist value to compare to as the first in the array
    currentvalue = a[0]

    # Comparing with 'currentvalue' starting at the second in the array
    for i in range(1, len(a)):

        # Comparing and adding to count
        if a[i] == currentvalue:
            count += 1
        
        # Comparing current count to max and changing maxcount if necessary
        elif (count > maxCount):
            maxCount = count
            maxValue = currentvalue
        
        # Setting new current value and resetting count for next iteration
        else:
            count = 1
            currentvalue = a[i]
    
    # Returning the mode of the array
    return maxValue

# Defining main function
def main():

    # Calling mode function
    print("The mode of the array is:", mode(num))

# Calling main function
if __name__ == "__main__":
    main()





























