from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI  # Wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions
import datetime
from datetime import date
import ast

class EmployeeScheduleSpecificUI:
    def __init__(self, id = "", start_date = ""):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.id = id
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.start_date = start_date

    def specific_employee_weekly_schedule(self, destinations_list):
        '''Print sequence for the Airplane Data Menu'''
        print_format = "%-17s%-16s%-16s%-16s%-16s%-16s%-16s%-0s"
        days = self.get_days_list(self.start_date)
        weekday = self.get_weekday_list(self.start_date)

        self.PrintUi.logo()
        self.PrintUi.print_header(f"Employee Schedules > {self.id}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"Employee {self.id}'s weekly schedule, starting from {str(self.start_date)[0:10]}:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(' ________________________________________________________________________________________________________________'))
        print(self.PrintUi.allign_left(print_format % (f"|{weekday[0]} {days[0]}", 
                                                       f"{weekday[1]} {days[1]}",
                                                       f"{weekday[2]} {days[2]}",
                                                       f"{weekday[3]} {days[3]}",
                                                       f"{weekday[4]} {days[4]}",
                                                       f"{weekday[5]} {days[5]}",
                                                       f"{weekday[6]} {days[6]}",
                                                       "|")))
        print(self.PrintUi.allign_left(print_format % (f"|{destinations_list[0]}", 
                                                       f"{destinations_list[1]}",
                                                       f"{destinations_list[2]}",
                                                       f"{destinations_list[3]}",
                                                       f"{destinations_list[4]}",
                                                       f"{destinations_list[5]}",
                                                       f"{destinations_list[6]}",
                                                       "|")))
        print(self.PrintUi.allign_left('|________________________________________________________________________________________________________________|'))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_center(
            "0 : Back To Employee Schedules         00 : Change Week          n : Previous Week            m : Next Week"))
        print(self.PrintUi.end_line())

    def get_days_list(self, start_date):
        days = []
        for n in range(7):
            days.append(str(start_date)[8:10])
            start_date += datetime.timedelta(1)
        return days
    
    def get_weekday_list(self, start_date):
        weekday = []
        for n in range(7):
            weekday_num = date.weekday(start_date) #Returns 0 for monday, 1 for tuesday .... 6 for sunday
            weekday.append(self.weekdays[weekday_num])
            start_date += datetime.timedelta(1)
        return weekday

    def get_destination_list(self, print_data, start_date):
        destinations_list = []
        days = []
        for n in range(7):
            days.append(start_date)
            start_date += datetime.timedelta(1)
        for day in days:
            append_check = False
            for dict in print_data:
                destination = ast.literal_eval(dict['destination'])
                if str(dict['departure_datetime'])[0:10] == str(day)[0:10] and not append_check:
                    destinations_list.append(destination['city'])
                    append_check = True
                elif str(dict['return_datetime'])[0:10] == str(day)[0:10] and not append_check:
                    destinations_list.append('Reykjavik')
                    append_check = True
            if not append_check:
                destinations_list.append('Not Working')
        return destinations_list

    def input_prompt(self):
        '''Starting function for EmployeeScheduleSpecificUI''' 
        while True:
            print_data = self.Logic.all_work_trips_of_employee(self.id, self.start_date.strftime('%Y-%m-%d %H:%M'))
            print_data = self.Logic.object_list_to_dict_list(print_data)
            destinations_list = self.get_destination_list(print_data, self.start_date)
            self.specific_employee_weekly_schedule(destinations_list)
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "q":
                print("Goodbye")
                exit()
            elif command == "00": #change week
                input_check = False
                while not input_check:
                    try:
                        command = input("Enter the first day of the new week (YYYY-MM-DD): ")
                        if command.lower() == "q":
                            print("Goodbye")
                            exit()
                        year, month, day = command.split('-')
                        input_check = True
                        self.start_date = datetime.datetime(int(year), int(month), int(day), 0,0)
                    except ValueError as e:
                        print(f"Error in input: {e}")
                        input_check = False
            elif command == "n": #see last week
                self.start_date -= datetime.timedelta(7)
            elif command == "m": #see next week
                self.start_date += datetime.timedelta(7)
            else:
                print("Invalid input, try again")
