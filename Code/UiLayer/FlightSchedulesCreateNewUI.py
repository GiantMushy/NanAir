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
        self.PrintUi.print_header("Flight Schedules > Create New > Input Day of Departure", "left")
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
        self.PrintUi.print_header("Flight Schedules > Create New > Departing Time", "left")
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
        self.PrintUi.print_header("Flight Schedules > Create New > Input Return Time", "left")
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

    def input_destination(self):
        '''Print sequence for Creating a new trip : Destination'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Flight Schedules > Create New > Select Destination", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_trip[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left("--> Select Destination from the list below:"))
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

    def input_plane(self):
        '''Print sequence for Creating a new trip : Plane'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Flight Schedules > Create New > Select Plane", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_trip[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_trip[3]}"))
        print(self.PrintUi.allign_left("--> Select a Plane from the list below"))
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

    def new_created(self):
        '''Print sequence when a new trip has been created'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Flight Schedules > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("New Trip Created:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"     Destination:    {self.new_trip[3]}"))
        print(self.PrintUi.allign_left(f"Day of Departure:    {self.new_trip[1]}"))
        print(self.PrintUi.allign_left(f"  Departure Time:    {self.new_trip[0]}"))
        print(self.PrintUi.allign_left(f"     Return Time:    {self.new_trip[2]}"))
        print(self.PrintUi.allign_left(f"           Plane:    {self.new_trip[4]}"))
        print(self.PrintUi.allign_left(f"   Flight Number:    {self.new_trip[5]}"))
        print(self.PrintUi.allign_left(f"    Staff Status:    Not Staffed"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 1 : Remake trip (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Save and Create Another trip"))
        print(self.PrintUi.allign_left(" 3 : Save and Return to the Flight Schedules"))
        print(self.PrintUi.allign_left(" 4 : Discard and Return to the Flight Schedules"))
        print(self.PrintUi.end_line())

    def create_new_sequence(self):
        n = 1
        input_check = True
        while n < 6:
            if n == 1:
                self.input_departure_day()
                data = input("Enter trip Type: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_trip_type(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 2:
                self.input_departure_time()
                data = input("Enter trip Role: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_trip_role(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 3:
                self.input_return_time()
                data = input("Enter Name: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_name(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 4:
                self.input_destination()
                data = input("Enter Social Security Number: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_social_security_number(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                
            elif n == 5:
                self.input_plane()
                data = input("Enter Phone number: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_contact_phone_number(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            if input_check:
                self.new_trip.append(data)
                n += 1

    def input_prompt(self):
        '''Starting function for creating a new trip'''
        self.create_new_sequence()
        while True:
            self.new_created()
            command = input("Enter command: ")
            if command == "1":
                self.new_trip = []
                self.create_new_sequence()
            elif command == "2":
                try:
                    self.Logic.add_trip(self.new_trip[0], self.new_trip[1], name=self.new_trip[2], social_security_number=self.new_trip[3],
                                            mobile_phone_number=self.new_trip[4], address=self.new_trip[5], email_address=self.new_trip[6], home_phone_number=self.new_trip[7])
                except ValueError as e:
                    print(f"Error: {e}")
                self.new_trip = []
                self.create_new_sequence()
            elif command == "3":
                try:
                    self.Logic.add_trip(self.new_trip[0], self.new_trip[1], name=self.new_trip[2], social_security_number=self.new_trip[3],
                                            mobile_phone_number=self.new_trip[4], address=self.new_trip[5], email_address=self.new_trip[6], home_phone_number=self.new_trip[7])
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