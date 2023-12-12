from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI  # Wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions
from Code.UiLayer.AirplaneDataCreateNewUI import AirplaneDataCreateNewUI
from Code.UiLayer.AirplaneDataEditUI import AirplaneDataEditUI


class AirplaneDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()

    def airplane_data_output(self, printed_dict):
        '''Print sequence for the Airplane Data Menu'''

        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Airplanes"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_airplane_table(printed_dict, 15)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            " 0 : Back                          00 : Create New Airplane                  <ID> : Edit Airplane Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for AirplaneDataUI'''
        while True:
            temp_list_data = self.Logic.list_airplanes_detailed()
            all_airplane_data = self.Logic.object_list_to_dict_list(
                temp_list_data)
            self.airplane_data_output(all_airplane_data)
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "00":
                create_new = AirplaneDataCreateNewUI()
                create_new.input_prompt()
            elif command.isdigit():
                for dict in all_airplane_data:
                    if int(command) == int(dict['id']):
                        edit = AirplaneDataEditUI(dict['id'])
                        edit.input_prompt()
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")
