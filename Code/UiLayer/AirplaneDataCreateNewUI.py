#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class AirplaneDataCreateNewUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.new_airplane = []

    def input_name(self):
        '''Print sequence for Creating a new Airplane : Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu > Create New > Input Name", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Airplane"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("--> Input Name"))
        print(self.PrintUi.allign_left("    Current Location"))
        print(self.PrintUi.allign_left("    Manufacturer"))
        print(self.PrintUi.allign_left("    Type"))
        print(self.PrintUi.allign_left("    Seats"))
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
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_current_location(self):
        '''Print sequence for Creating a new Airplane : Current Location'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Current Location", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Airplane"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_airplane[0]}"))
        print(self.PrintUi.allign_left("--> Input Current Location"))
        print(self.PrintUi.allign_left("    Manufacturer"))
        print(self.PrintUi.allign_left("    Type"))
        print(self.PrintUi.allign_left("    Seats"))
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

    def input_manufacturer(self):
        '''Print sequence for Creating a new Airplane : Manufacturer'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu > Create New > Input Manufacturer", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Airplane"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_airplane[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[1]}"))
        print(self.PrintUi.allign_left("--> Input Manufacturer"))
        print(self.PrintUi.allign_left("    Type"))
        print(self.PrintUi.allign_left("    Seats"))
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
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_type(self):
        '''Print sequence for Creating a new Airplane : Type'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu > Create New > Input Type", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Airplane"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_airplane[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[2]}"))
        print(self.PrintUi.allign_left("--> Input Type"))
        print(self.PrintUi.allign_left("    Seats"))
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

    def input_seats(self):
        '''Print sequence for Creating a new Airplane : Seats'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu > Create New > Input Seats", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Airplane"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_airplane[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[3]}"))
        print(self.PrintUi.allign_left("--> Input Number of seats"))
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
        '''Print sequence when a new Airplane has been created'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("New Airplane Created:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_airplane[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[3]}"))
        print(self.PrintUi.allign_left(f"    {self.new_airplane[4]}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 1 : Remake Airplane (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Create Another Airplane"))
        print(self.PrintUi.allign_left(" 0 : Return to the Airplane Database Menu"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for creating a new Airplane'''
        n = 1
        while n < 6:
            if n == 1:
                self.input_name()
                data = input("Enter Name: ")
                #------------Ask Logic if input actualy a name--------------
            elif n == 2:
                self.input_manufacturer()
                data = input("Enter Current Location: ")
                #------------Ask Logic if input actualy a valid Location--------------
            elif n == 3:
                self.input_manufacturer()
                data = input("Enter Manufacturer: ")
                #------------Ask Logic if input actualy a valid Manufacturer--------------
            elif n == 4:
                self.input_type()
                data = input("Enter Type: ")
                #------------Ask Logic if input actualy an Airplane type--------------
            elif n == 5:
                self.input_seats()
                data = input("Enter Seats: ")
                #------------Ask Logic if input actualy a realistic seat number--------------
            self.new_airplane.append(data)
            n += 1
        
        while True:
            self.new_created()
            command = input("Enter command: ")
            if command == "0":
                #--------------------send data to Logic-----------------------
                ####-----NEEDS FIXING: Back doesnt always go to AirplaneData after multiple Airplane creations-----####
                break
            elif command == "1":
                self.new_airplane = []
                self.input_prompt()
            elif command == "2":
                #--------------------send data to Logic-----------------------
                self.new_airplane = []
                self.input_prompt()
            else:
                print("Invalid input, try again")