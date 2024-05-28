

import sys


year = int(sys.argv[1])

isLeapYear = (year % 4 == 0)
isLeapYear = isLeapYear and ((year % 100) != 0)
isLeapYear = isLeapYear or ((year % 400) == 0)

print(isLeapYear)
# This didn't work for me, not quite sure why just yet.













# def main():
#     days = "MonTueWedThuFriSatSun"
#     d = int(eval(input("Pick a day of the week (1-7): ")))
#     fst = (d-1) * 3
#     print(days[fst:fst+3], "is the", str(d)+"-th day of the week.")

# main()


# def main():
#     print("Change Counter\n")

#     print("Please enter the count of each coin type.")
#     quarters = int(input("Quarters: "))
#     dimes = int(input("Dimes: "))
#     nickels = int(input("Nickels: "))
#     pennies = int(input("Pennies: "))

#     total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

#     print("The total value of your change is ${0}.{1:0>2}".format(total//100, total%100))

# main()


















