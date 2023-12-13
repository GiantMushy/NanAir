from Code.DataLayer.DataLayerAPI import DataLayerAPI
from Code.Models.Destination import Destination


class DestinationManagerLogic:
    def __init__(self):
        self.destination_data = DataLayerAPI()
        self.create_hq_destination()

    def create_hq_destination(self):
        '''
        Need to ensure headquarters are always created, to always know which flight is  going home using the airport
        '''
        if not self.find_destination_by_id("01"):
            self.add_destination(
                city="Reykjavík", airport="RKV", country="Iceland", distance="0", travel_time="0", contact_name="N/A", contact_phone_number="N/A")

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

        # if airport equal to RKV, raise error
        if kwargs['id'] != "01":
            if kwargs['airport'] == "RKV":
                raise ValueError("Airport cannot be Headquarters")

        destination_id = self.generate_unique_destination_id()
        kwargs['id'] = destination_id

        new_destination = Destination(**kwargs)
        self.destination_data.add_destination(new_destination)

    def list_all_destinations(self):
        """Returns a list of all Destinations."""
        return self.destination_data.read_all_destinations()

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

    def get_headquarters(self):
        '''
        Returns the headquarters of NAN air
        '''
        return self.find_destination_by_id("01")

    def update_emergency_contact(self, destination_id, contact_name, contact_phone_number):
        '''
        Update emergency contact and phone number of destination.

        :param destination_id: ID of the destination to update
        :param contact_name: new contact name
        :param contact_phone_number: new contact phone number
        '''
        destination = self.find_destination_by_id(destination_id)
        if destination_id == "01":
            raise ValueError(
                "Cannot update emergency contact of headquarters")
        if not destination or not destination_id or not contact_name or not contact_phone_number:
            raise ValueError("Invalid input")
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
