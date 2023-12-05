#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.DestinationDataCreateNewUI import DestinationDataCreateNewUI
from UiLayer.DestinationDataEditUI import DestinationDataEditUI

class DestinationDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        
    def destination_data_output(self):
        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Destinations"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("------------Table goes here-------------"))
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
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 0 : Back                     00 : Create New Destination                  <Destination number> : Edit Destination Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        while True:
            self.destination_data_output()
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "1":
                edit = DestinationDataEditUI([])
                edit.input_prompt()
            elif command == "00":
                create_new = DestinationDataCreateNewUI()
                create_new.input_prompt()
            else:
                print("Invalid input, try again")