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

        # validate input data, further checks on the data itself (births etc.) can be
        # implemented here later on.
        required_fields = [name, ssn, phone, address, email, home_phone]
        if any(field is None or field == '' for field in required_fields):
            raise ValueError(
                "All fields are required and cannot be empty, please try again.")

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
        if any(key in updates for key in ['id', 'name', 'social_security_number']):
            raise ValueError(
                "Modification of 'id', 'name', or 'social_security_number' is not allowed")

        employees = self.list_all_employees()
        employee_found = False
        updated_employees = []

        for emp in employees:
            if emp.id == employee_id:
                employee_found = True
                for key, value in updates.items():
                    if hasattr(emp, key):
                        setattr(emp, key, value)
                    else:
                        raise ValueError(f"Invalid field: {key}")
            updated_employees.append(emp)

        if not employee_found:
            raise ValueError(f"Employee with ID {employee_id} not found")

        self.employee_data.modify_employee_data(updated_employees)

    def delete_employee(self, employee_id):
        employees = self.list_all_employees()
        if not any(emp.id == employee_id for emp in employees):
            raise ValueError(f"Employee with ID {employee_id} not found")

        remaining_employees = [
            emp for emp in employees if emp.id != employee_id]
        self.employee_data.delete_employee_data(remaining_employees)

    # B-requirements will be implemented  here.
