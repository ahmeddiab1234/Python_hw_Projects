# HW - 2 - OOP - Inhertance - Easy - Build Hierarchy

class CommunityMember:
    pass

class Employee(CommunityMember):
    pass

class Faculty(Employee):
    pass

class Administrator(Faculty):
    pass

class Teacher(Faculty):
    pass

class AdministratorTeacher(Administrator, Teacher):
    pass


class Staff(Employee):
    pass


class Student(CommunityMember):
    pass


class Alumnus(CommunityMember):
    pass




