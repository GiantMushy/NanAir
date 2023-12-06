from DataLayer.EmployeeData import EmployeeData
from DataLayer.WorkTripData import WorkTripData


class DataLayerAPI:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.work_trip_data = WorkTripData()

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

    ################# WorkTripData #################
    def read_all_work_trips(self):
        """
        returns a list of WorkTrip objects.

        Returns:
            list: A list of WorkTrip objects representing all the work trips read from the file.
        """
        return self.work_trip_data.read_all_work_trips()

    def add_work_trip(self, work_trip):
        """Add a new work trip to the CSV file."""
        self.work_trip_data.add_work_trip(work_trip)

    def get_mock_destinations(self):
        """Temporary method to return detailed mock destinations."""
        return self.work_trip_data.get_mock_destinations()
