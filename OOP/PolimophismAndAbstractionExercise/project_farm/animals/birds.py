from PolimophismAndAbstractionExercise.project_farm.animals.animal import Bird


class Owl(Bird):

    #WEIGHT_INCR = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def allowed_food(self):
        return ["Meat"]

    def weight_incr(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"

    # def feed(self, food):
    #     if not isinstance(food, Meat):
    #         return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
    #     self.weight += self.WEIGHT_INCR * food.quantity
    #     self.food_eaten += food.quantity


class Hen(Bird):
    #WEIGHT_INCR = 0.35
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def allowed_food(self):
        return ["Meat", "Vegetable", "Fruit", "Seed"]

    def weight_incr(self):
        return 0.35

    def make_sound(self):
        return "Cluck"

    # def feed(self, food):
    #     self.weight += self.WEIGHT_INCR * food.quantity
    #     self.food_eaten += food.quantity