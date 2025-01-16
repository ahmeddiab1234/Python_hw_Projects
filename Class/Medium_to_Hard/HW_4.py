# HW - 3 - Medium to Hard - OOP - Classes - Students Grades - Wrapper

class StudentGradesInfo:
    statistics_total_prints = 0

    def __init__(self, student_id):
        self.student_id = student_id
        self.grades = {}  

    def adjust_grade(self, grade):
        if grade < 0:
            return 0
        if grade > 100:
            return 100
        return grade

    def add_grade(self, grade, course_name):
        grade = self.adjust_grade(grade)
        if course_name in self.grades:
            return False  

        self.grades[course_name] = grade
        return True

    @classmethod
    def increment_statistics(cls):
        cls.statistics_total_prints += 1

    def print_info(self):
        self.increment_statistics()
        print(f'Grades info for Student ID {self.student_id}')
        for course_name, grade in self.grades.items():
            print(f'Course: {course_name} - Grade: {grade}')

    def get_total_grades_sum(self):
        return {
            "total_sum": sum(self.grades.values()),
            "max_possible_sum": 100 * len(self.grades),
        }

class StudentGradesInfoWrapper:
    def __init__(self, stu):
        self.stu = stu
        self.student_id = stu.student_id
        self.grades = list(stu.grades.items())
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.grades):
            course, grade = self.grades[self.index]
            self.index += 1
            return grade, course
        raise StopIteration

    def adjust_grade(self, grade):
        return self.stu.adjust_grade(grade)

    def add_grade(self, grade, course_name):
        return self.stu.add_grade(grade, course_name)

    def print_info(self):
        return self.stu.print_info()

    def get_total_grades_sum(self):
        return self.stu.get_total_grades_sum()


if __name__ == '__main__':
    student = StudentGradesInfo('ID1234')
    
    student.add_grade(70, 'Math')
    student.add_grade(70, 'prgramming 1')
    student.add_grade(85, 'prgramming 2')
    student_wrapper = StudentGradesInfoWrapper(student)

    for grade, course in student_wrapper:
        print(f'Course: {course} - Grade: {grade}')
    
    print(student_wrapper.get_total_grades_sum())


"""
Course: Math - Grade: 70
Course: prgramming 1 - Grade: 70
Course: prgramming 2 - Grade:70
"""