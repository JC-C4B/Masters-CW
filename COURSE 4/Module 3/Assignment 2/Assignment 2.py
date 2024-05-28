



# ------------------------------------------------------------------------------------------------------------------
# I coded the tribonacci functions using the examples given in our presentation, and used both so as not to 
# make a mistake and not fulfill the requirements
# ------------------------------------------------------------------------------------------------------------------

# Defining Tribonacci function with n attribute for user input, and list 'values' for previous calculations
def tribo1(n, values):

    # Case if n has already been computed
    if (n < len(values)):
        if (values[n] != 0):
            return values[n]
    
    # Solving for the 'n'th placement if not already in values
    ans = (tribo1(n-1, values)) + (tribo1(n-2, values)) + (tribo1(n-3, values)) 

    # Appending to the values list
    values += [0] * (n-len(values)) + [ans]

    # Returning the answer for the 'n'th value
    return ans

# ------------------------------------------------------------------------------------------------------------------
# Second function, currently not in main call but still functional
# ------------------------------------------------------------------------------------------------------------------

# Defining Tribonacci function with n attribute for user input
def tribo2(n):

    # Setting first 3 elements to 1
    a, b, c = 1, 1, 1

    # Case for elements before the 3rd to return 1
    if (n < 3):
        return 1
    
    # Case if searching for an element >= 3
    # Iterating through all numbers n times to get to the 'n'th value
    for i in range(3, n):
        a, b, c = b, c, a + b + c

    # Finally returning c's final calculation as it is equal to the 'n'th value
    return c

# ------------------------------------------------------------------------------------------------------------------

# Defining main function
def main():

    # User input
    n = int(eval(input("Enter an integer: ")))

    # Defining values
    values = [0, 1, 1, 1]

    # Print statement
    print("The {}-th element of the Tribonacci sequence is {}".format(n, tribo1(n, values)))

# Calling main function
if __name__ == "__main__":
    main()
































