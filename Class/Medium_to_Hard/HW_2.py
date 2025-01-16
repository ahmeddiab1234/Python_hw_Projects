# HW - 2 - Medium to Hard - OOP - Classes - Students Grades - Testing

statistics_total_prints = 0

class StudentGradesInfo1:
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


# Testing on the base code

class StudentGradesInfoTester1:
    @classmethod
    def test_total_courses_cnt(cls):
        student = StudentGradesInfo1('ID5678')
        student.add_grade(90, 'Math')
        student.add_grade(85, 'Science')
        assert len(student.grades) == 2, "Total courses count test failed!"
        print("test_total_courses_cnt passed!")

    @classmethod
    def test_grades_sum(cls):
        student = StudentGradesInfo1('ID5678')
        student.add_grade(90, 'Math')
        student.add_grade(85, 'Science')
        result = student.get_total_grades_sum()
        assert result["total_sum"] == 175, "Grades sum test failed!"
        assert result["max_possible_sum"] == 200, "Max possible sum test failed!"
        print("test_grades_sum passed!")

    @classmethod
    def test_printing(cls):
        student = StudentGradesInfo1('ID5678')
        student.add_grade(90, 'Math')
        student.add_grade(85, 'Science')
        # Simulate print output
        import io
        from contextlib import redirect_stdout
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            student.print_info()
        output = buffer.getvalue()
        assert "Grades info for Student ID ID5678" in output, "Printing test failed!"
        assert "Course: Math - Grade: 90" in output, "Math course printing failed!"
        assert "Course: Science - Grade: 85" in output, "Science course printing failed!"
        print("test_printing passed!")

    @classmethod
    def test_all(cls):
        calls = [
            cls.test_total_courses_cnt,
            cls.test_grades_sum,
            cls.test_printing,
        ]
        for call in calls:
            call()


# cprrect cpde
class StudentGradesInfo2:
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


# Testing on the correct codeclass StudentGradesInfoTester:
class StudentGradesInfoTester2:
    @classmethod
    def test_total_courses_cnt(cls):
        student = StudentGradesInfo2('ID5678')
        student.add_grade(90, 'Math')
        student.add_grade(85, 'Science')
        assert len(student.grades) == 2, "Total courses count test failed!"
        print("test_total_courses_cnt passed!")

    @classmethod
    def test_grades_sum(cls):
        student = StudentGradesInfo2('ID5678')
        student.add_grade(90, 'Math')
        student.add_grade(85, 'Science')
        result = student.get_total_grades_sum()
        assert result["total_sum"] == 175, "Grades sum test failed!"
        assert result["max_possible_sum"] == 200, "Max possible sum test failed!"
        print("test_grades_sum passed!")

    @classmethod
    def test_printing(cls):
        student = StudentGradesInfo2('ID5678')
        student.add_grade(90, 'Math')
        student.add_grade(85, 'Science')
        # Simulate print output
        import io
        from contextlib import redirect_stdout
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            student.print_info()
        output = buffer.getvalue()
        assert "Grades info for Student ID ID5678" in output, "Printing test failed!"
        assert "Course: Math - Grade: 90" in output, "Math course printing failed!"
        assert "Course: Science - Grade: 85" in output, "Science course printing failed!"
        print("test_printing passed!")

    @classmethod
    def test_all(cls):
        calls = [
            cls.test_total_courses_cnt,
            cls.test_grades_sum,
            cls.test_printing,
        ]
        for call in calls:
            call()

if __name__ == "__main__":
    # StudentGradesInfoTester1.test_all() #assert result["total_sum"] == 175, "Grades sum test failed!"
    StudentGradesInfoTester2.test_all()
