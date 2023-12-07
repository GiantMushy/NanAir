from DataLayer.EmployeeData import EmployeeData
from DataLayer.DestinationData import Destination_Data

class DataLayerAPI:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.destination_data = Destination_Data()

    def read_all_employees(self):
        """
        Read all employees from the Employee CSV file and return them as a list of Employee objects.
        :return: List of Employee objects.
        """
        return self.employee_data.read_all_employees()

    def read_all_pilots(self):
        """
        Read all pilots from the Pilot CSV file and return them as a list of Pilot objects.
        :return: List of Pilot objects.
        """
        return self.employee_data.read_all_pilots()

    def read_all_flight_attendants(self):
        """
        Read all flight attendants from the FlightAttendant CSV file and return them as a list of FlightAttendant objects.
        :return: List of FlightAttendant objects.
        """
        return self.employee_data.read_all_flight_attendants()

    def add_employee(self, employee):
        """
        Add a new employee to the CSV file.
        :param employee: Employee object to be added.
        """
        self.employee_data.add_employee(employee)

    def modify_employee_data(self, updated_employees):
        """
        Write the updated list of employees to the CSV file.
        :param updated_employees: List of Employee objects with updated information.
        """
        self.employee_data.modify_employee_data(updated_employees)

    def add_pilot(self, pilot):
        """
        Add a new pilot to the Pilot CSV file.
        :param pilot: Pilot object to be added.
        """
        self.employee_data.add_pilot(pilot)

    def add_flight_attendant(self, flight_attendant):
        """
        Add a new flight attendant to the FlightAttendant CSV file.
        :param flight_attendant: FlightAttendant object to be added.
        """
        self.employee_data.add_flight_attendant(flight_attendant)

    def read_all_destinations(self):
        """
        Read all destinations from the Destination CSV file and return them as a list of Destination objects.
        :return: List of Destination objects.
        """
        return self.destination_data.read_all_destinations()

    def add_destination(self, destination):
        """
        Add a new destination to the Destination CSV file.
        :param destination: Destination object to be added.
        """
        self.destination_data.add_destination(destination)

    def modify_destination_data(self, updated_destinations):
        """
        Write the updated list of destinations to the CSV file.
        :param updated_destinations: List of Destination objects with updated information.
        """
        self.destination_data.modify_destination_data(updated_destinations)
