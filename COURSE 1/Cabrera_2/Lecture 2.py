



a = 2
b = 5 
c = 4

if a > b and a > c:
    max = a

if b > a and b > c:
    max = b

if c > a and c > b:
    max = c

print(max)


temp = eval(input("Give me a temperature in Fahrenheit: "))

def main():
    

    if temp <= 0:
        print("The weather is near polar conditions!")
    elif temp > 0 and temp <= 32:
        print("IT's freezing outside!")
    elif temp > 32 and temp <= 50:
        print("Brrr.... it's cold out!")
    elif temp > 50 and temp <= 80:
        print("It's pretty warm out!")
    else:
        print("It's boiling hot outside!")

main()


