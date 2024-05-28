# Juan Carlos Cabrera
# Importing our business layer
from MP5BL import BL

# Defining our presentation layer class
class Presentation:

    # Initializing our class
    def __init__(self):
        self.business_logic = BL()

    # Defining our menu function
    def run(self):

        # Greeting our user
        print("Welcome to your Personal Meal Planner!\n")
        print("+--------------------------------------------+")
        print("1. Get Cookbooks")
        print("2. Get Recipes from Cookbook")
        print("3. Get Ingredients from Recipe")
        print("4. Assign Recipe to Day")
        print("0. Exit")
        print("+--------------------------------------------+\n")

        # Choosing what to do based of user input
        while True:
            choice = input("What option would you like to choose?: ")
            
            # Getting cookbook names
            if choice == '1':
                cookbooks = self.business_logic.get_cookbooks()
                print("Cookbooks:", cookbooks)

            # Getting recipe names from a cookbook
            elif choice == '2':
                cookbook_name = input("Please enter the name of the Cookbook: ")
                recipes = self.business_logic.get_recipes_from_cookbook(cookbook_name)
                print(f"Recipes from '{cookbook_name}':", recipes)

            # Getting ingredients from a recipe
            elif choice == '3':
                recipe_name = input("Please enter the recipe name: ")
                ingredients = self.business_logic.get_ingredients_from_recipe(recipe_name)
                print(f"Ingredients for '{recipe_name}':", ingredients)

            # Setting a recipe to a specific day
            elif choice == '4':
                recipe_name = input("Please enter the name of the recipe you'd like to assign to a day: ")
                day = input("Please enter the day you'd like to assign: ")
                self.business_logic.assign_recipe_to_day(recipe_name, day)
                print(f"'{recipe_name}' assigned to '{day}'.")

            # exiting the menu
            elif choice == '0':
                print("\nヾ(￣▽￣) Bye~Bye~\n")
                break
            
            # In case of an input error
            else:
                print("Only numbers from 0 - 4 are valid inputs. Please try again.")

# Calling our main function/ starting our options menu
if __name__ == "__main__":
    presentation_layer = Presentation()
    presentation_layer.run()
