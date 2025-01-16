class EmployeeClass:
    def __init__(self):
        self.employee_list = []
        self.current_id = 0

    def add_employee(self, name, age, salary):
        self.employee_list.append({"id": self.current_id, "name": name, "age": age, "salary": salary})
        self.current_id += 1

    def get_all_employees(self):
        return sorted(self.employee_list, key=lambda x: x["id"])

    def delete_by_age(self, start_age, end_age):
        initial_count = len(self.employee_list)
        self.employee_list = [
            employee for employee in self.employee_list
            if not (start_age <= employee["age"] <= end_age)
        ]
        return initial_count - len(self.employee_list)

    def update_salary(self, name, salary):
        for employee in self.employee_list:
            if employee["name"].lower() == name.lower():
                employee["salary"] = salary
                return True
        return False
    

    