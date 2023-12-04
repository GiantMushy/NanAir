#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.MainMenuUI import MainMenuUI

class LoginUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def login_output(self):
        self.PrintUi.logo()
        self.PrintUi.print_header("Login", "center")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_center("1 : Trip Manager"))
        print(self.PrintUi.allign_center("2 : Human Resources"))
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
            self.login_output()
            command = input("Enter you command: ")
            command = command.lower()

            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                main_menu = MainMenuUI()
                main_menu.input_prompt()
            elif command == "2":
                main_menu = MainMenuUI()
                main_menu.input_prompt()
            else:
                print("Invalid input, try again")