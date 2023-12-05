#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.AirplaneDataCreateNewUI import AirplaneDataCreateNewUI
from UiLayer.AirplaneDataEditUI import AirplaneDataEditUI

class AirplaneDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def airplane_data_output(self):
        '''Print sequence for the Airplane Data Menu'''
        data = [{'id' : '001', 'Name Of Airlpaine': 'Oliver', 'Current Location': 'Nuuk', 'Type': 'DHC-8-200', 'Manufacturer': 'De Havilland', 'Capacity': '37'},
                {'id' : '002', 'Name Of Airplaine': 'Matthías', 'Current Location': '> Reykjavík', 'Type': 'DHC-8-400', 'Manufacturer': 'De Havilland', 'Capacity': '76'},
                {'id' : '003', 'Name Of Airplaine': 'Þorvarður', 'Current Location': 'Kulisuuk', 'Type': 'DHC-8-200', 'Manufacturer': 'De Havilland', 'Capacity': '37'},
                {'id' : '004', 'Name Of Airplaine': 'Benjamín', 'Current Location': 'Svalbard', 'Type': 'DHC-8-400', 'Manufacturer': 'De Havilland', 'Capacity': '76'},
                {'id' : '005', 'Name Of Airplaine': 'Edda', 'Current Location': '> Nuuk', 'Type': 'DHC-8-200', 'Manufacturer': 'De Havilland', 'Capacity': '37'}]

        self.PrintUi.logo()
        self.PrintUi.print_header("Airplane Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Airplanes"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_airplane_table(data, 15)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 0 : Back                     00 : Create New Airplane                  <ID> : Edit Airplane Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for AirplaneDataUI'''
        while True:
            self.airplane_data_output()
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "1":
                edit = AirplaneDataEditUI([]) #needs employee data input
                edit.input_prompt()
            elif command == "00":
                create_new = AirplaneDataCreateNewUI()
                create_new.input_prompt()
            else:
                print("Invalid input, try again")