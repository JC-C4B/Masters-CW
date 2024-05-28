# Importing platform and os
import platform
import os

# @author Juan Carlos Cabrera
# Tested on a Windows 11 OS

# Referred the Module 6 presentation and the os module description page linked below:
# https://docs.python.org/3/library/os.path.html


# Defining our conversion function
def conversion(fpath):
    
    # Finding the current operating system
    current = platform.system()
    
    # Converting to Windows format if the OS is Windows
    if current == "Windows":
        newpath = os.path.normpath(fpath)

    # Converting to Mac format if the OS is not Windows
    else:

        # I learned I have to use two backslashes here to avoid inputting a command 
        newpath = fpath.replace("\\", "/")

    # Returning our newly converted file path
    return newpath

# Defining our main function
def main():

    # Creating a variable for the user input the path they desire to be converted
    fpath = input("Please enter the file name and path: ")

    # Converting the path using our conversion function
    newpath = conversion(fpath)

    # Printing the new file path
    print("The converted version of your file path is: ", newpath)

# Calling our main function
if __name__ == "__main__":
    main()




























