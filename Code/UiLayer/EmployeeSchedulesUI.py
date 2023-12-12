from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI #Wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions
import datetime
import ast

class EmployeeSchedulesUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()

    def employee_schedules_output(self, start_date, working_notworking_all):
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Schedules", "left")
        print(self.PrintUi.empty_line())
        if working_notworking_all == "all":
            print(self.PrintUi.allign_left(f"List of Employees Work Status on {start_date.date()}:"))
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("%-6s%-20s%-20s" % ('Id', 'Name', 'Flying to')))
            print(self.PrintUi.empty_line())
            self.print_employees_all(13)
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("<Id> : See Employee's weekly schedule          A : Show Only Working Employees      S : Show Only Non-Working Employees"))
        elif working_notworking_all == "working":
            print(self.PrintUi.allign_left(f"List of Employees Working on {start_date.date()}:"))
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("%-6s%-20s%-20s" % ('Id', 'Name', 'Flying to')))
            print(self.PrintUi.empty_line())
            self.print_employees_working(13)
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("<Id> : See Employee's weekly schedule          D : Show All Employees      S : Show Only Non-Working Employees"))
        else:
            print(self.PrintUi.allign_left(f"List of Employees Not Working on {start_date.date()}:"))
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("%-6s%-20s%-20s" % ('Id', 'Name', 'Work Status')))
            print(self.PrintUi.empty_line())
            self.print_employees_not_working(13)
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("<Id> : See Employee's weekly schedule          A : Show Only Working Employees      D : Show All Employees"))
        print(self.PrintUi.allign_left("         0 : Back              00 : Change Day                n : See Yesterday             m : See Tomorrow"))
        print(self.PrintUi.end_line())

    def print_employees_all(self, line_num):
        line_count = 0
        print(self.working)
        print(self.not_working)
        while line_count != line_num:
            print(self.PrintUi.empty_line())
            line_count += 1
            
    def print_employees_working(self, line_num):
        line_count = 0
        print_format = "%-6s%-20s%-20s"

        for dic in self.working:
            destination = ast.literal_eval(dic['destination'])
            employee = self.Logic.object_to_dict(self.Logic.find_employee_by_id(dic['employee_id']))
            print(self.PrintUi.allign_left(print_format % (f"{dic['employee_id']} : ", employee['name'], f"{destination['city']}, {destination['country']}")))
            line_count += 1

        while line_count != line_num:
            print(self.PrintUi.empty_line())
            line_count += 1
            
    def print_employees_not_working(self, line_num):
        line_count = 0
        print_format = "%-6s%-20s%-20s"
        
        for dic in self.working:
            destination = ast.literal_eval(dic['destination'])
            employee = self.Logic.object_to_dict(self.Logic.find_employee_by_id(dic['employee_id']))
            print(self.PrintUi.allign_left(print_format % (f"{dic['employee_id']} : ", employee['name'], f"{destination['city']}, {destination['country']}")))
            line_count += 1

        while line_count != line_num:
            print(self.PrintUi.empty_line())
            line_count += 1

    def innitiate_and_switch_lists(self, start_date):
        self.working = self.Logic.list_employees_working_and_destinations(start_date.strftime('%Y-%m-%d %H:%M')) #list of dictionaries
        #[{'employee_id': '001', 'destination': "{'id': '02', 'city': 'Matta city', 'airport': 'Matti airport', 'country': 'Mattaland', 'distance': '6', 'travel_time': '40', 'contact_name': 'Helgi', 'contact_phone_number': '9876543'}"}, 
        # {'employee_id': '002', 'destination': "{'id': '02', 'city': 'Matta city', 'airport': 'Matti airport', 'country': 'Mattaland', 'distance': '6', 'travel_time': '40', 'contact_name': 'Helgi', 'contact_phone_number': '9876543'}"}]
        self.not_working = self.Logic.list_all_available_employees(start_date.strftime('%Y-%m-%d %H:%M')) #list of id's ['003', '004', '005', '006', '007', '008', '009', '010']
        #return self.Logic.object_list_to_dict_list(printed_data)

    def input_prompt(self):
        '''Starting function for AirplaneDataUI'''
        day_timedelta = datetime.timedelta(1)
        start_date = datetime.datetime(2023,12,12,0,0)
        working_notworking_all = "working"
        while True:
            self.innitiate_and_switch_lists(start_date)
            self.employee_schedules_output(start_date, working_notworking_all)
            command = input("Enter your command: ").lower()

            if command == "0":
                break
            elif command == "00": #change day
                input_check = False
                while not input_check:
                    try:
                        command = input("Enter a day (YYYY-MM-DD): ").lower()
                        if command == "q":
                            print("Goodbye")
                            exit()
                        year, month, day = command.split('-')
                        start_date = datetime.datetime(int(year), int(month), int(day), 0,0)
                        input_check = True
                    except ValueError as e:
                        print(f"Error: {e}")
                        input_check = False
            elif command.isdigit(): #see employees weekly schedule
                pass
            elif command == "a": #show working employees
                working_notworking_all = "working"
            elif command == "s": #show non-working employees
                working_notworking_all = "not working"
            elif command == "d": #show ALL employees
                working_notworking_all = "all"
            elif command == "n": #see yesterday
                start_date = start_date - day_timedelta 
            elif command == "m": #see tomorrow
                start_date = start_date + day_timedelta
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")