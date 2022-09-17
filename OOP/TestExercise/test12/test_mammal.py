from TestExercise.project_mammal.mammal import Mammal

import unittest

class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.animal = Mammal('Teddy', 'bear', 'roar')

    def test_animal_init(self):
        result_name = self.animal.name
        result_type = self.animal.type
        result_sound = self.animal.sound

        expected_result_name = 'Teddy'
        expected_result_type = 'bear'
        expected_result_sound = 'roar'
        self.assertEqual(expected_result_name, result_name)
        self.assertEqual(expected_result_type, result_type)
        self.assertEqual(expected_result_sound, result_sound)

    def test_make_sound__expect_str_with_sound(self):
        result = self.animal.make_sound()
        expected_result = 'Teddy makes roar'
        self.assertEqual(expected_result, result)

    def test_get_kingdom__expect_to_return_kingdom(self):
        result = self.animal.get_kingdom()
        expected_result = 'animals'
        self.assertEqual(expected_result, result)

    def test_info__expect_to_return_animal_info(self):
        result = self.animal.info()
        expected_result = 'Teddy is of type bear'
        self.assertEqual(expected_result, result)