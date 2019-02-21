
from time import sleep

class Cake:

    def __init__(self, ingredients: dict, cooking_time: int, name="undefined"):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.state = "not cooked"

    def get_state(self):
        return self.state
    
    def get_ingredient(self):
        return [(ingredient, quantity) for ingredient, quantity in self.ingredients.items()]

    def __str__(self):
        return self.name

    def cook(self):
        sleep(self.cooking_time)
        self.state="cooked"
