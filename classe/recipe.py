class Recipe:

    def __init__(self):
        self.recipes = {}
        self.init_recipes()
    
    def get_recipes(self):
        return self.recipes
    
    def init_recipes(self):
        with open("data//recette.txt", "r") as book:
            for line in book.readlines():
                recette = line.rstrip("\n").split(" ")
                self.recipes[recette[0]] =[tuple(element.split(":")) for element in recette[1:]]
    
    def add_recipes(self, recipe_name: str, ingredient: list):
        if recipe_name not in self.recipes:
            self.recipes[recipe_name] = ingredient
            with open("data//recette.txt", "a") as book:
                book.write(recipe_name)
                for element in ingredient:
                    book.write(" " + ":".join(element))
                book.write("\n")
