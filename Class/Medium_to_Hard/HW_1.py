# HW - 1 - Medium to Hard - OOP - Classes - Students Grades - Code Review

statistics_total_prints = 0

class StudentGradesInfo:
    def __init__(self, id):
        self.id = id
        self.grades = []
        self.courses_names = []

    def adjust_grade(self, grade):
        if grade < 0:
            return grade 
        if grade > 100:
            return 100
        return grade

    """
    This function adds a new course IFF the course is not already added 
    If added, course old value is not overwritten!
    """
    def add_grade(self, grade, course_name):
        self.grades.append(self.adjust_grade(grade))

        if course_name in self.courses_names:
            return False
        self.courses_names.append(course_name)
        return True


    def print(self):
        global statistics_total_prints
        statistics_total_prints +=1

        print(f'Grades info for Student ID {self.id}')
        for idx in range(len(self.grades)):
            print(f'Course: {self.courses_names[idx]}'
                  f'- Grade: {self.grades[idx]}' )
        
    def get_total_grades_sum(self):
        return {sum(self.grades), 100 * len(self.grades)}


# if __name__ == '__main__':
#     student1 = StudentGradesInfo('ID1234')
#     student1.add_grade(70, 'Math')
#     student1.add_grade(70, 'programming 1')
#     student1.add_grade(85, 'programming 2')

#     student1.print()
#     print(student1.get_total_grades_sum())


"""
statistics_total_prints = 0  -> must be static method in the class not global varibales 
we wouldn't be want global statistics_total_prints in print funcion

to avoid overwrite and index out of range error we can make dict (course_name: grade)
instead two lists this will update the grade automitically in the dict without make new item in list

in adjuct grade in the condition if grade < 0  the fun return grade but it must return 0 as we don't want to return negative value
"""


# cprrect cpde
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


# if __name__ == '__main__':
#     student1 = StudentGradesInfo('ID1234')
#     student1.add_grade(70, 'Math')
#     student1.add_grade(70, 'Programming 1')
#     student1.add_grade(85, 'Programming 2')

#     student1.print_info()
#     print(student1.get_total_grades_sum())
