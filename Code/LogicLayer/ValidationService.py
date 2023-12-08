from Code.DataLayer.DataLayerAPI import DataLayerAPI
from Code.LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic


class ValidationSerivce:
    def __init__(self):
        self.data = DataLayerAPI()

    def test(self):
        all_work_trips = self.data.read_all_work_trips

        for trip in all_work_trips:
            print(trip.__dict__.id == work_trip_id)

    def validate_work_trip(self, all_work_trips):
        pass

    def check_employee_availability(self, date):
        all_work_trips = self.data.read_all_work_trips()
 
        all_work_days = [trip for trip in all_work_trips if trip.departure_datetime.year == date.year and trip.departure_datetime.month == date.month and trip.departure_datetime.day == date.day]
        busy_employees = []

        for trip in all_work_days:
            if trip.crew_members:
                busy_employees += trip.crew_members.split(",")

        all_employees = self.data.read_all_employees()
        available_employees = [emp.id for emp in all_employees if emp.id not in busy_employees]

        return available_employees
