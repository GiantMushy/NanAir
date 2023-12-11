from LogicLayer.LogicLayerAPI import LogicLayerAPI
from UiLayer.PrintFunctions import PrintFunctions
import datetime


class FlightSchedulesCreateRecurringUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.new_trip = []

    def input_departure_day(self):
        '''Print sequence for Creating a new trip : Departing Day'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Flight Schedules > Create New > Input Day of Departure", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("--> Input the First Day of Departure (YYYY-MM-DD)"))
        print(self.PrintUi.allign_left("    Departure Time"))
        print(self.PrintUi.allign_left("    Return Time"))
        print(self.PrintUi.allign_left("    Destination"))
        print(self.PrintUi.allign_left("    Plane"))
        print(self.PrintUi.allign_left("    Days between Trips"))
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
        print(self.PrintUi.end_line())

    def new_created(self):
        '''Print sequence when a new trip has been created'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Flight Schedules > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("New Trip Created:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"       Departure:    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(f"          Return:    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left(f"     Destination:    {self.new_trip[3]['city']}, {self.new_trip[3]['country']}"))
        print(self.PrintUi.allign_left(f"           Plane:    {self.new_trip[4]['id']}: {self.new_trip[4]['name']}, {self.new_trip[4]['type']}"))
        print(self.PrintUi.allign_left(f"      Recurrence:    {self.new_trip[5]} days"))
        print(self.PrintUi.allign_left(f"   Flight Number:    ---Flight Number Goes Here---"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 1 : Remake trip (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Save and Create Another Trip"))
        print(self.PrintUi.allign_left(" 3 : Save and Return to the Flight Schedules"))
        print(self.PrintUi.allign_left(" 4 : Discard and Return to the Flight Schedules"))
        print(self.PrintUi.end_line())

    def create_new_sequence(self):
        n = 1
        input_check = True
        self.new_trip = ['error0','error1','error2','error3', 'error4']
        while n < 7:
                
            if n == 5:
                printed_data = self.Logic.list_all_airplanes() #################### Breyta í list_available_airplanes() ###############################
                printed_data = self.Logic.object_list_to_dict_list(printed_data)
                input_check_planes = False

                if len(printed_data) != 0:
                    self.input_plane(printed_data)
                    data = input("Enter Plane selection: ").lower()
                    if data == "q":
                        print("Goodbye")
                        exit()
                    try:
                        for dic in printed_data:
                            if int(data) == int(dic['id']):
                                self.new_trip[4] = self.Logic.find_airplane_by_id(dic['id'])
                                self.new_trip[4] = self.Logic.object_to_dict(self.new_trip[4])
                                input_check = True
                                input_check_planes = True
                    except ValueError as e:
                        print(f"Error: {e}")
                        input_check = False
                    if not input_check_planes:
                        print("Invalid input, try again")
                        input_check = False
                else: # ERROR MESSAGE -----------------------------------------------
                    print("No Planes available during this time period")
                    print("1 : Start over")
                    print("2 : Go back to Flight Schedules")
                    command = input("Input Command:").lower()
                    if command == "q":
                        print("Goodbye")
                        exit()
                    elif command == '1':
                        self.new_trip = ['error0','error1','error2','error3']
                        input_check = True
                        n = 0
                    elif command == '2':
                        return 'break'

            elif n == 6:
                self.input_recurrence()
                data = input("Enter Days between Flights: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.new_trip[5] = int(data)
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            if input_check:
                n += 1
        return ''

    def input_prompt(self):
        '''Starting function for creating a new trip'''
        break_check = self.create_new_sequence()
        while True:
            if break_check == 'break':
                break
            self.new_created()
            command = input("Enter command: ")
            if command == "1":
                self.new_trip = []
                break_check = self.create_new_sequence()
                if break_check == 'break':
                    break
            elif command == "2":
                try:
                    self.Logic.add_work_trip(destination = self.new_trip[0], departure_datetime = self.new_trip[1], return_datetime = self.new_trip[2])
                    self.new_trip = []
                    break_check = self.create_new_sequence()
                except ValueError as e:
                    print(f"Work Trip save was unsuccessfull: {e}")
                if break_check == 'break':
                    break
            elif command == "3":
                try:
                    self.Logic.add_work_trip(destination = self.new_trip[0], departure_datetime = self.new_trip[1], return_datetime = self.new_trip[2])
                    break
                except ValueError as e:
                    print(f"Work Trip save was unsuccessfull: {e}")
            elif command == "4":
                break    
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")