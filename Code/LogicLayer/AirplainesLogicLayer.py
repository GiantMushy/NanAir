from DataLayer.AirplainesDataLayer import AirplaineData
from Models.AirplaineModel import Airplaine

class AirplaineManagerLogic:
    def __init__(self):
        self.AirplainesData_data = AirplaineData()

def AddAirplaine(self, NameOfPlane, CurrentLocation, Type, Manufacturer, Capacity):
        if not NameOfPlane or not NameOfPlane.isalpha():
            raise ValueError("The name of the airplaine must be a non-empty string of alphabetic characters")

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
        try:
             NameOfPlane = str(NameOfPlane)
        except ValueError:
             raise ValueError("The Name of the plane must only contain letters")
        try: 
             CurrentLocation = str(CurrentLocation)
        except ValueError:
             raise ValueError("Current location must only have letters")


        

        # Create a new Airplaine Object
        NewAirplaine = Airplaine(
            NameOfPlane=NameOfPlane,
            CurrentLocation=CurrentLocation,
            Type=Type,
            Manufacturer=Manufacturer,
            Capacity=Capacity,
            
        )

        # Adding new airplaine
        self.AirplaineData.AddAirplaine(NewAirplaine)

def EditAirplaine(self, NameOfPlaine, updates):
    """"Finds the airplaine by the name """
    if any(key in updates for key in['Name', 'Type', 'Manufacturer']):
         raise ValueError( "Modification of 'Name', 'Type' or 'Manufacturer' is not allowed")
    
    airplanes = self.AirplainesData_data.ReadAllAirplaines()
    airplane_found = False
    updated_airplanes = []


     
        
        