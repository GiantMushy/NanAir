from LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic
from LogicLayer.WorkTripLogic import WorkTripLogic


class LogicLayerAPI:
    def __init__(self):
        self.employee_logic = EmployeeManagerLogic()
        self.work_trip_logic = WorkTripLogic()

    ############################## EmployeeManagerLogic ###############################
    def add_employee(self, employee_type, employee_role, **kwargs):
        """
        Adds a new employee to the system.
        Can add either a pilot or a flight attendant based on the employee type.
        Validates required fields before adding.
        :param employee_type: 'pilot' or 'flight_attendant'.
        :param kwargs: Attributes of the employee.
        :raises ValueError: If required fields are missing or empty.
        """
        self.employee_logic.add_employee(
            employee_type, employee_role, **kwargs)

    def list_all_employees(self):
        """Returns a list of all employees."""
        return self.employee_logic.list_all_employees()

    def list_all_pilots(self):
        """
        Returns a list of all pilots with their general employee information.
        :return: List of dictionaries combining Pilot and Employee objects.
        """
        return self.employee_logic.list_all_pilots()

    def list_all_flight_attendants(self):
        """
        Compiles a list of all flight attendants with their general employee information.
        :return: List of dictionaries combining FlightAttendant and Employee objects.
        """
        return self.employee_logic.list_all_flight_attendants()

    def is_pilot(self, employee_id):
        """Checks if an employee is a pilot.

        Args:
            employee_id (str): The ID of the employee to check.

        Returns:
            bool: True if the employee is a pilot, False otherwise.
        """
        return self.employee_logic.is_pilot(employee_id)

    def is_flight_attendant(self, employee_id):
        """Checks if an employee is a flight attendant.

        Args:
            employee_id (str): The ID of the employee to check.

        Returns:
            bool: True if the employee is a flight attendant, False otherwise.
        """
        return self.employee_logic.is_flight_attendant(employee_id)

    def modify_employee(self, employee_id, **updates):
        """
        Modifies the attributes of an existing employee.
        Restrictions apply to modifying ID, name, and social security number.

        :param employee_id: ID of the employee to be modified.
        :param updates: Dictionary of updates to be applied. (modify_employee(123, phone="1234567", address="New Address")
        :raises ValueError: If trying to modify restricted fields or employee not found.
        """
        return self.employee_logic.modify_employee(employee_id, **updates)

    ############################## WorkTripLogic ###############################
    def add_work_trip(self, destination, departure_datetime, return_datetime, crew_members=None):
        """
        Adds a new work trip to the system.
        Validates required fields before adding.

        :param destination: Destination of the work trip.
        :param departure_datetime: Departure date and time.
        :param return_datetime: Return date and time.
        :param crew_members: List of crew member IDs (optional).
        :raises ValueError: If required fields are missing or empty.
        """
        self.work_trip_logic.add_work_trip(
            destination, departure_datetime, return_datetime, crew_members)

    def get_mock_destinations(self):
        """Temporary method to return detailed mock destinations."""
        return self.work_trip_logic.get_mock_destinations()

    def list_all_work_trips(self):
        """
        returns a list of WorkTrip objects.

        Returns:
            list: A list of WorkTrip objects representing all the work trips read from the file.
        """
        return self.work_trip_logic.list_all_work_trips()
