# Juan Carlos Cabrera
# Importing mysql.connector
import mysql.connector

# Creating our class to interact with the database
class DAL:

    # Establishing our connection to the database
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="MealPlanning"
        )

    # Creating a function to call our stored procedures within the database by name
    def call_stored_procedure(self, procedure_name):
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(f"CALL {procedure_name}()")
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")



