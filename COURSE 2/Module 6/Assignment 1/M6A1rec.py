
# Importing sys to higher the recursion limit
import sys
# Importing math to use the floor function
import math

# Raising recursion limit
sys.setrecursionlimit(5000)

# Input: Any positive integer, n
# Output: The number of digits found in the binary representation of the positive integer, n
def digi(n):

    # If n = 1, return a digit count of 1
    if n == 1:
        return 1

    #  If n > 1, add 1 and recursively divide n by 2 until n == 1 , executing the exception (totaling 2 + (n/2))
    else:
        return 1 + math.floor(digi(n/2))

# Define main function
def main():

    # Find amount of binary digits for 32
    print(digi(32))
    print("--------------------\n")
    
    # Find amount of binary digits for 75
    print(digi(75))
    print("--------------------\n")

# Call main function
if __name__ == "__main__":
    main()



# Input: A positive integer n
# Output: The positive sum of the squares of the inputted integer
def sqsum(n):

    # Exception for whne the inputted integer is 1
    if n == 1:
        return n

    # Adding the squares of the integers from one to n-1 to n^2
    else:
        return (n**2 + sqsum(n - 1))


# Define main function
def main():

    # Find amount of binary digits for 32
    print(sqsum(5))
    print("--------------------\n")
    
    # Find amount of binary digits for 75
    print(sqsum(10))
    print("--------------------\n")

# Call main function
if __name__ == "__main__":
    main()





























