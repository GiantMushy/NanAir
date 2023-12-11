from Code.UiLayer.LoginUI import LoginUI
from Code.UiLayer.FlightSchedulesUI import FlightSchedulesUI
from Code.UiLayer.EmployeeSchedulesUI import EmployeeSchedulesUI
from Code.UiLayer.EmployeeDataUI import EmployeeDataUI
from Code.UiLayer.DestinationDataUI import DestinationDataUI
from Code.UiLayer.AirplaneDataUI import AirplaneDataUI

login = LoginUI()
flght_sched = FlightSchedulesUI()
empl_sched = EmployeeSchedulesUI()
empl_data = EmployeeDataUI()
dest_data = DestinationDataUI()
air_data = AirplaneDataUI()

login.input_prompt()