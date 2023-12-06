from DataLayer.DataLayerAPI import DataLayerAPI
from Models.Destination import Destination


class DestinationManagerLogic:
    def __init__(self):
        self.destination_data = DataLayerAPI()

    def generate_unique_destination_id(self):
        """
        Generates a unique Destination ID.
        If no Destinations exist, starts from '001'.
        Otherwise, increments the maximum existing ID by 1.
        :return: A string representing the unique ID.
        """
        destinations = self.destination_data.read_all_destinations()
        if not destinations:
            # base case, no Destinations in the database
            return "001"

        # find the highest existing ID and increment by 1
        max_id = max(int(emp.id) for emp in destinations)
        new_id = max_id + 1
        return str(new_id).zfill(3)  # pad with zeros to maintain a length of 3

    def add_destination(self, **kwargs):
        """
        Adds a new Destination to the system.
        Validates required fields before adding.

        :param kwargs: Attributes of the Destination.
        :raises ValueError: If required fields are missing or empty.
        """
        required_fields = ['city', 'airport','country', 'distance','travel_time','contact_name','contact_phone_number']
        if any(kwargs.get(field) is None or kwargs.get(field) == '' for field in required_fields):
            raise ValueError("Required fields cannot be empty.")

        destination_id = self.generate_unique_destination_id()
        kwargs['id'] = destination_id

        # add general employee information
        new_destination = Destination(**kwargs)
        self.destination_data.add_destination(new_destination)

    def list_all_destinations(self):
        """Returns a list of all Destinations."""
        return self.destination_data.read_all_destinations()

    def object_list_to_dict_list(self, object_list):
        dict_list = []
        for obj in object_list:
            dict_list.append(obj.__dict__)

        return dict_list

    def find_destination_by_id(self, destination_id):
        """
        Finds an Destination by their ID.
        :param Destination_id: ID of the Destination to find.
        :return: Destination object if found, None otherwise.
        """
        return next((emp for emp in self.destination_data.read_all_destinations() if emp.id == destination_id), None)

    # specific request, check fields for Destination if valid
    def field_checker(self, field, input):
        '''
        Checks Destination inputs, and checks if something has letters when not supposed to
        and if something has numbers when not supposed to.
        :param field: field to check
        :param input: user input to check for the given field
        '''
        allowed_fields = ['city', 'airport','country', 'distance', 'travel_time', 'contact_name', 'contact_phone_number']
        field = field.lower()
        if field not in allowed_fields:
            raise ValueError(
                "Invalid field type, must be 'city', 'airport','country', 'distance', 'travel_time', 'contact_name', 'contact_phone_number'"
            )
        else:
            if field in ['city', 'airport','country', 'contact_name']:
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
