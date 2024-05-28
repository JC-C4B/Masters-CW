# myList = []

# print(myList)

# myList.append(1)

# print(myList)

# # Does not seem like things can be appeneded within the same parenthesees.
# myList.append(2)
# myList.append(3)

# print(myList)

# Let's talk about queues:
# He didn't explain, but hopefully this helps a little lmao:





def queue(self):
    self.queue = []
    return self.queue

def enqueue(self, item):
    self.queue.append(item)

def dequeue(self):
    self.queue.pop(0)

def front(self):
    print(f'{self.queue[0]}')

def isEmpty(self):
    if(self.queue == []):
        return True
    else:
        return False

#    Above is to his standards, but how tf were we supposed to know

#  DO NOT USE THIS FOR THE PROJECT, MAKE USE OF LISTS AND CREATE THE DEQUE FROM SCRATCH
# from queue import Queue


# q = Queue(maxsize = 3)

# q.put("a")
# q.put("b")
# q.put("c")





