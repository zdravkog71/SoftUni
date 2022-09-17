from EncapsulationExercise.project_pizza.dough import Dough
from EncapsulationExercise.project_pizza.pizza import Pizza
from EncapsulationExercise.project_pizza.topping import Topping

d = Dough("Sugar", "Mixing", 20)
t = Topping("Tomato", 20)
p = Pizza("Burger", d, 200)
p.add_topping(t)
print(p.calculate_total_weight())
p.add_topping(t)


print(p.calculate_total_weight())



