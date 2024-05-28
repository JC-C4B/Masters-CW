



# # Arrays to be tested:
# A1 = [12,  23,  37,  45,  63,  82,  47,  75,  91,  88,  102]
# A2 = [-1.7,  6.5,  8.2,  0.0,  4.7,  6.3,  9.5,  12.2,  37.9,  53.2]

# # Input: An array of numbers, a, and an integer indicating how many array values should be included in the calculations
# # Output: The calculated value of the array's mean
# def amean(a, n):

#     # Case exception for when the number of values reaches 0
#     if n == 0:

#         return a[n]

#     # Plugging in formula given to find the mean, Number of values = n
#     else: 
#         return (((n - 1)/ n * amean(a, n - 1)) + (1/n) * a[n - 1])

# # Defining main function
# def main():

#     # Printing the means of the given arrays
#     print("------------------------------")
#     print("A1 mean: ", amean(A1, 11))
#     print("------------------------------")
#     print("A2 mean: ", amean(A2, 10))
#     print("------------------------------\n")

# # Calling main function
# if __name__ == "__main__":
#     main()



# # Given arrays:
# A1 = [100, 87, 85, 80, 72, 67, 55, 50, 48, 42, 40, 31, 25, 22, 18] 

# # Input: An array, A in descending order, the starting and ending length value fo the array, and a key, k
# # Output: Index i such that A[i] = k or None if no match is found
# def BinarySearch(A, start, end, k):
    
#     # Condition for key not found
#     if start > end:
#         return None

#     # Printing every subscript of the function
#     elif end >= start:
#         print(A[start:end])

#     # Defining mid-point
#     m = ((end + start) // 2)

#     # Condition for key found
#     if A[m] == k:
        
#         return m

#     # Condition for key being > m, meaning it is in the start half
#     elif A[m] < k:
        
#         return BinarySearch(A, start, m - 1, k)
    
#     # Condition for key being < m, meaning it is in the end half
#     else:

#         return BinarySearch(A, m + 1, end, k)

# # Defining main function
# def main():

#     # Searching for each given key and printing results
#     print("Given Array, Key = 87, found index number: ", BinarySearch(A1, 0, 14, 87))
#     print("------------------------------")
#     print("Given Array, Key = 48, found index number: ", BinarySearch(A1, 0, 14, 48))
#     print("------------------------------")
#     print("Given Array, Key = 33, found index number: ", BinarySearch(A1, 0, 14, 33))
#     print("------------------------------")
#     print("Given Array, Key = 10, found index number: ", BinarySearch(A1, 0, 14, 10))
#     print("------------------------------")
    
# # Calling main function
# if __name__ == "__main__":
#     main()


# Input: Two non-negative integers
# Output: The greatest common divisor of the two inputs
def GCD(m, n):

    # Printing every integer passing through the recursive call
    print(m, n)

    if n == 0:
        return m

    else:
        return GCD(n, m % n)

# Defining main function
def main():

    # Finding GCD for given instances
    print("The GCD for (2468, 1357) is: ", GCD(2468, 1357))
    print("------------------------------")
    print("The GCD for (111, 378) is: ", GCD(111, 378))
    print("------------------------------")
    print("The GCD for (123456789, 987654321) is: ", GCD(123456789, 987654321))
    print("------------------------------")

# Calling main function
if __name__ == "__main__":
    main()






























