#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class AirplaneDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def airplane_data_output(self):
        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Airplanes"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("------------Table goes here-------------"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 0 : Back                     00 : Create New Airplane                  <Airplane number> : Edit Airplane Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        while True:
            self.airplane_data_output()
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