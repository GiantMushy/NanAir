import csv
import os
from Models.Employee import Employee

# TODO: update to include no business logic, and move it to the logiclayer


class EmployeeData:
    def __init__(self, filename='DataLayer/Repository/Employee.csv'):
        """
        Initialize the EmployeeData with the path to CSV file with employee data.
        """
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        Check if CSV file exists, creating one if not
        """

        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'name', 'social_security_number',
                                                          'address', 'mobile_phone_number',
                                                          'email_address', 'home_phone_number'])
                writer.writeheader()

    def read_all_employees(self):
        """
        Read all employees from the CSV file and return them as a list of Employee objects.
        :return: List of Employee objects.
        """
        employees = []
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employees.append(Employee(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.filename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return employees

    def add_employee(self, employee):
        """
        Add a new employee to the CSV file.
        :param employee: Employee object to be added.
        """
        required_fields = ['id', 'name', 'social_security_number', 'address',
                           'mobile_phone_number', 'email_address']

        # checking for missing required fields
        for field in required_fields:
            if getattr(employee, field, None) is None:
                raise ValueError(f"Missing required employee field: {field}")

        try:
            with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=employee.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(employee.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def modify_employee(self, id, **updates):
        """
        Modify an existing employee's details in the CSV file.
        :param id: ID of the employee to be modified.
        :param updates: Dictionary of updates to be applied.
        """
        if any(key in updates for key in ['id', 'name', 'social_security_number']):
            raise ValueError(
                "Modification of 'id', 'name', or 'social_security_number' is not allowed")

        employees = self.read_all_employees()
        employee_found = False
        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=employees[0].__dict__.keys())
                writer.writeheader()
                for emp in employees:
                    if emp.id == id:
                        employee_found = True
                        for key, value in updates.items():
                            setattr(emp, key, value)
                    writer.writerow(emp.__dict__)
        except Exception as e:
            raise Exception(f"An error occurred while modifying the file: {e}")

        if not employee_found:
            raise ValueError(f"Employee with ID {id} not found")

    def delete_employee(self, id):
        """
        Delete an employee from the CSV file based on their ID.
        :param id: ID of the employee to be deleted.
        """
        employees = self.read_all_employees()
        if not any(emp.id == id for emp in employees):
            raise ValueError(f"Employee with ID {id} not found")

        employees = [emp for emp in employees if emp.id != id]

        # check if the employees list is empty before proceeding
        if not employees:
            # if the list is empty, clear the file or handle it as needed
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'name', 'social_security_number',
                                                          'address', 'mobile_phone_number',
                                                          'email_address', 'home_phone_number'])
                writer.writeheader()
            return

        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=employees[0].__dict__.keys())
                writer.writeheader()
                for emp in employees:
                    writer.writerow(emp.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while deleting from the file: {e}")
