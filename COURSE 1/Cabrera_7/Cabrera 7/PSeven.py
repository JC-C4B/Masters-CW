
# Importing all necessary functions for the test
import time
import random
from random import shuffle

from datetime import datetime

from selectionSort import selection_sort
from bubbleSort import bubblesort

# Defining amount of numbers for list 
NumberOfEntries = 300000

# Create list using random import
mylist = [random.sample(range(300000), NumberOfEntries)]

# Shuffling the list to create a random order
shuffle(mylist)

# Creating a function to time the Selection sort method
def timeSelectionsort():
    print ("Starting Selection Sort method\n")
    mycopy = mylist.copy()
    start = time.time()
    selection_sort(mycopy)
    end = time.time()
    print(f"Time taken by Selection sort method: {end - start} sec\n")

#  Creating a function to time the Bubble sort method
def timeBubblesort():
    print ("Starting Bubble Sort method\n")
    mycopy = mylist.copy()
    start = time.time()
    bubblesort(mycopy)
    end = time.time()
    print(f"Time taken by Bubble sort method: {end - start} sec\n")

# Defining the main function & calling the timers
def main():

    print("Time test starting, please be patient ...\n")
    timeSelectionsort()
    timeBubblesort()

# Calling main function
if __name__ == "__main__":
    main()


# Of the two sorting algorithms, Selection sort is the most efficient. It's code is more streamlined and has a better
# approach toward sorting a list by finding the smallest item and bringing it to the front, instead of having to comb
# through the list over and over to organize it fully. This was proven through Selection sort's shorter time to complete.


























