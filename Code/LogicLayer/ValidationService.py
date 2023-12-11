from Code.DataLayer.DataLayerAPI import DataLayerAPI
from Code.LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic


class ValidationService:
    def __init__(self):
        self.data = DataLayerAPI() 

    def test(self):
        '''Reads the information for id's in WorkTrip.csv'''
        all_work_trips = self.data.read_all_work_trips

        #Prints out all of the id's
        for trip in all_work_trips:
            print(trip.__dict__.id == work_trip_id)

    
    def check_employee_availability(self, date): 
        '''Checks if there are any employees available for a specific workdate. 
        It takes out the ones that are not available and gives a list of 
        employee numbers that are available'''

        all_work_trips = self.data.read_all_work_trips()
 
        #Reads all work days and sees which employees working on those days and edits them out of the day
        all_work_days = [trip for trip in all_work_trips if trip.departure_datetime.year == date.year and trip.departure_datetime.month == date.month and trip.departure_datetime.day == date.day]
        busy_employees = []

        #Splits all of the employees 
        for trip in all_work_days:
            if trip.crew_members:
                busy_employees += trip.crew_members.split(",")

        #Isolates the employees that are working on a specific day and gives a list of employees that are available for that day
        all_employees = self.data.read_all_employees()
        available_employees = [emp.id for emp in all_employees if emp.id not in busy_employees]

        #Returns a list of available employees
        return available_employees


    def validate_work_trip(self):
        '''Here the function makes a requirement of at least 2 pilots (1 captain and 1 co-pilot) 
        and at least one senior flight attendant. There can be more than one flight attendants 
        on each flight but not without a senior flight attendant'''
        pass
