# Juan Carlos Cabrera
# Importing our DAL to create our business layer
from MP5DAL import DAL

# Creating our business layer class, and defining its functions
class BL:
    def __init__(self):
        self.dal = DAL()

    def get_cookbooks(self):
        return self.dal.call_stored_procedure("GetCookbooks")

    def get_recipes_from_cookbook(self, cookbook_name):
        return self.dal.call_stored_procedure("GetRecipesFromCookbook", [cookbook_name])

    def get_ingredients_from_recipe(self, recipe_name):
        return self.dal.call_stored_procedure("GetIngredientsFromRecipe", [recipe_name])

    def assign_recipe_to_day(self, recipe_name, day):
        self.dal.call_stored_procedure("AssignRecipeToDay", [recipe_name, day])
