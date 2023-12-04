#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.EmployeeDataCreateNewUI import EmployeeDataCreateNewUI
from UiLayer.EmployeeDataEditUI import EmployeeDataEditUI

class EmployeeDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def employee_data_output(self):
        '''Print sequence for the Employee Data Menu'''
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
        '''Starting function for EmployeeDataUI'''
        while True:
            self.employee_data_output()
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "1":
                edit = EmployeeDataEditUI([])
                edit.input_prompt()
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            else:
                print("Invalid input, try again")