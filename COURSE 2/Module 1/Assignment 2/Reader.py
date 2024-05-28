


# Creating an empty list to store file's data
a = []

# Opening file and getting it's data
with open("data.txt", "r") as data:
    for line in data.readlines():
        a.append(int(line))

# Sorting the list
a.sort()

# Implementing linked list and node classes, L (as seen in class)

class Node(object):
    
    def __init__(self, data):
        
        self.data = data
        self.next = None

class LinkedList(object):
    
    def __init__(self, sequence):
        
        self.head = Node(sequence[0])
        current = self.head
        
        for i in sequence[1:]:
            current.next = Node(i)
            current = current.next
    
    def sinsert(self, newobj):

        check = False
        
        # If X is already in L, remove x
        while self.head is not None and self.head.data == newobj.data:
            self.head = self.head.next
            check = True
            print("\nThe inputted item was previously in the list, and has been removed.\n")
            break
        
        if self.head is not None:
            rcurrent = self.head
            while rcurrent.next is not None:
                if rcurrent.next.data == newobj.data:
                    rcurrent.next = rcurrent.next.next
                    check = True
                    print("\nThe inputted item was previously in the list, and has been removed.")
                    break
                else:
                    rcurrent = rcurrent.next

        # If x not in L, insert it to the appropriate position so L remains sorted
        # Look for the position to insert x in L
        if check == False:
            
            if self.head is None or self.head.data >= newobj.data:
                newobj = self.head
                self.head = newobj
                return self.head

            current = self.head

            while current.next is not None and current.next.data < newobj.data:
                current = current.next
            
            newobj.next = current.next
            current.next = newobj
            
            print("\nThe inputted item has been inserted into the list.")

    # Function to print the list
    def listprint(self):
        toprint = self.head
        while toprint is not None:
            print(toprint.data)
            toprint = toprint.next

# Make Linked list structure L
L = LinkedList(a)

# Print list to see contents
L.listprint()



# Define main function
def main():

    # Asking user for input
    x = Node(int(input("\nPlease input an integer value\n")))

    # Checking input and inserting if not already in list
    L.sinsert(x)

    # Printing new list
    print("\n")

    L.listprint()

# Call main function
if __name__ == "__main__":
    main()























