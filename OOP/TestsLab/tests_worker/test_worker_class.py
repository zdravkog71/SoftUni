import unittest
from unittest import TestCase
from TestsLab.project_woker import Worker

class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Zdravko', 500, 100)

    def test_worker_name(self):
        result = self.worker.name
        expected_result = 'Zdravko'
        self.assertEqual(expected_result, result)

    def test_worker_salary(self):
        result = self.worker.salary
        expected_result = 500
        self.assertEqual(expected_result, result)

    def test_worker_energy(self):
        result = self.worker.energy
        expected_result = 100
        self.assertEqual(expected_result, result)

    def test__worker_init__expect_0_money(self):
        result = self.worker.money
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_energy_is_incr_after_rest(self):
        self.worker.rest()
        result = self.worker.energy
        expected_result = 101
        self.assertEqual(expected_result, result)

    def test__work__when_energy_is_0__expect_to_raise(self):
        worker = Worker('Test Name', 100, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

        self.assertIsNotNone(ex)

    def test__work__when_energy_is_more_than_0__expect_money_incr(self):
        self.worker.work()
        result = self.worker.money
        expected_result = 500
        self.assertEqual(expected_result, result)

    def test__work__when_energy_is_more_then_0__expect_enerdy_decr(self):
        self.worker.work()
        result = self.worker.energy
        expected_result = 99
        self.assertEqual(expected_result, result)

    def test__get_info__expect_return_msg(self):
        result = self.worker.get_info()
        expected_result = 'Zdravko has saved 0 money.'
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()