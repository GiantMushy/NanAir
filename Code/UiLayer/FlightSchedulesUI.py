from LogicLayer.LogicLayerAPI import LogicLayerAPI
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.FlightSchedulesCreateNewUI import FlightSchedulesCreateNewUI
import datetime

class FlightSchedulesUI:
    def __init__(self, user = ""):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.user = user

    def flight_schedules_output(self, printed_data, start_date, end_date):
        self.PrintUi.logo()
        self.PrintUi.print_header(self.user + " > Flight Schedules", "left")
        print(self.PrintUi.empty_line())
        if not end_date:
            print(self.PrintUi.allign_left(f"Flights Departing on {start_date.date()}:"))
        else:
            print(self.PrintUi.allign_left(f"Flights Departing between {start_date.date()} - {end_date.date()}:"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_flight_schedule_table(printed_data, start_date, end_date, 12)
        print(self.PrintUi.empty_line())

        if self.user == "Trip Manager":
            print(self.PrintUi.allign_left("   A : Create New Trip"))
            print(self.PrintUi.allign_left("<ID> : Create Recurring Trip from ID          D : Change between Day/Week"))
        else:
            print(self.PrintUi.allign_left("   A : Create New Trip"))
            print(self.PrintUi.allign_left("<ID> : Examine Staff Status of Trip           D : Change between Day/Week"))
        print(self.PrintUi.empty_line())

        if not end_date:
            print(self.PrintUi.allign_left("0 : Back              00 : Change Day                n : See Yesterday             m : See Tomorrow"))
        else:
            print(self.PrintUi.allign_left("0 : Back              00 : Change Week               n : Previous Week             m : Next Week"))
        print(self.PrintUi.end_line())

    def innitiate_and_switch_lists(self, time, start_date,):
        temp_list_data = self.Logic.work_trip_validity_period(time, start_date.strftime('%Y-%m-%d %H:%M'))
        printed_data = self.Logic.object_list_to_dict_list(temp_list_data)
        return printed_data

    def input_prompt(self):
        '''Starting function for EmployeeDataUI'''
        time = 'weekly'
        #start_date = '2032-11-14 00:00'
        day_timedelta = datetime.timedelta(1)        
        week = datetime.timedelta(7)
        start_date = datetime.datetime(2032,11,14,0,0)
        end_date = start_date + week
        while True:
            printed_data = self.innitiate_and_switch_lists(time, start_date)
            self.flight_schedules_output(printed_data, start_date, end_date)
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "00": #change day/week
                input_check = False
                if time == 'weekly':
                    while not input_check:
                        try:
                            year, month, day = input("Enter the first day of the new week (YYYY-MM-DD): ").split('-')
                            input_check = True
                            start_date = datetime.datetime(int(year), int(month), int(day), 0,0)
                            end_date = start_date + week
                        except ValueError as e:
                            print(f"Error: {e}")
                            input_check = False
                else:
                    while not input_check:
                        try:
                            year, month, day = input("Enter a day (YYYY-MM-DD): ").split('-')
                            input_check = True
                            start_date = datetime.datetime(int(year), int(month), int(day), 0,0)
                        except ValueError as e:
                            print(f"Error: {e}")
                            input_check = False
            elif command.isdigit():
                for dict in printed_data:
                    if int(command) == int(dict["id"]):
                        if self.user == "Trip Manager": ########### Create Recurring Work Trip ############
                            input_check_recurring = False
                            while not input_check_recurring:
                                recurrence_count = input("Input number of recurring flights to be scheduled: ").lower()
                                if recurrence_count == "q":
                                    print("Goodbye")
                                    exit()
                                try:
                                    recurrence_count = int(recurrence_count)
                                    input_check_recurring = True
                                except ValueError as e:
                                    print(f"Error: {e}")
                                    input_check_recurring = False
                            input_check_recurring = False
                            while not input_check_recurring:
                                recurrence_days = input("Input the amount of days between recurring trips (daily = 1, weekly = 7, etc.): ").lower()
                                if recurrence_days == "q":
                                    print("Goodbye")
                                    exit()
                                try:
                                    recurrence_days = int(recurrence_days)
                                    input_check_recurring = True
                                except ValueError as e:
                                    print(f"Error: {e}")
                                    input_check_recurring = False
                            self.Logic.create_recurring_work_trips()

                        else:                        ############# Staff Trips #############
                            print("Staff Trips") 
                        #edit = FlightSchedulesStaffStatusUI(dict["id"])
                        #edit.input_prompt()

            elif command == "d": #change between week and day
                if time == 'weekly':
                    time = 'daily'
                    end_date = None
                else:
                    time = 'weekly'
                    end_date = start_date + week 
            elif command == "n": #see yesterday/last week
                if time == 'weekly':
                    start_date = start_date - week 
                    end_date = start_date - week 
                else:
                    start_date = start_date - day_timedelta 
            elif command == "m": #see tomorrow/next week
                if time == 'weekly':
                    start_date = start_date + week 
                    end_date = start_date + week 
                else:
                    start_date = start_date + day_timedelta
            elif command == "a":
                if self.user == 'Trip Manager':
                    create_new = FlightSchedulesCreateNewUI()
                    create_new.input_prompt()
            elif command == "s":
                if self.user == 'Trip Manager':
                    #re_create = FlightSchedulesReCreateUI()
                    #re_create.input_prompt()
                    print("Create existing trip")
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")