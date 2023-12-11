from LogicLayer.LogicLayerAPI import LogicLayerAPI
from UiLayer.PrintFunctions import PrintFunctions

class EmployeeSchedulesUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()

    def employee_schedules_output(self):
        date = "08.01.24"
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Schedules", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"List of Employees Work Status on {date}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("------------Table goes here-------------"))
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
        print(self.PrintUi.allign_left("A : Show Only Working Employees                   <Nr> : See Specific Employee's Week Schedule"))
        print(self.PrintUi.allign_left("S : Show Only Non-Working Employees"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("0 : Back To Main Menu       00 : Change Day          n : Previous Day             m : Next Day"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        while True:
            self.employee_schedules_output()
            command = input("Enter you command: ").lower()          

            if command == "q":
                print("Goodbye")
                break
            elif command == "0":
                pass
            elif command == "00":
                pass
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")