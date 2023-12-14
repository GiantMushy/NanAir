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
        print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")  # 123
        str_length = len(text)
        if allignment == "center":
            spaces = (123 - str_length)
            odd_even = spaces % 2
            left_spaces = (spaces - odd_even) * 0.5
            left_spaces = int(left_spaces)
            right_spaces = (spaces + odd_even) * 0.5
            right_spaces = int(right_spaces)
            print_str = "█" + (" " * left_spaces) + text + \
                (" " * right_spaces) + "█"
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
        print(
            "|_   \|_   _|    /  \    |_   \|_   _|        /  \    |_   _|_   __ \     = =(____AA____D")
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

    def auto_shorten_name(self, name, min_length):
        '''Abbreviates input name'''
        if len(name) > min_length:
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

        print(self.allign_left(print_format % ("ID", "Name", "SSN",
              "Address", "Mobile Phone", "Email", "Home Phone")))
        print(self.empty_line())
        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 20:  # shorten names
                    vals[n] = self.shorten_name(vals[n], 19)
            if vals[6] == '':
                # Empty Home Phone input prints "--Not Given--"
                vals[6] = "--Not Given--"
            print(self.allign_left(print_format % (
                vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6])))
            line_count += 1
        while line_count <= line_num:
            # fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1

    def print_airplane_type_table(self, data, line_num):
        line_count = 0
        print_format = "%-20s%-15s%-10s"

        print(self.allign_left(print_format %
              ("Type", "Manufacturer", "Capacity",)))
        print(self.empty_line())
        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 20:  # shorten names
                    vals[n] = self.shorten_name(vals[n], 19)
            print(self.allign_left(print_format % (
                vals[0], vals[1], vals[2])))
            line_count += 1
        while line_count <= line_num:
            # fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1

    def print_destination_table(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s%-20s%-12s%-15s%-15s%-0s"

        print(self.allign_left(print_format % ("ID", "City", "Airport",
              "Country", "Distance", "Travel Time", "Emerg. Name", "Emerg. Phone")))
        print(self.empty_line())
        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18:  # shorten names
                    vals[n] = self.shorten_name(vals[n], 18)
            time = f'{int(vals[5])//60}hrs {int(vals[5])%60}min'
            print(self.allign_left(print_format % (
                vals[0], vals[1], vals[2], vals[3], vals[4] + "km", time, vals[6], vals[7])))
            line_count += 1
        while line_count <= line_num:
            # fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1

    def print_airplane_table(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s%-10s%-20s%-20s%-0s"

        print(self.allign_left(print_format % ("ID", "Name",
              "Type", "Capacity", "Available Next", "Destination", "Flight Number")))
        print(self.empty_line())
        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18:  # shorten names
                    vals[n] = self.shorten_name(vals[n], 18)
            print(self.allign_left(print_format %
                  (vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6])))
            line_count += 1
        while line_count <= line_num:
            # fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1

    def print_flight_schedule_table(self, data, line_num):
        line_count = 0
        # Adjusted print format to include new fields
        print_format = "%-7s%-7s%-5s%-15s%-12s%-12s%-15s%-17s%-15s%-0s"

        # Print the header with new fields
        print(self.allign_left(print_format % ('Id', 'From', 'To', 'Date', 'Dep. Time',
              'Flight Nr.', 'Staff Status', 'Sold Tickets', 'Avail. Tickets', 'Situation')))
        print(self.empty_line())

        for dic in data:
            # Translates the stringed dictionary to a literal dictionary
            destination = ast.literal_eval(dic['destination'])

            # Determine staff status
            if dic['validity'] is True:
                staff_status = 'Staffed'
            else:
                staff_status = 'Not Staffed'

            # Print the flight details for start flight
            print(self.allign_left(print_format % (
                dic['id'],
                'RKV',
                destination['airport'],
                dic['departure_datetime'].date(),
                dic['departure_datetime'].time(),
                dic['flight_number_start'],
                staff_status,
                dic['sold_tickets_start'],
                dic['available_tickets_start'],
                dic['current_situation']
            )))

            # Print the flight details for return flight
            print(self.allign_left(print_format % (
                '',
                destination['airport'],
                'RKV',
                dic['return_datetime'].date(),
                dic['return_datetime'].time(),
                dic['flight_number_end'],
                staff_status,
                dic['sold_tickets_end'],
                dic['available_tickets_end'],
                "-*-"
            )))

            line_count += 1

        while line_count <= line_num:
            # Fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1

    def print_employee_schedule_table(self, data, line_num):
        pass

    def print_destinations(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s%-20s"

        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18:  # shorten names
                    vals[n] = self.shorten_name(vals[n], 18)
            print(self.allign_left(print_format %
                  (vals[0], vals[1], vals[3], vals[2])))
            line_count += 1

        while line_count <= line_num:
            # fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1

    def print_available_planes_bugged(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s%-20s"

        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18:  # shorten names
                    vals[n] = self.shorten_name(vals[n], 18)
            # id 0, name 1, type 3, capacity 5
            print(vals)
            print(self.allign_left(print_format %
                  (vals[0], vals[1], vals[3], vals[5])))
            line_count += 1

    def print_available_planes(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-20s%-20s"

        for dic in data:
            vals = []
            for value in dic.values():
                vals.append(value)
            for n in range(len(vals)):
                if len(vals[n]) > 18:  # shorten names
                    vals[n] = self.shorten_name(vals[n], 18)
            # id 0, name 1, type 2
            print(self.allign_left(print_format %
                  (vals[0], vals[1], vals[2])))
            line_count += 1

        while line_count <= line_num:
            # fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1

    def print_employee_table_detailed(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-25s%-15s%-25s%-20s%-0s"

        keys_to_print = ['id', 'name', 'social_security_number',
                         'address', 'mobile_phone_number', 'role']

        print(self.allign_left(print_format %
              ("ID", "Name", "SSN", "Address", "Phone Number", "Role")))
        print(self.empty_line())
        for dic in data:
            vals = []
            for key in keys_to_print:
                vals.append(dic[key])
            for n in range(len(vals)):
                if len(vals[n]) > 25:
                    vals[n] = self.shorten_name(vals[n], 18)
            print(self.allign_left(print_format % (
                vals[0], vals[1], vals[2], vals[3], vals[4], vals[5])))
            line_count += 1

        while line_count <= line_num:
            # fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1

    def print_pilots_table_detailed(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-25s%-15s%-25s%-15s%-15s%-0s"

        keys_to_print = ['id', 'name', 'social_security_number',
                         'address', 'mobile_phone_number', 'pilot_role', 'airplane_type']

        print(self.allign_left(print_format %
              ("ID", "Name", "SSN", "Address", "Phone Number", "Role", "Pilot License")))
        print(self.empty_line())
        for dic in data:
            vals = []
            for key in keys_to_print:
                vals.append(dic[key])
            for n in range(len(vals)):
                if len(vals[n]) > 25:
                    vals[n] = self.shorten_name(vals[n], 18)
            print(self.allign_left(print_format % (
                vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6])))
            line_count += 1

        while line_count <= line_num:
            # fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1

    def print_flight_attendants_table_detailed(self, data, line_num):
        line_count = 0
        print_format = "%-5s%-25s%-15s%-25s%-15s%-0s"

        keys_to_print = ['id', 'name', 'social_security_number',
                         'address', 'mobile_phone_number', 'attendant_role']

        print(self.allign_left(print_format %
                               ("ID", "Name", "SSN", "Address", "Phone Number", "Role")))
        print(self.empty_line())
        for dic in data:
            vals = []
            for key in keys_to_print:
                vals.append(dic[key])
            for n in range(len(vals)):
                if len(vals[n]) > 25:
                    vals[n] = self.shorten_name(vals[n], 18)
            print(self.allign_left(print_format % (
                vals[0], vals[1], vals[2], vals[3], vals[4], vals[5])))
            line_count += 1

        while line_count <= line_num:
            # fills out UI box to correct size with empty lines
            print(self.empty_line())
            line_count += 1
