"""\nThis module contains the class 'Rectangle' found in our first course.\n """

# Define rectangle class
class Rectangle:
    """ This class defines an object with the properties of a rectangle.
        It has two instance variables;
        - The length of the object
        - The width of the object. """

    # Give attributes of length and width
    def __init__(self, l, w):
        """The constructor of a 'Rectangle' object that assigns the data taken from
          'l' to the length, and 'w' to the width."""    
        
        self.Length = l
        self.Width = w

    # Create a function to calculate the Perimeter 
    def Perimeter(self):
        """This function takes the length and width parameters of the rectangle object 
            and uses them to calculate the perimeter of the rectangle by
            inputting them into the formula (2 * L) + (2 * W)."""    
        
        return 2*eval(self.Length) + 2*eval(self.Width)
    
    # Create a function to calculate the Area
    def Area(self):
        """This function takes the length and width parameters of the rectangle object
            and uses them to calculate the area of the rectangle by 
            inputting them into the forula (L * W)."""  
          
        return eval(self.Length) * eval(self.Width)
    
    # Create a function to display the properties of the rectangle
    def display(self):
        """This function displays the characteristics of the rectangle object.
            It does so by printing:
            - Its length
            - Its width
            - Its perimeter
            - Its area. """    

        print("The Length entered was: ", self.Length)
        print("The Width entered was: ", self.Width)
        print("The Perimeter of your rectangle is: ", self.Perimeter())
        print("The Area of your rectangle is: ", self.Area())




























