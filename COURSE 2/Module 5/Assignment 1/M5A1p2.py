


# Specified Arrays
A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52] 
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63] 
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

# Input: An array(A), and two elements/indexes from said array, i and j
# Output: an updated array with A[i] and A[j] swapped
def Swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Input: An array of integers
# Output: An array sorted in decreasing order
def BubbleSort(A):

    # Showing original Array
    print("\nOrigin Array being sorted: ", A)

    # Amount of swaps executed
    swapcount = 0

    # Amount of comparisons executed
    compcount = 0

    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if A[j + 1] > A[j]:
                Swap(A, j + 1, j)

                # If swap is successful, add to counter
                swapcount += 1
            
            # Add one to the comparison counter regardless of whether it was successful or not
            compcount += 1
        
        # Print after every iteration
        print(A)
        
    # Printing the total amount of comparisons executed
    print("Total amount of comparisons executed: ", compcount)

    # Printing the total amount of swaps executed
    print("Total amount of swaps executed: ", swapcount)

# Define main function
def main():

    # Bubble sort all specified arrays
    BubbleSort(A4)
    print("---------------------------------")
    BubbleSort(A5)
    print("---------------------------------")
    BubbleSort(A6)
    print("---------------------------------")

# Call main function
if __name__ == "__main__":
    main()

























