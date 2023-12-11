from LogicLayer.LogicLayerAPI import LogicLayerAPI #Wrapper
from UiLayer.PrintFunctions import PrintFunctions

class DestinationDataCreateNewUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.new_destination = []

    def input_city(self):
        '''Print sequence for Creating a new Destination : City'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > City", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("--> Input City"))
        print(self.PrintUi.allign_left("    Airport"))
        print(self.PrintUi.allign_left("    Country"))
        print(self.PrintUi.allign_left("    Distance"))
        print(self.PrintUi.allign_left("    Travel Time"))
        print(self.PrintUi.allign_left("    Emergency Contact Name"))
        print(self.PrintUi.allign_left("    Emergency Contact Phone Number"))
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

    def input_airport(self):
        '''Print sequence for Creating a new Destination : Airport'''
        self.PrintUi.logo()
        self.PrintUi.print_header("destination Database Menu > Create New > Airport", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_destination[0]}"))
        print(self.PrintUi.allign_left("--> Input Airport abbreviatons"))
        print(self.PrintUi.allign_left("    Country"))
        print(self.PrintUi.allign_left("    Distance"))
        print(self.PrintUi.allign_left("    Travel Time"))
        print(self.PrintUi.allign_left("    Emergency Contact Name"))
        print(self.PrintUi.allign_left("    Emergency Contact Phone Number"))
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

    def input_country(self):
        '''Print sequence for Creating a new Destination : Country'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Country", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[1]}"))
        print(self.PrintUi.allign_left("--> Input Country"))
        print(self.PrintUi.allign_left("    Distance"))
        print(self.PrintUi.allign_left("    Travel Time"))
        print(self.PrintUi.allign_left("    Emergency Contact Name"))
        print(self.PrintUi.allign_left("    Emergency Contact Phone Number"))
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

    def input_distance(self):
        '''Print sequence for Creating a new Destination : Distance'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Distance", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[2]}"))
        print(self.PrintUi.allign_left("--> Input Distance (km)"))
        print(self.PrintUi.allign_left("    Travel Time"))
        print(self.PrintUi.allign_left("    Emergency Contact Name"))
        print(self.PrintUi.allign_left("    Emergency Contact Phone Number"))
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

    def input_travel_time(self):
        '''Print sequence for Creating a new Destination : Travel Time'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Travel Time", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[3]}km"))
        print(self.PrintUi.allign_left("--> Input Travel Time (min)"))
        print(self.PrintUi.allign_left("    Emergency Contact Name"))
        print(self.PrintUi.allign_left("    Emergency Contact Phone Number"))
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

    def input_emerg_contact_name(self):
        '''Print sequence for Creating a new Destination : Emergency Contact Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Contact Name", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[3]}km"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[4]}min"))
        print(self.PrintUi.allign_left("--> Input the Emergency Contact's name"))
        print(self.PrintUi.allign_left("    Emergency Contact Phone Number"))
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

    def input_emerg_contact_phone_number(self):
        '''Print sequence for Creating a new Destination : Emergency Contact'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Emergency Contact", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[3]}km"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[4]}min"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[5]}"))
        print(self.PrintUi.allign_left("--> Input The Emergency Contact's phone number"))
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
        '''Print sequence when a new Destination has been created'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("New Destination Created:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[3]}km"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[4]}min"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[5]}"))
        print(self.PrintUi.allign_left(f"    {self.new_destination[6]}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 1 : Remake Destination (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Save and Create Another Destination"))
        print(self.PrintUi.allign_left(" 3 : Save and Return to the Destination Database Menu"))
        print(self.PrintUi.allign_left(" 4 : Discard and Return to the Destination Database Menu"))
        print(self.PrintUi.end_line())

    def create_new_sequence(self):
        n = 1
        input_check = True
        while n < 8:
            if n == 1:
                self.input_city()
                data = input("Enter City: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_city(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 2:
                self.input_airport()
                data = input("Enter Airport: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_airport(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 3:
                self.input_country()
                data = input("Enter Country: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_country(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 4:
                self.input_distance()
                data = input("Enter Distance: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_distance(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                
            elif n == 5:
                self.input_travel_time()
                data = input("Enter Travel Time: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_travel_time(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 6:
                self.input_emerg_contact_name()
                data = input("Enter Contact Name: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_contact_name(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 7:
                self.input_emerg_contact_phone_number()
                data = input("Enter Phone Number: ")
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
                self.new_destination.append(data)
                n += 1

    def input_prompt(self):
        '''Starting function for creating a new Destination'''
        self.create_new_sequence()
        while True:
            self.new_created()
            command = input("Enter command: ")
            if command == "1":  #re=create
                self.new_destination = []
                self.create_new_sequence()
            elif command == "2": #save and create new
                try:
                    self.Logic.add_destination(city=self.new_destination[0], airport=self.new_destination[1], country=self.new_destination[2], distance=self.new_destination[3],
                                                travel_time=self.new_destination[4], contact_name=self.new_destination[5], contact_phone_number=self.new_destination[6])
                    self.new_destination = []
                    self.create_new_sequence()
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "3": #save and exit
                try:
                    self.Logic.add_destination(city=self.new_destination[0], airport=self.new_destination[1], country=self.new_destination[2], distance=self.new_destination[3],
                                            travel_time=self.new_destination[4], contact_name=self.new_destination[5], contact_phone_number=self.new_destination[6])
                    break
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "4": #discard and exit
                break    
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")
