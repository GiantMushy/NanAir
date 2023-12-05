#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.AirplaneDataCreateNewUI import AirplaneDataCreateNewUI
from UiLayer.AirplaneDataEditUI import AirplaneDataEditUI

class AirplaneDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def airplane_data_output(self):
        '''Print sequence for the Airplane Data Menu'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Airplanes"))
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
        print(self.PrintUi.allign_left(" 0 : Back                     00 : Create New Airplane                  <Airplane number> : Edit Airplane Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for AirplaneDataUI'''
        while True:
            self.airplane_data_output()
            command = input("Enter you command: ")            

            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                edit = AirplaneDataEditUI([]) #needs employee data input
                edit.input_prompt()
            elif command == "00":
                create_new = AirplaneDataCreateNewUI()
                create_new.input_prompt()
            else:
                print("Invalid input, try again")