from LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic
from LogicLayer.DestinationLogic import DestinationManagerLogic

class LogicLayerAPI:
    def __init__(self):
        self.employee_logic = EmployeeManagerLogic()
        self.destination_logic = DestinationManagerLogic()

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

    def object_list_to_dict_list(self, object_list):
        return self.employee_logic.object_list_to_dict_list(object_list)
    

        ############################## DestinationManagerLogic ###############################
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

    def object_list_to_dict_list(self, object_list):
        return self.employee_logic.object_list_to_dict_list(object_list)
    
    def is_destination(self, City):
        return self.destination_logic.is_destination(City)
    
    def is_airport(self, Airport):
        return self.destination_logic.is_airport(Airport)
    
    def is_country(self, Country):
        return self.destination_logic.is_country(Country)
    
    def is_distance(self, Distance):
        return self.destination_logic.is_distance(Distance)
    
    def is_travel_time(self, Travel_Time):
        return self.destination_logic.is_travel_time(Travel_Time)
    
    def is_contact_name(self, Contact_Name):
        return self.destination_logic.is_contact_name(Contact_Name)
    
    def is_contact_phone_number(self, Contact_Phone_Number):
        return self.destination_logic.is_contact_phone_number(Contact_Phone_Number)
    
    def add_new_destination(self, City, Airport, Country, Distance, Travel_Time, Contact_Name, Contact_Phone_Number):
        return self.destination_logic.add_new_destination(City, Airport, Country, Distance, Travel_Time, Contact_Name, Contact_Phone_Number)

