

# Create a class for the node object
class Node(object):
    
    # Like a linked list but giving to options for direction
    def __init__(self, data):
        
        self.data = data
        self.Left = None
        self.Right = None

# Create a Tree class
class Tree:
    
    # Define the root of the tree/ first value to branch out from
    def __init__(self, d=None):
        if d == None:
            self.Root = None
        else:
            self.Root = Node(d) 

    # Insert function
    def insert(self, d):

        # Choosing whether to insert left or right
        def __whereto__(n, d):
            
            # If current node is greater than data, insert Left
            if n.data > d:

                # If current left node is empty, insert
                if n.Left == None:
                    n.Left = Node(d)
            
                # If that fails, try inserting on left child
                else:
                    __whereto__(n.Left, d)

            # If current node is less than data, insert Right
            elif n.data < d:
                
                # If current right node is empty, insert
                if n.Right == None:
                    n.Right = Node(d)
                
                # If that fails, try inserting on right child
                else:
                    __whereto__(n.Right, d)

        # If the Root is empty, make input the root
        if self.Root == None:
            self.Root = Node(d)

        # If root is not empty, create a new edge
        else:

            # If root is greater than data, insert left
            if self.Root.data > d:
                if self.Root.Left == None:
                    self.Root.Left = Node(d)
                
                # If left node is taken, use said node as the root and try again
                else:
                    __whereto__(self.Root.Left, d)

            # If root is less than data, insert right
            elif self.Root.data < d:
                if self.Root.Right == None:
                    self.Root.Right = Node(d)

                # If right node is taken, use said node as the root and try again
                else:
                    __whereto__(self.Root.Right, d)

    # Function to print in preorder to make creating an adjacency matrix easier
    def printPreorder(self):
        
        # Function to go through the whole tree and print each element in order of value & height starting form node
        def __visit__(n, h):
            
            # Cycle through each node under input
            if n != None:
                print("---"*h, n.data)
                __visit__(n.Left, h + 1)
                __visit__(n.Right, h + 1)

        # Print in Preorder starting with Root
        print("+--------+")
        __visit__(self.Root, 1)
        print("+--------+")   




# Creating an empty list to store file's data
numbers = []

# Opening file and getting it's data
with open("Numbers.txt", "r") as data:
    for line in data.readlines():
        numbers.append(int(line))

# Adjaceny matrix of the Tree I created
graph = [
[0, 26, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0], 
[0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 10, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 10, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 8, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 14],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Node Reference for self clarity
# graph = [
# [0, 26, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0] --- 30
# [0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] --- 4
# [0, 0, 0, 10, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0] --- 16
# [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  --- 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  --- 10
# [0, 0, 0, 0, 0, 0, 5, 2, 0, 0, 0, 0, 0, 0, 0]  --- 23
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  --- 18
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  --- 25
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 10, 0, 0, 0, 0]  --- 34
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  --- 31
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 8, 0, 0]  --- 44
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  --- 39
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 14]  --- 52
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  --- 46
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  --- 66
# ]


def main():
    T = Tree()

    for i in numbers:
        T.insert(i)

    T.printPreorder()

    print("\n\n")

    for i in graph:
        print(i)

if __name__ == "__main__":
    main()

