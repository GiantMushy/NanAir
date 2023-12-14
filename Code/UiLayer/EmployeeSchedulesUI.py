from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI  # Wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions
from Code.UiLayer.EmployeeScheduleSpecificUI import EmployeeScheduleSpecificUI
import datetime
import ast


class EmployeeSchedulesUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()

    def employee_schedules_output(self, start_date, working_notworking_all):
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Schedules", "left")
        print_format = "%-6s%-20s%-30s%-20s"
        print(self.PrintUi.empty_line())
        if working_notworking_all == "all":
            print(self.PrintUi.allign_left(
                f"List of Employees Work Status on {start_date.date()}:"))
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left(print_format %
                  ('Id', 'Name', 'Position', 'Flying to')))
            print(self.PrintUi.empty_line())
            self.print_employees_all(print_format, 13)
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left(
                "<Id> : See Employee's weekly schedule          A : Show Only Working Employees      S : Show Only Non-Working Employees"))
        elif working_notworking_all == "working":
            print(self.PrintUi.allign_left(
                f"List of Employees Working on {start_date.date()}:"))
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left(print_format %
                  ('Id', 'Name', 'Position', 'Flying to')))
            print(self.PrintUi.empty_line())
            self.print_employees_working(print_format, 13)
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left(
                " <Id> : See Employee's weekly schedule          D : Show All Employees      S : Show Only Non-Working Employees"))
        else:
            print(self.PrintUi.allign_left(
                f"List of Employees Not Working on {start_date.date()}:"))
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left(print_format %
                  ('Id', 'Name', 'Position', 'Work Status')))
            print(self.PrintUi.empty_line())
            self.print_employees_not_working(print_format, 13)
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left(
                "  <Id> : See Employee's weekly schedule          A : Show Only Working Employees      D : Show All Employees"))
        print(self.PrintUi.allign_left(
            "         0 : Back              00 : Change Day                n : See Yesterday             m : See Tomorrow"))
        print(self.PrintUi.end_line())

    def print_employees_all(self, print_format, line_num):
        line_count = 0

        for dic in self.working:
            destination = ast.literal_eval(dic['destination'])
            employee = self.Logic.object_to_dict(
                self.Logic.find_employee_by_id_detailed(dic['employee_id']))
            name = employee['name']
            if len(name) > 19:
                name = self.PrintUi.shorten_name(name)
            print(self.PrintUi.allign_left(print_format % (
                f"{dic['employee_id']} :", name, employee['role'], f"{destination['city']}, {destination['country']}")))
            line_count += 1

        for id in self.not_working:
            employee = self.Logic.object_to_dict(
                self.Logic.find_employee_by_id_detailed(id))
            name = employee['name']
            if len(name) > 19:
                name = self.PrintUi.shorten_name(name)
            print(self.PrintUi.allign_left(print_format %
                  (f"{id} : ", name, employee['role'], "Not Working")))
            line_count += 1

        while line_count != line_num:
            print(self.PrintUi.empty_line())
            line_count += 1

    def print_employees_working(self, print_format, line_num):
        line_count = 0

        for dic in self.working:
            destination = ast.literal_eval(dic['destination'])
            employee = self.Logic.object_to_dict(
                self.Logic.find_employee_by_id_detailed(dic['employee_id']))
            name = employee['name']
            if len(name) > 19:
                name = self.PrintUi.shorten_name(name)
            print(self.PrintUi.allign_left(print_format % (
                f"{dic['employee_id']} :", name, employee['role'], f"{destination['city']}, {destination['country']}")))
            line_count += 1

        while line_count != line_num:
            print(self.PrintUi.empty_line())
            line_count += 1

    def print_employees_not_working(self, print_format, line_num):
        line_count = 0

        for id in self.not_working:
            employee = self.Logic.object_to_dict(
                self.Logic.find_employee_by_id_detailed(id))
            name = employee['name']
            if len(name) > 19:
                name = self.PrintUi.shorten_name(name)
            print(self.PrintUi.allign_left(print_format %
                  (f"{id} :", name, employee['role'], "Not Working")))
            line_count += 1

        while line_count != line_num:
            print(self.PrintUi.empty_line())
            line_count += 1

    def innitiate_and_switch_lists(self, start_date):
        self.working = self.Logic.list_employees_working_and_destinations(
            start_date.strftime('%Y-%m-%d %H:%M'))  # list of dictionaries
        self.not_working = self.Logic.list_all_available_employees(start_date.strftime(
            '%Y-%m-%d %H:%M'))  # list of id's ['003', '004', '005', '006', '007', '008', '009', '010']

    def input_prompt(self):
        '''Starting function for EmployeeSchedulesUI'''
        day_timedelta = datetime.timedelta(1)
        start_date = datetime.datetime.now()
        working_notworking_all = "working"
        while True:
            self.innitiate_and_switch_lists(start_date)
            self.employee_schedules_output(start_date, working_notworking_all)
            command = input("Enter your command: ").lower()

            if command == "0":
                break
            elif command == "00":  # change days
                start_date = self.PrintUi.change_date()
            elif command.isdigit():  # see employees weekly schedule
                if working_notworking_all == 'all':
                    invalid = True
                    for dic in self.working:
                        if int(command) == int(dic['employee_id']):
                            invalid = False
                            specific = EmployeeScheduleSpecificUI(
                                dic['employee_id'], start_date)
                            specific.input_prompt()
                    for id in self.not_working:
                        if int(command) == int(id):
                            invalid = False
                            specific = EmployeeScheduleSpecificUI(
                                id, start_date)
                            specific.input_prompt()
                    if invalid:
                        print("Invalid input, try again")
                elif working_notworking_all == "working":
                    invalid = True
                    for dic in self.working:
                        if int(command) == int(dic['employee_id']):
                            invalid = False
                            specific = EmployeeScheduleSpecificUI(
                                dic['employee_id'], start_date)
                            specific.input_prompt()
                    if invalid:
                        print("Invalid input, try again")
                elif working_notworking_all == "not working":
                    invalid = True
                    for id in self.not_working:
                        if int(command) == int(id):
                            invalid = False
                            specific = EmployeeScheduleSpecificUI(
                                id, start_date)
                            specific.input_prompt()
                    if invalid:
                        print("Invalid input, try again")
                else:
                    print("Invalid input, try again")
            elif command == "a":  # show working employees
                working_notworking_all = "working"
            elif command == "s":  # show non-working employees
                working_notworking_all = "not working"
            elif command == "d":  # show ALL employees
                working_notworking_all = "all"
            elif command == "n":  # see yesterday
                start_date = start_date - day_timedelta
            elif command == "m":  # see tomorrow
                start_date = start_date + day_timedelta
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")
