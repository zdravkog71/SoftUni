from TestsLab.project.car_manager import Car

import unittest

class CarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("a", "b", 1, 4)

    def test_init_expect_make_model_fuelconsum_capacity_fuelamount(self):
        result_make = self.car.make
        result_model = self.car.model
        result_fuel_consumption = self.car.fuel_consumption
        result_capacity = self.car.fuel_capacity
        result_fuel_amount = self.car.fuel_amount
        expected_result_make = 'a'
        expected_result_model = 'b'
        expected_result_fuel_consumption = 1
        expected_result_capacity = 4
        expected_result_fuel_amount = 0
        self.assertEqual(expected_result_make, result_make)
        self.assertEqual(expected_result_model, result_model)
        self.assertEqual(expected_result_fuel_consumption, result_fuel_consumption)
        self.assertEqual(expected_result_capacity, result_capacity)
        self.assertEqual(expected_result_fuel_amount, result_fuel_amount)

    def test_make__make_is_empty__expect_error_raise(self):
        with self.assertRaises(Exception) as ex:
            car_empty = Car('','c',1,4)
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_model__model_is_empty__expect_error_raise(self):
        with self.assertRaises(Exception) as ex:
            car_empty = Car('a','',1,4)
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_consumption__consumtion_is_empty__expect_error_raise(self):
        with self.assertRaises(Exception) as ex:
            car_empty = Car('a','c',0,4)
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_capacity__fuel_capacity_is_empty__expect_error_raise(self):
        with self.assertRaises(Exception) as ex:
            car_empty = Car('a','c',1,0)
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_fuel_amount__fuel_amount_is_negative__expect_error_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_refuel__fuel_amount_is_zero__expect_error_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel__fuel_amount_is_negative__expect_error_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel__add_fuel__expect_fuel_amount_incr(self):
        self.car.refuel(3)
        result = self.car.fuel_amount
        expected_result = 3
        self.assertEqual(expected_result, result)

    def test_refuel__add_fuel_more_than_capacity__expect_fuel_amount_incr_to_capacity(self):
        self.car.refuel(10)
        result = self.car.fuel_amount
        expected_result = 4
        self.assertEqual(expected_result, result)

    def test_drive__distance_is_longer__expect_error_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10000)
        self.assertEqual('You don\'t have enough fuel to drive!', str(ex.exception))

    def test_drive__drive_distance__expect_fuel_amount_to_decr(self):
        self.car.refuel(4)
        self.car.drive(100)
        result = self.car.fuel_amount
        expected_result = 3
        self.assertEqual(expected_result, result)





if __name__ == "__main__":
    unittest.main()