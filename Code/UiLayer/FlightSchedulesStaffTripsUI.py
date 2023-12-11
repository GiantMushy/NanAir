from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI
from Code.UiLayer.PrintFunctions import PrintFunctions
import ast
import datetime
#id,destination,departure_datetime,return_datetime,airplane,flight_number_start,flight_number_end,crew_members
#id = 001,
# destination = "{'id': '02', 'city': 'Matta city', 'airport': 'Matti airport', 'country': 'Mattaland', 'distance': '6', 'travel_time': '40', 'contact_name': 'Helgi', 'contact_phone_number': '9876543'}",
# dep_datetime = 2023-12-11 21:53,
# ret_datetime = 2023-12-12 03:53,
# airplane = "{'id': '001', 'name': 'Katla', 'type': 'AKN-77'}",
# flight_number_start = NA020,
# flight_number_end =   NA021,
# crew_members = "004,002"

class FlightSchedulesStaffTripsUI:
    def __init__(self, trip = {}):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.trip = trip
        self.destination = ast.literal_eval(trip['destination']) #translates the stringed dictionary to a literal dictionary
        self.airplane = ast.literal_eval(trip['airplane'])

        self.crew_members = trip['crew_members'].split(',')
        if self.crew_members[0] == '':
            self.crew_members[0] = "Not Staffed"
        while len(self.crew_members) < 3:
            self.crew_members.append("Not Staffed")

    def show_staff_status(self):
        '''Print sequence for showing staff status'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Human Resources > Flight Schedules > Staff Trip", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"Reykjavik > {self.destination['city']}  |  {self.trip['departure_datetime']} > {self.trip['return_datetime']}"))
        print(self.PrintUi.allign_left(f"Captain:                {self.crew_members[0]}"))
        print(self.PrintUi.allign_left(f"Co=Captain>:            {self.crew_members[1]}"))
        print(self.PrintUi.allign_left(f"Head Stewerdess:        {self.crew_members[2]}")) #14 empty lines
        if len(self.crew_members) > 3:
            line_count = 0
            for n in range(len(self.crew_members)):
                print(self.PrintUi.allign_left(f"Stewerdess:             {self.crew_members[n+2]}"))
                line_count += 1
            while line_count != 14:
                print(self.PrintUi.empty_line())
                line_count += 1
        print(self.PrintUi.end_line())

    def create_new_sequence(self):
        n = 1
        input_check = True
        self.new_trip = ['error0','error1','error2','error3']
        while n < 6:
            if n == 1:
                self.input_departure_day()
                data = input("Enter Departure Day: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    date_data = data.split('-')
                    dep_day = datetime.date(int(date_data[0]), int(date_data[1]), int(date_data[2]))
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                except IndexError:
                    print("ERROR: Date must be input in the correct format (YYYY-MM-DD)")
                    input_check = False

            elif n == 2:
                self.input_departure_time(dep_day)
                data = input("Enter Departure Time: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    data = data.split(':')
                    self.new_trip[1] = str(datetime.datetime(int(date_data[0]), int(date_data[1]), int(date_data[2]), int(data[0]), int(data[1])))[0:-3] 
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                except IndexError:
                    print("ERROR: Time must be input in the correct format (HH:MM)")
                    input_check = False

            elif n == 3:
                self.input_return_time()
                data = input("Enter Return Time: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    data = data.split(':')
                    self.new_trip[2] = str(datetime.datetime(int(date_data[0]), int(date_data[1]), int(date_data[2]), int(data[0]), int(data[1])))[0:-3] 
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                except IndexError:
                    print("ERROR: Time must be input in the correct format (HH:MM)")
                    input_check = False

            elif n == 4:
                printed_data = self.Logic.list_all_destinations()
                printed_data = self.Logic.object_list_to_dict_list(
                    printed_data)
                self.input_destination(printed_data)
                input_check_destinations = False

                data = input("Enter Destination selection: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    for dic in printed_data:
                        if int(data) == int(dic['id']):
                            self.new_trip[0] = self.Logic.find_destination_by_id(dic['id'])
                            self.new_trip[0] = self.Logic.object_to_dict(self.new_trip[0])
                            input_check = True
                            input_check_destinations = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                if not input_check_destinations:
                    print("Invalid input, try again")
                    input_check = False
                
            elif n == 5:
                printed_data = self.Logic.list_all_airplanes() #################### Breyt í list_available_airplanes() ###############################
                printed_data = self.Logic.object_list_to_dict_list(printed_data)
                input_check_planes = False
                if len(printed_data) != 0:
                    self.input_plane(printed_data)
                    data = input("Enter Plane selection: ").lower()
                    if data == "q":
                        print("Goodbye")
                        exit()
                    try:
                        for dic in printed_data:
                            if int(data) == int(dic['id']):
                                self.new_trip[3] = self.Logic.find_airplane_by_id(dic['id'])
                                self.new_trip[3] = self.Logic.object_to_dict(self.new_trip[3])
                                input_check = True
                                input_check_planes = True
                    except ValueError as e:
                        print(f"Error: {e}")
                        input_check = False
                    if not input_check_planes:
                        print("Invalid input, try again")
                        input_check = False
                else: # ERROR MESSAGE -----------------------------------------------
                    print("No Planes available during this time period")
                    print("1 : Start over")
                    print("2 : Go back to Flight Schedules")
                    command = input("Input Command:").lower()
                    if command == "q":
                        print("Goodbye")
                        exit()
                    elif command == '1':
                        self.new_trip = ['error0','error1','error2','error3']
                        input_check = 0
                    elif command == '2':
                        return 'break'

            if input_check:
                n += 1
        return ''

    def input_prompt(self):
        '''Starting function for creating a new trip'''
        break_check = self.create_new_sequence()
        while True:
            if break_check == 'break':
                break
            self.new_created()
            command = input("Enter command: ")
            if command == "1":
                self.new_trip = []
                break_check = self.create_new_sequence()
                if break_check == 'break':
                    break
            elif command == "2":
                try:
                    self.Logic.add_work_trip(destination = self.new_trip[0], departure_datetime = self.new_trip[1], return_datetime = self.new_trip[2])
                    self.new_trip = []
                    break_check = self.create_new_sequence()
                except ValueError as e:
                    print(f"Work Trip save was unsuccessfull: {e}")
                if break_check == 'break':
                    break
            elif command == "3":
                try:
                    self.Logic.add_work_trip(
                        destination=self.new_trip[0], departure_datetime=self.new_trip[1], return_datetime=self.new_trip[2])
                    break
                except ValueError as e:
                    print(f"Work Trip save was unsuccessfull: {e}")
            elif command == "4":
                break
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")
