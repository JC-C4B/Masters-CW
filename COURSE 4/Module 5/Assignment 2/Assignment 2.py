

from random import randrange

# Creating a Double Array queue using the code from our presentation
class Queue:
    def __init__(self):

        # Implementing in and out arrays
        self.a_in = []
        self.a_out = []

        # Implementing the logical size (as seen in Dynamic array section of presentation)
        self.s = 0

        # Implementing allocated memory size (as seen in Dynamic array section of presentation)
        self.m = 2 * self.s
    
    # Defining queue function
    def enqueue(self, d):
        
        # Case if the queue is at max capacity
        if self.s == self.m:

            # Allocate more space, append, note the increase in size, and return 
            # True for Costly operation
            self.m = self.m*2
            self.a_in.append(d)
            self.s += 1
            return True

        # Case if queue is not at max capacity
        else:

            # Append to queue, note the increase in size, and return False to indicate cheap operation
            self.a_in.append(d)
            self.s += 1
            return False

    # Defining dequeue function
    def dequeue(self):
        
        # Case if there is nothing in the array
        if not self.a_out:
            return None
        
        # Moving element from one array to the other, noting change in size, returning Dequeued element
        if (self.a_out == []):
            for d in self.a_in:
                self.a_out.append(d)
            self.a_in = []
        
        self.s -= 1
        return self.a_out.pop(0)

# Defining Costly/Cheap test function using the code from our presentation
def test(initialSize, probRemove):

    # Keeping track of the amount of Costly & Cheap operations
    accCheap, accCostly = 0, 0

    # Implementing our Queue class into the test, setting size and Max size to input
    testqueue = Queue()
    testqueue.s = initialSize
    testqueue.m = 2 * testqueue.s

    # Loop for randomly decided enqueues/dequeues
    for i in range(100000):

        # Dequeuing if less than the probability to remove
        if (randrange(100) < probRemove):
            if (testqueue.s > 0):
                testqueue.dequeue()
                testqueue.s -= 1
                accCheap += 1
        
        # Enqueuing if greater than the probability to remove
        else:
            if testqueue.enqueue(i):
                accCostly += 1
            else:
                accCheap += 1
            
    # Printing results after every test
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costy: {:7} ({:3.1}%)".format(accCostly,accCostly/(accCostly+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,accCheap/(accCostly+accCheap)))

def main():

    # # Calling test function with test cases used in previous assignment
    # # as well as some new ones
    # test(1, 10)
    # test(1, 25)
    # test(1, 50)
    # test(10, 70)
    # test(100, 99)
    # test(2, 10)
    # test(20, 5)
    # test(500, 5)

    # # Using to seperate results
    # print("----------------------------------------------------------------")

    # # Using test sizes from the dynamic array section of the presentation
    # # to double check accuarcy of the program
    # test(20, 1)
    # test(20, 5)
    # test(50, 1)
    # test(50, 5)
    # test(100, 1)
    # test(100, 5)

    # print("----------------------------------------------------------------")
    
    # Asking the user for input and computing the expected number of 
    # Costly and Cheap operations with a large random sample (100,000 randomly decided operations)
    ins = int(input("Please enter your desired intial size: "))
    pr = int(input("Please enter your desired probabilty of removal: "))

    test(ins, pr)


if __name__ == "__main__":
    main()



























