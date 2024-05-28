


# # First set of numbers, to be divided by 7
# fset = [20, 21, 25, 28, 33, 34, 35, 36, 41, 42]

# # Second set of numbers, to be divided by 9
# sset = [18, 54, 76, 81, 36, 48, 99]

# # Input: An array of numbers, and the integer they are to be divided by
# # Output: the amount of numbers in the array that are divisible by the inputted integer
# def diviseven(a, d):

#     count = 0

#     # Searching through inputted array and adding one to the count for every number divisible by inputted integer
#     for i in range(len(a)):
#         if a[i] % d == 0:
#             count += 1

#     # Returning the count after going through the entire array
#     return count

# # Defining main function
# def main():

#     # Inputting respective arrays and divisors.
#     print("\nThe amount of numbers divisible by 7 in an array of", fset, "is: ")
#     print(diviseven(fset, 7))

#     print("\nThe amount of numbers divisible by 9 in an array of", sset, "is: ")
#     print(diviseven(sset, 9))

# # Calling main function
# if __name__ == "__main__":
#     main()


# # First array
# fset = [50, 120, 250, 100, 20, 300, 200]

# # Second array
# sset = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]

# # Input: an array of numbers
# # Output: the absolute value of the smallest gap between two elements in the array
# # Function to find the smallest gap in the array
# def smallestgap(a):

#     # Setting a constant larger that any element in the array to make argument swap the value with the first entry
#     smallest = 999999

#     # Cycling through the array and finding the absolute value from subtracting each pair, then filtering which is the smallest
#     for i in range(0, len(a) - 1):
#         for j in range(i + 1, len(a)):
#             if abs(a[i] - a[j]) < smallest:
#                 smallest = abs(a[i] - a[j])
                
#     return smallest

# # Defining main function
# def main():

#     # Inputting the first array
#     print("\nThe smallest gap between all pairs of elements in the array", fset, "is: ")
#     print(smallestgap(fset))

#     # Inputting the second array
#     print("\nThe smallest gap between all pairs of elements in the array", sset, "is: ")
#     print(smallestgap(sset))

# # Calling main function
# if __name__=="__main__":
#     main()


# Matrix 1
no = 2
moa = [[2, 7], [3, 5]]
mob = [[8, -4], [6, 6]]

# Matrix 2
nt = 3
mta = [[1, 0, 2], [3, -2, 5], [6, 2, -3]]
mtb = [[.3, .25, .1], [.4, .8, 0], [-.5, .75, .6]]

# Input: The dimension of our matricies, n, and two nxn matricies
# Output: the product of multiplying the two matricies
def multimatri(n, mo, mt):

    # Creating a blank matrix using the given n dimension to fill with correct answers after calculation
    product = [[0 for i in range(n)] for j in range(n)]

    # I for the rows in our first matrix
    for i in range(n):
        # J for the columns in the second matrix
        for j in range(n):
            # K for the rows in the second matrix
            for k in range(n):
                # Filling in the empty product matrix with the correct product for each element
                product[i][j] = product[i][j] + mo[i][k] * mt[k][j]

    return product

# Defining main function
def main():
    
    # Inputting first matrix
    print("\nThe product of multiplying matricies", moa, " and, ", mob, " is: ")
    print(multimatri(no, moa, mob))

    # Inputting second matrix
    print("\nThe product of multiplying matricies", mta, " and, ", mtb, " is: ")
    print(multimatri(nt, mta, mtb))

# Calling main function
if __name__ == "__main__":
    main()



























