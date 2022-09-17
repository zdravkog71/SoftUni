from PolimophismAndAbstractionExercise.project_farm.animals.animal import Mammal


class Mouse(Mammal):
    #WEIGHT_INCR = 0.1
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def allowed_food(self):
        return ["Vegetable", "Fruit"]

    def weight_incr(self):
        return 0.1

    def make_sound(self):
        return "Squeak"

    # def feed(self, food):
    #     if not (isinstance(food, Vegetable) or isinstance(food, Fruit)):
    #         return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
    #
    #     self.weight += self.WEIGHT_INCR * food.quantity
    #     self.food_eaten += food.quantity


class Dog(Mammal):
    #WEIGHT_INCR = 0.4
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def allowed_food(self):
        return ["Meat"]

    def weight_incr(self):
        return 0.4

    def make_sound(self):
        return "Woof!"

    # def feed(self, food):
    #     if not isinstance(food, Meat):
    #         return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
    #     self.weight += self.WEIGHT_INCR * food.quantity
    #     self.food_eaten += food.quantity

class Cat(Mammal):
    #WEIGHT_INCR = 0.3
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def allowed_food(self):
        return ["Meat", "Vegetable"]

    def weight_incr(self):
        return 0.3

    def make_sound(self):
        return "Meow"

    # def feed(self, food):
    #     if not (isinstance(food, Vegetable) or isinstance(food, Meat)):
    #         return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
    #
    #     self.weight += self.WEIGHT_INCR * food.quantity
    #     self.food_eaten += food.quantity


class Tiger(Mammal):
    #WEIGHT_INCR = 1
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def allowed_food(self):
        return ["Meat"]

    def weight_incr(self):
        return 1

    def make_sound(self):
        return "ROAR!!!"

    # def feed(self, food):
    #     if not isinstance(food, Meat):
    #         return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
    #     self.weight += self.WEIGHT_INCR * food.quantity
    #     self.food_eaten += food.quantity