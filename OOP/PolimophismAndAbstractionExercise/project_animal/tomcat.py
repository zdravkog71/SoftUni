from PolimophismAndAbstractionExercise.project_animal.cat import Cat

class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")


    def make_sound(self):
        return "Hiss"

    # def __repr__(self):
    #     return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"