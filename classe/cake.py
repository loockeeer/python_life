from time import sleep
class Cake:
    def __init__(self, name="undefined", ingredients=dict(), temps_cuisson=int(), unit=str()):
        self.ingredients=ingredients
        self.temps_cuisson=temps_cuisson
        self.unit=unit
        self.state="not cooked"
        self.name=name
        if unit=="s":
            pass
        if unit=="m":
            temps_cuisson=temps_cuisson/60
        if unit=="h":
            temps_cuisson=temps_cuisson/60
            temps_cuisson=temps_cuisson/60
    def get_state(self):
        return self.state
    def __str__(self):
        return self.name
    def cook(self):
        sleep(self.temps_cuisson)
        self.state="cooked"
