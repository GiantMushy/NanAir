from DataLayer.AirplainesDataLayer import AirplaineData
from Models.AirplaineModel import Airplaine

class AirplaineManagerLogic:
    def __init__(self):
        self.AirplainesData_data = AirplaineData()
        
def generate_unique_airplaine_id(self):
        """
        Generates a unique airplaine ID.
        If no airplaines exist, starts from '001'.
        Otherwise, increments the maximum existing ID by 1.
        :return: A string representing the unique ID.
        """
        airplaines = self.airplaine_data.read_all_airplaines()
        if not airplaines:
            # base case, no airplaines in the database
            return "001"

        # find the highest existing ID and increment by 1
        max_id = max(int(plaines.id) for plaines in airplaines)
        new_id = max_id + 1
        return str(new_id).zfill(3)  # pad with zeros to maintain a length of 3


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

    for plaines in airplanes:
        if plaines.NameOfPlaine == NameOfPlaine:
            airplaine_found = True
            for key, value in updates.items():
                if hasattr(plaines, key):
                    setattr(plaines, key, value)
                else:
                    raise ValueError(f"Invalid field:{key}")
        updated_airplanes.append(plaines)

    if not airplaine_found:
        raise ValueError(f"Airplaine with name {NameOfPlaine} not found")
    
    # Write the updated list back to the data layer
    self.AirplainesData_data.ModifyAirplaineData(updated_airplanes)
                   


     
        
        