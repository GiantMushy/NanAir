from LogicLayer.LogicLayerAPI import LogicLayerAPI #Wrapper
from UiLayer.PrintFunctions import PrintFunctions

class AirplaneDataCreateNewUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
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
        '''Print sequence for Creating a new Airplane : Capacity'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu > Create New > Input Capacity", "left")
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
        print(self.PrintUi.allign_left(" 1 : Remake Airplane (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Save and Create Another Airplane"))
        print(self.PrintUi.allign_left(" 3 : Save and Return to the Airplane Database Menu"))
        print(self.PrintUi.allign_left(" 4 : Discard and Return to the Airplane Database Menu"))
        print(self.PrintUi.end_line())

    def create_new_sequence(self):
        n = 1
        input_check = True
        while n < 6:
            if n == 1:
                self.input_name()
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

            elif n == 2:
                self.input_current_location()
                data = input("Enter Current Location: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_current_location(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 3:
                self.input_manufacturer()
                data = input("Enter Manufacturer: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_manufacturer(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 4:
                self.input_type()
                data = input("Enter Airplane Type: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_type(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

                
            elif n == 5:
                self.input_seats()
                data = input("Enter Capacity: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_capacity(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            if input_check:
                self.new_airplane.append(data)
                n += 1

    def input_prompt(self):
        '''Starting function for creating a new Airplane'''
        self.create_new_sequence()
        while True:
            self.new_created()
            command = input("Enter command: ")
            if command == "1":  #re=create
                self.new_airplane = []
                self.create_new_sequence()
            elif command == "2": #save and create new
                try:
                    self.Logic.add_airplane(name=self.new_airplane[0], current_location=self.new_airplane[1], type=self.new_airplane[2], manufacturer=self.new_airplane[3],
                                                capacity=self.new_airplane[4])
                    self.new_airplane = []
                    self.create_new_sequence()
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "3": #save and exit
                try:
                    self.Logic.add_airplane(name=self.new_airplane[0], current_location=self.new_airplane[1], type=self.new_airplane[2], manufacturer=self.new_airplane[3],
                                                capacity=self.new_airplane[4])
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