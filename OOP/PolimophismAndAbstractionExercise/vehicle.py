from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, furl_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = furl_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_spent = distance * (self.fuel_consumption + 0.9)
        if fuel_spent <= self.fuel_quantity:
            self.fuel_quantity -= fuel_spent

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_spent = distance * (self.fuel_consumption + 1.6)
        if fuel_spent <= self.fuel_quantity:
            self.fuel_quantity -= fuel_spent

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)