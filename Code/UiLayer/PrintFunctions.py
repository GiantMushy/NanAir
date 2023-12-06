class PrintFunctions:
    def __init__(self):
        pass

    def empty_line(self):
        '''Returns the printable string of an empty line'''
        return "║                                                                                                                           ║"
    
    def end_line(self):
        '''Returns the printable string of the end line ui'''
        return "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"

    def allign_left(self, text):
        '''returns a printable string where the input text has been alligned on the left'''
        text_len = len(text)
        if text_len < 120:
            return "║" + "   " + text + (" " * (120 - text_len)) + "║"
        else:
            return "║" + "   " + text
    
    def allign_center(self, text):
        '''returns a printable string where the input text has been alligned in the center of the line'''
        str_length = len(text)
        spaces = (123 - str_length)
        odd_even = spaces % 2
        left_spaces = (spaces - odd_even) * 0.5
        left_spaces = int(left_spaces)
        right_spaces = (spaces + odd_even) * 0.5
        right_spaces = int(right_spaces)
        return "║" + (" " * left_spaces) + text + (" " * right_spaces) + "║"   

    def print_header(self, text, allignment):
        '''Prints the header of the interface'''
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
        '''Prints the Company Logo'''
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

    def shorten_name(self, name, min_length):
        '''Abbreviates input name'''
        names = name.split()
        if len(names) > 1:
            for n in range(len(names)-1):
                names[n+1] = names[n+1][0] + "."
        name = " ".join(names)

        if len(name) > min_length:
            name = name[0] + ". (Name Too Long)"
        return name

    def print_employee_table(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-15s%-20s%-15s%-25s%-0s"
        
        print(self.allign_left(print_format % ("ID", "Name", "SSN", "Address", "Mobile Phone", "Email", "Home Phone")))
        print(self.empty_line())
        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18: #shorten names
                    vals[n] = self.shorten_name(vals[n])
            if vals[6] == '':
                vals[6] = "--Not Given--" #Empty Home Phone input prints "--Not Given--"
            print(self.allign_left(print_format % (vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6])))
            line_count += 1
        while line_count <= line_num:
            print(self.empty_line()) #fills out UI box to correct size with empty lines
            line_count += 1

    def print_destination_table(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s%-20s%-12s%-15s%-15s%-0s"
        
        print(self.allign_left(print_format % ("ID", "City", "Airport", "Country", "Distance", "Travel Time", "Emerg. Name", "Emerg. Phone")))
        print(self.empty_line())
        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18: #shorten names
                    vals[n] = self.shorten_name(vals[n])
            print(self.allign_left(print_format % (vals[0], vals[1], vals[2], vals[3], vals[4] + "km", vals[5] + "min", vals[6], vals[7])))
            line_count += 1
        while line_count <= line_num:
            print(self.empty_line()) #fills out UI box to correct size with empty lines
            line_count += 1

    def print_airplane_table(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s%-15s%-20s%-0s"
        
        print(self.allign_left(print_format % ("ID", "City", "Current Location", "Type", "Manufacturer", "Capacity")))
        print(self.empty_line())
        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18: #shorten names
                    vals[n] = self.shorten_name(vals[n])
            print(self.allign_left(print_format % (vals[0], vals[1], vals[2], vals[3], vals[4], vals[5])))
            line_count += 1
        while line_count <= line_num:
            print(self.empty_line()) #fills out UI box to correct size with empty lines
            line_count += 1