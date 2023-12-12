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

# 2032-11-14
#year = int(2032)
#month = int(11)
#day = int(14)
#date = date(year, month, day)

lst = v.check_employee_availability('2023-12-12 14:00')
print(lst)

#v.validate_work_trip("002", "005", ["001", "004"])