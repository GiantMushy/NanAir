from Code.DataLayer.DataLayerAPI import DataLayerAPI
from Code.Models.Airplane import Airplane


class AirplaneManagerLogic:
    def __init__(self):
        self.airplane_data = DataLayerAPI()

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
        required_fields = ['name','current_location','type','manufacturer','capacity']
        if any(kwargs.get(field) is None or kwargs.get(field) == '' for field in required_fields):
            raise ValueError("Required fields cannot be empty.")

        airplane_id = self.generate_unique_airplane_id()
        kwargs['id'] = airplane_id

        # add general employee information
        new_airplane = Airplane(**kwargs)
        self.airplane_data.add_airplane(new_airplane)

    def list_all_airplanes(self):
        """Returns a list of all airplanes."""
        return self.airplane_data.read_all_airplanes()

    def object_list_to_dict_list(self, object_list):
        dict_list = []
        for obj in object_list:
            dict_list.append(obj.__dict__)

        return dict_list

    def find_airplane_by_id(self, airplane_id):
        """
        Finds an airplane by their ID.
        :param airplane_id: ID of the airplane to find.
        :return: airplane object if found, None otherwise.
        """
        return next((emp for emp in self.airplane_data.read_all_airplanes() if emp.id == airplane_id), None)

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

    # specific request, check fields for airplane if valid
    def field_checker(self, field, input):
        '''
        Checks airplane inputs, and checks if something has letters when not supposed to
        and if something has numbers when not supposed to.
        :param field: field to check
        :param input: user input to check for the given field
        '''
        allowed_fields = ['name','current_location','type','manufacturer','capacity']
        field = field.lower()
        if field not in allowed_fields:
            raise ValueError(
                "Invalid field type, must be 'name','current_location','type','manufacturer','capacity'"
            )
        else:
            if field in ['name','current_location','manufacturer']:
                if input.isalpha():
                    return True
                else:
                    return False
            else:
                if input.isdigit():
                    return True
                else:
                    return False

    # B-requirements will be implemented  here.
