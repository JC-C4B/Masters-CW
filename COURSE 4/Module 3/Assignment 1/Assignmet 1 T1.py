



# balanced 0-1 matrices

from itertools import combinations

def permutations(n):
    ones = list(combinations(list(range(n)),n//2))
    ans = []
    for o in ones:
        case = []
        for i in range(n):
            if (i in o):
                case.append(1)
            else:
                case.append(0)
        ans.append(case)
    return ans

def check(mat):
    n = len(mat[0])
    for j in range(n):
        acc0, acc1 = 0, 0
        for i in range(len(mat)):
            if (mat[i][j] == 1):
                acc1 += 1
            elif (mat[i][j] == 0):
                acc0 += 1
            if (acc0 > (n//2)) or (acc1 > n//2):
                return False
    return True

def layer(r, mat, perm, ans):
    for p in perm:
        mat.append(p)
        if check(mat):
            if (r+1 == len(p)):
                ans += 1
            else:
                ans = layer(r+1, mat, perm, ans)
        mat.pop()
    return ans

# ----------------------------------------------------------------------------------------
# Chaninging main call code to allow for sequential calls instead of asking for user input
# ----------------------------------------------------------------------------------------

# Removed the function call and input section, and added 'n' as an attribute for the program call
def balanced01mat(n):
    print("Computing the number of balanced matrices for an order of:", n)
    perm = permutations(n)
    ans = layer(0, [], perm, 0)
    print("The number of balanced matrices is", ans)

# Defining main function
def main():

    # Calling 2, 4, 6, and 8 separately to solve for each individually
    # balanced01mat(2)
    # balanced01mat(4)
    # balanced01mat(6)
    # balanced01mat(8)

    # Calling for all four sequentially
    sequence = [2, 4, 6, 8]

    # Using a 'for' loop to call each item in the list sequentially instead of all at once
    for i in sequence:
        balanced01mat(i)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------
#                                  Comments / Remarks
# ----------------------------------------------------------------------------------------

# Solving for 2 & 4 was thankfully quick (although I do not expect much from my laptop in terms of computation)
# And they confirmed the program was working and giving correct outputs after crossreferencing with the class presentation

# My estimate for 6 was somewhere in hundred-thousands after seeing the leap between 2 and 4 and considering the sheer 
# amount of possible combinations within matricies of order 6. After a (shorter than expecting) bit of loading, 
# the number of balanced matricies came out to 297200! which was greater than expected but still thankfully within the bounds
# of my prediction.

# For an order of 8, I went in with the fear of my laptop not having enough strength to process this.
# My estimate for the outcome was ~ 1.5 million after seeing the leap from 4 to 6. 
# Unfortunately, my computer was unable to solve for an order of 8. 




























