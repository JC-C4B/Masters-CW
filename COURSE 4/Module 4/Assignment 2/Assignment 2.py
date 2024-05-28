
# Getting data from our csv file, making a placeholder attribute for the name of the csv file
def readcsv(csvname):

    # Creating a list to store items in
    items = []

    # Appending from csv to list
    with open(csvname, "r") as data:

        # Seperating data using the commas, and organizing the data into the list
        for line in data.readlines():
            name, value, height, width, depth = line.strip().split(",")
            items.append((name, int(value), int(height), int(width), int(depth)))
    
    # Returning the list
    return items

# Defining Cubic Limit algorithm
def cubiclim(items, cl):

    # Creating a list of the items based off value per volume
    best = []

    # Calculating value per volume, and the volume itself
    for i in range(len(items)):
        
        # Appending value per volume, volume, value, and index
        best.append([(items[i][1]) / (items[i][2] * items[i][3] * items[i][4]), (items[i][2] * items[i][3] * items[i][4]), items[i][1], i])
    
    # Sorting from high to low
    best.sort(reverse=True)    

    # Creating a list for all items used in final answer
    ans = []

    # Total volume
    tv = 0 

    # Loop condition
    found = True

    # Loop that runs until nothing else can fit
    while (found):        
        
        # Ending loop 
        found = False
        
        # Checking if anything else fits
        for i in best:

            # If it does fit, add it to the list and restart the loop
            if tv + i[1] <= cl:
                ans.append(i)
                tv += i[1]
                found = True
                break
    
    # Return the final list of items
    return ans

# Defining main function
def main():

    # Asking the user for a cubic limit to find the most optimal use of space for value
    capacity = int(input("Please enter a volume capacity (cubic inches): "))
    answer = cubiclim(readcsv("packs.csv"), capacity)

    # Total Value, Total cubic volume
    tv, tcv = 0, 0

    # Printing the items added and their details
    for a in answer:
        print("Item - Value:", a[2], "- Volume:", a[1], "inches cubed")
        tv += a[2]
        tcv += a[1]

    # Printing the final counts
    print("\nItems:", len(answer), "- Value:", tv, "- Volume:", tcv, "inches cubed")

# Calling main program
if __name__ == "__main__":
    main()
