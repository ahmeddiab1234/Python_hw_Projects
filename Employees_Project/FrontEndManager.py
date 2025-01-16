class FrontEndClass:
    def __init__(self):
        pass

    def print_menu_options(self):
        print("Program Options:")
        print("1) Add a new employee")
        print("2) List all employees")
        print("3) Delete by age range")
        print("4) Update salary given a name")
        print("5) End the program")

    def get_menu_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice (1-5): "))
                if 1 <= choice <= 5:
                    return choice
                print("Invalid range. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def get_employee_data(self):
        name = input("Enter the employee name: ").strip()
        while True:
            try:
                age = int(input("Enter the employee age: "))
                salary = int(input("Enter the employee salary: "))
                return name, age, salary
            except ValueError:
                print("Invalid input. Age and salary must be integers.")

    def get_age_range(self):
        while True:
            try:
                start_age = int(input("Enter the starting age: "))
                end_age = int(input("Enter the ending age: "))
                if start_age > end_age:
                    print("Start age must be less than or equal to end age.")
                else:
                    return start_age, end_age
            except ValueError:
                print("Invalid input. Please enter integers for the age range.")

    def get_name_and_salary(self):
        name = input("Enter the employee name: ").strip()
        while True:
            try:
                salary = int(input("Enter the new salary: "))
                return name, salary
            except ValueError:
                print("Invalid input. Salary must be an integer.")

    def show_message(self, message):
        print(message)

    def display_employees(self, employees):
        if not employees:
            print("No employees at the moment!")
        else:
            print("\n----------- Employees List -----------")
            for employee in employees:
                print(f"Employee: {employee['name']} has age {employee['age']} and salary {employee['salary']}")
            print()