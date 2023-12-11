from LogicLayer.LogicLayerAPI import LogicLayerAPI
from UiLayer.PrintFunctions import PrintFunctions
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
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_departure_time(self):
        '''Print sequence for Creating a new trip : Departure Time'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Departing Time", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_trip[0]}"))
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
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_return_time(self):
        '''Print sequence for Creating a new trip : Return Time'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Input Return Time", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_trip[0]}"))
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
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_destination(self, printed_data):
        '''Print sequence for Creating a new trip : Destination'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Select Destination", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_trip[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left(
            "--> Select Destination from the list below:"))
        print(self.PrintUi.allign_left("    Plane"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.print_destinations(printed_data, 9))
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_plane(self, printed_data):
        '''Print sequence for Creating a new trip : Plane'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Select Plane", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_trip[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[3]}"))
        print(self.PrintUi.allign_left("--> Select a Plane from the list below"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.list_available_planes(printed_data, 9))
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def new_created(self):
        '''Print sequence when a new trip has been created'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Flight Schedules > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("New Trip Created:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"     Destination:    {self.new_trip[3]}"))
        print(self.PrintUi.allign_left(
            f"Day of Departure:    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(
            f"  Departure Time:    {self.new_trip[0]}"))
        print(self.PrintUi.allign_left(
            f"     Return Time:    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left(
            f"           Plane:    {self.new_trip[4]}"))
        print(self.PrintUi.allign_left(
            f"   Flight Number:    {self.new_trip[5]}"))
        print(self.PrintUi.allign_left(f"    Staff Status:    Not Staffed"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            " 1 : Remake trip (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Save and Create Another Trip"))
        print(self.PrintUi.allign_left(
            " 3 : Save and Return to the Flight Schedules"))
        print(self.PrintUi.allign_left(
            " 4 : Discard and Return to the Flight Schedules"))
        print(self.PrintUi.end_line())

    def create_new_sequence(self):
        n = 1
        input_check = True
        self.new_trip = ['', '', '', '']
        while n < 6:
            if n == 1:
                self.input_departure_day()
                data = input("Enter Departure Day: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    date_data = data.split('-')
                    test = datetime.date(int(date_data[0]), int(
                        date_data[1]), int(date_data[2]))
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 2:
                self.input_departure_time()
                data = input("Enter Departure Time: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    data = data.split(':')
                    departing_datetime = datetime.datetime(int(date_data[0]), int(
                        date_data[1]), int(date_data[2]), int(data[0]), int(data[1]))
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 3:
                self.input_return_time()
                data = input("Enter Return Time: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    data = data.split(':')
                    returning_datetime = datetime.datetime(int(date_data[0]), int(
                        date_data[1]), int(date_data[2]), int(data[0]), int(data[1]))
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 4:
                printed_data = self.Logic.list_all_destinations()
                printed_data = self.Logic.object_list_to_dict_list(
                    printed_data)
                self.input_destination(printed_data)

                data = input("Enter Destination selection: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    for dic in printed_data:
                        if int(data) == int(dic['id']):
                            destination = self.Logic.find_destination_by_id(
                                self, dic['id'])
                            input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 5:
                printed_data = self.Logic.list_all_available_airplanes()
                printed_data = self.Logic.object_list_to_dict_list(
                    printed_data)
                if len(printed_data) != 0:
                    self.input_plane(printed_data)
                    data = input("Enter Plane selection: ")
                    if data == "q":
                        print("Goodbye")
                        exit()
                    try:
                        for dic in printed_data:
                            if int(data) == int(dic['id']):
                                destination = self.Logic.find_airplane_by_id(
                                    self, dic['id'])
                                input_check = True
                    except ValueError as e:
                        print(f"Error: {e}")
                        input_check = False
                else:  # ERROR MESSAGE -----------------------------------------------
                    print("No Planes available during this time period")
                    print("1 : Start over")
                    print("2 : Go back to Flight Schedules")
                    command = input("Input Command:").lower()
                    if command == "q":
                        print("Goodbye")
                        exit()
                    elif command == '1':
                        input_check = 0
                    elif command == '2':
                        return 'break'

            if input_check:
                n += 1
            if input_check == 6:
                new_trip = [destination, departing_datetime,
                            returning_datetime, plane]
        return new_trip

    def input_prompt(self):
        '''Starting function for creating a new trip'''
        self.new_trip = self.create_new_sequence()
        while True:
            if self.new_trip == 'break':
                break
            self.new_created()
            command = input("Enter command: ")
            if command == "1":
                self.new_trip = []
                self.new_trip = self.create_new_sequence()
                if self.new_trip == 'break':
                    break
            elif command == "2":
                try:
                    self.Logic.add_work_trip(
                        destination=self.new_trip[0], departure_datetime=self.new_trip[1], return_datetime=self.new_trip[2])
                except ValueError as e:
                    print(f"Error: {e}")
                self.new_trip = []
                self.new_trip = self.create_new_sequence()
                if self.new_trip == 'break':
                    break
            elif command == "3":
                try:
                    self.Logic.add_work_trip(
                        destination=self.new_trip[0], departure_datetime=self.new_trip[1], return_datetime=self.new_trip[2])
                    break
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "4":
                break
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")
