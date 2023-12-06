from LogicLayer.LogicLayerAPI import LogicLayerAPI
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.EmployeeDataCreateNewUI import EmployeeDataCreateNewUI
from UiLayer.EmployeeDataEditUI import EmployeeDataEditUI

class EmployeeDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        
    def employee_data_output(self, printed_dicts, employee_type):
        '''Print sequence for the Employee Data Menu'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of " + employee_type[0]))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_employee_table(printed_dicts, 14)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(employee_type[1]))
        print(self.PrintUi.allign_left(" 0 : Back       q : exit       00 : Create New Employee      <ID> : Edit Employee Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for EmployeeDataUI'''
        temp_list_data = self.Logic.list_all_employees()
        all_employee_data = self.Logic.object_list_to_dict_list(temp_list_data)
        all_pilot_data = self.Logic.list_all_pilots()
        all_flight_attendant_data = self.Logic.list_all_flight_attendants()

        printed_dicts = all_employee_data
        employee_type = ["Employees", " A : Show Pilots               S : Show Flight-Attendants"]
        while True:
            self.employee_data_output(printed_dicts, employee_type)
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            elif command.isdigit():
                for dict in printed_dicts:
                    if int(command) == int(dict["id"]):
                        edit = EmployeeDataEditUI(dict)
                        edit.input_prompt()
            elif command == "a":
                printed_dicts = all_pilot_data
                employee_type = ["Pilots", " D : Show All Employees        S : Show Flight-Attendants"]
            elif command == "s":
                printed_dicts = all_flight_attendant_data
                employee_type = ["Flight Attendants", " A : Show Pilots               D : Show All Employees"]
            elif command == "d":
                printed_dicts = all_employee_data
                employee_type = ["Employees", " A : Show Pilots               S : Show Flight-Attendants"]
            elif command == "q":
                exit()
            else:
                print("Invalid input, try again")