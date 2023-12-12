from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI #Wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions
import datetime

class EmployeeSchedulesUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()

    def employee_schedules_output(self, printed_data, start_date, working_notworking_all):
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Schedules", "left")
        print(self.PrintUi.empty_line())
        if working_notworking_all == "all":
            print(self.PrintUi.allign_left(f"List of Employees Work Status on {start_date.date()}:"))
            print(self.PrintUi.empty_line())
            self.print_employee_schedule_table(printed_data, 15)
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("<Id> : See Employee's weekly schedule          A : Show Only Working Employees      S : Show Only Non-Working Employees"))
        elif working_notworking_all == "working":
            print(self.PrintUi.allign_left(f"List of Employees Working on {start_date.date()}:"))
            print(self.PrintUi.empty_line())
            self.print_employee_schedule_table(printed_data, 15)
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("<Id> : See Employee's weekly schedule          D : Show All Employees      S : Show Only Non-Working Employees"))
        else:
            print(self.PrintUi.allign_left(f"List of Employees Not Working on {start_date.date()}:"))
            print(self.PrintUi.empty_line())
            self.print_employee_schedule_table(printed_data, 15)
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("<Id> : See Employee's weekly schedule          A : Show Only Working Employees      D : Show All Employees"))
        print(self.PrintUi.allign_left("         0 : Back              00 : Change Day                n : See Yesterday             m : See Tomorrow"))
        print(self.PrintUi.end_line())

    def print_employee_schedule_table(self, printed_data, line_num):
        line_count = 0
        print(printed_data)
        while line_count != line_num:
            print(self.PrintUi.empty_line())
            line_count += 1

    def innitiate_and_switch_lists(self, start_date):
        return self.Logic.list_employees_working_and_destinations(start_date.strftime('%Y-%m-%d %H:%M'))
        #return self.Logic.object_list_to_dict_list(printed_data)

    def input_prompt(self):
        '''Starting function for AirplaneDataUI'''
        day_timedelta = datetime.timedelta(1)
        start_date = datetime.datetime(2024,1,15,0,0)
        working_notworking_all = "all"
        while True:
            printed_data = self.innitiate_and_switch_lists(start_date)
            self.employee_schedules_output(printed_data, start_date, working_notworking_all)
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
                pass
            elif command == "s": #show non-working employees
                pass
            elif command == "d": #show ALL employees
                pass
            elif command == "n": #see yesterday
                start_date = start_date - day_timedelta 
            elif command == "m": #see tomorrow
                start_date = start_date + day_timedelta
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")