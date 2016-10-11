"""
Demonstrating a Student is a Person concept in oop
Kevin Oyowe
"""
class Person(object):  # super class (main).
    def __init__(self, gender="Male", date_of_birth='1980'):
        self.gender = gender
        self.date_of_birth = date_of_birth


class Student(Person):  # inheritance
    def __init__(self, gender, date_of_birth, first_name, other_names, department, course, year_of_study):
        super().__init__(gender, date_of_birth)
	self.first_name = first_name
	self.other_names = other_names
        self.department = department
        self.course = course
        self.year_of_study = year_of_study


student1 = Student('male', '01-01-1990', 'Information Sciences', 'Computer Studies', 'Year 1')

print(student1.first_name)
print(student1.other_names)
print(student1.gender)
print(student1.date_of_birth)
print(student1.department)
print(student1.course)
print(student1.year_of_study)
