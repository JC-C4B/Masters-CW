# Main Function
def main():


    # Define rectangle class
    class Rectangle:
        # Give attributes of length and width
        def __init__(self, l, w):
            self.Length = l
            self.Width = w
        # Create a function to calculate the Perimeter 
        def Perimeter(self):
            return 2*eval(self.Length) + 2*eval(self.Width)
        # Create a function to calculate the Area
        def Area(self):
            return eval(self.Length) * eval(self.Width)
        # Create a function to display the properties of the rectangle
        def display(self):
                print("The Length entered was: ", self.Length)
                print("The Width entered was: ", self.Width)
                print("The Perimeter of your rectangle is: ", self.Perimeter())
                print("The Area of your rectangle is: ", self.Area())
    # Define Parallelepiped as a subclass of Rectangle
    class Parallelepiped(Rectangle):
        # Make class inherit Length and width from Rectangle class
        # Add new attribute for height
        def __init__(self, l, w, h):
            Rectangle.__init__(self, l, w)
            self.Height = h
        # Create a function to claculate the Volume
        def Volume(self):
            return eval(self.Length) * eval(self.Width) * eval(self.Height)
    # Create a new Rectangle to enter parameters
    userRect = Rectangle(input("Enter the length of your rectangle: "), input("Enter the width of your rectangle: "))
    userRect.display()
    # Create a new Parallelepiped using the length and width of the new rectangle
    userPara = Parallelepiped(userRect.Length, userRect.Width, input("Enter the desired height of your object: "))
    print("The Volume of your object is: ", userPara.Volume())

# Call main function
if __name__ == "__main__":
   while True:
        try:
            main()
            break
        except:
            print("Something went wrong, please only input valid numbers.")
        continue
   





















