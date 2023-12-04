#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.EmployeeDataCreateNewUI import EmployeeDataCreateNewUI

class EmployeeDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def employee_data_output(self):
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Employees"))
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
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 0 : Back                     00 : Create New Employee                  <Employee number> : Edit Employee Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        while True:
            self.employee_data_output()
            command = input("Enter you command: ")            

            if command == "q":
                print("Goodbye")
                break
            elif command == "0":
                pass
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            else:
                print("Invalid input, try again")