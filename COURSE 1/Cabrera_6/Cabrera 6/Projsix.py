

# Creating a class for the Deque
class Deque:
        
    # Initializing the class as a list
    def __init__(self):
        self.queue = []

    # Creating function to display the queue
    def displayQ(self):
        print("\nOur current queue is: ")
        print(self.queue)

    # Creating a function to add an item to the front of our queue
    def addfrontQ(self, item):
        self.queue.append(item)
        
    # Creating a function to add an item to the back of our queue
    def addbackQ(self, item):
        self.queue.insert(0, item)

        # Creating a function to remove the item at the front of the queue
    def pfront(self):
        print("\nRemoving first item in queue:", self.queue.pop())
        

    # Creating a function to remove the item at the back of the queue 
    def pback(self):
        print("\nRemoving last item in queue:", self.queue.pop(0))
        

    # Creating a function to check if the queue is empty
    def isEmpty(self):
        if(self.queue == []):
            return True
        else:
            return False

# Defining our main function            
def main():

    # Creating an instance of the queue
    deq = Deque()
    
    # Adding different things into the queue
    deq.addbackQ(44)
    deq.addbackQ("Spider man")
    deq.addfrontQ(5)
    
    # Last thing added to the front of the queue
    deq.addfrontQ(False)
    # Last thing added to the back of the queue
    deq.addbackQ(25)
    
    # Checking if the queue is empty
    deq.displayQ()
    deq.isEmpty()

    # Removing the item at the front of the queue (should be the last item added to the front of the queue)
    deq.pfront()
    deq.displayQ()

    # Removing the item at the back of the queue (should be the last item added to the back of the queue)
    deq.pback()
    deq.displayQ()

    # Situational to test if the queue is empty / not empty
    if deq.isEmpty() == True:
        print("The queue is currently empty")
    else:
        print("The queue is not currently empty")

    
# Executing main function
if __name__ == "__main__":
     main()


