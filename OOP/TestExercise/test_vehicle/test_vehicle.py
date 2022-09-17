from TestExercise.project_vehicle.vehicle import Vehicle

import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(2.5, 50.5)

    def test_init__expect_fuel_capacity_horse_power_fuel_consumption(self):
        result_fuel = self.car.fuel
        result_capacity = self.car.capacity
        result_horse_power = self.car.horse_power
        result_fuel_consumption = self.car.DEFAULT_FUEL_CONSUMPTION
        expected_result_fuel = 2.5
        expected_result_capacity = 2.5
        expected_result_horse_power = 50.5
        expected_result_fuel_consumption = 1.25
        self.assertEqual(expected_result_fuel, result_fuel)
        self.assertEqual(expected_result_capacity, result_capacity)
        self.assertEqual(expected_result_horse_power, result_horse_power)
        self.assertEqual(expected_result_fuel_consumption, result_fuel_consumption)

    def test_drive__not_enough_fuel__raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive__drive_distance__expect_fuel_decr(self):
        self.car.drive(1)
        result = self.car.fuel
        expected_result = 1.25
        self.assertEqual(expected_result, result)

    def test_refuel__not_too_much_fuel__raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(1000)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel__refuel__expect_fuel_incr(self):
        self.car.drive(1)
        self.car.refuel(1.25)
        result = self.car.fuel
        expected_result = 2.5
        self.assertEqual(expected_result, result)

    def test_return_string(self):
        result = self.car.__str__()
        expected_result = 'The vehicle has 50.5 horse power with 2.5 fuel left and 1.25 fuel consumption'
        self.assertEqual(expected_result, result)
