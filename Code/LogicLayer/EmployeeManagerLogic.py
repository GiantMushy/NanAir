from DataLayer.DataLayerAPI import DataLayerAPI
from Models.Employee import Employee
from Models.Pilot import Pilot
from Models.FlightAttendant import FlightAttendant


class EmployeeManagerLogic:
    def __init__(self):
        self.employee_data = DataLayerAPI()

    def generate_unique_employee_id(self):
        """
        Generates a unique employee ID.
        If no employees exist, starts from '001'.
        Otherwise, increments the maximum existing ID by 1.
        :return: A string representing the unique ID.
        """
        employees = self.employee_data.read_all_employees()
        if not employees:
            # base case, no employees in the database
            return "001"

        # find the highest existing ID and increment by 1
        max_id = max(int(emp.id) for emp in employees)
        new_id = max_id + 1
        return str(new_id).zfill(3)  # pad with zeros to maintain a length of 3

    def add_employee(self, employee_type, employee_role, **kwargs):
        """
        Adds a new employee to the system.
        Can add either a pilot or a flight attendant based on the employee type.
        Validates required fields before adding.

        :param employee_type: 'pilot' or 'flight_attendant'.
        :param kwargs: Attributes of the employee.
        :raises ValueError: If required fields are missing or empty.
        """
        required_fields = ['name', 'social_security_number',
                           'mobile_phone_number', 'address', 'email_address']
        if any(kwargs.get(field) is None or kwargs.get(field) == '' for field in required_fields):
            raise ValueError("Required fields cannot be empty.")

        employee_id = self.generate_unique_employee_id()
        kwargs['id'] = employee_id

        # add general employee information
        new_employee = Employee(**kwargs)
        self.employee_data.add_employee(new_employee)

        # add specific role information
        if employee_type.lower() == 'pilot':
            # checking role of pilot, if either captain or co-pilot
            if employee_role.lower() == 'captain':
                employee_role = 'Captain'
            elif employee_role.lower() == 'copilot' or employee_role.lower() == 'co-pilot':
                employee_role = 'Co-Pilot'
            else:
                raise ValueError(
                    "Invalid pilot role. Must be 'Captain' or 'Co-Pilot'.")
            pilot = Pilot(kwargs['id'], employee_role)
            self.employee_data.add_pilot(pilot)
        elif employee_type.lower() == 'flight_attendant':
            # checking role of flight attendant, if either senior flight attendant or flight attendant
            if employee_role.lower() == 'senior flight attendant':
                employee_role = 'Senior Flight Attendant'
            elif employee_role.lower() == 'flight attendant':
                employee_role = 'Flight Attendant'
            else:
                raise ValueError(
                    "Invalid flight attendant role. Must be 'Senior Flight Attendant' or 'Flight Attendant'.")
            flight_attendant = FlightAttendant(kwargs['id'], employee_role)
            self.employee_data.add_flight_attendant(flight_attendant)
        else:
            raise ValueError(
                "Invalid employee type, must be either Pilot or Flight Attendant.")

    def list_all_employees(self):
        """Returns a list of all employees."""
        return self.employee_data.read_all_employees()

    def list_all_pilots(self):
        """
        Compiles a list of all pilots with their general employee information.
        :return: List of dictionaries combining Pilot and Employee objects.
        """
        pilots = self.employee_data.read_all_pilots()
        combined_pilots = []
        for pilot in pilots:
            employee = self.find_employee_by_id(pilot.id)
            # combine the values of two dictionaries having same key
            combined_pilot = {**employee.__dict__, **pilot.__dict__}
            combined_pilots.append(combined_pilot)
        return combined_pilots

    def list_all_flight_attendants(self):
        """
        Compiles a list of all flight attendants with their general employee information.
        :return: List of dictionaries combining FlightAttendant and Employee objects.
        """
        flight_attendants = self.employee_data.read_all_flight_attendants()
        combined_flight_attendants = []
        for flight_attendant in flight_attendants:
            employee = self.find_employee_by_id(flight_attendant.id)
            combined_flight_attendant = {
                **employee.__dict__, **flight_attendant.__dict__}
            combined_flight_attendants.append(combined_flight_attendant)
        return combined_flight_attendants

    def is_pilot(self, employee_id):
        """Checks if an employee is a pilot.

        Args:
            employee_id (str): The ID of the employee to check.

        Returns:
            bool: True if the employee is a pilot, False otherwise.
        """
        employee_id_int = int(employee_id)
        return any(int(pilot.id) == employee_id_int for pilot in self.employee_data.read_all_pilots())

    def is_flight_attendant(self, employee_id):
        """Checks if an employee is a flight attendant.

        Args:
            employee_id (str): The ID of the employee to check.

        Returns:
            bool: True if the employee is a flight attendant, False otherwise.
        """
        employee_id_int = int(employee_id)
        return any(int(attendant.id) == employee_id_int for attendant in self.employee_data.read_all_flight_attendants())

    def find_employee_by_id(self, employee_id):
        """
        Finds an employee by their ID.
        :param employee_id: ID of the employee to find.
        :return: Employee object if found, None otherwise.
        """
        return next((emp for emp in self.employee_data.read_all_employees() if emp.id == employee_id), None)

    def modify_employee(self, employee_id, **updates):
        """
        Modifies the attributes of an existing employee.
        Restrictions apply to modifying ID, name, and social security number.

        :param employee_id: ID of the employee to be modified.
        :param updates: Dictionary of updates to be applied. (modify_employee(123, phone="1234567", address="New Address")
        :raises ValueError: If trying to modify restricted fields or employee not found.
        """
        if any(key in updates for key in ['id', 'name', 'social_security_number']):
            raise ValueError(
                "Modification of 'id', 'name', or 'social_security_number' is not allowed")

        employees = self.list_all_employees()
        employee_found = False
        updated_employees = []

        # update employee information if found
        for emp in employees:
            if emp.id == employee_id:
                employee_found = True
                for key, value in updates.items():
                    if hasattr(emp, key):
                        setattr(emp, key, value)
                    else:
                        raise ValueError(f"Invalid field: {key}")
            updated_employees.append(emp)

        if not employee_found:
            raise ValueError(f"Employee with ID {employee_id} not found")

        # write the updated list back to the data layer
        self.employee_data.modify_employee_data(updated_employees)

    # B-requirements will be implemented  here.
