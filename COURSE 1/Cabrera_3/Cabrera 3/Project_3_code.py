

import random
from random import randint

# Variable for grid size
grid_size = 10
# Declaration of Array 
guess_grid = [ [""] * grid_size for i in range(grid_size)]
# Number of ships
num_of_ships = 5

# Function to draw the grid/array
def drawboard(myBoard):
    # Printing header column labels
    print(" +---+---+---+---+---+---+---+---+---+---+")
    print(" | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
    print(" +---+---+---+---+---+---+---+---+---+---+")
    # Printing rows and columns (%d for external row number and %s for array information)
    row_number = 0
    for row in myBoard:
        print("%d|%s|" % (row_number, "|".join(row)))
        print(" +---+---+---+---+---+---+---+---+---+---+")
        row_number += 1

# Function to set up the board
def setupBoard(myBoard):
    i = j = 0

    while i < grid_size:
        while j < grid_size:
            # Store the string "i, j" into the array, and making free spaces have a " . "
            myBoard[i][j] = " . "
            j += 1
        j = 0
        i += 1

    # Prepare ships on the board and assure there are a total of 5 in different spaces
    for ships in range(num_of_ships):
        random_row, random_column = randint(0, 9), randint(0, 9)
        while myBoard[random_row][random_column] == " S ":
            random_row, random_column = randint(0, 9), randint(0, 9)
        ships = myBoard[random_row][random_column] = " S "


# Create a function for user input, and to check if they hit or missed a ship
def checkHitOrMiss():
        
    print("Guess where your oppnent's remaining battleships are: ")
    while True:
        try:
            row = input("Enter the row of your guess: ")
            # Checks if valid row
            while row not in "0123456789":
                print("Something went wrong. Please enter a valid row.")
                row = input("Enter the row of your guess: ")

            column = input("Enter the column of your guess: ")
            # Checks if valid column
            while column not in "0123456789":
                print("Something went wrong. Please enter a valid column.")
                column = input("Enter the column of your guess: ")   
        # Exception for the unexpected
        except:
            print("Something went wrong. Restarting...")
            continue   
        return int(row), int(column)
 
# Function to count the ships
def shipC(guess_grid):
    count = 0
    for row in guess_grid:
        for column in row:
            if column == " X ":
                count += 1
    return count
# Function to check if the game is over
def isGameOver():
    shipC(guess_grid)
    if shipC(guess_grid) == 5:
        return True
    else:
        return False

def main(myBoard):
    # Set up the board
    setupBoard(myBoard)
  
    # Welcome player to the game
    print("\nWelcome to Battleship!")
    
    # Have the game run while isGameover == False and break when true
    while isGameOver() == False:
        print("There are", 5 - shipC(myBoard), "ships remaining.")
        # Draw the board
        drawboard(myBoard)
        # Prompt user for input & filter it
        row, column = checkHitOrMiss()
        if myBoard[row][column] == " O ":
            print("This space has been chosen previously.")
        elif myBoard[row][column] == " S ":
            print("\nHIT!")
            myBoard[row][column] = " X "
        elif myBoard[row][column] == " X ":
            print("\nHIT")
        else:
            print("\nMISS!")
            myBoard[row][column] = " O "
        if isGameOver() == True:
            drawboard(myBoard)
            print("\nYou've sunken all battleships!")
            print("Congratulations! You've won!")   
            break


main(guess_grid)





























