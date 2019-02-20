class Personne:

    def __init__(self, userName, age):
        self.name = userName
        self.age = age
        self.abilities = {}
        self.sleep = False
        self.active = False
        self.location = "Home"
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_abilities(self, abilities):
        if abilities not in self.abilities:
            self.abilities[abilities] = 0
    
    def get_lvl_abilities(self, name):
        if name in self.abilities:
            return self.abilities[name]
    
    def get_all_abilities(self):
        return [abilities for abilities in self.abilities]
    
    def add_lvl_abilities(self, name, value = 1):
        if name in self.abilities:
            self.abilities[name] += value
    
    def awake(self):
        return not self.sleep
    
    def is_active(self):
        return self.active
    
    def go_somewhere(self, position):
        self.location = position.capitalize()
