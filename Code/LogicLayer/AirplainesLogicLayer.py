from DataLayer.AirplainesDataLayer import AirplaineData
from Models.AirplaineModel import Airplaine

class AirplaineManagerLogic:
    def __init__(self):
        self.AirplainesData_data = AirplaineData()

def list_all_destinations(self):
        return self.destination_data.read_all_destinations()


def add_destination(self, NameOfPlane, CurrentLocation, Type, Manufacturer, Capacity):
        if not NameOfPlane or not NameOfPlane.isalpha():
            raise ValueError("City must be a non-empty string of alphabetic characters")

        if not CurrentLocation or not CurrentLocation.isalpha():
            raise ValueError("CurrentLocation must be a non-empty string of alphabetic characters")
#Skoða types því 1-3 eru stafir 4 og 7 eru - og 5 er tala og 6-9 er tala
        if not Type or not Type.isalpha():
            raise ValueError("Type must be a non-empty string with alphabetic characters and numbers")

        if not Manufacturer.isalpha():
            raise ValueError("Manufacturer must be a non-empty string of alphabetic characters")

        if not Capacity.isdigit():
            raise ValueError("Capacity must be a positive integer")

        # Validate that Distance, Travel_Time, and Contact_Phone_Number are digits
        try:
            Capacity = int(Capacity)
        except ValueError:
            raise ValueError("Distance, Travel Time, and Contact Phone Number must be numeric")

        # Create a new Destination object
        NewAirplaine = Airplaine(
            NameOfPlane=NameOfPlane,
            CurrentLocation=CurrentLocation,
            Type=Type,
            Manufacturer=Manufacturer,
            Capacity=Capacity,
            
        )

        # Adding new airplaine
        self.AirplaineData.AddAirplaine(NewAirplaine)