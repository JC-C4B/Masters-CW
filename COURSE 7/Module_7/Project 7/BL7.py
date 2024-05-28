# Importing our DAL class
from DAL7 import DAL

# Creating our business layer class
class BL:
    def __init__(self):
        self.dal = DAL()

        # Creating a dictionary to use as a cache for our data
        self.cache = {}  

    # WF1: Adding a new item to a room
    def add_item(self):
        item_name = input("Enter the name of the item: ")
        item_description = input("Enter the item description: ")
        item_amount = int(input("Enter the item quantity: "))
        self.dal.call_add_item(item_name, item_description, item_amount)
        print("Item(s) added successfully!")

        # Updating our cache with the inputted item
        self.cache[item_name] = {"description": item_description, "amount": item_amount}

    # WF2: Moving items from one room to another
    def move_items(self):
        item_name = input("Enter the name of the item: ")
        from_room = input("Enter the name of the starting room: ")
        to_room = input("Enter the name of the desired room: ")
        item_quantity = int(input("Enter the quantity you'd like to move: "))
        
        # Checking if the item is in the cache, and Updating our cache 
        if item_name in self.cache:
            self.cache[item_name]["amount"] -= item_quantity
        
        self.dal.call_move_items(item_name, from_room, to_room, item_quantity)
        print("Item(s) moved successfully!")

        

    # WF3: Updating the quantity of an item in a room
    def update_item_amount_in_room(self):
        item_name = input("Enter the name of the item you'd like to update: ")
        new_amount = int(input("Enter the new quantity of your item: "))
        room_name = input("Enter the name of the room your item is in: ")
        self.dal.call_update_item_amount_in_room(item_name, new_amount, room_name)
        print("Updated successfully!")

        # Updating our cache
        if item_name in self.cache:
            self.cache[item_name]["amount"] = new_amount
