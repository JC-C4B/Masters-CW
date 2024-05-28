

# # Importing random to create random unique dataset
# import random

# # Creating a random array
# num = []
# length = 1000
# for i in range(length):
#     num.append(random.randint(1,1000000))

# # Creating random unique array to test function with
# unum = random.sample(range(0,1000000), 1000)

# # Checking the uniqueness through Decrease and Conquer, returning whether unique or not
# def unique(a):
#     ans = True
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if (i != j) and (a[i] == a[j]):
#                 ans = False
#                 break
#         if (not ans):
#             break
#     return ans

# # Defining main function
# def main():
    
#     # Print whether uniqueness is True or False
#     print("Is the array unique?:", unique(num))

# # Call main function
# if __name__ == "__main__":
#     main()

# -------------------------------------------------------------------------------

# Importing random to create random unique dataset
import random

# Creating a random array
num = []
length = 1000
for i in range(length):
    num.append(random.randint(1,1000000))

# Creating random unique array to test function with
unum = random.sample(range(1,1000000), 1000)

# Checking the uniqueness through Transform and Conquer, returning whether unique or not
def uniqueSorted(a):
    a.sort()
    for i in range(len(a)):
        if (a[i - 1] == a[i]):
            return False
    return True

# Defining main function
def main():
    
    # Print whether uniqueness is True or False
    print("Is the array unique?:", uniqueSorted(num))

# Call main function
if __name__ == "__main__":
    main()



















