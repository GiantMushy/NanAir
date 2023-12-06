from DataLayer.DataLayerAPI import DataLayerAPI
from Models.Destination import Destination


class DestinationManagerLogic:
    def __init__(self):
        self.Destination_data = DataLayerAPI()

    def generate_unique_Destination_id(self):
        """
        Generates a unique Destination ID.
        If no Destinations exist, starts from '001'.
        Otherwise, increments the maximum existing ID by 1.
        :return: A string representing the unique ID.
        """
        Destinations = self.Destination_data.read_all_Destinations()
        if not Destinations:
            # base case, no Destinations in the database
            return "001"

        # find the highest existing ID and increment by 1
        max_id = max(int(emp.id) for emp in Destinations)
        new_id = max_id + 1
        return str(new_id).zfill(3)  # pad with zeros to maintain a length of 3

    def add_Destination(self, **kwargs):
        """
        Adds a new Destination to the system.
        Can add either a pilot or a flight attendant based on the Destination type.
        Validates required fields before adding.

        :param Destination_type: 'pilot' or 'flight_attendant'.
        :param kwargs: Attributes of the Destination.
        :raises ValueError: If required fields are missing or empty.
        """
        required_fields = ['name', 'social_security_number',
                           'mobile_phone_number', 'address', 'email_address']
        if any(kwargs.get(field) is None or kwargs.get(field) == '' for field in required_fields):
            raise ValueError("Required fields cannot be empty.")

        Destination_id = self.generate_unique_Destination_id()
        kwargs['id'] = Destination_id

    def list_all_Destinations(self):
        """Returns a list of all Destinations."""
        return self.Destination_data.read_all_Destinations()

    def object_list_to_dict_list(self, object_list):
        dict_list = []
        for obj in object_list:
            dict_list.append(obj.__dict__)

        return dict_list

    def find_Destination_by_id(self, Destination_id):
        """
        Finds an Destination by their ID.
        :param Destination_id: ID of the Destination to find.
        :return: Destination object if found, None otherwise.
        """
        return next((emp for emp in self.Destination_data.read_all_Destinations() if emp.id == Destination_id), None)

    def modify_Destination(self, Destination_id, **updates):
        """
        Modifies the attributes of an existing Destination.
        Restrictions apply to modifying ID, name, and social security number.

        :param Destination_id: ID of the Destination to be modified.
        :param updates: Dictionary of updates to be applied. (modify_Destination(123, phone="1234567", address="New Address")
        :raises ValueError: If trying to modify restricted fields or Destination not found.
        """
        if any(key in updates for key in ['id', 'name', 'social_security_number']):
            raise ValueError(
                "Modification of 'id', 'name', or 'social_security_number' is not allowed")

        Destinations = self.list_all_Destinations()
        Destination_found = False
        updated_Destinations = []

        # update Destination information if found
        for emp in Destinations:
            if emp.id == Destination_id:
                Destination_found = True
                for key, value in updates.items():
                    if hasattr(emp, key):
                        setattr(emp, key, value)
                    else:
                        raise ValueError(f"Invalid field: {key}")
            updated_Destinations.append(emp)

        if not Destination_found:
            raise ValueError(f"Destination with ID {Destination_id} not found")

        # write the updated list back to the data layer
        self.Destination_data.modify_Destination_data(updated_Destinations)

        # specific request, check fields for Destination if valid
        def field_checker(self, field, input):
            '''
            Checks Destination inputs, and checks if something has letters when not supposed to
            and if something has numbers when not supposed to.
            :param field: field to check
            :param input: user input to check for the given field
            '''
            allowed_fields = ['name', 'ssn',
                              'mobile', 'address', 'email_address']
            field = field.lower()
            if field not in allowed_fields:
                raise ValueError(
                    "Invalid field type, must be name, ssn, mobile, address or email_address"
                )
            else:
                if field in ['name', 'email_address, address']:
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
