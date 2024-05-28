

# Defining main function
def main():

    # Welcome Message
    print("\nIs it cold in Canada today?\n")

    # Threshold prompt
    check = False

    while not check:
        try:
            threshold = int(input("What temperature in celsius is considered cold for Canadians?: \n"))
        except ValueError:
            print("\nThe input was not a valid integer, please try again: \n")
            continue
        else:
            check = True

    # Current temp in Fahrenheit prompt
    check2 = False

    while not check2:
        try:
            Ftemp = int(input("\nWhat is the current temperature in Fahrenheit?: \n"))
        except ValueError:
            print("\nThe input was not a valid integer, please try again: \n")
            continue
        else: 
            check2 = True


    # Converting to Celsius
    Ctemp = (5/9) * (Ftemp - 32)

    # Decision for output:
    if Ctemp <= threshold:
        print("\nToday's temperature is cold for a Canadian!")

    else:
        print("\nIt is not cold for a Canadian today.")

# Calling main function
if __name__ == "__main__":
    main()




























