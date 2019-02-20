class Personne:

    def __init__(self, userName, age):
        self.name = userName
        self.age = age
        self.lvl = 0
        self.abilities = {}
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def get_lvl(self):
        return self.lvl

    def add_abilities(self):
        pass
    