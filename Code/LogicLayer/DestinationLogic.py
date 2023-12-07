from DataLayer.DataLayerAPI import DataLayerAPI
from Models.Destination import Destination

class DestinationManagerLogic:
    def __init__(self):
        self.destination_data = DataLayerAPI()

    def list_all_destinations(self):
        return self.destination_data.read_all_destinations()

    def generate_unique_destination_id(self):
        destinations = self.destination_data.read_all_destinations()
        
        if not destinations:
            # base case, no destinations in the database
            return "001"

        max_id = max(int(dest.id) for dest in destinations)
        new_id = max_id + 1
        return str(new_id).zfill(3)  
    
    def is_destination(self, City):
        if not City or not City.replace(" ", "").isalpha():
            raise ValueError("City must be a non-empty string of alphabetic characters")
    
    def is_airport(self, Airport):
        if not Airport or not Airport.replace(" ", "").isalpha():
            raise ValueError("Airport must be a non-empty string of alphabetic characters")
    
    def is_country(self, Country):
        if not Country or not Country.replace(" ", "").isalpha():
            raise ValueError("Country must be a non-empty string of alphabetic characters")
    
    def is_distance(self, Distance):
        if not Distance.isdigit():
            raise ValueError("Distance must be a positive integer")
        try:
            Distance = int(Distance)
        except ValueError:
            raise ValueError("Distance must be numeric")
        if Distance > 20000:
            raise ValueError("Distance must be less than 20,000km (half the circumference of the Earth)")
            
    def is_travel_time(self, Travel_Time):
        if not Travel_Time.isdigit():
            raise ValueError("Travel Time must be a positive integer")
        try:
            Travel_Time = int(Travel_Time)
        except:
            raise ValueError("Travel Time and must be numeric")
        
    def is_contact_name(self, Contact_Name):
        if not Contact_Name or not Contact_Name.replace(" ", "").isalpha():
            raise ValueError("Contact Name must be a non-empty string of alphabetic characters")
    
    def is_contact_phone_number(self, Contact_Phone_Number):
        if not Contact_Phone_Number.replace(" ", "").isdigit():
            raise ValueError("Contact Phone Number must be a positive integer")
        try:
            Contact_Phone_Number = int(Contact_Phone_Number.replace(" ", ""))
        except:
            raise ValueError("Contact Phone Number must be numeric")
    
    def add_new_destination(self, City, Airport, Country, Distance, Travel_Time, Contact_Name, Contact_Phone_Number): 
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