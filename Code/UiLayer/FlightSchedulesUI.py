#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class FlightSchedulesUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def airplane_data_output(self):
        self.PrintUi.logo()
        self.PrintUi.print_header("Flight Schedules", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"Flights Departing in the week of: {} - {}", "08.01.24", "14.01.24"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("------------Table goes here-------------"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("<Nr> : Examine Staff Status of Trip"))
        print(self.PrintUi.allign_left("   S : Change Schedule Duration to 1 Day"))
        print(self.PrintUi.allign_left("   D : Create New Trip"))
        print(self.PrintUi.allign_left("   F : Re-Create Existing Trip"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 0 : Back              00 : Change Week               n : Previous Week             m : Next Week"))
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