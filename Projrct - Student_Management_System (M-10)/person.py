from school import School
import random

class Person:
    def __init__(self, name) -> None:
        self.name = name


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1, 100)
    

class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.marks = {}     # {"eng" : 78, "ICT" : 90}
        self.subject_grade = {}     # {"eng" : 'A', 'math' : 'A+'}
        self.grade = None   # final grade


    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            sum += point
        gpa = sum / len(self.subject_grade)
        self.grade = School.value_to_grade(gpa)


    # rahi.id == 
    # rahi.id = 12

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value