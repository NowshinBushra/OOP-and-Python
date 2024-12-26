from person import Teacher
from school import School

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam() # 1-100
            self.marks[self.name] = mark    # {"eng" : 78}
            self.subject_grade[self.name] = School.calculate_grade(mark)    # {"eng" : 'A'}
