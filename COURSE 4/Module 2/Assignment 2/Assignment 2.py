



# Create a tree node
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, data):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, data):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right,
                                          temp.data)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def getMaxValueNode(self, root):
        if root is None or root.right is None:
            return root
        return self.getMaxValueNode(root.right)

    def printPreOrder(self, root):
        if not root:
            return
        print(root.data, end=" ")
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)

    def printInOrder(self, root):
        if not root:
            return
        self.printInOrder(root.left)
        print(root.data, end=" ")
        self.printInOrder(root.right)

# -----------------------------------------------------------------------
    # Defining a function to print in post order
    def printPostOrder(self, root):

        # Case if there is no root
        if not root:
            return
        
        # Start by printing farthest left node
        self.printPostOrder(root.left)

        # Then print the node right of the current root node
        self.printPostOrder(root.right)

        # Finally, print the current node
        print(root.data, end = " ")
# -----------------------------------------------------------------------

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            print(currPtr.data)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


# -------------------------------------------------------------------------------
# Work on second project starts here:
# -------------------------------------------------------------------------------

# Defining main function
def main():

    # Defining placeholders / objects
    myTree = AVLTree()
    root = None
    nums = []
    
    # Creating a loop scenario
    fin = False
    
    # Starting the loop
    while fin != True:
        
        # Asking the user for an integer to add to the tree, giving the option to quit the program
        anum = int(input("Please enter a positive integer you'd like to add to the AVL Tree,\nInputing an integer already present will remove it.\nEnter a negative integer if you'd like to quit.\n"))

        # Case if the number is greater than zero
        if anum > 0:

            # If the number is already in the list, delete it from the list and the tree
            if anum in nums:
                    
                    # Removing from list and setting parameters
                    nums.remove(anum)
                    data = anum

                    # Deleting from AVL Tree
                    root = myTree.delete_node(root, data)
                    
                    # Print the tree 
                    print("\nAfter Deletion of {}: ".format(data))
                    myTree.printHelper(root, "", True)

            # If not in the list, add it to both the list and the tree 
            else:

                # Adding to list and setting parameters
                nums.append(anum)
                data = anum

                # Adding to the AVL Tree
                root = myTree.insert_node(root, anum)
                
                # Print the tree 
                print("\nAfter Insertion of {}: ".format(data))
                myTree.printHelper(root, "", True)
            
        # Break the program if a negative integer is entered
        else:
            fin = True
            break

# Calling main function
main()

# -------------------------------------------------------------------------------
# Report / Comments
# -------------------------------------------------------------------------------

# While the use of the base code provided to us from example 3 made this process a lot easier,
# I still ended up making the error of appending the user input to the tree twice at a time due to an oversight in appending from the list, 
# and I also made some mistakes with my indentation within the loop that lead to never printing the tree.
# Thankfully through looking back through my previous coursework I was able to identify my issues and resolve them in a manner that works.
# Overall, this project/excercise definitely jogged my memory and helped me feel more confident in my ability to code!

# -------------------------------------------------------------------------------