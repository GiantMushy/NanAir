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

        if not Type or not Type.isalpha():
            raise ValueError("Type must be a non-empty string with alphabetic characters and numbers")

        if not Manufacturer.isalpha():
            raise ValueError("Manufacturer must be a non-empty string of alphabetic characters")

        if not Capacity.isdigit():
            raise ValueError("Capacity must be a positive integer")

        # Validate that capacity only has digits
        try:
            Capacity = int(Capacity)
        except ValueError:
            raise ValueError("Capacity must be numeric")
        #Validate that name of plane and current location only has letters and 

        #validate tha 1-3 of type is letters and 4-7 is - and 5 is a number and 6-9 is a number

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