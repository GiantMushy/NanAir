from DataLayer.DataLayerAPI import DataLayerAPI
from LogicLayer.AirplaneTypeLogic import AirplaneTypeLogic
from LogicLayer.FlightLogic import FlightLogic
from Models.Airplane import Airplane


class AirplaneManagerLogic:
    def __init__(self):
        self.airplane_data = DataLayerAPI()
        self.airplane_type_logic = AirplaneTypeLogic()
        self.flight_logic = FlightLogic()

    def generate_unique_airplane_id(self):
        """
        Generates a unique Airplane ID.
        If no airplanes exist, starts from '001'.
        Otherwise, increments the maximum existing ID by 1.
        :return: A string representing the unique ID.
        """
        airplanes = self.airplane_data.read_all_airplanes()
        if not airplanes:
            # base case, no airplanes in the database
            return "001"

        # find the highest existing ID and increment by 1
        max_id = max(int(emp.id) for emp in airplanes)
        new_id = max_id + 1
        return str(new_id).zfill(3)  # pad with zeros to maintain a length of 3

    def add_airplane(self, **kwargs):
        """
        Adds a new airplane to the system.
        Validates required fields before adding.

        :param kwargs: Attributes of the airplane.
        :raises ValueError: If required fields are missing or empty.
        """
        required_fields = ['name', 'type']
        if any(kwargs.get(field) is None or kwargs.get(field) == '' for field in required_fields):
            raise ValueError("Required fields cannot be empty.")

        # type must be a valid airplane type
        airplane_type = kwargs['type']
        if not self.airplane_type_logic.find_type_data(airplane_type):
            raise ValueError(
                f"Airplane type doesnt exist, make sure to add it: {airplane_type}")

        airplane_id = self.generate_unique_airplane_id()
        kwargs['id'] = airplane_id

        # add airplane information
        new_airplane = Airplane(**kwargs)
        self.airplane_data.add_airplane(new_airplane)

    def list_all_airplanes(self):
        """Returns a list of all airplanes."""
        return self.airplane_data.read_all_airplanes()

    def find_airplane_by_id(self, airplane_id):
        """
        Finds an airplane by their ID.
        :param airplane_id: ID of the airplane to find.
        :return: airplane object if found, None otherwise.
        """

        all_airplanes = self.airplane_data.read_all_airplanes()
        for plane in all_airplanes:
            if int(plane.id) == int(airplane_id):
                return plane

        return None

    def modify_airplane(self, airplane_id, **updates):
        """
        Modifies the attributes of an existing airplane.
        Restrictions apply to modifying ID, name, and social security number.

        :param airplane_id: ID of the airplane to be modified.
        :param updates: Dictionary of updates to be applied. (modify_airplane(123, current_location= "Reykjavik", name="Squiggle")
        :raises ValueError: If trying to modify restricted fields or airplane not found.
        """

        airplanes = self.list_all_airplanes()
        airplane_found = False
        updated_airplanes = []

        # update airplane information if found
        for air in airplanes:
            if air.id == airplane_id:
                airplane_found = True
                for key, value in updates.items():
                    if hasattr(air, key):
                        setattr(air, key, value)
                    else:
                        raise ValueError(f"Invalid field: {key}")
            updated_airplanes.append(air)

        if not airplane_found:
            raise ValueError(f"Airplane with ID {airplane_id} not found")

        # write the updated list back to the data layer
        self.airplane_data.modify_airplane_data(updated_airplanes)

    def is_airplane_created(self, airplane_id):
        '''
        Checks if airplane is created.

        :param airplane_id: ID of the airplane to check.

        Returns, return: True if airplane is created, False otherwise.
        '''
        if self.find_airplane_by_id(airplane_id) is not None:
            return True
        else:
            return False

    def list_airplanes_detailed(self):
        '''
        Returns a list of all airplanes with detailed information.
        '''
        # day and time of airplane when it is next available if in use
        # name of destination if in use
        # flight number if in use
        # name, type and capacity
        # if destination KEF, then next available is arrival_datetime of that flight
        # if destination not KEF, then flight_number incremented by one, arrival_datetime of that flight is next available!

        airplanes = self.list_all_airplanes()
        detailed_airplanes = []
        for airplane in airplanes:
            airplane_dict = airplane
            airplane_type = airplane_dict.type
            airplane_type_obj = self.airplane_type_logic.find_type_data(
                airplane_type)
            airplane_capacity = airplane_type_obj.capacity
            airplane_dict.capacity = airplane_capacity
            flight_or_none = self.flight_logic.is_airplane_in_use(
                airplane.id)
            if flight_or_none is not None:
                if flight_or_none.end_at == "KEF":
                    airplane_dict.next_available = flight_or_none.arrival_datetime
                    airplane_dict.destination = flight_or_none.end_at
                    airplane_dict.flight_number = flight_or_none.flight_number
                else:
                    # format is NA-XX-numbers, need to increment flight number "numbers" by one
                    flight_number = flight_or_none.flight_number
                    last_2_numbers = int(flight_number[4:])
                    next_flight_number = f"{flight_number[:4]}{last_2_numbers+1}"
                    next_flight_home = self.flight_logic.get_flight_by_id(
                        next_flight_number)
                    airplane_dict.next_available = next_flight_home.arrival_datetime
                    airplane_dict.destination = flight_or_none.end_at
                    airplane_dict.flight_number = flight_number

            detailed_airplanes.append(airplane_dict)
        return detailed_airplanes
