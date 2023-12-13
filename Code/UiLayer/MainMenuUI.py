# from logic_ui_wrapper import wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions
from Code.UiLayer.FlightSchedulesUI import FlightSchedulesUI
from Code.UiLayer.EmployeeSchedulesUI import EmployeeSchedulesUI
from Code.UiLayer.EmployeeDataUI import EmployeeDataUI
from Code.UiLayer.DestinationDataUI import DestinationDataUI
from Code.UiLayer.AirplaneDataUI import AirplaneDataUI


class MainMenuUI:
    def __init__(self, user=""):
        self.PrintUi = PrintFunctions()
        self.user = user

    def main_menu_output(self):
        '''Print sequence for the Main Menu'''
        self.PrintUi.logo()
        self.PrintUi.print_header(self.user + " > Main Menu", "center")
        print(self.PrintUi.empty_line())
        if self.user == "Trip Manager":
            print(self.PrintUi.allign_center(
                "        1 : View and Create Flight Schedules "))
        else:
            print(self.PrintUi.allign_center(
                "      1 : View and Staff Flight Schedules"))
        print(self.PrintUi.allign_center("2 : Employee Schedules       "))
        print(self.PrintUi.allign_center("3 : Employee Database Menu   "))
        print(self.PrintUi.allign_center("4 : Destination Database Menu"))
        print(self.PrintUi.allign_center("5 : Airplane Database Menu   "))
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
        '''Starting function for the Main Menu'''
        while True:
            self.main_menu_output()
            command = input("Enter you command: ")
            command = command.lower()

            if command == "0":
                break
            elif command == "1":
                flight_schedules = FlightSchedulesUI(self.user)
                flight_schedules.input_prompt()
            elif command == "2":
                employee_schedules = EmployeeSchedulesUI()
                employee_schedules.input_prompt()
            elif command == "3":
                employee_database = EmployeeDataUI()
                employee_database.input_prompt()
            elif command == "4":
                destination_database = DestinationDataUI()
                destination_database.input_prompt()
            elif command == "5":
                airplane_database = AirplaneDataUI()
                airplane_database.input_prompt()
            elif command == "0":
                pass
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")
