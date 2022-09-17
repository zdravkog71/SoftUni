from EncapsulationExercise.project_zoo.animal import Animal


class Lion(Animal):
    def __init__(self, name, gender, age, money_for_care=50):
        super().__init__(name, gender, age)
        self.money_for_care = money_for_care
