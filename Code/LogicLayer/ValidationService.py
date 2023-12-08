from DataLayer.DataLayerAPI import DataLayerAPI
from LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic


class ValidationSerivce:
    def __init__(self):
        self.data = DataLayerAPI()

    def test(self):
        all_work_trips = self.data.read_all_work_trips

        for trip in all_work_trips:
            print(trip.__dict__.id == work_trip_id)

    def validate_work_trip(self, all_work_trips):
        pass

    def validate_employee_availability(self):
        pass