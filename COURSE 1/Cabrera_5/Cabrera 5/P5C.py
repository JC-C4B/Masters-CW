

# Define main function
def main():
    
    # Create Parent/Super class (Student)
    class Student:
        # Initialize the class
        def __init__(self, name, age):
            self.name = name
            self.age = age
        # Create display method 
        def display(self):
            print("\n")
            print("Hello, my name is",self.name,"and I am", self.age,"years old.")
    
    # Create Engineer subclass inheriting from Student
    class Engineer(Student):
        # Initialize subclass, inherit necessary attributes
        def __init__(self, name, age, courses):
            Student.__init__(self, name, age)
            self.courses = courses
        #  Create Engineer display method
        def displayEngineer(self):
            print("\n")
            print("Hello, my name is",self.name,"and I am", self.age,"years old.")
            print("I am an Engineering student currently taking", self.courses, "courses.")
    
    #  Create Doctor subclass inheriting from Student
    class Doctor(Student):
        # Initialize subclass, inherit necessary attributes
        def __init__(self, name, age, hospital):
            Student.__init__(self, name, age)
            self.hospital = hospital
        # Create Doctor display method
        def displayDoctor(self):
            print("\n") 
            print("Hello, my name is",self.name,"and I am", self.age,"years old.")
            print("I am a Medical student currently working at", self.hospital, "hospital.")

    
    # Test Parent class functionality through instance
    # s = Student("Samantha", 20)
    # s.display()

    # Create Engineer instance
    engi = Engineer("John", 22, 6)
    # Test Engineer display method
    engi.displayEngineer()

    # Create Doctor instance
    doc = Doctor("Patricia", 28, "Saint John's")
    # Test Doctor display method
    doc.displayDoctor()

# Call main function
if __name__ == "__main__":
    main()

























