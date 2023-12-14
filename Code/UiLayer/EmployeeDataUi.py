from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI
from Code.UiLayer.PrintFunctions import PrintFunctions
from Code.UiLayer.EmployeeDataCreateNewUI import EmployeeDataCreateNewUI
from Code.UiLayer.EmployeeDataEditUI import EmployeeDataEditUI


class EmployeeDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()

    def all_employees_detailed(self):
        '''Returns a list of all employees with detailed information'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Employees"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_employee_table_detailed(
            self.Logic.object_list_to_dict_list(self.Logic.list_all_employees_detailed()), 14)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_center(
            " 0 : Back      00 : Create New Employee      <ID> : View/Edit Employee Data"))
        print(self.PrintUi.allign_center(
            " A : Show all Pilots      S : Show all Flight Attendants"))
        print(self.PrintUi.end_line())

    def pilots_detailed(self):
        '''Returns a list of all employees with detailed information'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Pilots", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Pilots"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_pilots_table_detailed(
            (self.Logic.list_all_pilots()), 14)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_center(
            " 0 : Back      00 : Create New Employee      <ID> : View/Edit Employee Data"))
        print(self.PrintUi.allign_center(
            " A : All pilots sorted by pilot license       S: Show all pilots with a specific pilot license"))
        print(self.PrintUi.end_line())

    def flight_attendants_detailed(self):
        '''Returns a list of all employees with detailed information'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Employee Database Menu > Flight Attendants", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Flight Attendants"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_flight_attendants_table_detailed(
            (self.Logic.list_all_flight_attendants()), 14)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_center(
            " 0 : Back      00 : Create New Employee      <ID> : View/Edit Employee Data"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.end_line())

    def pilot_sorted_by_type(self):
        '''Returns a list of all employees with detailed information'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Employee Database Menu > Pilots > Sorted by pilot license", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Pilots"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_pilots_table_detailed(
            (self.Logic.object_list_to_dict_list(self.Logic.list_pilots_sorted_by_airplane_type())), 14)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_center(
            " 0 : Back      00 : Create New Employee      <ID> : View/Edit Employee Data"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.end_line())

    def pilot_specific_type(self, type):
        '''Returns a list of all employees with detailed information'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Employee Database Menu > Pilots > Pilots with licence on {type}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Pilots"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_pilots_table_detailed(
            (self.Logic.object_list_to_dict_list(self.Logic.list_pilots_by_airplane_type(type))), 14)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_center(
            " 0 : Back      00 : Create New Employee      <ID> : View/Edit Employee Data"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.end_line())

    def input_airplane_type(self):
        '''Print sequence for Creating a new Employee : Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Employee Database Menu > Pilots > Choosing Type", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Choose type of airplane"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        if self.Logic.list_all_airplane_types() == []:
            print(self.PrintUi.allign_left(
                "It seems that there are no airplane types in the database, please add some airplanes before creating a pilot."))
            print(self.PrintUi.allign_left(
                "Enter '0' to go back."))
            for i in range(10):
                print(self.PrintUi.empty_line())

        else:
            self.PrintUi.print_airplane_type_table(
                self.Logic.object_list_to_dict_list((self.Logic.list_all_airplane_types())), 12)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            " 0 : Back"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for EmployeeDataUI'''
        while True:
            self.all_employees_detailed()
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            elif command.isdigit():
                for dict in self.Logic.object_list_to_dict_list(self.Logic.list_all_employees_detailed()):
                    if int(command) == int(dict['id']):
                        edit = EmployeeDataEditUI(dict['id'])
                        edit.input_prompt()
            elif command == "q":
                print("Goodbye")
                exit()
            elif command == "a":
                self.display_pilot_menu()
            elif command == "s":
                self.display_flight_attendants_menu()
            else:
                print("Invalid input, try again")

    def display_flight_attendants_menu(self):
        while True:
            self.flight_attendants_detailed()
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            elif command.isdigit():
                self.isdigit_edit_emp(command)
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")

    def isdigit_edit_emp(self, command):
        if command.isdigit():
            for dict in self.Logic.object_list_to_dict_list(self.Logic.list_all_employees_detailed()):
                if int(command) == int(dict['id']):
                    edit = EmployeeDataEditUI(dict['id'])
                    edit.input_prompt()

    def display_pilot_menu(self):
        while True:
            self.pilots_detailed()
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            elif command.isdigit():
                self.isdigit_edit_emp(command)

            elif command == "q":
                print("Goodbye")
                exit()
            elif command == "a":
                self.display_pilot_sorted_by_type()
            elif command == "s":
                self.display_choose_airplane_type()
            else:
                print("Invalid input, try again")

    def display_choose_airplane_type(self):
        while True:

            self.input_airplane_type()
            command = input("Enter you command: ").lower()

            if command == "0":
                break

            elif command == "q":
                print("Goodbye")
                exit()

            elif self.Logic.find_type_data(command.upper()) is not None:
                self.display_pilot_specific_type(command.upper())
            else:
                print("Invalid input, try again")

    def display_pilot_specific_type(self, type):
        while True:
            self.pilot_specific_type(type)
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            elif command.isdigit():
                self.isdigit_edit_emp(command)

            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")

    def display_pilot_sorted_by_type(self):
        while True:
            self.pilot_sorted_by_type()
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            elif command.isdigit():
                self.isdigit_edit_emp(command)

            elif command == "q":
                print("Goodbye")
                exit()         ################ CRASH REPORT ##############
            else:
                print("Invalid input, try again")
