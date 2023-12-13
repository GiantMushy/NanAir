from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI
from Code.UiLayer.PrintFunctions import PrintFunctions
import datetime


class FlightSchedulesCreateNewUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.new_trip = []

    def input_departure_day(self):
        '''Print sequence for Creating a new trip : Departing Day'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Input Day of Departure", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("--> Input Day of Departure (YYYY-MM-DD)"))
        print(self.PrintUi.allign_left("    Departure Time"))
        print(self.PrintUi.allign_left("    Return Time"))
        print(self.PrintUi.allign_left("    Destination"))
        print(self.PrintUi.allign_left("    Plane"))
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
        print(self.PrintUi.end_line())

    def input_departure_time(self,dep_day):
        '''Print sequence for Creating a new trip : Departure Time'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Departing Time", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {dep_day}"))
        print(self.PrintUi.allign_left("--> Departure Time (HH:MM)"))
        print(self.PrintUi.allign_left("    Return Time"))
        print(self.PrintUi.allign_left("    Destination"))
        print(self.PrintUi.allign_left("    Plane"))
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
        print(self.PrintUi.end_line())

    def input_return_time(self):
        '''Print sequence for Creating a new trip : Return Time'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Input Return Time", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left("--> Input Return Time (HH:MM)"))
        print(self.PrintUi.allign_left("    Destination"))
        print(self.PrintUi.allign_left("    Plane"))
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
        print(self.PrintUi.empty_line())
        print(self.PrintUi.end_line())

    def input_destination(self, printed_data):
        '''Print sequence for Creating a new trip : Destination'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Select Destination", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left(
            "--> Select Destination from the list below:"))
        print(self.PrintUi.allign_left("    Plane"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_destinations(printed_data,11)
        print(self.PrintUi.end_line())

    def input_plane(self, printed_data):
        '''Print sequence for Creating a new trip : Plane'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Select Plane", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[0]['city']}, {self.new_trip[0]['country']}"))
        print(self.PrintUi.allign_left("--> Select a Plane from the list below"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_available_planes(printed_data,11)
        print(self.PrintUi.end_line())

    def new_created(self):
        '''Print sequence when a new trip has been created'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("New Trip Created:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"       Departure:    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(f"          Return:    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left(f"     Destination:    {self.new_trip[0]['city']}, {self.new_trip[0]['country']}"))
        print(self.PrintUi.allign_left(f"           Plane:    {self.new_trip[3]['id']}: {self.new_trip[3]['name']}, {self.new_trip[3]['type']}"))
        print(self.PrintUi.allign_left(f"    Staff Status:    Not Staffed"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 1 : Remake trip (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Save and Create Another Trip"))
        print(self.PrintUi.allign_left(
            " 3 : Save and Return to the Flight Schedules"))
        print(self.PrintUi.allign_left(
            " 4 : Discard and Return to the Flight Schedules"))
        print(self.PrintUi.end_line())

    def create_new_sequence(self):
        n = 1
        input_check = True
        self.new_trip = ['error0','error1','error2','error3']
        while n < 6:
            if n == 1:
                self.input_departure_day()
                data = input("Enter Departure Day: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    date_data = data.split('-')
                    dep_day = datetime.date(int(date_data[0]), int(date_data[1]), int(date_data[2]))
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                except IndexError:
                    print("ERROR: Date must be input in the correct format (YYYY-MM-DD)")
                    input_check = False

            elif n == 2:
                self.input_departure_time(dep_day)
                data = input("Enter Departure Time: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    data = data.split(':')
                    self.new_trip[1] = str(datetime.datetime(int(date_data[0]), int(date_data[1]), int(date_data[2]), int(data[0]), int(data[1])))[0:-3] 
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                except IndexError:
                    print("ERROR: Time must be input in the correct format (HH:MM)")
                    input_check = False

            elif n == 3:
                self.input_return_time()
                data = input("Enter Return Time: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    data = data.split(':')
                    self.new_trip[2] = str(datetime.datetime(int(date_data[0]), int(date_data[1]), int(date_data[2]), int(data[0]), int(data[1])))[0:-3] 
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                except IndexError:
                    print("ERROR: Time must be input in the correct format (HH:MM)")
                    input_check = False

            elif n == 4:
                printed_data = self.Logic.list_all_destinations()
                printed_data = self.Logic.object_list_to_dict_list(
                    printed_data)
                self.input_destination(printed_data)
                input_check_destinations = False

                data = input("Enter Destination selection: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    for dic in printed_data:
                        if int(data) == int(dic['id']):
                            self.new_trip[0] = self.Logic.find_destination_by_id(dic['id'])
                            self.new_trip[0] = self.Logic.object_to_dict(self.new_trip[0])
                            input_check = True
                            input_check_destinations = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                if not input_check_destinations:
                    print("Invalid input, try again")
                    input_check = False
                
            elif n == 5:
                printed_data = self.Logic.list_all_airplanes() #################### Breyt í list_available_airplanes() ###############################
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
                                self.new_trip[3] = self.Logic.find_airplane_by_id(dic['id'])
                                self.new_trip[3] = self.Logic.object_to_dict(self.new_trip[3])
                                print(self.new_trip[3])
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
                        input_check = 0
                    elif command == '2':
                        return 'break'

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
                    destination=self.new_trip[0]['id']
                    departure_datetime=self.new_trip[1]
                    return_datetime=self.new_trip[2]
                    airplane = self.new_trip[3]['id']
                    self.Logic.add_work_trip(
                        destination, departure_datetime, 
                        return_datetime, airplane)
                    self.new_trip = []
                    break_check = self.create_new_sequence()
                except ValueError as e:
                    print(f"Work Trip save was unsuccessfull: {e}")
                if break_check == 'break':
                    break
            elif command == "3":
                try:
                    destination=self.new_trip[0]['id']
                    departure_datetime=self.new_trip[1]
                    return_datetime=self.new_trip[2]
                    airplane = self.new_trip[3]['id']
                    self.Logic.add_work_trip(
                        destination, departure_datetime, 
                        return_datetime, airplane)
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
