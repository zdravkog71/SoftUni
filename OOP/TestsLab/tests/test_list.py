from TestsLab.project.list import IntegerList

import unittest

class IntergerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.integer_list = IntegerList(1,2,3,'zdr')

    def test_get_data__expect_list(self):
        result = self.integer_list.get_data()
        expected_result = [1,2,3]
        self.assertEqual(expected_result, result)

    def test_add_element__expect_append_int_to_list(self):
        self.integer_list.add(10)
        expected_result = [1,2,3,10]
        result = self.integer_list.get_data()
        self.assertEqual(expected_result, result)

    def test_add_element__expect_append_return_list_integers(self):
        result = self.integer_list.add(10)
        expected_result = [1,2,3,10]

        self.assertEqual(expected_result, result)

    def test_add_element__add_non_int_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.add(2.5)
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_remove_index__index_outside_rasises_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.remove_index(10)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_remove_index__valid_index_expect_removed_el_to_be_returned(self):
        result = self.integer_list.remove_index(0)
        expected_result = 1
        self.assertEqual(expected_result, result)

    def test_remove_index__valid_index_expect_removed_el(self):
        self.integer_list.remove_index(0)
        result = self.integer_list.get_data()
        expected_result = [2,3]
        self.assertEqual(expected_result, result)

    def test_get__index_outside_rasises_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.get(10)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get__expect_element_on_index_to_be_returned(self):
        result = self.integer_list.get(0)
        expected_result = 1
        self.assertEqual(expected_result, result)

    def test_insert__index_outside__rasises_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.insert(10, 20)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert__insert_non_int__raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.insert(0, 2.5)
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert__expect_element_on_index_to_be_inserted(self):
        self.integer_list.insert(0,10)
        result = self.integer_list.get_data()
        expected_result = [10,1,2,3]
        self.assertEqual(expected_result, result)

    def test_get_biggest__expect_biggest_bumber(self):
        result = self.integer_list.get_biggest()
        expected_result = 3
        self.assertEqual(expected_result, result)

    def test_get_index__expect_index_of_element_to_be_returned(self):
        result = self.integer_list.get_index(1)
        expected_result = 0
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
