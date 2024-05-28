from random import randrange

def test(initialSize, probRemove):
    accCheap, accCosty = 0, 0
    s = initialSize
    m = 2*s

    for i in range(100000):

        if (randrange(100) < probRemove):
            if (s > 0):
                s -= 1
        else:
            if (s == m):
                m = m*2
                s += 1
                accCosty += 1
            else:
                s += 1
                accCheap += 1

    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costy: {:7} ({:3.1}%)".format(accCosty,accCosty/(accCosty+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,accCheap/(accCosty+accCheap)))

def main():
    test(1, 10)
    test(1, 25)
    test(1, 50)
    test(10, 70)
    test(100, 99)
    test(2, 10)
    test(20, 5)
    test(500, 5)
    print("----------------------------------------------")
    test(20, 1)
    test(20, 5)
    test(50, 1)
    test(50, 5)
    test(100, 1)
    test(100, 5)

main()

# ----------------------------------------------------------------------------------
#                                     Comments
# ----------------------------------------------------------------------------------

# Although I used the code given to us in the lecture, my code is returning percentages that are considerably smaller than
# what was shown in the presentation. (I believe it has to do with the iteration through the range of 100,000 but couldn't fix it unfortunately)

# That being said, while testing the code I realized that the probability of a costly algorithm 
# goes up when the intitial size of the array is lower and the chance to remove is higher. 
# I believe this is because the array would have to be resized everytime it goes over capacity,
# thus making it more costly.

# However, the highest percentage I achieved was 0.0002% (which would be equivalent to 0.02% when referencing the presentation),
# and this was achieved with an initial size of 1 and removal rate of anywhere between 1 - 24 / 100 (Anything afterward got smaller).

# While the combination to find >= 1% was not found I believe it is because while the array is small in size and needs to resize,
# it will never cost much to resize a small array, as having to iterate over a shorter amount is still relatively easy for a computer.
# The only way I can think of where this would become an issue is if the array is incredibly small, which wouldn't make sense in practice,
# and leads me to believe that reaching a probability of costly operations of at least 1% is not practically possible.
