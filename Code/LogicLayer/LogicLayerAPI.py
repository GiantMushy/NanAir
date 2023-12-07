from LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic
from LogicLayer.DestinationManagerLogic import DestinationManagerLogic
from LogicLayer.AirplaneManagerLogic import AirplaneManagerLogic


class LogicLayerAPI:
    def __init__(self):
        self.employee_logic = EmployeeManagerLogic()
        self.destination_logic = DestinationManagerLogic()
        self.airplane_logic = AirplaneManagerLogic()

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
    
    def find_employee_by_id(self, employee_id):
        """
        Finds an employee by their ID.
        :param employee_id: ID of the employee to find.
        :return: Employee object if found, None otherwise.
        """
        return self.employee_logic.find_employee_by_id(employee_id)

    
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
        :return: Airplane object if found, None otherwise.
        """
        return self.airplane_logic.find_airplane_by_id(airplane_id)

    ############################## GeneralUseLogic ###############################

    def object_list_to_dict_list(self, object_list):
        return self.employee_logic.object_list_to_dict_list(object_list)
    
    def object_to_dict(self,object):
        return self.employee_logic.object_to_dict(object)
    
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
