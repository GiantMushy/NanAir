

class PrintFuncitons:
    def __init__(self):
        pass

    def empty_line(self):
        return "║                                                                                                                           ║"
    
    def end_line(self):
        return "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"

    def left_allign_text(self, text):
        text_len = len(text)
        return "║" + "   " + text + (" " * (120 - text_len)) + "║"
    
    def center_allign_text(self, text):
        text_len = len(text)
        side_spaces = (123 - text_len) * 0.5
        return "║" + (" " * side_spaces) + text + (" " * side_spaces) + "║"    

    def print_header(self, text, allignment):
        print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")#123
        str_length = len(text)
        if allignment == "center":
            side_spaces = (123 - str_length) * 0.5
            print_str = "█" + (" "*side_spaces) + text + (" "*side_spaces) + "█"
            print(print_str)
        elif allignment == "left":
            right_space = 120 - str_length
            print_str = "█" + "   " + text + (" " * right_space) + "█"
        elif allignment == "right":
            left_space = 121 - str_length
            print_str = "█" + (" " * left_space) + text + "  " + "█"
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
