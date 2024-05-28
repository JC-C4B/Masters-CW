

# Defining main function
def zigzag():

    # Welcome message
    print("\nWelcome to the zigzag function, please input your values below.\n")

    #  Prompt for ZigZag inputs
    check = False
    
    while not check:

        try:

            a = int(input("\nInput a value for a: "))
            b = int(input("\nInput a value for b: "))
            c = int(input("\nInput a value for c: "))
        
        except ValueError:
            print("\nThe input was not a valid integer, please try again: \n")
            continue
        
        else:
            check = True

    # Scenarios for return value
    if a < b > c:
        return True
    
    elif a > b < c:
        return True

    else:
        return False

# Defining main function
def main():
    
    # 
    result = zigzag()
    
    if result == True:
        print("\nYour inputs are a ZigZag!\n")
    
    else: 
        print("\nYour inputs are not a ZigZag.")

if __name__ == "__main__":
    main()































