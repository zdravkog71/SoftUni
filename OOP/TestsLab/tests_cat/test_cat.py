from TestsLab.project_cat.cat import Cat

import unittest

class CatTests(unittest.TestCase):
    NAME = 'Kuku'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__expect_size_to_incr(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__expect_cat_is_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat__after_eating_raises(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertIsNotNone(ex)
        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep__when_fed_is_false__raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertIsNotNone(ex)
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep__after_sleeping__ecpect_sleepy_to_be_false(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()