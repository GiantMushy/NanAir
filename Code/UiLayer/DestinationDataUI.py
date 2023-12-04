#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class DestinationDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def airplane_data_output(self):
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Destinations"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("------------Table goes here-------------"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 0 : Back                     00 : Create New Destination                  <Destination number> : Edit Destination Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        while True:
            self.destination_data_output()
            command = input("Enter you command: ")            

            if command == "q":
                print("Goodbye")
                break
            elif command == "0":
                pass
            elif command == "00":
                pass
            else:
                print("Invalid input, try again")