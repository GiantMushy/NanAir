from DataLayer.DataLayerAPI import DataLayerAPI
from Models.Destination import Destination


class DestinationManagerLogic:
    def __init__(self):
        self.destination_data = DataLayerAPI()
        self.create_hq_destination()

    def create_hq_destination(self):
        if not self.find_destination_by_id("01"):
            self.add_destination(
                city="Reykjavík", airport="KEF", country="Iceland", distance="0", travel_time="0", contact_name="N/A", contact_phone_number="N/A")

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
            return "01"

        # find the highest existing ID and increment by 1
        max_id = max(int(emp.id) for emp in destinations)
        new_id = max_id + 1
        return str(new_id).zfill(2)  # pad with zeros to maintain a length of 3

    def add_destination(self, **kwargs):
        """
        Adds a new Destination to the system.
        Validates required fields before adding.

        :param kwargs: Attributes of the Destination.
        :raises ValueError: If required fields are missing or empty.
        """
        required_fields = ['city', 'airport', 'country', 'distance',
                           'travel_time', 'contact_name', 'contact_phone_number']
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
        all_destinations = self.destination_data.read_all_destinations()
        for destination in all_destinations:
            if int(destination.id) == int(destination_id):
                return destination

        return None

    # specific request, check fields for Destination if valid
    def field_checker(self, field, input):
        '''
        Checks Destination inputs, and checks if something has letters when not supposed to
        and if something has numbers when not supposed to.

        :param field: field to check
        :param input: user input to check for the given field
        '''
        allowed_fields = ['city', 'airport', 'country', 'distance',
                          'travel_time', 'contact_name', 'contact_phone_number']
        field = field.lower()
        if field not in allowed_fields:
            raise ValueError(
                "Invalid field type, must be 'city', 'airport','country', 'distance', 'travel_time', 'contact_name', 'contact_phone_number'"
            )
        else:
            if field in ['city', 'airport', 'country', 'contact_name']:
                if input.isalpha():
                    return True
                else:
                    return False
            else:
                if input.isdigit():
                    return True
                else:
                    return False

    def get_headquarters(self):
        return self.find_destination_by_id("01")

    def update_emergency_contact(self, destination_id, contact_name, contact_phone_number):
        destination = self.find_destination_by_id(destination_id)
        destination.contact_name = contact_name
        destination.contact_phone_number = contact_phone_number
        old_destinations = self.list_all_destinations()
        new_destinations = []
        for dest in old_destinations:
            if dest.id == destination_id:
                new_destinations.append(destination)
            else:
                new_destinations.append(dest)
        self.destination_data.modify_destination_data(new_destinations)

    ##################### Input Varification #############################
    def is_destination(self, City):
        if not City or not City.replace(" ", "").isalpha():
            raise ValueError(
                "City must be a non-empty string of alphabetic characters")

    def is_airport(self, Airport):
        if not Airport or not Airport.replace(" ", "").isalpha():
            raise ValueError(
                "Airport must be a non-empty string of alphabetic characters")

    def is_country(self, Country):
        if not Country or not Country.replace(" ", "").isalpha():
            raise ValueError(
                "Country must be a non-empty string of alphabetic characters")

    def is_distance(self, Distance):
        if not Distance.isdigit():
            raise ValueError("Distance must be a positive integer")
        try:
            Distance = int(Distance)
        except ValueError:
            raise ValueError("Distance must be numeric")
        if Distance > 20000:
            raise ValueError(
                "Distance must be less than 20,000km (half the circumference of the Earth)")

    def is_travel_time(self, Travel_Time):
        if not Travel_Time.isdigit():
            raise ValueError("Travel Time must be a positive integer")
        try:
            Travel_Time = int(Travel_Time)
        except:
            raise ValueError("Travel Time and must be numeric")

    def is_contact_name(self, Contact_Name):
        if not Contact_Name or not Contact_Name.replace(" ", "").isalpha():
            raise ValueError(
                "Contact Name must be a non-empty string of alphabetic characters")

    def is_contact_phone_number(self, Contact_Phone_Number):
        if not Contact_Phone_Number.replace(" ", "").isdigit():
            raise ValueError("Contact Phone Number must be a positive integer")
        try:
            Contact_Phone_Number = int(Contact_Phone_Number.replace(" ", ""))
        except:
            raise ValueError("Contact Phone Number must be numeric")
    # B-requirements will be implemented  here.
