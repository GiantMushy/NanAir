#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class FlightSchedulesUI:
    def __init__(self, user = ""):
        self.PrintUi = PrintFunctions()
        self.user = user

    def flight_schedules_output(self):
        start_date = "08.01.24"
        end_date = "14.01.24"
        self.PrintUi.logo()
        self.PrintUi.print_header(self.user + " > Flight Schedules", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"Flights Departing in the week of: {start_date} - {end_date}"))
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
        print(self.PrintUi.allign_left("<Nr> : Examine Staff Status of Trip                  S : Change Schedule Duration to 1 Day"))
        if self.user == "Trip Manager":
            print(self.PrintUi.allign_left("   D : Create New Trip                               F : Re-Create Existing Trip"))
        else:
            print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("0 : Back              00 : Change Week               n : Previous Week             m : Next Week"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        while True:
            self.flight_schedules_output()
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