
# Importing random to shuffle the array
import random

# Creating our placheolder array
rarry = []

# Appending an equal number of 0's and 1's
for i in range(5000):
    rarry.append(0)

for i in range(5000):
    rarry.append(1)

random.shuffle(rarry)

# Defining randomized Las Vegas algorithm
def Vegas(x):
    
    # Counting the attempts made at finding the first '1'
    attempts = 0
    
    # Looping until the first one is found
    while True:

        # Creating a placheolder for a random index
        index = random.randint(0, 9999)

        # adding one to the counter for every attempt
        attempts += 1

        # Case if the element at the random index is a '1'
        if x[index] == 1:
            print("Position of first 1 found:", index)
            print("Number of tries:", attempts)

            # Stopping the loop
            break

# Defining main function
def main():

    # Calling the Vegas function
    Vegas(rarry)

# Calling main function
if __name__ == "__main__":
    main()






















