from DataLayer.DestinationData import Destination_Data
from Models.Destination import Destination

class DestinationManagerLogic:
    def __init__(self):
        self.destination_data = Destination_Data()

    def list_all_destinations(self):
        return self.destination_data.read_all_destinations()

    def add_destination(self, City, Airport, Country, Distance, Travel_Time, Contact_Name, Contact_Phone_Number):
        if not City or not City.isalpha():
            raise ValueError("City must be a non-empty string of alphabetic characters")

        if not Airport or not Airport.isalpha():
            raise ValueError("Airport must be a non-empty string of alphabetic characters")

        if not Country or not Country.isalpha():
            raise ValueError("Country must be a non-empty string of alphabetic characters")

        if not Distance.isdigit():
            raise ValueError("Distance must be a positive integer")

        if not Travel_Time.isdigit():
            raise ValueError("Travel Time must be a positive integer")

        if not Contact_Name or not Contact_Name.isalpha():
            raise ValueError("Contact Name must be a non-empty string of alphabetic characters")

        if not Contact_Phone_Number.isdigit():
            raise ValueError("Contact Phone Number must be a positive integer")

        # Validate that Distance, Travel_Time, and Contact_Phone_Number are digits
        try:
            Distance = int(Distance)
            Travel_Time = int(Travel_Time)
            Contact_Phone_Number = int(Contact_Phone_Number)
        except ValueError:
            raise ValueError("Distance, Travel Time, and Contact Phone Number must be numeric")

        # Create a new Destination object
        new_destination = Destination(
            City=City,
            Airport=Airport,
            Country=Country,
            Distance=Distance,
            Travel_Time=Travel_Time,
            Contact_Name=Contact_Name,
            Contact_Phone_Number=Contact_Phone_Number
        )

        # Adding new destination
        self.destination_data.add_destination(new_destination)