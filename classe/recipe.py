class Recipe:

    def __init__(self):
        self.recipes = self.init_recipes()
    
    def init_recipes(self):
        with open("data//recette.txt", "r") as book:
            texte = book.read()
        print(texte)
        return 0