from Employee import EmployeeClass
from FrontEndManager import FrontEndClass

class EmployeeManagerClass:
    def __init__(self, frontend, employee):
        self.frontend = frontend
        self.employee = employee

    def _add_employee(self):
        name, age, salary = self.frontend.get_employee_data()
        self.employee.add_employee(name, age, salary)
        self.frontend.show_message("Employee added successfully!")

    def _list_employees(self):
        employees = self.employee.get_all_employees()
        self.frontend.display_employees(employees)

    def _delete_by_age(self):
        start_age, end_age = self.frontend.get_age_range()
        deleted_count = self.employee.delete_by_age(start_age, end_age)
        self.frontend.show_message(f"Deleted {deleted_count} employees.")

    def _update_salary(self):
        name, salary = self.frontend.get_name_and_salary()
        if self.employee.update_salary(name, salary):
            self.frontend.show_message(f"Updated {name}'s salary to {salary}.")
        else:
            self.frontend.show_message("Employee not found.")

if __name__ == "__main__":
    frontend = FrontEndClass()
    employee = EmployeeClass()
    manager = EmployeeManagerClass(frontend, employee)

    while True:
        frontend.print_menu_options()
        choice = frontend.get_menu_choice()

        if choice == 1:
            manager._add_employee()
        elif choice == 2:
            manager._list_employees()
        elif choice == 3:
            manager._delete_by_age()
        elif choice == 4:
            manager._update_salary()
        elif choice == 5:
            frontend.show_message("Exiting program. Goodbye!")
            break


