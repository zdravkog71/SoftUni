from InheritanceExercises.project_shop.product import Product

class Drink(Product):
    def __init__(self, name):
        super(Drink, self).__init__(name, quantity=10)





