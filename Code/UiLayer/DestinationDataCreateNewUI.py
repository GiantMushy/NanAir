#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class DestinationDataCreateNewUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.new_Destination = []

    def input_country(self):
        '''Print sequence for Creating a new Destination : Country'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Input Country", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("--> Input Country"))
        print(self.PrintUi.allign_left("    City"))
        print(self.PrintUi.allign_left("    Airport"))
        print(self.PrintUi.allign_left("    Distance"))
        print(self.PrintUi.allign_left("    Travel Time"))
        print(self.PrintUi.allign_left("    Emergency Contact"))
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

    def input_city(self):
        '''Print sequence for Creating a new Destination : City'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input City", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_Destination[0]}"))
        print(self.PrintUi.allign_left("--> Input City"))
        print(self.PrintUi.allign_left("    Airport"))
        print(self.PrintUi.allign_left("    Distance"))
        print(self.PrintUi.allign_left("    Travel Time"))
        print(self.PrintUi.allign_left("    Emergency Contact"))
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
        self.PrintUi.print_header("Destination Database Menu > Create New > Input Airport", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_Destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[1]}"))
        print(self.PrintUi.allign_left("--> Input Airport Name"))
        print(self.PrintUi.allign_left("    Distance"))
        print(self.PrintUi.allign_left("    Travel Time"))
        print(self.PrintUi.allign_left("    Emergency Contact"))
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

    def input_distance(self):
        '''Print sequence for Creating a new Destination : Distance'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Input Distance", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_Destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[2]}"))
        print(self.PrintUi.allign_left("--> Input Distance[km]"))
        print(self.PrintUi.allign_left("    Travel Time"))
        print(self.PrintUi.allign_left("    Emergency Contact"))
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

    def input_travel_time(self):
        '''Print sequence for Creating a new Destination : Travel Time'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Input Travel Time", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_Destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[3]}km"))
        print(self.PrintUi.allign_left("--> Input Travel Time(min)"))
        print(self.PrintUi.allign_left("    Emergency Contact"))
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

    def input_emerg_contact(self):
        '''Print sequence for Creating a new Destination : Emergency Contact'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Input Emergency Contact", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Destination"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_Destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[3]}km"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[4]}min"))
        print(self.PrintUi.allign_left("--> Input Emergency Contact"))
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
        '''Print sequence when a new Destination has been created'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("New Destination Created:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_Destination[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[3]}km"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[4]}min"))
        print(self.PrintUi.allign_left(f"    {self.new_Destination[5]}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 1 : Remake Destination (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Create Another Destination"))
        print(self.PrintUi.allign_left(" 0 : Return to the Destination Database Menu"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for creating a new Destination'''
        n = 1
        while n < 7:
            if n == 1:
                self.input_country()
                data = input("Enter Country: ")
                #------------Ask Logic if input actualy a Country--------------
            elif n == 2:
                self.input_city()
                data = input("Enter City: ")
                #------------Ask Logic if input actualy a valid city--------------
            elif n == 3:
                self.input_airport()
                data = input("Enter Airport Name: ")
                #------------Ask Logic if input actualy a valid Airport for city--------------
            elif n == 4:
                self.input_distance()
                data = input("Enter Distance: ")
                #------------Ask Logic if input actualy a Distance--------------
            elif n == 5:
                self.input_travel_time()
                data = input("Enter Travel Time: ")
                #------------Ask Logic if input actualy a realistic time--------------
            elif n == 6:
                self.input_emerg_contact()
                data = input("Enter Emergency Contact: ")
                #------------Ask Logic if input actualy a realistic phone number--------------
            self.new_Destination.append(data)
            n += 1
        
        while True:
            self.new_created()
            command = input("Enter command: ")
            if command == "0":
                #--------------------send data to Logic-----------------------
                ####-----NEEDS FIXING: Back doesnt always go to DestinationData after multiple Destination creations-----####
                break
            elif command == "1":
                self.new_Destination = []
                self.input_prompt()
            elif command == "2":
                #--------------------send data to Logic-----------------------
                self.new_Destination = []
                self.input_prompt()
            else:
                print("Invalid input, try again")