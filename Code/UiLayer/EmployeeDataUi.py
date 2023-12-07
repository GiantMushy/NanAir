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

    def innitiate_and_switch_lists(self, employee_type):
        temp_list_data = self.Logic.list_all_employees()
        if employee_type == 0:
            return self.Logic.object_list_to_dict_list(temp_list_data)
        elif employee_type == 1:
            return self.Logic.list_all_pilots()
        elif employee_type == 2:
            return self.Logic.list_all_flight_attendants()

    def input_prompt(self):
        '''Starting function for EmployeeDataUI'''
        employee_type = 0 #0 = all ---- 1 = Pilots -----2 = Flight Attendants
        employee_type_prints = [["Employees", " A : Show Pilots               S : Show Flight-Attendants"],
                                ["Pilots", " D : Show All Employees        S : Show Flight-Attendants"],
                                ["Flight Attendants", " A : Show Pilots               D : Show All Employees"]]
        while True:
            printed_dicts = self.innitiate_and_switch_lists(employee_type)
            self.employee_data_output(printed_dicts, employee_type_prints[employee_type])
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            elif command.isdigit():
                for dict in printed_dicts:
                    if int(command) == int(dict["id"]):
                        edit = EmployeeDataEditUI(dict["id"])
                        edit.input_prompt()
            elif command == "a":
                employee_type = 1
            elif command == "s":
                employee_type = 2
            elif command == "d":
                employee_type = 0
            elif command == "q":
                exit()
            else:
                print("Invalid input, try again")