from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI
from Code.UiLayer.PrintFunctions import PrintFunctions
import ast


class FlightSchedulesStaffTripsUI:
    def __init__(self, trip_id=""):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.trip_id = trip_id

    def show_staff_status(self):
        '''Print sequence for showing staff status'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Human Resources > Flight Schedules > Staff Trip {self.trip['id']}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.empty_line())
        print_format = "%-20s%-20s%-20s%-20s"
        print(self.PrintUi.allign_left(print_format % (
            "Captain:", self.crew_dicts[0]['id'], self.crew_dicts[0]['name'], self.crew_dicts[0]['social_security_number'])))
        print(self.PrintUi.allign_left(print_format % (
            "Co-Pilot:", self.crew_dicts[1]['id'], self.crew_dicts[1]['name'], self.crew_dicts[1]['social_security_number'])))
        print(self.PrintUi.allign_left(print_format % ("Sr. Flight Att.:",
              self.crew_dicts[2]['id'], self.crew_dicts[2]['name'], self.crew_dicts[2]['social_security_number'])))
        line_count = 0

        if len(self.crew_dicts) > 3:
            for n in range(len(self.crew_dicts)-3):
                print(self.PrintUi.allign_left(print_format % ("Flight Attendant:",
                      self.crew_dicts[2+n]['id'], self.crew_dicts[2+n]['name'], self.crew_dicts[2+n]['social_security_number'])))
                line_count += 1

        while line_count != 10:
            print(self.PrintUi.empty_line())
            line_count += 1

        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"A : Assign Captain to Trip                  S : Assign Co-Pilot to Trip"))
        print(self.PrintUi.allign_left(
            f"D : Assign Sr. Flight Attendant to Trip      F : Assign Flight Attendant to Trip           0 : Back to Flight Schedules"))
        print(self.PrintUi.end_line())

    def assign_captain(self):
        '''Print sequence for assigning captain to Trip'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Human Resources > Flight Schedules > Staff Trip {self.trip['id']} > Captain", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.allign_left(f"Assign available Captain"))
        print(self.PrintUi.empty_line())
        print_format = "%-4s%-20s%-20s"
        line_count = 0
        for n in range(len(self.available_captains)):
            print(self.PrintUi.allign_left(print_format % (
                f"{n+1} :", self.available_captains[0]['name'], f"({self.available_captains[0]['social_security_number']})")))
            line_count += 1
        while line_count != 13:
            print(self.PrintUi.empty_line())
            line_count += 1

        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"0 : Back"))
        print(self.PrintUi.end_line())

    def assign_copilot(self):
        '''Print sequence for assigning copilot to Trip'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Human Resources > Flight Schedules > Staff Trip {self.trip['id']} > Copilot", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.allign_left(f"Assign available Co-Pilot"))
        print(self.PrintUi.empty_line())
        print_format = "%-4s%-20s%-20s"
        line_count = 0
        for n in range(len(self.available_copilots)):
            print(self.PrintUi.allign_left(print_format % (
                f"{n+1} :", self.available_copilots[0]['name'], f"({self.available_copilots[0]['social_security_number']})")))
            line_count += 1
        while line_count != 13:
            print(self.PrintUi.empty_line())
            line_count += 1

        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"0 : Back"))
        print(self.PrintUi.end_line())

    def assign_sr_flight_attendant(self):
        '''Print sequence for assigning Senior Flight Attendant to Trip'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Human Resources > Flight Schedules > Staff Trip {self.trip['id']}> Senior Flight Attendant", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.allign_left(
            f"Assign available Senior Flight Attendant"))
        print(self.PrintUi.empty_line())
        print_format = "%-4s%-20s%-20s"
        line_count = 0
        for n in range(len(self.available_senior_flight_attendants)):
            print(self.PrintUi.allign_left(print_format % (
                f"{n+1} :", self.available_senior_flight_attendants[0]['name'], f"({self.available_senior_flight_attendants[0]['social_security_number']})")))
            line_count += 1
        while line_count != 13:
            print(self.PrintUi.empty_line())
            line_count += 1

        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"0 : Back"))
        print(self.PrintUi.end_line())

    def assign_flight_attendant(self):
        '''Print sequence for assigning Flight Attendants to Trip'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Human Resources > Flight Schedules > Staff Trip {self.trip['id']} > Flight Attendants", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.allign_left(f"Assign available Flight Attendant"))
        print(self.PrintUi.empty_line())
        print_format = "%-4s%-20s%-20s"
        line_count = 0
        for n in range(len(self.available_flight_attendants)):
            print(self.PrintUi.allign_left(print_format % (
                f"{n+1} :", self.available_flight_attendants[0]['name'], f"({self.available_flight_attendants[0]['social_security_number']})")))
            line_count += 1
        while line_count != 13:
            print(self.PrintUi.empty_line())
            line_count += 1

        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"0 : Back"))
        print(self.PrintUi.end_line())

    def innitiate_dict_lists(self):
        '''Updates the data for each type of employee and their availability'''
        self.trip = self.Logic.object_to_dict(
            self.Logic.find_work_trip_by_id(self.trip_id))
        airplane = ast.literal_eval(self.trip['airplane'])

        self.innitiate_available_captains(airplane)
        self.innitiate_available_copilots(airplane)
        self.innitiate_available_sr_fa()
        self.innitiate_available_fa()
        self.innitiate_crew_dicts()

    def innitiate_available_captains(self, airplane):
        '''Updates the data for Captain availablity'''
        self.available_captains = self.Logic.object_list_to_dict_list(self.Logic.list_all_available_captains_by_type(
            airplane['type'], self.trip['departure_datetime'].strftime('%Y-%m-%d %H:%M')))

    def innitiate_available_copilots(self, airplane):
        '''Updates the data for Co-Pilot availablity'''
        self.available_copilots = self.Logic.object_list_to_dict_list(self.Logic.list_all_available_copilots_by_type(
            airplane['type'], self.trip['departure_datetime'].strftime('%Y-%m-%d %H:%M')))

    def innitiate_available_sr_fa(self):
        '''Updates the data for Senior Flight Attendant availablity'''
        self.available_senior_flight_attendants = self.Logic.list_all_available_senior_fa(
            self.trip['departure_datetime'].strftime('%Y-%m-%d %H:%M'))

    def innitiate_available_fa(self):
        '''Updates the data for Flight Attendant availablity'''
        self.available_flight_attendants = self.Logic.object_list_to_dict_list(self.Logic.list_all_available_fa(
            self.trip['departure_datetime'].strftime('%Y-%m-%d %H:%M')))

    def innitiate_crew_dicts(self):
        '''Updates the data for assigned staff for the given trip'''
        # translates the stringed dictionary to a literal dictionary
        self.destination = ast.literal_eval(self.trip['destination'])
        self.airplane = ast.literal_eval(self.trip['airplane'])

        self.crew_dicts = [{'id': 'Not Staffed', 'name': '', 'social_security_number': ''},
                           {'id': 'Not Staffed', 'name': '',
                               'social_security_number': ''},
                           {'id': 'Not Staffed', 'name': '', 'social_security_number': ''}]
        # createing list of already assigned crew members i 'crew_members' is not empty
        if self.trip['crew_members'].split(',') == ['']:
            pass
        else:
            for employee_id in self.trip['crew_members'].split(','):
                if self.Logic.is_captain(employee_id):
                    self.crew_dicts[0] = self.Logic.object_to_dict(
                        self.Logic.find_employee_by_id(employee_id))
                elif self.Logic.is_pilot(employee_id):
                    self.crew_dicts[1] = self.Logic.object_to_dict(
                        self.Logic.find_employee_by_id(employee_id))
                elif self.Logic.is_senior_flight_attendant(employee_id):
                    self.crew_dicts[2] = self.Logic.object_to_dict(
                        self.Logic.find_employee_by_id(employee_id))
                elif self.Logic.is_flight_attendant(employee_id):
                    self.crew_dicts.append(self.Logic.object_to_dict(
                        self.Logic.find_employee_by_id(employee_id)))

    def input_prompt(self):
        '''Starting function for Assigning Staff to Trips'''
        while True:
            self.innitiate_dict_lists()
            self.show_staff_status()
            command = input("Enter command: ").lower()
            if command == "q":
                print("Goodbye")
                exit()
            elif command == "0":
                break

            elif command == "a":  # assign Captain
                if len(self.available_captains) != 0:
                    self.assign_captain()
                    input_check = False
                    while not input_check:
                        command = input("Input selection: ")
                        if command == "q":
                            print("Goodbye")
                            exit()
                        elif command == "0":
                            input_check = True

                        # Checks if command is a valid int in range of the given list
                        elif command.isdigit() and int(command) <= len(self.available_captains):
                            try:
                                self.Logic.add_crew_member(
                                    self.trip['id'], self.available_captains[int(command)-1]['id'])
                                print(
                                    f"{self.available_captains[int(command)-1]['id']}:{self.available_captains[int(command)-1]['name']} has been added to the trip")
                                input_check = True
                            except ValueError as e:
                                print(
                                    f"Error occured when adding employee to the Trip: {e}")
                        else:
                            print("Incorrect input, try again")
                else:
                    print("No available Captains during this time period")

            elif command == "s":  # assign CoPilot
                if len(self.available_copilots) != 0:
                    self.assign_copilot()
                    input_check = False
                    while not input_check:
                        command = input("Input selection: ")
                        if command == "q":
                            print("Goodbye")
                            exit()
                        elif command == "0":
                            input_check = True

                        # Checks if command is a valid int and in range of the given list
                        elif command.isdigit() and int(command) <= len(self.available_copilots):
                            try:
                                self.Logic.add_crew_member(
                                    self.trip['id'], self.available_copilots[int(command)-1]['id'])
                                print(
                                    f"{self.available_copilots[int(command)-1]['id']}:{self.available_copilots[int(command)-1]['name']} has been added to the trip")
                                input_check = True
                            except ValueError as e:
                                print(
                                    f"Error occurred when adding employee to the Trip: {e}")
                        else:
                            print("Incorrect input, try again")
                else:
                    print("No available Co-Pilots during this time period")

            elif command == "d":  # assign Sr. Flight Attendants
                if len(self.available_senior_flight_attendants) != 0:
                    self.assign_sr_flight_attendant()
                    input_check = False
                    while not input_check:
                        command = input("Input selection: ")
                        if command == "q":
                            print("Goodbye")
                            exit()
                        elif command == "0":
                            input_check = True

                        # Checks if command is a valid int in range of the given list
                        elif command.isdigit() and int(command) <= len(self.available_senior_flight_attendants):
                            try:
                                self.Logic.add_crew_member(
                                    self.trip['id'], self.available_senior_flight_attendants[int(command)-1]['id'])
                                print(
                                    f"{self.available_senior_flight_attendants[int(command)-1]['id']}:{self.available_senior_flight_attendants[int(command)-1]['name']} has been added to the trip")
                                input_check = True
                            except ValueError as e:
                                print(
                                    f"Error occurred when adding employee to the Trip: {e}")
                        else:
                            print("Incorrect input, try again")
                else:
                    print("No available Sr. Flight Attendants during this time period")

            elif command == "f":  # assign Flight Attendants
                if len(self.available_flight_attendants) != 0:
                    self.assign_flight_attendant()
                    input_check = False
                    while not input_check:
                        command = input("Input selection: ")
                        if command == "q":
                            print("Goodbye")
                            exit()
                        elif command == "0":
                            input_check = True

                        # Checks if command is a valid int in range of the given list
                        elif command.isdigit() and int(command) <= len(self.available_flight_attendants):
                            try:
                                self.Logic.add_crew_member(
                                    self.trip['id'], self.available_flight_attendants[int(command)-1]['id'])
                                print(
                                    f"{self.available_flight_attendants[int(command)-1]['id']}:{self.available_flight_attendants[int(command)-1]['name']} has been added to the trip")
                                input_check = True
                            except ValueError as e:
                                print(
                                    f"Error occured when adding employee to the Trip: {e}")
                        else:
                            print("Incorrect input, try again")
                else:
                    print("No available Flight Attendants during this time period")

            else:
                print("Invalid input, try again")
