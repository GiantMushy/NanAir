from DataLayer.EmployeeData import EmployeeData
from Models.Employee import Employee

# TODO: add docstrings, and implement logic from storage layer in here.


class EmployeeManagerLogic:
    def __init__(self):
        self.employee_data = EmployeeData()

    def generate_unique_employee_id(self):
        employees = self.employee_data.read_all_employees()
        if not employees:
            return "001"  # base case, no employees in the database

        max_id = max(int(emp.id) for emp in employees)
        new_id = max_id + 1  # incrementing the id by 1
        return str(new_id).zfill(3)  # just padding the id with zeros

    def add_employee(self, name, ssn, phone, address, email, home_phone):
        employee_id = self.generate_unique_employee_id()

        # create new Employee object
        new_employee = Employee(employee_id, name, ssn,
                                address, phone, email, home_phone)

        # adding new employee
        self.employee_data.add_employee(new_employee)

    def list_all_employees(self):
        return self.employee_data.read_all_employees()

    def find_employee_by_id(self, employee_id):
        return next((emp for emp in self.employee_data.read_all_employees() if emp.id == employee_id), None)

    def modify_employee(self, employee_id, **updates):
        self.employee_data.modify_employee(employee_id, **updates)

    def delete_employee(self, employee_id):
        self.employee_data.delete_employee(employee_id)

    # B-requirements will be implemented  here.
