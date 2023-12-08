from LogicLayer.LogicLayerAPI import LogicLayerAPI
from UiLayer.PrintFunctions import PrintFunctions

class FlightSchedulesUI:
    def __init__(self, user = ""):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.user = user

    def flight_schedules_output(self, printed_data, date_start, date_end):
        self.PrintUi.logo()
        self.PrintUi.print_header(self.user + " > Flight Schedules", "left")
        print(self.PrintUi.empty_line())
        if not date_end:
            print(self.PrintUi.allign_left(f"Flights Departing on {date_start}:"))
        else:
            print(self.PrintUi.allign_left(f"Flights Departing between {date_start} - {date_end}:"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_flight_schedule_table(printed_data, date_start, date_end, 12)
        print(self.PrintUi.empty_line())
        if self.user == "Trip Manager":
            print(self.PrintUi.allign_left("   A : Create New Trip                               S : Re-Create Existing Trip"))
        else:
            print(self.PrintUi.empty_line())
        if not date_end:
            print(self.PrintUi.allign_left("<Nr> : Examine Staff Status of Trip                  D : Change Schedule Duration to Week"))
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("0 : Back              00 : Change Day                n : See Yesterday             m : See Tomorrow"))
        else:
            print(self.PrintUi.allign_left("<Nr> : Examine Staff Status of Trip                  D : Change Schedule Duration to 1 Day"))
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_left("0 : Back              00 : Change Week               n : Previous Week             m : Next Week"))
        print(self.PrintUi.end_line())

    def innitiate_and_switch_lists(self, time, start_date,):
        temp_list_data = self.Logic.work_trip_validity_period(time, start_date)
        printed_data = self.Logic.object_list_to_dict_list(temp_list_data)
        return printed_data
        #if time == 'day':
        #elif time == 'week':
        #    return self.Logic.list_all_pilots()

    def input_prompt(self):
        '''Starting function for EmployeeDataUI'''
        time = 'weekly'
        date_start = '2032-11-14 00:00'
        date_end = '2032-11-20 00:00'
        while True:
            printed_data = self.innitiate_and_switch_lists(time, date_start)
            self.flight_schedules_output(printed_data, date_start, date_end)
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "00": #change day/week
                pass
            elif command.isdigit():
                for dict in printed_data:
                    if int(command) == int(dict["id"]):
                        #edit = FlightSchedulesStaffStatusUI(dict["id"])
                        #edit.input_prompt()
                        print(f"gonna see staff status of {command}")

            elif command == "d": #change between week and day
                if time == 'weekly':
                    time = 'daily'
                    date_end = None
                else:
                    time = 'weekly'
                    date_end = f'{date_start[0:5]}-{date_start[5:7]}-{int(date_start[8:10])+7} {date_start[10:]}'
            elif command == "n": #see yesterday/last week
                if time == 'weekly':
                    date_start = f'{date_start[0:5]}-{date_start[5:7]}-{int(date_start[8:10])-7} {date_start[10:]}'
                    date_end = f'{date_start[0:5]}-{date_start[5:7]}-{int(date_start[8:10])+7} {date_start[10:]}'
                else:
                    date_start = f'{date_start[0:5]}-{date_start[5:7]}-{int(date_start[8:10])-1} {date_start[10:]}'
            elif command == "m": #see tomorrow/next week
                if time == 'weekly':
                    date_start = f'{date_start[0:5]}-{date_start[5:7]}-{int(date_start[8:10])+7} {date_start[10:]}'
                    date_end = f'{date_start[0:5]}-{date_start[5:7]}-{int(date_start[8:10])+7} {date_start[10:]}'
                else:
                    date_start = f'{date_start[0:5]}-{date_start[5:7]}-{int(date_start[8:10])+1} {date_start[10:]}'
            elif command == "a":
                if self.user == 'Trip Manager':
                    #create_new = FlightSchedulesCreateNewUI()
                    #create_new.input_prompt()
                    print("Create New")
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