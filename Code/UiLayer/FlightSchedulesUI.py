from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI
from Code.UiLayer.PrintFunctions import PrintFunctions
from Code.UiLayer.FlightSchedulesCreateNewUI import FlightSchedulesCreateNewUI
from Code.UiLayer.FlightSchedulesStaffTripsUI import FlightSchedulesStaffTripsUI
import datetime


class FlightSchedulesUI:
    def __init__(self, user=""):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.user = user

    def flight_schedules_output(self, printed_data, start_date, end_date):
        '''Prints the Flight Schedule Table'''
        self.PrintUi.logo()
        self.PrintUi.print_header(self.user + " > Flight Schedules", "left")
        print(self.PrintUi.empty_line())
        if not end_date:
            print(self.PrintUi.allign_left(
                f"Flights Departing on {start_date.date()}:"))
        else:
            print(self.PrintUi.allign_left(
                f"Flights Departing between {start_date.date()} - {end_date.date()}:"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_flight_schedule_table(printed_data, 12)
        print(self.PrintUi.empty_line())

        if self.user == "Trip Manager":
            print(self.PrintUi.allign_left("   A : Create New Trip"))
            print(self.PrintUi.allign_left(
                "<Id> : Create Recurring Trip from ID     D : Change between Day/Week      <Flight Nr.-X> : Add X tickets to flight "))
        else:
            print(self.PrintUi.empty_line())
            print(self.PrintUi.allign_center(
                "<ID> : Staff Trip           D : Change between Day/Week"))
        print(self.PrintUi.empty_line())

        if not end_date:
            print(self.PrintUi.allign_center(
                "0 : Back              00 : Change Day                n : See Yesterday             m : See Tomorrow"))
        else:
            print(self.PrintUi.allign_center(
                "0 : Back              00 : Change Week               n : Previous Week             m : Next Week"))
        print(self.PrintUi.end_line())

    def innitiate_and_switch_lists(self, time, start_date,):
        '''Updates the data for given start date and time period (time == 'week' or time == 'day')'''
        printed_data = self.Logic.work_trip_validity_period(
            time, start_date.strftime('%Y-%m-%d %H:%M'))
        return self.Logic.object_list_to_dict_list(printed_data)

    def input_prompt(self):
        '''Starting function for FlightSchedulesUI'''
        time = 'weekly'
        week = datetime.timedelta(6)
        start_date = datetime.datetime.now()
        end_date = start_date + week
        while True:
            printed_data = self.innitiate_and_switch_lists(time, start_date)
            self.flight_schedules_output(printed_data, start_date, end_date)
            command = input("Enter your command: ").lower()
            
            if command == "0":
                break
            elif command == "00":  # change day/week
                start_date = self.PrintUi.change_date()
                if time == 'weekly':
                    end_date = start_date + week
            elif command.isdigit():
                for dict in printed_data:
                    if int(command) == int(dict["id"]):
                        if self.user == "Trip Manager":  # Create Recurring Work Trip ############
                            input_check = False
                            while not input_check:
                                input_check_secondary = False
                                while not input_check_secondary:
                                    recurrence_count = input(
                                        "Input number of recurring flights to be scheduled ( [0] : back ): ").lower()
                                    if recurrence_count == "q":
                                        print("Goodbye")
                                        exit()
                                    elif recurrence_count == "0":
                                        input_check = True
                                        break
                                    try:
                                        recurrence_count = int(recurrence_count)
                                        input_check_secondary = True
                                    except ValueError as e:
                                        print(f"Error: {e}")
                                if input_check:
                                    break
                                input_check_secondary = False
                                while not input_check_secondary:
                                    recurrence_days = input(
                                        "Input the amount of days between recurring trips (daily = 1, weekly = 7, etc.)...( [0] : back ): ").lower()
                                    if recurrence_days == "q":
                                        print("Goodbye")
                                        exit()
                                    elif recurrence_count == "0":
                                        input_check = True
                                        break
                                    try:
                                        recurrence_days = int(recurrence_days)
                                        input_check_secondary = True
                                    except ValueError as e:
                                        print(f"Error: {e}")
                                if input_check:
                                    break
                                try:
                                    self.Logic.create_recurring_work_trips(
                                        dict['id'], recurrence_days, recurrence_count)
                                    input_check = True
                                except ValueError as e:
                                    print(f"Error: {e}")

                        else:  # Staff Trips #############
                            staff_trips = FlightSchedulesStaffTripsUI(
                                dict['id'])
                            staff_trips.input_prompt()

            elif command == "d":  # change between week and day
                if time == 'weekly':
                    time = 'daily'
                    end_date = None
                else:
                    time = 'weekly'
                    end_date = start_date + week
            elif command == "n":  # see yesterday/last week
                if time == 'weekly':
                    start_date -= datetime.timedelta(7)
                    end_date = start_date + week
                else:
                    start_date -= datetime.timedelta(1)
            elif command == "m":  # see tomorrow/next week
                if time == 'weekly':
                    start_date += datetime.timedelta(7)
                    end_date = start_date + week
                else:
                    start_date += datetime.timedelta(1)
            elif command == "a":
                if self.user == 'Trip Manager':
                    create_new = FlightSchedulesCreateNewUI()
                    create_new.input_prompt()

            elif "-" in command and command[:2].upper() == "NA":
                flight_nr, ticket_count = command.split("-")
                flight_nr = flight_nr.upper()
                print(f"Flight nr: {flight_nr}, ticket count: {ticket_count}")
                if self.Logic.get_flight_by_id(flight_nr) != None:

                    try:
                        ticket_count = int(ticket_count)
                        self.Logic.change_sold_tickets(flight_nr, ticket_count)
                        # somehow reset window

                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Invalid flight number")
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")
