from Code.LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic
from Code.LogicLayer.WorkTripLogic import WorkTripLogic
from Code.LogicLayer.DestinationManagerLogic import DestinationManagerLogic
from Code.LogicLayer.AirplaneManagerLogic import AirplaneManagerLogic
from Code.LogicLayer.FlightLogic import FlightLogic
from Code.LogicLayer.AirplaneTypeLogic import AirplaneTypeLogic
from Code.LogicLayer.IsChecks import IsChecks


class LogicLayerAPI:
    def __init__(self):
        self.employee_logic = EmployeeManagerLogic()
        self.work_trip_logic = WorkTripLogic()
        self.destination_logic = DestinationManagerLogic()
        self.airplane_logic = AirplaneManagerLogic()
        self.flight_logic = FlightLogic()
        self.airplane_type_logic = AirplaneTypeLogic()
        self.check = IsChecks()

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

    def list_pilots_by_airplane_type(self, airplane_type):
        '''
        Takes a airplane type string and returns a list of pilots that can fly that airplane type

        :param airplane_type: airplane type string f.x ("AKN-77")

        Returns, return: list of pilots that can fly that airplane type
        '''
        return self.employee_logic.list_pilots_by_airplane_type(airplane_type)

    def list_pilots_sorted_by_airplane_type(self):
        '''
        Returns a list of pilots sorted by airplane type

        Returns, return: list of pilots sorted by airplane type
        '''
        return self.employee_logic.list_pilots_sorted_by_airplane_type()

    def find_employee_by_id(self, employee_id):
        """
        Finds an employee by their ID.

        :param employee_id: ID of the employee to find.

        Returns, return: Employee object if found, None otherwise.
        """
        return self.employee_logic.find_employee_by_id(employee_id)

    def find_employee_by_id_detailed(self, employee_id):
        """
        Finds an employee by their ID with more detail

        :param employee_id: ID of the employee to find.

        Returns, return: Employee object if found, None otherwise.
        """
        return self.employee_logic.find_employee_by_id_detailed(employee_id)

    def list_all_employees_detailed(self):
        '''
        Returns a list of all employees with more detail.
        '''
        return self.employee_logic.list_all_employees_detailed()

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

    def list_all_work_trips(self):
        '''
        Returns, return: A list of detailed work_trips
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

    def list_employees_working_and_destinations(self, string_date):
        '''
        Lists all employee id's who are working on given date and to which destination they're going.

        :param string_date: The date to check, in string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13" 

        Returns, return: a list of dictionaries, with the employee_id and destination for given day.
        '''
        return self.work_trip_logic.list_employees_working_and_destinations(string_date)

    def list_all_busy_employees(self, string_date):
        '''
        List all employees who are working at a certain date. 

        :param string_date: The date to check, in string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13" 

        Returns, return: a list of employee ids busy on the date

        '''
        return self.work_trip_logic.list_all_busy_employees(string_date)

    def list_all_available_employees(self, string_date):
        '''
        List all employees who are not working at a certain date. 

        :param string_date: The date to check, in string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13" 

        Returns, return: a list of employee ids busy on the date

        '''
        return self.work_trip_logic.list_all_available_employees(string_date)

    def all_work_trips_of_employee(self, employee_id, string_date):
        '''
        Returns all work trips of employee id in week, the date given is the 
        start of the week that is searched. Example: 2004-6-6 14:00, search range
        is 2004-6-6 14:00 - 2004-6-13 14:00.

        :param employee_id: ID of the employee to check.
        :param employee_id: string date start of the week to check.
        '''
        return self.work_trip_logic.all_work_trips_of_employee(employee_id, string_date)

    def get_recommended_departure_datetime(self, destination_id, departure_datetime):
        '''
        Returns a recommended departure datetime for a work trip based on the destination and departure datetime, basically
        using the destination trip time and departure time to calculate the recommended departure time.

        :param destination_id: ID of the destination to check.
        :param departure_datetime: string date start of the week to check. In the format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"
        '''
        return self.work_trip_logic.get_recommended_departure_datetime(destination_id, departure_datetime)

    def list_all_available_pilots_by_type(self, airplane_type, date):
        '''
        Lists all available pilots dor a certain date with licence on airplane type

        :param airplane_type: airplane type string
        :param date: date to check if employees available

        Returns, return: list of pilots that can fly airplane type and are available on date
        '''
        return self.work_trip_logic.list_all_available_pilots_by_type(airplane_type, date)

    def list_all_available_senior_fa(self, date):
        '''
        Lists all available senior fa for a certain date

        :param date: date to check if employees available

        Returns, return: list of pilots that can fly airplane type and are available on date
        '''
        return self.work_trip_logic.list_all_available_senior_fa(date)

    def list_all_available_fa(self, date):
        '''
        Lists all available fa for a certain date

        :param date: date to check if employees available

        Returns, return: list of pilots that can fly airplane type and are available on date
        '''
        return self.work_trip_logic.list_all_available_fa(date)

    def list_all_available_captains_by_type(self, airplane_type, date):
        '''
        Listing all available Captains for a certain date with licence on airplane type

        :param airplane_type: airplane type string
        :param date: date to check if employees available
        '''
        return self.work_trip_logic.list_all_available_captains_by_type(airplane_type, date)

    def list_all_available_copilots_by_type(self, airplane_type, date):
        '''
        Listing all available Co-Pilots for a certain date with licence on airplane type

        :param airplane_type: airplane type string
        :param date: date to check if employees available
        '''
        return self.work_trip_logic.list_all_available_copilots_by_type(airplane_type, date)

    def find_work_trip_by_id(self, work_trip_id):
        '''
        Gets work trip by ID.

        :param work_trip_id: ID of the work trip to get.
        '''
        return self.work_trip_logic.get_work_trip_by_id(work_trip_id)

    ############################## Destination Manager Logic ###############################

    def list_all_destinations(self):
        """Returns a list of all destinations."""
        return self.destination_logic.list_all_destinations()

    def add_destination(self, **kwargs):
        """
        Adds a new destination to the system.
        Validates required fields before adding.

        :raises ValueError: If required fields are missing or empty.
        """
        self.destination_logic.add_destination(**kwargs)

    def find_destination_by_id(self, destination_id):
        """
        Finds an destination by their ID.

        :param destination_id: ID of the destination to find.

        :return: Destination object if found, None otherwise.
        """
        return self.destination_logic.find_destination_by_id(destination_id)

    def update_emergency_contact(self, destination_id, contact_name, contact_phone_number):
        '''
        Update emergency contact and phone number of destination.

        :param destination_id: ID of the destination to update
        :param contact_name: new contact name
        :param contact_phone_number: new contact phone number
        '''
        self.destination_logic.update_emergency_contact(
            destination_id, contact_name, contact_phone_number)

    ############################## Airplane Manager Logic ###############################

    def list_all_airplanes(self):
        """Returns a list of all airplanes."""
        return self.airplane_logic.list_all_airplanes()

    def add_airplane(self, **kwargs):
        """
        Adds a new airplane to the system.
        Validates required fields before adding.

        :raises ValueError: If required fields are missing or empty.
        """
        self.airplane_logic.add_airplane(**kwargs)

    def modify_airplane(self, airplane_id, **updates):
        """
        Modifies the attributes of an existing airplane.

        :param airplane_id: ID of the airplane to be modified.
        :param updates: Dictionary of updates to be applied. (modify_airplane(123, tpe="1234567", current_location="New Address")

        :raises ValueError: If trying to modify restricted fields or airplane not found.
        """
        return self.airplane_logic.modify_airplane(airplane_id, **updates)

    def find_airplane_by_id(self, airplane_id):
        """
        Finds an airplane by their ID.

        :param airplane_id: ID of the airplane to find.

        Returns, return: Airplane object if found, None otherwise.
        """
        return self.airplane_logic.find_airplane_by_id(airplane_id)

    def list_airplanes_detailed(self):
        '''
        Returns a list of all airplanes with detailed information.
        '''
        return self.airplane_logic.list_airplanes_detailed()

    ############################## FlightLogic ###############################

    def list_all_flights(self):
        """Returns, return: a list of all flights."""
        return self.flight_logic.list_all_flights()

    def add_flight(self, **kwargs):
        """
        Adds a new airplane to the system.
        Validates required fields before adding.

        :raises ValueError: If required fields are missing or empty.
        """
        self.flight_logic.add_flight(**kwargs)

    def get_flight_by_id(self, flight_id):
        '''
        Find flight object using its flight id

        :param flight_id: ID of the flight to find

        Returns, return: Flight object with the given id.
        '''
        return self.flight_logic.get_flight_by_id(flight_id)

    def get_all_flights_by_destination_id(self, destination_id):
        '''
        All flights flying to a specific destination

        :param destination_id: ID of the destination to find

        Returns, return: List of Flight objects with the given destination id.
        '''
        return self.flight_logic.get_all_flights_by_destination_id(destination_id)

    def change_sold_tickets(self, flight_id, tickets_sold):
        '''
        Add sold tickets to flight

        :param flight_number: Number of the flight to change

        :param tickets_sold: Number of tickets sold to add to flight
        '''
        self.flight_logic.change_sold_tickets(flight_id, tickets_sold)

    def get_sold_tickets(self, flight_id):
        '''
        Sold tickets of flight

        :param flight_number: Number of the flight to get sold tickets from

        Returns, return: string number of sold tickets
        '''
        return self.flight_logic.get_sold_tickets(flight_id)

    def get_available_tickets(self, flight_id):
        '''
        Capacity minus the sold tickets

        :param flight_number: Number of the flight to get available tickets from

        Returns, return: string number of available tickets
        '''
        return self.flight_logic.get_available_tickets(flight_id)

    def is_airplane_available(self, airplane_id, departure_datetime, return_datetime):
        '''
        Checks if airplane is available for a given time period

        :param airplane_id: ID of the airplane to check
        :param departure_datetime: Departure date and time. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"
        :param return_datetime: Return date and time. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"

        Returns, return: True if airplane is available, False otherwise
        '''
        return self.flight_logic.is_airplane_available(airplane_id, departure_datetime, return_datetime)

    ############################## AirplaneTypeLogic ###############################

    def add_airplane_type(self, **kwargs):
        """
        Adds a new airplane type to the system.
        Validates required fields before adding.

        :param kwargs: Attributes of the airplane type.

        :raises ValueError: If required fields are missing or empty.
        """
        self.airplane_type_logic.add_airplane_type(**kwargs)

    def list_all_airplane_types(self):
        """Returns, return: a list of all airplane types."""
        return self.airplane_type_logic.list_all_airplane_types()

    def find_type_data(self, airplane_type):
        """
        Finds an airplane type object by their type.

        :param airplane_type: type of the airplane to find.
        Returns, return: airplane object if found, None otherwise.
        """
        return self.airplane_type_logic.find_type_data(airplane_type)

    ############################## Input Varification ###############################

    def is_city(self, City):
        return self.check.is_city(City)

    def is_airport(self, Airport):
        return self.check.is_airport(Airport)

    def is_country(self, Country):
        return self.check.is_country(Country)

    def is_distance(self, Distance):
        return self.check.is_distance(Distance)

    def is_travel_time(self, Travel_Time):
        return self.check.is_travel_time(Travel_Time)

    def is_contact_name(self, Contact_Name):
        return self.check.is_contact_name(Contact_Name)

    def is_contact_phone_number(self, Contact_Phone_Number):
        return self.check.is_contact_phone_number(Contact_Phone_Number)

    def is_home_phone(self, home_phone):
        return self.check.is_home_phone(home_phone)

    def is_name(self, Name):
        return self.check.is_name(Name)

    def is_current_location(self, Current_Location):
        return self.check.is_current_location(Current_Location)

    def is_social_security_number(self, social_security_number):
        return self.check.is_social_security_number(social_security_number)

    def is_type(self, Type):
        return self.check.is_type(Type)

    def is_manufacturer(self, Manufacturer):
        return self.check.is_manufacturer(Manufacturer)

    def is_capacity(self, Capacity):
        return self.check.is_capacity(Capacity)

    def is_address(self, address):
        return self.check.is_address(address)

    def is_email(self, Email):
        return self.check.is_email(Email)

    def is_right_day_of_departure(self, input_departure_day):
        return self.check.is_right_day_of_departure(input_departure_day)

    def is_return_time_dd_rd(self, input_departure_day, input_return_day):
        return self.check.is_return_time_dd_rd(input_departure_day, input_return_day)

    def is_date(self, date):
        return self.check.is_date(date)

    def departure_date_past(self, departure_date):
        return self.check.departure_date_past(departure_date)

    def departure_datetime_past(self, departure_datetime):
        return self.check.departure_datetime_past(departure_datetime)

    def flight_sched_destination_validation(self, departure_datetime, return_datetime, destination_obj):
        return self.check.flight_sched_destination_validation(departure_datetime, return_datetime, destination_obj)

    ############################## GeneralUseLogic ###############################

    def object_list_to_dict_list(self, object_list):
        return self.employee_logic.object_list_to_dict_list(object_list)

    def object_to_dict(self, object):
        return self.employee_logic.object_to_dict(object)
