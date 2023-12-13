from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI  # Wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions

class AirplaneDataEditUI:
    def __init__(self, airplane_id=""):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.airplane_id = airplane_id

    def airplane_data_edit_output(self):
        '''Print sequence for editing Airplane Data (initial)'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Airplane Database Menu > Edit > " + self.PrintUi.auto_shorten_name(self.airplane['name'], 70), "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Airplane Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"1 : Name                  {self.PrintUi.auto_shorten_name(self.airplane['name'], 70)}"))
        print(self.PrintUi.allign_left(
            f"    Type                  {self.airplane['type']}"))
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
        print(self.PrintUi.allign_left(" 0 : Back"))
        print(self.PrintUi.end_line())

    def edit_data(self, changed_data):
        '''Print sequence for editing Airplane Data'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Airplane Database Menu > Edit > {self.PrintUi.auto_shorten_name(self.airplane['name'], 65)} > {changed_data}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Airplane Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    Name                  {self.PrintUi.auto_shorten_name(self.airplane['name'], 70)}"))

        print(self.PrintUi.allign_left(
            f"    Type                  {self.airplane['type']}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Input new {changed_data}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for editing Airplane Data'''
        while True:
            input_check = False
            airplane_obj = self.Logic.find_airplane_by_id(self.airplane_id)
            self.airplane = self.Logic.object_to_dict(airplane_obj)
            self.airplane_data_edit_output()
            command = input("Enter you command: ")

            if command == "0":
                # -------------Send new Data to Logic-------------
                break

            elif command == "1":
                self.edit_data("Name")
                while not input_check:
                    command = input("Input new Name: ").lower()
                    if command == "q":
                        print("Goodbye")
                        exit()
                    try:
                        self.Logic.is_name(command)
                        input_check = True
                        try:
                            self.Logic.modify_airplane(
                                self.airplane['id'], name=command)
                        except ValueError as e:
                            print(f"Error: {e}")
                    except ValueError as e:
                        print(f"Error: {e}")
                        input_check = False
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")
