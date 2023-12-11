# from UiLayer.LoginUI import LoginUI
# from UiLayer.FlightSchedulesUI import FlightSchedulesUI
# from UiLayer.EmployeeSchedulesUI import EmployeeSchedulesUI
# from UiLayer.EmployeeDataUI import EmployeeDataUI
# from UiLayer.DestinationDataUI import DestinationDataUI
# from UiLayer.AirplaneDataUI import AirplaneDataUI
from Code.LogicLayer.ValidationService import ValidationService
from datetime import date

# login = LoginUI()
# flght_sched = FlightSchedulesUI()
# empl_sched = EmployeeSchedulesUI()
# empl_data = EmployeeDataUI()
# dest_data = DestinationDataUI()
# air_data = AirplaneDataUI()

# login.input_prompt()

v = ValidationService()

year = int(input())
month = int(input())
day = int(input())
date = date(year, month, day)

lst = v.check_employee_availability(20)
print(lst)