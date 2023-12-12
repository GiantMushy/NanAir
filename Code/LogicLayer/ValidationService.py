from Code.DataLayer.DataLayerAPI import DataLayerAPI
from Code.LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic
from Code.LogicLayer.Exceptions import *
from datetime import datetime, date

class ValidationService:
    def __init__(self):
        self.data = DataLayerAPI()
        self.emp_logic = EmployeeManagerLogic()


    def read_id(self):
        '''Reads the information for id's in WorkTrip.csv'''
        all_work_trips = self.data.read_all_work_trips

   
    def check_employee_availability(self, date): 
        '''Checks if there are any employees available for a specific workdate. 
        It takes out the ones that are not available and gives a list of 
        employee numbers that are available'''
        date_compare = datetime.strptime(date,"%Y-%m-%d %H:%M")
        date_compare = date_compare.date()

        all_work_trips = self.data.read_all_work_trips()

        busy_employees = []

        #Reads all work days and sees which employees working on those days and edits them out of the day
        all_work_days = []
        for trip in all_work_trips:
            departure_date = trip.departure_datetime.date()
            if date_compare == departure_date:
                busy_members = trip.crew_members.split(',')
                for busy in busy_members:
                    busy_employees.append(busy)
        
        #Seperates id's and takes out the ones that are busy
        for trip in all_work_days:
            crew_members_list = trip.crew_members.split(",") 
            for member in crew_members_list:
                busy_employees.append(member)

        #Finds available employees on a specific date
        all_employees = self.data.read_all_employees()
        available_employees = [emp.id for emp in all_employees if emp.id not in busy_employees] 

        #Returns a list of available employees on that day
        return available_employees 
        

    def validate_work_trip(self, pilot1id, pilot2id, flight_attendants_id_list):
        '''Here the function makes a requirement of at least 2 pilots (1 captain and 1 co-pilot) 
        and at least one senior flight attendant. There can be more than one flight attendants 
        on each flight but not without a senior flight attendant'''

        pilot1model = self.emp_logic.find_employee_by_id(pilot1id)
        pilot2model = self.emp_logic.find_employee_by_id(pilot2id)

        #Checks if there is a captain on the trip, if not it sends an error message that there 
        # needs to be at least one captain for this flight
        if not self.emp_logic.is_captain(pilot1id) and not self.emp_logic.is_captain(pilot2id):
            raise NoPilotException("No captain found, there needs to be at least one captain for this flight") #both pilots are not captains

        #Checks if there is a flight attendant on the flight and sends a error 
        # messsage if there is no flight attendant on the flight
        if len(flight_attendants_id_list) <= 0:
            raise NoFlightAttendantException("There needs to be at least one flight attendant for this flight") #Needs to have at least one FA
        found_manager = False

        #Checks if there is at least one senior flight attendant on the flight. 
        # If senior is not found it sends an error message that there is no senior on this flight
        for id in flight_attendants_id_list:
            if self.emp_logic.is_senior_flight_attendant(id):
                found_manager = True
        if found_manager == False:
            raise NoSeniorFlightAttendantException("There is no senior flight attendant. There needs to be a senior flight attendant for this flight") #none of the FAs is a senior
        
