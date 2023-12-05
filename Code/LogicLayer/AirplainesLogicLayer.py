from DataLayer.AirplainesDataLayer import AirplaineData
from Models.AirplaineModel import Airplaine

class AirplaneService:
    def __init__(self, airplane_data):
        self.airplane_data = airplane_data

    def get_all_airplanes(self):
        return self.airplane_data.read_all_airplaines()

    def find_airplane_by_name(self, name):
        all_airplanes = self.get_all_airplanes()
        return [airplane for airplane in all_airplanes if airplane.name == name]

    def add_new_airplane(self, airplane):
        self.airplane_data.add_airplaine(airplane)

    def update_airplane(self, updated_airplane):
        all_airplanes = self.get_all_airplanes()
        updated_airplanes = [airplane if airplane.name != updated_airplane.name else updated_airplane for airplane in all_airplanes]
        self.airplane_data.modify_airplaine_data(updated_airplanes)

   
