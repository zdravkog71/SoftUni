from InheritanceLab.project_person.person import Person
from InheritanceLab.project_person.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."