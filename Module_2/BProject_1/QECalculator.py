
# Importing math to make use of the square root function
import math

def quadratic(a, b, c):
    
    # Solving for the value within parentheses
    value = b**2 - 4 * a * c

    # Cases for finding the square root

    # If the value is negative there are no real sqaure roots
    if value < 0:
        return None
    
    # If the value is 0 there is only one answer
    elif value == 0:

        # Square root == 1, so the answer is just -b / 2a
        ans = -b / (2 * a)

        return [ans]
    
    # If the value is positive and greater than 0
    else:

        # Answer for addition
        ans1 = (-b + math.sqrt(value)) / (2 * a)

        # Answer for subtraction
        ans2 = (-b - math.sqrt(value)) / (2 * a)

        return [ans1, ans2]
        
    