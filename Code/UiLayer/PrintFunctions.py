class PrintFunctions:
    def __init__(self):
        pass

    def empty_line(self):
        return "║                                                                                                                           ║"
    
    def end_line(self):
        return "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"

    def allign_left(self, text):
        text_len = len(text)
        return "║" + "   " + text + (" " * (120 - text_len)) + "║"
    
    def allign_center(self, text):
        str_length = len(text)
        spaces = (123 - str_length)
        odd_even = spaces % 2
        left_spaces = (spaces - odd_even) * 0.5
        left_spaces = int(left_spaces)
        right_spaces = (spaces + odd_even) * 0.5
        right_spaces = int(right_spaces)
        return "║" + (" " * left_spaces) + text + (" " * right_spaces) + "║"   

    def print_header(self, text, allignment):
        print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")#123
        str_length = len(text)
        if allignment == "center":
            spaces = (123 - str_length)
            odd_even = spaces % 2
            left_spaces = (spaces - odd_even) * 0.5
            left_spaces = int(left_spaces)
            right_spaces = (spaces + odd_even) * 0.5
            right_spaces = int(right_spaces)
            print_str = "█" + (" " * left_spaces) + text + (" " * right_spaces) + "█"
        elif allignment == "left":
            right_space = 120 - str_length
            print_str = "█" + "   " + text + (" " * right_space) + "█"
        elif allignment == "right":
            left_space = 121 - str_length
            print_str = "█" + (" " * left_space) + text + "  " + "█"
        else:
            print_str = "Printing Error"
        print(print_str)
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

    def logo(self):
        print("                                                                  |                                   ")
        print("                                                                  |                                   ")
        print("                                                                  |                                   ")
        print("                                                                .-'-.                                 ")
        print("                                                               ' ___ '                                ")
        print("                                                     ---------'  .-.  '---------                      ")
        print("                                    \_________________________'  '-'  '_________________________/     ")
        print("                                      ''''''-|---|--/_\/_\==[]^',_m_,'^[]==/_\/_\--|---|-''''''       ")
        print("                                                    \ /\ /  ||/   H   \||  \ /\ /                     ")
        print("                                                     '--'   OO   O|O   OO   '--'                      ")
        print("                               ____  _____      __      ____  _____          __      _____ _______    ")
        print("                              |_   \|_   _|    /  \    |_   \|_   _|        /  \    |_   _|_   __ \   ")
        print("                                |   \ | |     / /\ \     |   \ | |         / /\ \     | |   | |__) |  ")
        print("                                | |\ \| |    / ____ \    | |\ \| |        / ____ \    | |   |  __ /   ")
        print("                               _| |_\   |_ _/ /    \ \_ _| |_\   |_     _/ /    \ \_ _| |_ _| |  \ \_ ")
        print("                              |_____|\____|____|  |____|_____|\____|   |____|  |____|_____|____| |___|")
        print("                                🅦 🅗 🅔 🅡 🅔  🅓 🅘 🅥 🅘 🅓 🅘 🅝 🅖  🅑 🅨  🅩 🅔 🅡 🅞  🅜 🅐 🅚 🅔 🅢  🅢 🅔 🅝 🅒 🅔")


#data = {'id': '001', 'name': 'Matti', 'social_security_number': '611563-4242', 'address': 'Mac street 1', 'mobile_phone_number': '6686453441', 'email_address': 'example71@gmail.com', 'home_phone_number': ''} 
# {'id': '002', 'name': 'Sara', 'social_security_number': '430730-9923', 'address': 'Microsoft street 1', 'mobile_phone_number': '1358799863', 'email_address': 'example55@gmail.com', 'home_phone_number': ''} 
# {'id': '003', 'name': 'Raggi', 'social_security_number': '164862-8280', 'address': 'AMZN street 1', 'mobile_phone_number': '9861589627', 'email_address': 'example38@gmail.com', 'home_phone_number': ''} 
# {'id': '004', 'name': 'Banani', 'social_security_number': '347784-3214', 'address': 'FB street 1', 'mobile_phone_number': '3550569113', 'email_address': 'example35@gmail.com', 'home_phone_number': ''} 
# {'id': '005', 'name': 'Epli', 'social_security_number': '628896-8506', 'address': 'Apple street 1', 'mobile_phone_number': '1002571434', 'email_address': 'example87@gmail.com', 'home_phone_number': ''}

    def print_table(self, data, line_num):
        print(data)