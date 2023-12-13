# from logic_ui_wrapper import wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions
from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI


class DestinationDataEditUI:
    def __init__(self, destination_id=""):
        self.PrintUi = PrintFunctions()
        # self.Destination = Destination
        self.Logic = LogicLayerAPI()
        self.destination_id = destination_id

    def Destination_data_edit_output(self):
        '''Print sequence for editing Destination Data (initial)'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Destination Database Menu > Edit > " + self.Destination['id'], "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Destination Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    City                       {self.Destination['city']}"))
        print(self.PrintUi.allign_left(
            f"    Airport                    {self.Destination['airport']}"))
        print(self.PrintUi.allign_left(
            f"    Country                    {self.Destination['country']}"))
        print(self.PrintUi.allign_left(
            f"    Distance                   {self.Destination['distance']}km"))
        print(self.PrintUi.allign_left(
            f"    Travel Time                {int(self.Destination['travel_time'])//60}hrs {int(self.Destination['travel_time'])%60}min"))
        print(self.PrintUi.allign_left(
            f"6 : Emergency Contact          {self.Destination['contact_name']}"))
        print(self.PrintUi.allign_left(
            f"6 : Emergency Phone Number     {self.Destination['contact_phone_number']}"))
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
        print(self.PrintUi.allign_left(
            " 0 : Back      6 : Edit Emergency Contact and Phone"))
        print(self.PrintUi.end_line())

    def edit_data_emergency_name(self):
        '''Print sequence for editing Destination Data'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Destination Database Menu > Edit > {self.Destination['id']} > Emergency Contact", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Destination Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    City                       {self.Destination['city']}"))
        print(self.PrintUi.allign_left(
            f"    Airport                    {self.Destination['airport']}"))
        print(self.PrintUi.allign_left(
            f"    Country                    {self.Destination['country']}"))
        print(self.PrintUi.allign_left(
            f"    Distance                   {self.Destination['distance']}km"))
        print(self.PrintUi.allign_left(
            f"    Travel Time                {int(self.Destination['travel_time'])//60}hrs {int(self.Destination['travel_time'])%60}min"))
        print(self.PrintUi.allign_left(
            f"--> Emergency Contact          {self.Destination['contact_name']}"))
        print(self.PrintUi.allign_left(
            f"    Emergency Phone Number     {self.Destination['contact_phone_number']}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Input new Emergency Contact: "))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            " 0 : Back "))
        print(self.PrintUi.end_line())

    def edit_data_emergency_phone(self, current_contact):
        '''Print sequence for editing Destination Data'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Destination Database Menu > Edit > {self.Destination['id']} > Emergency Phone Number", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Destination Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    City                       {self.Destination['city']}"))
        print(self.PrintUi.allign_left(
            f"    Airport                    {self.Destination['airport']}"))
        print(self.PrintUi.allign_left(
            f"    Country                    {self.Destination['country']}"))
        print(self.PrintUi.allign_left(
            f"    Distance                   {self.Destination['distance']}km"))
        print(self.PrintUi.allign_left(
            f"    Travel Time                {int(self.Destination['travel_time'])//60}hrs {int(self.Destination['travel_time'])%60}min"))
        print(self.PrintUi.allign_left(
            f"    Emergency Contact          {current_contact}"))
        print(self.PrintUi.allign_left(
            f"--> Emergency Phone Number     {self.Destination['contact_phone_number']}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Input new Emergency Phone Number: "))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            " 0 : Back "))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for editing Destination Data'''
        while True:
            destination_obj = self.Logic.find_destination_by_id(
                self.destination_id)

            self.Destination = self.Logic.object_to_dict(destination_obj)
            print(self.Destination)
            self.Destination_data_edit_output()
            command = input("Enter you command: ").lower()
            if command == "0":
                break
            elif command == "6":
                self.edit_data_emergency_name()
                command_1 = input("Input new Emergency Contact: ")
                if command_1 == "0":
                    break
                self.edit_data_emergency_phone(command_1)
                command_2 = input("Input new Emergency Contact Phone Number: ")
                if command_2 == "0":
                    break
                # -------------Send new Data to Logic-------------
                try:
                    self.Logic.update_emergency_contact(
                        self.destination_id, command_1, command_2)
                except ValueError as e:
                    print("Error: ", e)

            elif command == "q":
                exit()
            else:
                print("Invalid input, try again")
