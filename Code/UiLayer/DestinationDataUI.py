from LogicLayer.LogicLayerAPI import LogicLayerAPI #Wrapper
from UiLayer.PrintFunctions import PrintFunctions  #Print functions for the logo and stuff
from UiLayer.DestinationDataCreateNewUI import DestinationDataCreateNewUI
from UiLayer.DestinationDataEditUI import DestinationDataEditUI

class DestinationDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        
    def destination_data_output(self, printed_dict):
        '''Print sequence for the Destonation Data Menu'''

        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Destinations"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_destination_table(printed_dict, 15)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 0 : Back                     00 : Create New Destination"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for DestinationDataUI'''
        while True:
            temp_list_data = self.Logic.list_all_destinations()
            all_destination_data = self.Logic.object_list_to_dict_list(temp_list_data)
            self.destination_data_output(all_destination_data)
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "00":
                create_new = DestinationDataCreateNewUI()
                create_new.input_prompt()
            elif command == "q":
                exit()
            else:
                print("Invalid input, try again")