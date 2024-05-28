



# Defining Towers of Hanoi move count function, with a parameter for user input
def TOH(n):
    
    # Return 1 if there if only one disk left to move, because it will always take one move
    if n == 1:
        return 1
    
    # If there is more than one disk left to move plug the number of disks in to the recursive time-complexity formula given in class
    # which is T(n) = 2 * (n-1) + 1, and call recursively until you reach one disk left, and return the total move count
    else:
        return 2 * TOH(n-1) + 1

    
# Defining main function
def main():
    
    # Calling for user input
    disks = int(eval(input("\nPlease enter the amount of discs you'd like the move count for:\n")))

    # Printing the amount of moves necessary for the amount of disks inputted
    print("The move count for a Tower of Hanoi with", disks, "disk(s) would be:",TOH(disks))

# Calling main function
if __name__ == "__main__":
    main()































