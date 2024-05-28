""" @author Juan Carlos Cabrera """

# These are the websites I went to, to learn more about OS:

# https://www.python-engineer.com/posts/check-if-file-exists/
# https://pynative.com/python-delete-files-and-directories/
# https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac

# Importing necessary packages to make use of OS
import os
import shutil
import random

# Defining our main function
def main():

    # Setting while loop condition
    finished = False

    # Starting loop
    while not finished:

        # Setting desired folder name to a variable, giving the option to end the loop/program
        foldn = input("\nPlease enter the desired name of your folder, or type 'EXIT' to end the program: ")

        # Case if the user wants to exit
        if foldn == "EXIT":
            finished = True
            print("\n(。・∀・)/ <( Goodbye! )\n")
            continue
        
        # Case if a folder already exists under the name provided
        if os.path.isdir(foldn):

            # Removing the existing folder
            shutil.rmtree(foldn)
            print("\nRemoving existing folder ...\n")
            print("Folder removed!")

        # Creating the folder with the name provided
        os.mkdir(foldn)
        print("\nFolder ", foldn, " created!")

        # Making a list of 100 random numbers from 0-1000
        nums = [random.randint(0,1000) for i in range(100)]

        # Making a .txt file inside of the folder with all of the
        # Random numbers saved in it
        fpath = os.path.join(foldn, "numbers100.txt")
        with open(fpath, "w") as file:
            for i in nums:
                file.write(str(i) + "\n")

        print("Your text file was created and saved in the folder!")

# Calling our main function
if __name__ == "__main__":
    main()

































