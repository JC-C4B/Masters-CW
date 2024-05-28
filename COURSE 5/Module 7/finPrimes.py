import random

def guess():
    return random.randint(2, 5000)


def isPrime(x):

    # Checking if the number is greater than one
    if x > 1:

        # If greater than one, check for any factors
        for i in range(2, x):
            if (x % i) == 0:

                # Return false if there are any factors
                return False
        
        # Otherwise return true
        else:
            return True
    
    # If the number is <= 1, return false
    else:
        return False
            



def findPrimes(num):
    primes = []
    for i in range(num):
        p = guess()
        while not isPrime(p):
            p = guess()
        primes += [p]
    return primes

import cProfile
cProfile.run('print(findPrimes(500)[:10])')

