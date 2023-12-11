import datetime
import ast

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

    def logo1(self):
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

    def logo2(self):
        '''Prints the Company Logo'''
        print(" ____  _____      __      ____  _____          __      _____ _______    ")
        print("|_   \|_   _|    /  \    |_   \|_   _|        /  \    |_   _|_   __ \   ")
        print("  |   \ | |     / /\ \     |   \ | |         / /\ \     | |   | |__) |  ")
        print("  | |\ \| |    / ____ \    | |\ \| |        / ____ \    | |   |  __ /   ")
        print(" _| |_\   |_ _/ /    \ \_ _| |_\   |_     _/ /    \ \_ _| |_ _| |  \ \_ ")
        print("|_____|\____|____|  |____|_____|\____|   |____|  |____|_____|____| |___|")
        print("🅦 🅗 🅔 🅡 🅔  🅓 🅘 🅥 🅘 🅓 🅘 🅝 🅖  🅑 🅨  🅩 🅔 🅡 🅞  🅜 🅐 🅚 🅔 🅢  🅢 🅔 🅝 🅒 🅔")

    def logo(self):
        '''Prints the Company Logo'''
        print("                                                                              ______ ")
        print(" ____  _____      __      ____  _____          __      _____ _______          _\ _~-\___")
        print("|_   \|_   _|    /  \    |_   \|_   _|        /  \    |_   _|_   __ \     = =(____AA____D")
        print("  |   \ | |     / /\ \     |   \ | |         / /\ \     | |   | |__) |            \_____\______________________,-~~~~~-.._")
        print("  | |\ \| |    / ____ \    | |\ \| |        / ____ \    | |   |  __ /             /     o O o o o o O O o o o o o o O o  |\_")
        print(" _| |_\   |_ _/ /    \ \_ _| |_\   |_     _/ /    \ \_ _| |_ _| |  \ \_           `~-.__        ___..----..                  )")
        print("|_____|\____|____|  |____|_____|\____|   |____|  |____|_____|____| |___|                `---~~\___________/------------`````")
        print("                                                                                        =  ===(_________D")
        print("🅦 🅗 🅔 🅡 🅔  🅓 🅘 🅥 🅘 🅓 🅘 🅝 🅖  🅑 🅨  🅩 🅔 🅡 🅞  🅜 🅐 🅚 🅔 🅢  🅢 🅔 🅝 🅒 🅔")

    def shorten_name(self, name, min_length):
        '''Abbreviates input name'''
        names = name.split()
        if len(names) > 1:
            for n in range(len(names)-1):
                names[n+1] = names[n+1][0] + "."
        name = "".join(names)

        if len(name) > min_length:
            name = "(Item Too Long)"
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
                if len(vals[n]) > 20: #shorten names
                    vals[n] = self.shorten_name(vals[n], 19)
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
                    vals[n] = self.shorten_name(vals[n], 18)
            time = f'{int(vals[5])//60}hrs {int(vals[5])%60}min'
            print(self.allign_left(print_format % (vals[0], vals[1], vals[2], vals[3], vals[4] + "km", time, vals[6], vals[7])))
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
                    vals[n] = self.shorten_name(vals[n], 18)
            print(self.allign_left(print_format % (vals[0], vals[1], vals[2], vals[3], vals[4], vals[5])))
            line_count += 1
        while line_count <= line_num:
            print(self.empty_line()) #fills out UI box to correct size with empty lines
            line_count += 1

    def print_flight_schedule_table(self, data, date_start, date_end, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s%-15s%-15s%-15s%-15s%-0s"
        
        print(self.allign_left(print_format % ('Id','Departing','Destination','Date','Time','Plane','Flight Nr.','Staff Status')))
        print(self.empty_line())
        for dic in data:
            destination = ast.literal_eval(dic['destination']) #translates the stringed dictionary to a literal dictionary
            vals = []
            for value in dic.values():
                vals.append(value)
            if not dic['crew_members']:
                staff_status = 'Not Staffed'
            elif len(dic['crew_members']) < 8:
                staff_status = 'Not Staffed'
            else:
                staff_status = 'Staffed'
            print(self.allign_left(print_format % (dic['id'], 'Reykjavik', destination['country'], 
                                                   dic['departure_datetime'].date(), dic['departure_datetime'].time(),
                                                   "plane", 'NA040', staff_status)))
            print(self.allign_left(print_format % ( '', destination['country'], 'Reykjavik', 
                                                   dic['return_datetime'].date(), dic['return_datetime'].time(),
                                                   "plane", 'NA041', staff_status)))
            line_count += 1
        while line_count <= line_num:
            print(self.empty_line()) #fills out UI box to correct size with empty lines
            line_count += 1

    def print_employee_schedule_table(self,data,line_num):
        pass

    def print_destinations(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s%-20s"

        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18: #shorten names
                    vals[n] = self.shorten_name(vals[n], 18)
            print(self.allign_left(print_format % (vals[0], vals[1], vals[3], vals[2])))
            line_count += 1
        
        while line_count <= line_num:
            print(self.empty_line()) #fills out UI box to correct size with empty lines
            line_count += 1

    def print_available_planes(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s%-20s"

        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18: #shorten names
                    vals[n] = self.shorten_name(vals[n], 18)
            print(self.allign_left(print_format % (vals[0], vals[1], vals[3], vals[5]))) #id 0, name 1, type 3, capacity 5
            line_count += 1
        
        while line_count <= line_num:
            print(self.empty_line()) #fills out UI box to correct size with empty lines
            line_count += 1