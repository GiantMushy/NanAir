#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class DestinationDataEditUI:
    def __init__(self, Destination = []):
        self.PrintUi = PrintFunctions()
        #self.Destination = Destination
        self.Destination = ["Iceland", "Reykjavík", "Reykjavík Airport", "0", "0", "112"]

    def Destination_data_edit_output(self):
        '''Print sequence for editing Destination Data (initial)'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu > Edit > " + self.Destination[0], "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Destination Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"1 : Country               {self.Destination[0]}"))
        print(self.PrintUi.allign_left(f"2 : City                  {self.Destination[1]}"))
        print(self.PrintUi.allign_left(f"3 : Airport               {self.Destination[2]}"))
        print(self.PrintUi.allign_left(f"4 : Distance              {self.Destination[3]}km"))
        print(self.PrintUi.allign_left(f"5 : Travel Time           {self.Destination[4]}min."))
        print(self.PrintUi.allign_left(f"6 : Emergency Contact     {self.Destination[5]}"))
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
        '''Print sequence for editing Destination Data'''
        self.PrintUi.logo()
        self.PrintUi.print_header(f"Destination Database Menu > Edit > {self.Destination[0]} > {changed_data}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Destination Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Country               {self.Destination[0]}"))
        print(self.PrintUi.allign_left(f"    City                  {self.Destination[1]}"))
        print(self.PrintUi.allign_left(f"    Airport               {self.Destination[2]}"))
        print(self.PrintUi.allign_left(f"    Distance              {self.Destination[3]}km"))
        print(self.PrintUi.allign_left(f"    Travel Time           {self.Destination[4]}min."))
        print(self.PrintUi.allign_left(f"    Emergency Contact     {self.Destination[5]}"))
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
        '''Starting function for editing Destination Data'''
        while True:
            self.Destination_data_edit_output()
            command = input("Enter you command: ")            
            if command == "0":
                #-------------Send new Data to Logic-------------
                break
            elif command == "1":
                self.edit_data("Country")
                command = input("Input new Country: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                #----------------------Ask Logic if input is actual Country-------------------------
                self.Destination[0] = command
            elif command == "2":
                self.edit_data("City")
                command = input("Input new City: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                #----------------------Ask Logic if actual City-------------------------
                self.Destination[1] = command
            elif command == "3":
                self.edit_data("Airport")
                command = input("Input new Airport: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                #----------------------Ask Logic if actual Airport-------------------------
                self.Destination[2] = command
            elif command == "4":
                self.edit_data("Distance(km)")
                command = input("Input new Distance: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                #----------------------Ask Logic if actual Distance-------------------------
                self.Destination[3] = command
            elif command == "5":
                self.edit_data("Travel Time (min)")
                command = input("Input new Travel Time: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                #----------------------Ask Logic if actual Time-------------------------
                self.Destination[4] = command
            elif command == "6":
                self.edit_data("Emergency Contact")
                command = input("Input new Emergency Contact: ")
                if command == "q":
                    print("Goodbye")
                    exit()
                #----------------------Ask Logic if actual phone number/email-------------------------
                self.Destination[5] = command
            elif command == "q":
                exit()
            else:
                print("Invalid input, try again")