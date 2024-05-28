

from math import ceil

def egyptian(n, d):

    print("The Egyptian Fraction of {}/{}".format(n, d))
    ans = []

    # While numerator != 0, Compute minimal larger denominator, 
    # hold it to numerator list, update remainder
    while (n > 0):
        x = ceil(d / n)             
        ans.append(x)
        n, d = x * n - d, d * x

    for a in ans:
        print("1/{}".format(a), end = " ")

def main():

    print("Greedy Algorithm to compute Egyptian Fractions")

    stay = True

    while stay:
        n = int(input("Enter the numerator: "))
        d = int(input("Enter the denominator: "))
        egyptian(n,d)
        stay = ("n" != (input("\nCompute another? (no to stop) ")+" ")[0])

main()

# ------------------------------------------------------------------------------
# Comments
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Task 1
# ------------------------------------------------------------------------------

# 5/6 - The Egyptian fraction is: 1/2, 1/3

# 7/15 - The Egyptian fraction is: 1/3, 1/8, 1/120

# 23/34 - The Egyptian fraction is: 1/2, 1/6, 1/102

# 121/321 - The Egyptian fraction is: 1/3, 1/23, 1/7383

# 5/123 - The Egyptian fraction is: 1/25, 1/1538, 1/4729350

# ------------------------------------------------------------------------------
# Task 2
# ------------------------------------------------------------------------------

# 5/121 - The Egyptian fraction is: 1/25, 1/757, 1/763309, 1/873960180913, 1/1527612795642093385023488 --- Not the same as the presentation
# I believe this didn't work due to the nature of the greedy algorithm choosing the easiest denominator to find instead of the most 
# optimal solution. As pointed out in the presentation 1/25 is a larger fraction than 1/33, and it's evident the algorithm took that
# path because of it's greedy nature especially seeing how it is the larger fraction, hence making the later calculations easier.
# In reality 1/33 would prove far more efficient.

































