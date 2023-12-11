import csv
import os
from Code.Models.Employee import Employee
from Code.Models.Pilot import Pilot
from Code.Models.FlightAttendant import FlightAttendant


class EmployeeData:
    def __init__(self, employee_filename='Code/DataLayer/Repository/Employee.csv',
                 pilot_filename='Code/DataLayer/Repository/Pilot.csv',
                 flight_attendant_filename='Code/DataLayer/Repository/FlightAttendant.csv'):
        self.employee_filename = employee_filename
        self.pilot_filename = pilot_filename
        self.flight_attendant_filename = flight_attendant_filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        '''
        Check if CSV files exist, creating them if not with headers.
        '''
        self.create_file_if_not_exists(self.employee_filename, ['id', 'name', 'social_security_number',
                                                                'address', 'mobile_phone_number',
                                                                'email_address', 'home_phone_number'])
        self.create_file_if_not_exists(self.pilot_filename, [
                                       'id', 'pilot_role', 'airplane_type'])
        self.create_file_if_not_exists(self.flight_attendant_filename, [
                                       'id', 'attendant_role'])

    def create_file_if_not_exists(self, filename, fieldnames):
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    def read_all_employees(self):
        '''
        Read all employees from the Employee CSV file and return them as a list of Employee objects.

        Returns, return: List of Employee objects.
        '''
        employees = []
        try:
            with open(self.employee_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employees.append(Employee(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.employee_filename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return employees

    def read_all_pilots(self):
        '''
        Read all pilots from the Pilot CSV file and return them as a list of Pilot objects.

        Returns, return: List of Pilot objects.
        '''
        pilots = []
        try:
            with open(self.pilot_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    pilots.append(Pilot(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.pilot_filename} does not exist.")
        except Exception as e:
            raise Exception(
                f"An error occurred while reading the Pilot file: {e}")
        return pilots

    def read_all_flight_attendants(self):
        '''
        Read all flight attendants from the FlightAttendant CSV file and return them as a list of FlightAttendant objects.

        Return, return: List of FlightAttendant objects.
        '''
        flight_attendants = []
        try:
            with open(self.flight_attendant_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    flight_attendants.append(FlightAttendant(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.flight_attendant_filename} does not exist.")
        except Exception as e:
            raise Exception(
                f"An error occurred while reading the FlightAttendant file: {e}")
        return flight_attendants

    def add_employee(self, employee):
        '''
        Add a new employee to the CSV file.

        :param employee: Employee object to be added.
        '''

        try:
            with open(self.employee_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=employee.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(employee.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def modify_employee_data(self, updated_employees):
        '''
        Write the updated list of employees to the CSV file.

        :param updated_employees: List of Employee objects with updated information.
        '''
        try:
            with open(self.employee_filename, mode='w', newline='', encoding='utf-8') as file:
                if updated_employees:
                    writer = csv.DictWriter(
                        file, fieldnames=updated_employees[0].__dict__.keys())
                    writer.writeheader()
                    for emp in updated_employees:
                        writer.writerow(emp.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def add_pilot(self, pilot):
        '''
        Add a new pilot to the Pilot CSV file.

        :param pilot: Pilot object to be added.
        '''
        self.add_record(self.pilot_filename, pilot)

    def add_flight_attendant(self, flight_attendant):
        '''
        Add a new flight attendant to the FlightAttendant CSV file.

        :param flight_attendant: FlightAttendant object to be added.
        '''
        self.add_record(self.flight_attendant_filename, flight_attendant)

    def add_record(self, filename, record):
        try:
            with open(filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=record.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(record.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")
