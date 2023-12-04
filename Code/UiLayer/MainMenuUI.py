#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions
#from UiLayer.FlightSchedulesUI import FlightSchedulesUI
#from UiLayer.EmployeeSchedulesUI import EmployeeSchedulesUI
from UiLayer.EmployeeDataUI import EmployeeDataUI
from UiLayer.DestinationDataUI import DestinationDataUI
from UiLayer.AirplaneDataUI import AirplaneDataUI

class MainMenuUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def main_menu_output(self):
        self.PrintUi.logo()
        self.PrintUi.print_header("Main Menu", "center")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_center("1 : Flight Schedules"))
        print(self.PrintUi.allign_center("2 : Employee Schedules"))
        print(self.PrintUi.allign_center("3 : Employee Database Menu"))
        print(self.PrintUi.allign_center("4 : Destination Database Menu"))
        print(self.PrintUi.allign_center("5 : Airplane Database Menu"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line()) 
        print(self.PrintUi.allign_center("0: Back"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        while True:
            self.main_menu_output()
            command = input("Enter you command: ")
            command = command.lower()

            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                #flight_schedules = FlightSchedulesUI()
                #flight_schedules.input_prompt()
                pass
            elif command == "2":
                #employee_schedules = EmployeeSchedulesUI()
                #employee_schedules.input_prompt()
                pass
            elif command == "3":
                employee_database_menu = EmployeeDataUI()
                employee_database_menu.input_prompt()
            elif command == "4":
                destination_database_menu = DestinationDataUI()
                destination_database_menu.input_prompt()
                pass
            elif command == "5":
                airplane_database_menu = AirplaneDataUI()
                airplane_database_menu.input_prompt()
                pass
            elif command == "0":
                pass
            else:
                print("Invalid input, try again")