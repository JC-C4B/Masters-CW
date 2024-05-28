# Importing mySQL connector to interact with database
import mysql.connector

# Creating our Data Access Layer class
class DAL:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=input("Please input the Host ID:\n"),
            user=input("Please input your Username:\n"),
            password=input("Please input your password:\n"),
            database="Inventory"
        )
        self.cursor = self.conn.cursor()

    # Function for calling WF1 stored procedure
    def call_add_item(self, item_name, item_description, item_amount):
        self.cursor.callproc("AddNewItem", (item_name, item_description, item_amount))
        self.conn.commit()

    # Function for calling WF2 stored procedure
    def call_move_items(self, item_name, from_room, to_room, item_quantity):
        self.cursor.callproc("MoveItemsToRoom", (item_name, from_room, to_room, item_quantity))
        self.conn.commit()

    # Function for calling WF3 stored procedure
    def call_update_item_amount_in_room(self, item_name, new_amount, room_name):
        self.cursor.callproc("UpdateItemAmountInRoom", (item_name, new_amount, room_name))
        self.conn.commit()

    # Closing our connection
    def close_connection(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    dal = DAL()
    dal.close_connection()
