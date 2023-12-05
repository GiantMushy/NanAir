#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.DestinationDataCreateNewUI import DestinationDataCreateNewUI
from UiLayer.DestinationDataEditUI import DestinationDataEditUI

class DestinationDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        
    def destination_data_output(self):
        data = [{'id':'001', 'City': 'dj', 'Airport': 'ewd', 'Country': 'edewed', 'Distance': '23', 'Travel_Time': '32', 'Contact_Name': 'dse', 'Contact_Phone_Number': '2324233'},
        {'id':'002', 'City': 'frvt', 'Airport': 'fergtb', 'Country': 'ferg', 'Distance': '34', 'Travel_Time': '34', 'Contact_Name': 'dgerg', 'Contact_Phone_Number': '4443344'},
        {'id':'003', 'City': 'eihb', 'Airport': 'rfouhw', 'Country': 'tjou', 'Distance': '44', 'Travel_Time': '43', 'Contact_Name': 'fhbe', 'Contact_Phone_Number': '332'},
        {'id':'004', 'City': 'yugadw', 'Airport': 'est', 'Country': 'est', 'Distance': '46', 'Travel_Time': '64', 'Contact_Name': 'fhdserdth', 'Contact_Phone_Number': '4675457'},
        {'id':'005', 'City': 'edutfewf', 'Airport': 'ewfreq', 'Country': 'rewtyhg5w4eyt', 'Distance': '43', 'Travel_Time': '46', 'Contact_Name': 'trjhsdr', 'Contact_Phone_Number': '5454434'},
        {'id':'006', 'City': '3qefwiudsghfrwgh', 'Airport': 'thfjdstraterhtj', 'Country': 'tfjh', 'Distance': '45', 'Travel_Time': '34546', 'Contact_Name': 'fghdgg', 'Contact_Phone_Number': '5465543'},
        {'id':'007', 'City': 'hahha', 'Airport': 'eje', 'Country': 'feekj', 'Distance': '3', 'Travel_Time': 'ff', 'Contact_Name': 'ef', 'Contact_Phone_Number': 'efv'},
        {'id':'008', 'City': 'ferf', 'Airport': 'rfe', 'Country': 'rere', 'Distance': 'rf', 'Travel_Time': '3', 'Contact_Name': '3rdfc', 'Contact_Phone_Number': ''},
        {'id':'009', 'City': 'fdbh', 'Airport': 'htthh', 'Country': 'htthrth', 'Distance': 'htt', 'Travel_Time': '4', 'Contact_Name': 'tr', 'Contact_Phone_Number': 'grf'},
        {'id':'010', 'City': 'fewui', 'Airport': 'rgtfrgth', 'Country': 'rfgt', 'Distance': '565', 'Travel_Time': '76', 'Contact_Name': 'gfd', 'Contact_Phone_Number': '4332563'},
        {'id':'011', 'City': 'dcvfd', 'Airport': 'dcsvf', 'Country': 'dsvf', 'Distance': '345', 'Travel_Time': '456', 'Contact_Name': 'hnggdf', 'Contact_Phone_Number': '4355544'},
        {'id':'012', 'City': 'ygyugyu', 'Airport': 'jgyjgy', 'Country': 'vuyvy', 'Distance': '778', 'Travel_Time': '78987', 'Contact_Name': 'jgvgvjvhj', 'Contact_Phone_Number': '7898978'}]

        self.PrintUi.logo()
        self.PrintUi.print_header("Destination Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Destinations"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_destination_table(data, 15)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 0 : Back                     00 : Create New Destination                  <ID> : Edit Destination Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        while True:
            self.destination_data_output()
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "00":
                create_new = DestinationDataCreateNewUI()
                create_new.input_prompt()
            elif command == "1":
                edit = DestinationDataEditUI([])
                edit.input_prompt()
            else:
                print("Invalid input, try again")