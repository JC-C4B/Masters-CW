
# Specified Array/ Polynomial
A7 = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]

# Input: an integer X, and and exponent integer P
# Output: the result of the integer X raised to the power of exponent P
def power(x, p):

    answer = 0

    # Case for the power being 0
    if p == 0:
        return 1
    
    else:
        
        # Multiplying the integer by itself p times
        for i in range(p):
            
            if answer == 0:
                answer += x
            
            else:
                answer *= x
    
    return answer

# Input: A polynomial array and an integer x used to solve the polynomial
# Output: The resulting value of the polynomial once evaluated
def polyeval(A, x):

    # Stating the inputted values
    print("\nThe polynomial array inputted was:\n", A)
    print("\nThe value of x inputted was:\n", x)

    answer = 0

    # Solving the polynomial with input
    for i in range(len(A)):

        # Current element in array being worked on
        vari = A[i]

        # Current value of x after being raised to coinciding exponent
        pvari = (power(x, i))

        # Multiplying and adding to total
        A[i] = vari * pvari
        answer += A[i]
    
    # Returning final answer
    return answer


# Defining main function
def main():

    # Evaluating and printing the final answer of the polynomial
    print("-------------------------------------------------")
    print("\nThe value of the polynomial would be: ", polyeval(A7, 5.4),"\n")
    print("-------------------------------------------------\n")

# Calling main function
if __name__ == "__main__":
    main()
    

































