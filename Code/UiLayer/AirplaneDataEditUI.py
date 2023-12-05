#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class AirplaneDataEditUI:
    def __init__(self, Airplane = []):
        self.PrintUi = PrintFunctions()
        #self.Airplane = Airplane
        self.airplane = ["Edda", "Reykjavík", "Boeing", "747", "225"]

    def Airplane_data_edit_output(self):
        '''Print sequence for editing Airplane Data (initial)'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu > Edit > " + self.airplane[0], "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Airplane Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"1 : Name                  {self.Airplane[0]}"))
        print(self.PrintUi.allign_left(f"2 : Current Location      {self.Airplane[1]}"))
        print(self.PrintUi.allign_left(f"3 : Manufacturer          {self.Airplane[2]}"))
        print(self.PrintUi.allign_left(f"4 : Type                  {self.Airplane[3]}"))
        print(self.PrintUi.allign_left(f"5 : Seats                 {self.Airplane[4]}"))
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
        self.PrintUi.print_header(f"Airplane Database Menu > Edit > {self.Airplane[0]} > {changed_data}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Airplane Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Name                  {self.Airplane[0]}"))
        print(self.PrintUi.allign_left(f"    Current Location      {self.Airplane[1]}"))
        print(self.PrintUi.allign_left(f"    Manufacturer          {self.Airplane[2]}"))
        print(self.PrintUi.allign_left(f"    Type                  {self.Airplane[3]}"))
        print(self.PrintUi.allign_left(f"    Seats                 {self.Airplane[4]}"))
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
        print(self.PrintUi.allign_left(" 0 : Back"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for editing Airplane Data'''
        while True:
            self.Airplane_data_edit_output()
            command = input("Enter you command: ")            

            if command == "0":
                #-------------Send new Data to Logic-------------
                break
            elif command == "1":
                self.edit_data("Name")
                command = input("Input new Name: ")
                #----------------------Ask Logic if input is actual Name-------------------------
                self.Airplane[0] = command
            elif command == "2":
                self.edit_data("Current Location")
                command = input("Input new Current Location: ")
                #----------------------Ask Logic if actual Location-------------------------
                self.Airplane[1] = command
            elif command == "3":
                self.edit_data("Manufacturer")
                command = input("Input new Manufacturer: ")
                #----------------------Ask Logic if actual phone number-------------------------
                self.Airplane[2] = command
            elif command == "4":
                self.edit_data("Type")
                command = input("Input new Type: ")
                #----------------------Ask Logic if actual Address-------------------------
                self.Airplane[3] = command
            elif command == "5":
                self.edit_data("Seats")
                command = input("Input new seat ammount: ")
                #----------------------Ask Logic if actual email-------------------------
                self.Airplane[4] = command
            else:
                print("Invalid input, try again")