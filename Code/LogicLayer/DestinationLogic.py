from DataLayer.DestinationData import Destination_Data
from Models.Destination import Destination


class DestinationManagerLogic:
    def __init__(self):
        self.destination_data = Destination_Data()

    def list_all_destinations(self):
        return self.destination_data.read_all_destinations()

    def add_destination(self, City, Airport, Country, Distance, Travel_Time, Contact_Name, Contact_Phone_Number):

        # create new Destination object
        new_destination = Destination(
            City=City,
            Airport=Airport,
            Country=Country,
            Distance=Distance,
            Travel_Time=Travel_Time,
            Contact_Name=Contact_Name,
            Contact_Phone_Number=Contact_Phone_Number
        )

        # adding new destination
        self.destination_data.add_destination(new_destination)
