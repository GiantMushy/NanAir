from LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic
from LogicLayer.WorkTripLogic import WorkTripLogic


class LogicLayerAPI:
    def __init__(self):
        self.employee_logic = EmployeeManagerLogic()
        self.work_trip_logic = WorkTripLogic()

    ############################## EmployeeManagerLogic ###############################
    def add_employee(self, employee_type, employee_role, **kwargs):
        '''
        Adds a new employee to the system.
        Can add either a pilot or a flight attendant based on the employee type.
        Additionally choose role for employee type.

        :param employee_type: 'pilot' or 'flight_attendant'.
        :param employee_role: 'captain/co-pilot or flight attendant/senior flight attendant, string.
        :param kwargs: Attributes of the employee. (name='name',ssn='ssn'...etc)

        :raises ValueError: If required fields are missing or empty.
        '''
        self.employee_logic.add_employee(
            employee_type, employee_role, **kwargs)

    def list_all_employees(self):
        '''
        List of all employees.

        Returns, return: List of Employee objects.
        '''
        return self.employee_logic.list_all_employees()

    def list_all_pilots(self):
        '''
        Lists all employees who are pilots

        Returns, return: List of dictionaries combining Pilot and Employee objects on their ID's.
        '''
        return self.employee_logic.list_all_pilots()

    def list_all_flight_attendants(self):
        '''
        Lists all employees who are flight attendants

        Returns, return: List of dictionaries combining FlightAttendant and Employee objects on their ID's
        '''
        return self.employee_logic.list_all_flight_attendants()

    def is_pilot(self, employee_id):
        '''Checks if an employee is a pilot.

        :param employee_id: The ID of the employee to check, string.

        Returns, bool: True if the employee is a pilot, False otherwise.
        '''
        return self.employee_logic.is_pilot(employee_id)

    def is_flight_attendant(self, employee_id):
        '''Checks if an employee is a flight attendant.

        :param employee_id: The ID of the employee to check in string.

        Returns, return: True if the employee is a flight attendant, False otherwise.
        '''
        return self.employee_logic.is_flight_attendant(employee_id)

    def modify_employee(self, employee_id, **updates):
        '''
        Modifies the attributes of an existing employee.
        Restrictions apply to modifying ID, name, and social security number.

        :param employee_id: ID of the employee to be modified.
        :param updates: Dictionary of updates to be applied. (modify_employee(123, phone="1234567", address="New Address")

        :raises ValueError: If trying to modify restricted fields or employee not found.
        '''
        return self.employee_logic.modify_employee(employee_id, **updates)

    def is_employee(self, employee_id):
        '''Checks if an employee exists in the system.

        :param employee_id: employee_id: The ID of the employee to check.

        Returns, returns: bool True if the employee exists, False if not.
        '''
        return self.employee_logic.is_employee(employee_id)

    def is_captain(self, employee_id):
        '''
        Takes a employee id string and determines if employee is captain or not

        :param employee_id: ID of employee to check string f.x ("001")

        Returns, return: bool True if captain, False if not.
        '''
        return self.employee_logic.is_captain(employee_id)

    def is_senior_flight_attendant(self, employee_id):
        '''
        Takes a employee id string and determines if employee is senior flight attendant or not

        :param employee_id: ID of employee to check string f.x ("001")

        Returns, return: bool True if Senior flight attendant, False if not.
        '''
        return self.employee_logic.is_senior_flight_attendant(employee_id)

    ############################## WorkTripLogic ###############################
    def add_work_trip(self, destination, departure_datetime, return_datetime, crew_members=None):
        '''
        Adds a new work trip.

        :param destination: Destination object of the work trip.
        :param departure_datetime: Departure date and time. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"
        :param return_datetime: Return date and time. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"
        :param crew_members: String comma separated list of crew member IDs (optional). f.x. "001,002,003"

        :raises ValueError: If required fields are missing or empty.
        '''
        self.work_trip_logic.add_work_trip(
            destination, departure_datetime, return_datetime, crew_members)

    def get_mock_destinations(self):
        '''Mocking destinations data'''
        return self.work_trip_logic.get_mock_destinations()

    def list_all_work_trips(self):
        '''
        Returns, return: A list of all WorkTrip Objects.
        '''
        return self.work_trip_logic.list_all_work_trips()

    def add_crew_member(self, work_trip_id, employee_id):
        '''
        Adds a crew member to a WorkTrip object

        :param work_trip_id: The ID of the WorkTrip for the Employee ID to be added to
        :param employee_id: The ID of the employee to be added
        '''
        self.work_trip_logic.add_crew_member(work_trip_id, employee_id)

    def create_recurring_work_trips(self, work_trip_id, weekly_or_daily, number_of_recorrunces):
        '''
        Creates recurring WorkTrips of given WorkTrip either weekly or daily for a certain amount of times.

        :param work_trip_id: The ID of the work trip to be copied
        :param weekly_or_daily: A string either "weekly" or "daily"
        :param number_of_recurrunces: The number of times the work trip should be copied, (x days or x weeks)
        '''
        self.work_trip_logic.create_recurring_work_trips(
            work_trip_id, weekly_or_daily, number_of_recorrunces)

    def work_trip_validity_period(self, weekly_or_daily, start_date):
        '''
        :param weekly_or_daily: weekly or daily validity period
        :param start_date: The start date of the period, in string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"

        Returns, return: List of WorkTrip objects with additional field "validity" set to True or False.
        '''
        return self.work_trip_logic.work_trip_validity_period(
            weekly_or_daily, start_date)
