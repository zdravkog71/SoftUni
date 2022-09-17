from InheritanceExercises.project_animal.animal import Animal

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)