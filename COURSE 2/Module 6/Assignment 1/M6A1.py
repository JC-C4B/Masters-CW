
# # Importing math to use the floor function
# import math

# # Input: Any positive integer, n
# # Output: The number of digits found in the binary representation of the positive integer, n
# def digi(n):
    
#     # Making the function iterative to find the solution:
#     # Kept running into recursion errors even after raising the recursion limit through sys
#     result = 0
#     temp = n

#     # If n = 1, return a digit count of 1
#     if n == 1:
#         return 1

#     #  If n > 1, add one digit to the counter for every possible division by 2
#     else:
#         while temp >= 1:
#             result += 1
#             temp = math.floor(temp/2)
        
#         # Return the total
#         return result

# # Define main function
# def main():

#     # Find amount of binary digits for 32
#     print(digi(32))
#     print("--------------------\n")
    
#     # Find amount of binary digits for 75
#     print(digi(75))
#     print("--------------------\n")

# # Call main function
# if __name__ == "__main__":
#     main()


# Input: A positive integer n
# Output: The positive sum of the squares of the inputted integer
def sqsum(n):

    # Exception for whne the inputted integer is 1
    if n == 1:
        return n

    # Calculating the value of each sqaure and adding them together to get our answer
    else:
        temp = n
        result = 0

        while temp != 0:
            result += temp**2
            temp = temp - 1
        return result

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






















