
# Short report/comments can be found at the bottom of this file
import time
import random

# Starting with an input to create a random list of a specified size
length = int(input("Hello, please input an integer between 1000 - 10000 to create a random list of that length.\n"))

# Creating a random list of the inputted size
num = random.sample(range(0,length), length)

# Defining function to swap the positions of elements in a list
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] =A[temp]

# Defining function for our sort method
def SelectionSort(A):

    for i in range(len(A) - 1):
        m = i

        # Finding the smallest element in the array
        for j in range(i + 1, len(A)):
            if A[j] < A[m]:
                m = j
        
        # Swapping elements into increasing order
        Swap(A, i, m)
    
# Creating a function to time the Selection sort method
def timeSelectionsort():

    print ("Starting Selection Sort method\n")

    # Recording the start time of the function
    start = time.time()

    # Calling sort function
    SelectionSort(num)

    # Recording the end time of the function
    end = time.time()

    # Subtracting the start time from the end to get the time it took to complete the function
    print(f"Time taken by Selection sort method: {end - start} sec\n")
    
# Defining our main function
def main():

    timeSelectionsort()

# Calling main function
if __name__ == "__main__":
    main()

# -------------------------------------------------------------------------------------------
# Timings, Calculations, and Comments below:
# -------------------------------------------------------------------------------------------
# Timings
# -------------------------------------------------------------------------------------------
# 1000: 0.02786850929260254 sec
# 2000: 0.12362122535705566 sec
# 3000: 0.24844717979431152 sec
# 4000: 0.4957394599914551 sec
# 5000: 0.705031156539917 sec
# 6000: 0.9386544227600098 sec
# 7000: 1.3207404613494873 sec
# 8000: 1.854264497756958 sec
# 9000: 2.0884644985198975 sec
# 10000: 2.5349960327148438 sec

# -------------------------------------------------------------------------------------------
# Calculations
# -------------------------------------------------------------------------------------------
# Using the trick alluded to in class I could tell the Big-O time complexity of selection sort is O(n^2) 
# because it consists of two for loops. Aside from that is has a constant of 3 because it executes the 
# swap function (3 lines) with every iteration. 

# -------------------------------------------------------------------------------------------
# Comments
# -------------------------------------------------------------------------------------------
# With a time complexity of O(n^2) I was expecting the difference in time between an array of 1000 and 10000 to be two decimal places
# and was pleasantly surprised to see how arrcuate that was. With each calculation being done on a completely different randomized set 
# of numbers, that is larger in size than the previous set tested, the formula for time complexity is still shockingly consistent. 

# After attempting to use cProfile and somehow getting shorter times for larger numbers 
# (in spite of my laptop taking a significantly larger amount of time to calculate the results of the sorting function)
# I decided to use the timing method previously taught in the first course of our program.
# Creating the random list was easy thanks to the refresher from our in-class assignments,
# And creating the timer was also simple.
# -------------------------------------------------------------------------------------------
