

# Specified Arrays
A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

# Input: An array(A), and two elements/indexes from said array, i and j
# Output: an updated array with A[i] and A[j] swapped
def Swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Input: An array of integers
# Output: a sorted array in ascending order, done by prioritizing the placement of smallest elements first
def SelectionSort(A):

    # Showing original Array
    print("\nOrigin Array being sorted: ", A)

    # Counter for the total amount of comparisons done, not just the successful ones
    compcount = 0

    # Finding the first unsorted element in the array
    for i in range(len(A) - 1):
        m = i

        # Finding smallest element in the array and adding to the comparison counter
        for j in range(i + 1, len(A)):

            if A[j] < A[m]:
                m = j
                compcount += 1

            else:
                compcount += 1

        # Putting the smallest element at the front of the list and printing each 
        Swap(A, i, m)
        print(A)
    
    # Printing the total amount of comparisons executed
    print("Total amount of comparisons executed: ", compcount)

# Defining main function
def main():

    # Sorting each array 
    SelectionSort(A1)
    print("---------------------------------")
    SelectionSort(A2)
    print("---------------------------------")
    SelectionSort(A3)
    print("---------------------------------")
   
# Calling main function
if __name__ == "__main__":
    main()