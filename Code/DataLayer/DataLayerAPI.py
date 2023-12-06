from DataLayer.EmployeeData import EmployeeData
from DataLayer.DestinationData import DestinationData
from DataLayer.AirplaneData import AirplaneData


class DataLayerAPI:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.destination_data = DestinationData()
        self.airplane_data = AirplaneData()

    ################################## Employee Data Functions ###################################
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


    ################################## Destination Data Functions ###################################

    def read_all_destinations(self):
        """
        Read all destination from the Destination CSV file and return them as a list of Destination objects.
        :return: List of Destination objects.
        """
        return self.destination_data.read_all_destinations()

    def add_destination(self, destination):
        """
        Add a new destination to the CSV file.
        :param destination: Destination object to be added.
        """
        self.destination_data.add_destination(destination)

    ################################## Airplane Data Functions ###################################

    def read_all_airplanes(self):
        """
        Read all airplane from the Airplane CSV file and return them as a list of Airplane objects.
        :return: List of airplane objects.
        """
        return self.airplane_data.read_all_airplanes()

    def add_airplane(self, airplane):
        """
        Add a new airplane to the CSV file.
        :param airplane: Airplane object to be added.
        """
        self.airplane_data.add_airplane(airplane)

    def modify_airplane_data(self, updated_airplanes):
        """
        Write the updated list of airplanes to the CSV file.
        :param updated_airplanes: List of airplane objects with updated information.
        """
        self.airplane_data.modify_airplane_data(updated_airplanes)