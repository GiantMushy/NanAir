from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI
from Code.UiLayer.PrintFunctions import PrintFunctions
import ast

#{'id': '007', 
# 'destination': "{'id': '02', 'city': 'Matta city', 'airport': 'Matti airport', 'country': 'Mattaland', 'distance': '6', 'travel_time': '40', 'contact_name': 'Helgi', 'contact_phone_number': '9876543'}", 
# 'departure_datetime': datetime.datetime(2024, 1, 15, 21, 53), 
# 'return_datetime': datetime.datetime(2024, 1, 16, 3, 53), 
# 'airplane': "{'id': '001', 'name': 'Katla', 'type': 'AKN-77'}", 
# 'flight_number_start': 'NA0210', 'flight_number_end': 'NA0211', 
# 'crew_members': "004,002"
# 'sold_tickets_start': '0', 
# 'sold_tickets_end': '0', 
# 'available_tickets_start': '300', 
# 'available_tickets_end': '300', 
# 'current_situation': 'Not started', 
# 'validity': True}

class FlightSchedulesStaffTripsUI:
    def __init__(self, trip = {}):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.trip = trip
        self.destination = ast.literal_eval(trip['destination']) #translates the stringed dictionary to a literal dictionary
        self.airplane = ast.literal_eval(trip['airplane'])

        self.crew_dicts = [{'id' : 'Not Staffed', 'name' : '', 'social_security_number' : ''},
                           {'id' : 'Not Staffed', 'name' : '', 'social_security_number' : ''},
                           {'id' : 'Not Staffed', 'name' : '', 'social_security_number' : ''}]
        if self.trip['crew_members'].split(',') == ['']: #createing list of already assigned crew members
            pass
        else:
            for employee_id in self.trip['crew_members'].split(','):
                if self.Logic.is_captain(employee_id):
                    self.crew_dicts[0] = self.Logic.object_to_dict(self.Logic.find_employee_by_id(employee_id))
                elif self.Logic.is_pilot(employee_id):
                    self.crew_dicts[1] = self.Logic.object_to_dict(self.Logic.find_employee_by_id(employee_id))
                elif self.Logic.is_senior_flight_attendant(employee_id):
                    self.crew_dicts[2] = self.Logic.object_to_dict(self.Logic.find_employee_by_id(employee_id))
                elif self.Logic.is_flight_attendant(employee_id):
                    self.crew_dicts.append(self.Logic.object_to_dict(self.Logic.find_employee_by_id(employee_id)))
                

    def show_staff_status(self):
        '''Print sequence for showing staff status'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Human Resources > Flight Schedules > Staff Trip {self.trip['id']}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.empty_line())
        print_format = "%-20s%-20s%-20s%-20s"
        print(self.PrintUi.allign_left(print_format % ("Captain:", self.crew_dicts[0]['id'], self.crew_dicts[0]['name'], self.crew_dicts[0]['social_security_number'])))
        print(self.PrintUi.allign_left(print_format % ("Co-Pilot:", self.crew_dicts[1]['id'], self.crew_dicts[1]['name'], self.crew_dicts[1]['social_security_number'])))
        print(self.PrintUi.allign_left(print_format % ("Sr. Flight Att.:", self.crew_dicts[2]['id'], self.crew_dicts[2]['name'], self.crew_dicts[2]['social_security_number'])))
        line_count = 0

        if len(self.crew_dicts) > 3:
            for n in range(len(self.crew_dicts)-3):
                print(self.PrintUi.allign_left(print_format % ("Flight Attendat:", self.crew_dicts[2+n]['id'], self.crew_dicts[2+n]['name'], self.crew_dicts[2+n]['social_security_number'])))
                line_count += 1

        while line_count != 10:
            print(self.PrintUi.empty_line())
            line_count += 1
        
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"A : Assign Captain to Trip                  S : Assign Co-Pilot to Trip")) 
        print(self.PrintUi.allign_left(f"D : Assign Sr. Flight Attendat to Trip      F : Assign Flight Attendat to Trip           0 : Back to Flight Schedules")) 
        print(self.PrintUi.end_line())

    def assign_captain(self):
        '''Print sequence for assigning captain to Trip'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            f"Human Resources > Flight Schedules > Staff Trip {self.trip['id']} > Captain", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.allign_left(f"Assign available Captain")) 
        print(self.PrintUi.empty_line())
        print_format = "%-4s%-20s%-20s"
        line_count = 0
        for n in range(len(self.available_captains)):
            print(self.PrintUi.allign_left(print_format % (f"{n+1} :", self.available_captains[0]['name'], f"({self.available_captains[0]['social_security_number']})")))
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
        print(self.PrintUi.allign_left(f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.allign_left(f"Assign available Co-Pilot")) 
        print(self.PrintUi.empty_line())
        print_format = "%-4s%-20s%-20s"
        line_count = 0
        for n in range(len(self.available_copilots)):
            print(self.PrintUi.allign_left(print_format % (f"{n+1} :", self.available_copilots[0]['name'], f"({self.available_copilots[0]['social_security_number']})")))
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
        print(self.PrintUi.allign_left(f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.allign_left(f"Assign available Senior Flight Attendant")) 
        print(self.PrintUi.empty_line())
        print_format = "%-4s%-20s%-20s"
        line_count = 0
        for n in range(len(self.available_senior_flight_attendants)):
            print(self.PrintUi.allign_left(print_format % (f"{n+1} :", self.available_senior_flight_attendants[0]['name'], f"({self.available_senior_flight_attendants[0]['social_security_number']})")))
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
            f"Human Resources > Flight Schedules > Staff Trip {self.trip['id']} > flight_attendants", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.allign_left(f"Assign available Flight Attendant")) 
        print(self.PrintUi.empty_line())
        print_format = "%-4s%-20s%-20s"
        line_count = 0
        for n in range(len(self.available_flight_attendants)):
            print(self.PrintUi.allign_left(print_format % (f"{n+1} :", self.available_flight_attendants[0]['name'], f"({self.available_flight_attendants[0]['social_security_number']})")))
            line_count += 1
        while line_count != 13:
            print(self.PrintUi.empty_line())
            line_count += 1
        
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"0 : Back")) 
        print(self.PrintUi.end_line())

    def innitiate_dict_lists(self):
        #self.trip = self.Logic.find_trip_by_id(self.trip['id'])
        available_employees = self.Logic.list_all_available_employees(self.trip['departure_datetime'].strftime('%Y-%m-%d %H:%M'))
        self.available_captains = []
        self.available_copilots = []
        self.available_senior_flight_attendants = []
        self.available_flight_attendants = []
        for employee in available_employees:
            if self.Logic.is_captain(employee):
                self.available_captains.append(self.Logic.object_to_dict(self.Logic.find_employee_by_id(employee)))
            elif self.Logic.is_pilot(employee):
                self.available_copilots.append(self.Logic.object_to_dict(self.Logic.find_employee_by_id(employee)))
            elif self.Logic.is_senior_flight_attendant(employee):
                self.available_senior_flight_attendants.append(self.Logic.object_to_dict(self.Logic.find_employee_by_id(employee)))
            elif self.Logic.is_flight_attendant(employee):
                self.available_flight_attendants.append(self.Logic.object_to_dict(self.Logic.find_employee_by_id(employee)))

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

            elif command == "a": #assign Captain
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

                        elif command.isdigit() and int(command) <= len(self.available_captains): #Checks if command is a valid int in range of the given list
                            try:
                                self.Logic.add_crew_member(self.trip['id'], self.available_captains[int(command)-1]['id'])
                                print(f"{self.available_captains[int(command)-1]['id']}:{self.available_captains[int(command)-1]['name']} has been added to the trip")
                                input_check = True
                            except ValueError as e:
                                print(f"Error occured when adding employee to the Trip: {e}")
                        else:
                            print("Incorrect input, try again")
                else:
                    print("No available Capatains during this time period")

            elif command == "s": #assign CoPilot
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

                        elif command.isdigit() and int(command) <= len(self.available_copilots): #Checks if command is a valid int and in range of the given list
                            try:
                                self.Logic.add_crew_member(self.trip['id'], self.available_copilots[int(command)-1]['id'])
                                print(f"{self.available_copilots[int(command)-1]['id']}:{self.available_copilots[int(command)-1]['name']} has been added to the trip")
                                input_check = True
                            except ValueError as e:
                                print(f"Error occured when adding employee to the Trip: {e}")
                        else:
                            print("Incorrect input, try again")
                else:
                    print("No available CoPilots during this time period")

            elif command == "d": #assign Sr. Flight Attendants
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

                        elif command.isdigit() and int(command) <= len(self.available_senior_flight_attendants): #Checks if command is a valid int in range of the given list
                            try:
                                self.Logic.add_crew_member(self.trip['id'], self.available_senior_flight_attendants[int(command)-1]['id'])
                                print(f"{self.available_senior_flight_attendants[int(command)-1]['id']}:{self.available_senior_flight_attendants[int(command)-1]['name']} has been added to the trip")
                                input_check = True
                            except ValueError as e:
                                print(f"Error occured when adding employee to the Trip: {e}")
                        else:
                            print("Incorrect input, try again")
                else:
                    print("No available Sr. Flight Attendants during this time period")

            elif command == "f": #assign Flight Attendants
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

                        elif command.isdigit() and int(command) <= len(self.available_flight_attendants): #Checks if command is a valid int in range of the given list
                            try:
                                self.Logic.add_crew_member(self.trip['id'], self.available_flight_attendants[int(command)-1]['id'])
                                print(f"{self.available_flight_attendants[int(command)-1]['id']}:{self.available_flight_attendants[int(command)-1]['name']} has been added to the trip")
                                input_check = True
                            except ValueError as e:
                                print(f"Error occured when adding employee to the Trip: {e}")
                        else:
                            print("Incorrect input, try again")
                else:
                    print("No available Flight Attendants during this time period")

            else:
                print("Invalid input, try again")
