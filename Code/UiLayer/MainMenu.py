#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class MainMenu_UI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def menu_output(self):
        self.PrintUi.logo()
        self.PrintUi.print_header("Main Menu", "center")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("1 : Trip Manager"))
        print(self.PrintUi.allign_left("2 : Human Resources"))
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
        print(self.PrintUi.allign_left("*Hint: input the number you want to select and then enter"))
        print(self.PrintUi.allign_left(" For ex.: [1] --> Trip Manager"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.end_line())

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter you command: ")
            command = command.lower()

            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                pass
            elif command == "2":
                pass
            else:
                print("Invalid input, try again")