

# Using a for loop, write a code fragment that counts backward from 50 to 25 by 5’s and only prints out the values 50, 45, 40…etc. til 25.



for x in reversed(range(0, 51, 5)):
    if x >= 25:
        print(x) 







# Using a do-while loop, write a code fragment that reads a String from the keyboard from the user until the user types “EXIT”

print("Welcome to your diary. Please feel free to write to you're content.")



def main():
    
    ut = input("Tell me what's on your mind? If you'd like to stop type 'EXIT': ")

    while ut == "EXIT":
        print("Goodbye!")
        break

    else:
        main()
        


if __name__ == "__main__":
    main()






























