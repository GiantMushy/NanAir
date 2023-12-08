from LogicLayer.LogicLayerAPI import LogicLayerAPI
from UiLayer.PrintFunctions import PrintFunctions

class FlightSchedulesUI:
    def __init__(self, user = ""):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.user = user

    def flight_schedules_output(self, printed_data, time_period):
        self.PrintUi.logo()
        self.PrintUi.print_header(self.user + " > Flight Schedules", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"Flights Departing {time_period}"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_flight_schedules_table(printed_data, 14)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        if self.user == "Trip Manager":
            print(self.PrintUi.allign_left("   A : Create New Trip                               S : Re-Create Existing Trip"))
        else:
            print(self.PrintUi.empty_line())
        if len(time_period) > 15:
            print(self.PrintUi.allign_left("<Nr> : Examine Staff Status of Trip                  D : Change Schedule Duration to 1 Day"))
        else:
            print(self.PrintUi.allign_left("<Nr> : Examine Staff Status of Trip                  D : Change Schedule Duration to Week"))
        print(self.PrintUi.empty_line())
        if len(time_period) > 15:
            print(self.PrintUi.allign_left("0 : Back              00 : Change Week               n : Previous Week             m : Next Week"))
        else:
            print(self.PrintUi.allign_left("0 : Back              00 : Change Day                n : See Yesterday             m : See Tomorrow"))
        print(self.PrintUi.end_line())

    def innitiate_and_switch_lists(self, time):
        temp_list_data = self.Logic.list_all_work_trips()
        return self.Logic.object_list_to_dict_list(temp_list_data)
        #if time == 'day':
        #elif time == 'week':
        #    return self.Logic.list_all_pilots()

    def input_prompt(self):
        '''Starting function for EmployeeDataUI'''
        time = 'week'
        time_period = {'week':"in the week of: 08.01.24 - 14.01.24",
                       'day':"on: 08.01.24"}
        while True:
            printed_data = self.innitiate_and_switch_lists(time)
            self.employee_data_output(printed_data, time_period[time])
            command = input("Enter you command: ").lower()         

            if command == "0":
                break
            elif command == "00": #change day/week
                if len(time_period[time]) > 15:
                    print("Change Week")
                else:
                    print("Change Day")
            elif command.isdigit():
                for dict in printed_data:
                    if int(command) == int(dict["id"]):
                        #edit = FlightSchedulesStaffStatusUI(dict["id"])
                        #edit.input_prompt()
                        print(f"gonna see staff status of {command}")

            elif command == "d": #change between week and day
                if len(time_period[time]) > 15:
                    time = 'day'
                else:
                    time = 'week'
            elif command == "n": #see yesterday/last week
                if len(time_period[time]) > 15:
                    print("See yesterday")
                else:
                    print("See Last Week")
            elif command == "m": #see tomorrow/next week
                if len(time_period[time]) > 15:
                    print("See Next Week")
                else:
                    print("See Tomorrow")
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