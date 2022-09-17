class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def increase_price(self,amount):
        self.price += amount

    def decrease_price(self, amount):
        self.price -= amount

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity

        else:
            self.ingredients[ingredient] = quantity

        new_amount = price_per_quantity * quantity
        self.increase_price(new_amount)

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if not ingredient in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        # happy case:
        self.ingredients[ingredient] -= quantity
        new_amount = price_per_quantity * quantity
        self.decrease_price(new_amount)

    def make_order(self):
        self.ordered = True
        final_ingrediats = []
        for key,value in self.ingredients.items():
            final_ingrediats.append(f"{key}: {value}")

        return f"You've ordered pizza {self.name} prepared with {', '.join(final_ingrediats)} and the price will be {self.price}lv."



margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
