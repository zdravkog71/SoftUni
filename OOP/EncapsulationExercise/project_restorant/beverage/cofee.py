from EncapsulationExercise.project_restorant.beverage.hot_beverage import HotBeverage

class Cofee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.5
    def __init__(self, name, caffeine):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine