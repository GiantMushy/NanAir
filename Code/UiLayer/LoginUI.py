#from logic_ui_wrapper import wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions
from Code.UiLayer.MainMenuUI import MainMenuUI

class LoginUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def login_output(self):
        '''Print sequence for Login'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Login", "center")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_center("1 : Trip Manager   "))
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
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Input 'q' at any time to exit the program"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for Login (And the whole program)'''
        while True:
            self.login_output()
            command = input("Enter your command: ")
            command = command.lower()

            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                main_menu = MainMenuUI("Trip Manager")
                main_menu.input_prompt()
            elif command == "2":
                main_menu = MainMenuUI("Human Resources")
                main_menu.input_prompt()
            else:
                print("Invalid input, try again")