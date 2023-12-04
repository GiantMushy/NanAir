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
        Check if CSV file exists, creating one if not with headers
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

    def modify_employee_data(self, updated_employees):
        """
        Write the updated list of employees to the CSV file.
        :param updated_employees: List of Employee objects with updated information.
        """
        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                if updated_employees:
                    writer = csv.DictWriter(
                        file, fieldnames=updated_employees[0].__dict__.keys())
                    writer.writeheader()
                    for emp in updated_employees:
                        writer.writerow(emp.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def delete_employee(self, id):
        """
        Delete an employee from the CSV file based on their ID.
        :param id: ID of the employee to be deleted.
        """
        employees = self.read_all_employees()
        # filter out the employee to delete
        employees = [emp for emp in employees if emp.id != id]

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
