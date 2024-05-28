
# Importing random to shuffle the array
import random

# Creating our placheolder array
rarry = []

# Appending an equal number of 0's and 1's
for i in range(5000):
    rarry.append(0)

for i in range(5000):
    rarry.append(1)

# Shuffling array
random.shuffle(rarry)

# Defining randomized Monte Carlo algorithm
def Monte(x):
    
    # Setting K as the amount of tries available
    k = 10

    # Counting the attempts made at finding the first '1'
    attempts = 0
    
    # Attempting to find a 1 within k attempts
    for i in range(k):

        # Creating a random index to check
        index = random.randint(0,9999)

        # Adding to the count for every attempt
        attempts += 1

        # Case if a '1' is found within the attempts
        if x[index] == 1:
            print("Position of first 1 found:", index)
            print("Number of tries:", attempts)
            break
        
        # Case if the '1' is not found within the alloted tries
    else:
        print("Could not find a 1 in", k, "tries.")
    

# Defining main function
def main():

    # Calling the Monte function
    Monte(rarry)

# Calling main function
if __name__ == "__main__":
    main()


