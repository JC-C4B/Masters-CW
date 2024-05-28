import numpy as np

def main():

    # Input for the number of variables in the problem
    variables = int(input("Please input the total number of variables: "))

    # Input for the objective function coefficient
    FX = np.array([eval(input(f"Please enter the objective function coefficient for x{i+1}: ")) for i in range(variables)])

    # Input for the individual coefficients of each constraint
    A = np.array([[eval(input(f"Please enter the coefficient for x{i+1} in constraint {j+1}: ")) for i in range(variables)] for j in range(variables)])

    # Input for the constraint limits
    B = np.array([eval(input(f"Please enter the limit for the constraint {i+1}: ")) for i in range(variables)])

    # Finding the dot product between the inverse of matrix A and matrix B / The solution to the inputted linear equation
    X = np.linalg.inv(A).dot(B)

    # Rounding the solutions to get each variables real number
    OX = np.floor(X)

    # Finding the optimal value using the objective function coefficient
    Optimal = np.dot(FX, X)
    
    # List for individual variables
    individual = []

    # Computing for the individual variables; this gave me the most issues and I am stil not
    # entirely sure what else I can do to find the values individually.
    for i in range(variables):

        # Making a copy of A 
        A2 = A.copy()

        #  Replacing corresponding rows with the constraints from B
        A2[i, :] = B

        # Solving for the individual variables and appending to the list
        Xi = np.linalg.inv(A2).dot(B)
        individual.append(np.dot(FX, Xi))

    # Printing the results
    print(f"\nFor the linear equation provided, the optimal value would be: ${Optimal},")
    print(f"and the most optimal (rounded) solution to the equation would be: {OX}")
    print(f"The solution for individual variables are: {individual}")

# Calling the main function
if __name__ == "__main__":
    main()