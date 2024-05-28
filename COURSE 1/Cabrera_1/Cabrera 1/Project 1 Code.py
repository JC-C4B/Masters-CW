
# Import math for accurate pi
import math
from math import pi

# Greeting
print("Hello and welcome!")

# Main function
def main():
    
    # Defining user input as radius value
    r = eval(input("Please enter the radius of a circle or sphere: "))
    
    # Circumference formula function
    def cfren():
        fren = 2 * r * pi
        print(f"The circumference of a circle with a radius of", r, "is", fren)
    cfren()
    
    # Area formula function
    def area():
        a = pi * r**2
        print(f"The area of a circle with a radius of", r, "is", a)
    area()

    # Volume formula function
    def vol():
        v = 4/3 * pi * r**3
        print(f"The volume of a sphere with a radius of", r, "is", v)
    vol()
    
    # Restart function
    def again():
        print("Would you like to calculate another?")
        yn = (input("Y / N: "))
        if yn == "Y":
            main()
        elif yn == "y":
            main()    
        else:
            print("Good bye!")
    again()

  
# Executing main function    
if __name__ == "__main__":
    main()


























