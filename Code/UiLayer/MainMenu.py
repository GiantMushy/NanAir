#from logic_ui_wrapper import wrapper

class NanAirUi:
    def __init__(self):
        #self.nan_logic = NanLogic()
        pass

    def main_menu(self):
        NanAirUi.print_header("Main Menu", "middle")
        print("║                                                               ║")
        print("║   1 : Trip Manager                                            ║")
        print("║   2 : Human Resources                                         ║")
        print("║                                                               ║")
        print("║   *Hint: input the number you want to select and then enter   ║")
        print("║    For ex.: 1 --> Trip Manager                                ║")
        print("╚═══════════════════════════════════════════════════════════════╝")
    
    def print_header(self, text, allignment):
        print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        str_length = len(text)
        if allignment == "middle":
            side_spaces = (63 - str_length) * 0.5
            print_str = "█" + (" "*side_spaces) + text + (" "*side_spaces) + "█"
            print(print_str)
        elif allignment == "left":
            right_space = 60 - str_length
            print_str = "█" + "   " + text + (" " * right_space) + "█"
        elif allignment == "right":
            left_space = 61 - str_length
            print_str = "█" + (" " * left_space) + text + "  " + "█"
        #print("█                                                               █")#63 spaces
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

Nan = NanAirUi

Nan.main_menu()
    