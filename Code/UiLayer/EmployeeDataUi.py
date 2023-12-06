from LogicLayer.LogicLayerAPI import LogicLayerAPI
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.EmployeeDataCreateNewUI import EmployeeDataCreateNewUI
from UiLayer.EmployeeDataEditUI import EmployeeDataEditUI

class EmployeeDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()

    def employee_data_output(self):
        '''Print sequence for the Employee Data Menu'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Employees"))
        print(self.PrintUi.empty_line())
        list_data = self.Logic.list_all_employees()
        printable_dict = self.Logic.object_list_to_dict_list(list_data)
        self.PrintUi.print_employee_table(printable_dict, 13)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" A : Show Pilots               S  : Show Flight-Attendants"))
        print(self.PrintUi.allign_left(" 0 : Back                      00 : Create New Employee      <ID> : Edit Employee Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for EmployeeDataUI'''
        while True:
            self.employee_data_output()
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            elif command == "a":
                pass
            elif command == "s":
                pass
            elif command == "1": #make it take employee data
                edit = EmployeeDataEditUI([])
                edit.input_prompt()
            else:
                print("Invalid input, try again")