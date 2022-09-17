from project.student import Student

from unittest import TestCase, main

class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student('Zdravko', {'Python':['Python OOP']})

    def test_init_student__expect_atributes(self):
        result_name = self.student.name
        result_courses = self.student.courses
        expected_results_name = 'Zdravko'
        expected_results_cources = {'Python':'Python OOP'}
        self.assertEqual(expected_results_name, result_name)
        self.assertEqual(expected_results_cources, result_courses)

    def test_enroll__course_in_courses__add_notes_return_msg(self):
        result = self.student.enroll('Python', 'a', 'y')
        expected_result = 'Course already added. Notes have been updated.'
        self.assertEqual(expected_result, result)

    def test_enroll__course_in_courses__expect_to_add_notes(self):
        self.student.enroll('Python', 'a', 'y')
        result = self.student.courses['Python']
        expected_result = ['Python OOP','a']
        self.assertEqual(expected_result, result)

    def test_enroll__add_course_notes_y__add_notes_return_msg(self):
        result = self.student.enroll('Python1', 'a', 'Y')
        expected_result = 'Course and course notes have been added.'
        self.assertEqual(expected_result, result)

    def test_enroll__add_course_notes_y__add_course_and_notes(self):
        self.student.enroll('Python1', 'a', 'Y')
        result = self.student.courses['Python1']
        expected_result = 'a'
        self.assertEqual(expected_result, result)

    def test_enroll__add_course__add_course_and_notes(self):
        self.student.enroll('Python1', 'a', 'n')
        result = self.student.courses['Python1']
        expected_result = []
        self.assertEqual(expected_result, result)

    def test_enroll__add_course__add_course_and_notes__return_result(self):
        result = self.student.enroll('Python1', 'a', 'n')
        expected_result = 'Course has been added.'
        self.assertEqual(expected_result, result)

    def test_add_notes__no_course_found__raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python1', 'a')
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_add_notes__course_is_found__append_notes(self):
        self.student.add_notes('Python', 'a')
        result = self.student.courses['Python']
        expected_result = ['Python OOP', 'a']
        self.assertEqual(expected_result, result)

    def test_leave_course__course_is_not_in_courses__raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Python1')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))
        result = self.student.courses
        expected_result = {'Python':['Python OOP']}
        self.assertEqual(expected_result, result)

    def test_leave_course__course_is_in_courses__return_msg(self):
        result = self.student.leave_course('Python')
        expected_result = 'Course has been removed'
        self.assertEqual(expected_result, result)

    def test_leave_course__course_is_in_courses__expected_course_to_be_removed(self):
        self.student.leave_course('Python')
        result = self.student.courses
        expected_result = {}
        self.assertEqual(expected_result, result)
"""
    def __init__(self, name: str, courses=None):
        if courses is None:
            courses = {}
        self.name = name
        self.courses = courses  # {course_name: [notes]}
"""

if __name__ == '__main__':
    main()