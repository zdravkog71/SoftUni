from InheritanceExercises.project_vehicle.car import Car
from InheritanceExercises.project_vehicle.family_car import FamilyCar
from InheritanceExercises.project_vehicle.motorcycle import Motorcycle
from InheritanceExercises.project_vehicle.vehicle import Vehicle

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
motor = Motorcycle(50,150)
print(motor.fuel_consumption)
opel = Car(50,150)
print(opel.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)