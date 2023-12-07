from LogicLayer.LogicLayerAPI import LogicLayerAPI #Wrapper
from UiLayer.PrintFunctions import PrintFunctions

class AirplaneDataEditUI:
    def __init__(self, airplane_id = ""):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.airplane_id = airplane_id

    def airplane_data_edit_output(self):
        '''Print sequence for editing Airplane Data (initial)'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu > Edit > " + self.airplane['name'], "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Airplane Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"1 : Name                  {self.airplane['name']}"))
        print(self.PrintUi.allign_left(f"2 : Current Location      {self.airplane['current_location']}"))
        print(self.PrintUi.allign_left(f"3 : Type                  {self.airplane['type']}"))
        print(self.PrintUi.allign_left(f"4 : Manufacturer          {self.airplane['manufacturer']}"))
        print(self.PrintUi.allign_left(f"5 : Capacity              {self.airplane['capacity']}"))
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
        print(self.PrintUi.allign_left(" 0 : Back"))
        print(self.PrintUi.end_line())

    def edit_data(self, changed_data):
        '''Print sequence for editing Airplane Data'''
        self.PrintUi.logo()
        self.PrintUi.print_header(f"Airplane Database Menu > Edit > {self.airplane['name']} > {changed_data}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Airplane Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Name                  {self.airplane['name']}"))
        print(self.PrintUi.allign_left(f"    Current Location      {self.airplane['current_location']}"))
        print(self.PrintUi.allign_left(f"    Type                  {self.airplane['type']}"))
        print(self.PrintUi.allign_left(f"    Manufacturer          {self.airplane['manufacturer']}"))
        print(self.PrintUi.allign_left(f"    Capacity              {self.airplane['capacity']}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Input new {changed_data}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for editing Airplane Data'''
        while True:
            airplane_obj = self.Logic.find_airplane_by_id(self.airplane_id)
            self.airplane = self.Logic.object_to_dict(airplane_obj)
            self.airplane_data_edit_output()
            command = input("Enter you command: ")            

            if command == "0":
                #-------------Send new Data to Logic-------------
                break
            elif command == "1":
                self.edit_data("Name")
                command = input("Input new Name: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.modify_airplane(self.airplane['id'], name = command)
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "2":
                self.edit_data("Current Location")
                command = input("Input new Current Location: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.modify_airplane(self.airplane['id'], current_location = command)
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "3":
                self.edit_data("Type")
                command = input("Input new Type: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.modify_airplane(self.airplane['id'], type = command)
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "4":
                self.edit_data("Manufacturer")
                command = input("Input new Manufacturer: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.modify_airplane(self.airplane['id'], manufacturer = command)
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "5":
                self.edit_data("Seats")
                command = input("Input new seat ammount: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.modify_airplane(self.airplane['id'], capacity = command)
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")