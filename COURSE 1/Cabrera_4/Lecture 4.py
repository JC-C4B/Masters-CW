

import sys
sys.path

# A class is a data-type and an object is a variable of that data type.
# A class is a data-type and an object is a variable of that data type.
# A class is a data-type and an object is a variable of that data type.
# A class is a data-type and an object is a variable of that data type.
# A class is a data-type and an object is a variable of that data type.
# A class is a data-type and an object is a variable of that data type.
# A class is a data-type and an object is a variable of that data type.



# Example of a class:
# The parameters taken are self, n, and a.
# Self is defining the Class itself
# n is a variable for name
# a is a variable for age
class student:
    def __init__(self, n, a) :
        self.full_name = n
        self.age = a
# This function DOES NOT take a parameter; it is solely referencing itself (this is a good example)
    def get_age(self):
        return self.age

b = student("Bob", 21)
print(b.full_name)
print(b.get_age())