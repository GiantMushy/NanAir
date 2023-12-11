from DataLayer.DataLayerAPI import DataLayerAPI
from LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic
from LogicLayer.FlightLogic import FlightLogic
from LogicLayer.DestinationManagerLogic import DestinationManagerLogic
from LogicLayer.AirplaneManagerLogic import AirplaneManagerLogic
from LogicLayer.AirplaneTypeLogic import AirplaneTypeLogic
from Models.WorkTrip import WorkTrip
from datetime import datetime, timedelta

import ast

# for testing
from random import randint

# TODO: Since worktrips are at most two days, since a 12 hour flight
# is impossible, (12 for flying and for going back) it means that each employee
# can be busy for a maximum of 2 days, so can simply compare the
# takeoff in iceland and takeoff abroad dates, if different employee busy
# both days?


class WorkTripLogic:
    def __init__(self):
        self.work_trip_data = DataLayerAPI()
        self.employee_manager = EmployeeManagerLogic()
        self.flight_logic = FlightLogic()
        self.destination_logic = DestinationManagerLogic()
        self.airplane_logic = AirplaneManagerLogic()
        self.airplane_type_logic = AirplaneTypeLogic()

    def generate_unique_work_trip_id(self):
        '''
        Generates a unique work trip ID.

        Returns, return: Unique ID string
        '''
        work_trips = self.work_trip_data.read_all_work_trips()
        if not work_trips:
            return "001"

        max_id = max(int(trip.id) for trip in work_trips)
        new_id = max_id + 1
        return str(new_id).zfill(3)

    def add_work_trip(self, destination_id, departure_datetime, return_datetime, airplane):
        '''
        Adds a new work trip.

        :param destination: Destination id of the work trip.
        :param departure_datetime: Departure date and time. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"
        :param return_datetime: Return date and time. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"
        :param airplane: Airplane id of the work trip.

        :raises ValueError: If required fields are missing or empty.
        '''
        # TODO: add capacity into flights, assume airplane capacity given in worktrip is always correct
        # to make sure of that later on add airplane type in DB and use that when creating airplanes

        # if datetimes are indeed in the correct format
        try:
            formatting_departure_datetime = datetime.strptime(
                departure_datetime, '%Y-%m-%d %H:%M')
            formatting_return_datetime = datetime.strptime(
                return_datetime, '%Y-%m-%d %H:%M')
        except ValueError:
            raise ValueError(
                "Departure and return dates must be in the format YYYY-MM-DD HH:MM.")

        # date cannot be in the past, return_datetime cannot be less than departure_datetime
        if not destination_id or not departure_datetime or not return_datetime or not airplane:
            raise ValueError("Required fields cannot be empty.")

        if datetime.strptime(departure_datetime, '%Y-%m-%d %H:%M') < datetime.now() or datetime.strptime(return_datetime, '%Y-%m-%d %H:%M') < datetime.now():
            raise ValueError("Departure or return date cannot be in the past.")

        if datetime.strptime(return_datetime, '%Y-%m-%d %H:%M') < datetime.strptime(departure_datetime, '%Y-%m-%d %H:%M'):
            raise ValueError("Return date cannot be before departure date.")

        # if datetime.strptime(departure_datetime, '%Y-%m-%d %H:%M') < datetime.now() + timedelta(days=7):
            # raise ValueError(
            # "Worktrips cannot be created less than a week from today.")

        # destination can't be headquarters
        if int(destination_id) == int("01"):
            raise ValueError("Destination cannot be headquarters.")

        # departure time can never be the same as another departure time in worktrips
        all_work_trips = self.work_trip_data.read_all_work_trips()
        for trip in all_work_trips:
            if trip.departure_datetime == datetime.strptime(departure_datetime, '%Y-%m-%d %H:%M'):
                raise ValueError(
                    "Departure time cannot be the same as another departure time in worktrips.")

        # if destination exists
        destination = self.destination_logic.find_destination_by_id(
            destination_id)

        if not destination:
            raise ValueError("Destination does not exist.")

        # minimum required time between departure and return
        minimum_required_time = timedelta(
            hours=0.99) + timedelta(minutes=int(destination.travel_time) * 2)

        # Check if the time between departure and return is at least the minimum required time
        if (formatting_return_datetime - formatting_departure_datetime) < minimum_required_time:
            raise ValueError(
                "Time between departure and return must be at least 2 times the travel time of the destination object plus ~1 hours for overhead.")

        # TODO: also check if employees being added are indeed employees, and if they are available when validationservice added

        if not self.airplane_logic.is_airplane_created(airplane):
            raise ValueError("Airplane does not exist.")

        # passed all checks, now need to create 2 seperate flights, with seperate flight numbers
        # this needs to be somehow stored in the worktrip object, to find flights?
        # or a flight can have a work trip id?
        # its better for a worktrip to point to the two flight numbers, so need to create a function
        # in the format "NA<destinationid with padded zeroes><even numbers from iceland>/<odd numbers to iceland>"

        # create flight numbers
        flight_number_start, flight_number_end = self.flight_logic.create_flight_numbers(
            destination.id)

        departure_datetime_obj = datetime.strptime(
            departure_datetime, '%Y-%m-%d %H:%M')
        departure_plus_travel_time = departure_datetime_obj + \
            timedelta(minutes=int(destination.travel_time))

        return_datetime_obj = datetime.strptime(
            return_datetime, '%Y-%m-%d %H:%M')
        return_plus_travel_time = return_datetime_obj + \
            timedelta(minutes=int(destination.travel_time))

        # check if airplane is available
        if not self.flight_logic.is_airplane_available(airplane, departure_datetime, datetime.strftime(return_plus_travel_time, '%Y-%m-%d %H:%M')):
            raise ValueError("Airplane is not available.")

        self.flight_logic.add_flight(
            flight_number=flight_number_start,
            start_from=(self.destination_logic.get_headquarters()).airport,
            start_datetime=departure_datetime, end_at=destination.airport,
            arrival_datetime=departure_plus_travel_time.strftime(
                '%Y-%m-%d %H:%M'),
            airplane_id=airplane,
            capacity=self.get_airplane_capacity(airplane))

        self.flight_logic.add_flight(
            flight_number=flight_number_end,
            start_from=destination.airport,
            start_datetime=return_datetime,
            end_at=(self.destination_logic.get_headquarters()).airport,
            arrival_datetime=return_plus_travel_time.strftime(
                '%Y-%m-%d %H:%M'),
            airplane_id=airplane,
            capacity=self.get_airplane_capacity(airplane))

        airplane_dict = (
            self.airplane_logic.find_airplane_by_id(airplane)).__dict__

        work_trip_id = self.generate_unique_work_trip_id()
        new_work_trip = WorkTrip(
            work_trip_id, destination.__dict__, (departure_datetime), (return_datetime), airplane_dict, flight_number_start, flight_number_end, crew_members="")
        self.work_trip_data.add_work_trip(new_work_trip)

    def get_airplane_capacity(self, airplane_id):
        '''
        Gets airplane capacity.

        :param airplane_id: ID of the airplane to get capacity for.
        '''
        airplane = self.airplane_logic.find_airplane_by_id(airplane_id)
        airplane_type = self.airplane_type_logic.find_type_data(airplane.type)
        return airplane_type.capacity

    def get_recommended_departure_datetime(self, destination_id, departure_datetime):
        '''
        Gets recommended departure date and time for a work trip.

        :param destination_id: ID of the destination to get recommended departure date and time for.
        :param departure_datetime: Departure date and time. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"
        '''
        # for user interface, need to get recommended departure date and time

        destination = self.work_trip_data.read_destination_by_id(
            destination_id)

        recomm_return_abroad = datetime.strptime(
            departure_datetime, '%Y-%m-%d %H:%M') + timedelta(minutes=destination.travel_time)+timedelta(hours=1)
        return self.correct_datetime_format(recomm_return_abroad)

    def list_all_work_trips(self):
        '''
        Returns, return: A list of all WorkTrip Objects.
        '''
        # add to the work trip object, the amount of available seats and sold seats, and also the current situation of the work trip 4 options for situations, done, landed abroad, in air, not started
        all_work_trips_raw = self.work_trip_data.read_all_work_trips()
        all_work_trips = []

        # can use flight logic to get available and sold seats
        for trip in all_work_trips_raw:
            sold_tickets_start = self.flight_logic.get_sold_tickets(
                trip.flight_number_start)
            sold_tickets_end = self.flight_logic.get_sold_tickets(
                trip.flight_number_end)
            available_tickets_start = self.flight_logic.get_available_tickets(
                trip.flight_number_start)
            available_tickets_end = self.flight_logic.get_available_tickets(
                trip.flight_number_end)
            trip.sold_tickets_start = sold_tickets_start
            trip.sold_tickets_end = sold_tickets_end
            trip.available_tickets_start = available_tickets_start
            trip.available_tickets_end = available_tickets_end
            trip.current_situation = self.get_current_situation(trip.id)
            all_work_trips.append(trip)

        return all_work_trips

    def get_work_trip_by_id(self, work_trip_id):
        '''
        Gets work trip by ID.

        :param work_trip_id: ID of the work trip to get.
        '''
        all_work_trips = self.work_trip_data.read_all_work_trips()
        for trip in all_work_trips:
            if trip.id == work_trip_id:
                return trip

        return None

    def get_current_situation(self, work_trip_id):
        '''
        Gets current situation of work trip.

        :param work_trip_id: ID of the work trip to get situation for.
        '''
        work_trip = self.get_work_trip_by_id(work_trip_id)
        if not work_trip:
            raise ValueError("Work trip not found.")

        flight_start = self.flight_logic.get_flight_by_id(
            work_trip.flight_number_start)
        flight_end = self.flight_logic.get_flight_by_id(
            work_trip.flight_number_end)

        if not flight_start or not flight_end:
            raise ValueError("Flight not found.")

        start_departure = datetime.strptime(
            flight_start.start_datetime, '%Y-%m-%d %H:%M')
        end_departure = datetime.strptime(
            flight_end.start_datetime, '%Y-%m-%d %H:%M')
        start_arrival = datetime.strptime(
            flight_start.arrival_datetime, '%Y-%m-%d %H:%M')
        end_arrival = datetime.strptime(
            flight_end.arrival_datetime, '%Y-%m-%d %H:%M')

        now = datetime.now()

        if now < start_departure:
            return "Not started"
        elif start_departure <= now <= start_arrival:
            return "In air"
        elif start_arrival <= now <= end_departure:
            return "Landed abroad"
        elif end_departure <= now <= end_arrival:
            return "In air"
        elif now > end_arrival:
            return "Done"

    def add_crew_member(self, work_trip_id, employee_id):
        '''
        Adds a crew member to a WorkTrip object

        :param work_trip_id: The ID of the WorkTrip for the Employee ID to be added to
        :param employee_id: The ID of the employee to be added
        '''
        # check if employee is employee
        if not self.employee_manager.is_employee(employee_id):
            raise ValueError(
                f"Employee with ID {employee_id} is not an employee.")

        # check if employee is available
        if not self.validate_employee_availability():
            raise ValueError(
                f"Employee with ID {employee_id} is not available for this date.")

        all_work_trips = self.work_trip_data.read_all_work_trips()
        trip_found = False  # to raise error if no trip with id
        all_work_trips_updated = []
        for trip in all_work_trips:
            if trip.id == work_trip_id:
                trip_found = True
                if trip.crew_members == "":
                    updated_crew = []
                else:
                    updated_crew = trip.crew_members.split(",")

                if employee_id not in updated_crew:
                    # check here if employee is pilot and can fli airplane
                    airplane = ast.literal_eval(trip.airplane)  # trip.airplane
                    airplane_type = airplane['type']
                    if self.employee_manager.is_pilot(employee_id):
                        if not self.check_if_pilot_can_fly_airplane(airplane_type, employee_id):
                            raise ValueError(
                                f"Employee with ID {employee_id} cannot fly airplane with type {airplane_type}.")

                    updated_crew.append(employee_id)

                trip.crew_members = ",".join(updated_crew)

            all_work_trips_updated.append(trip)

        if not trip_found:
            raise ValueError(
                f"WorkTrip with ID {work_trip_id} does not exist.")

        self.work_trip_data.update_work_trip_data(all_work_trips_updated)

    def check_if_pilot_can_fly_airplane(self, airplane_type, employee_id):
        '''
        Checks if pilot can fly airplane type.

        :param airplane_type: The type of airplane to check.
        :param employee_id: The ID of the employee to check.
        '''
        # need to check if employee has license for airplane type, using employee manager list all pilots with license
        # and then check if employee id is in that list
        all_pilots = self.employee_manager.list_pilots_by_airplane_type(
            airplane_type)
        for pilot in all_pilots:
            if pilot.id == employee_id:
                return True

        return False

    def validate_employee_availability(self):
        '''wait for ValidationService to be implemented
        should be one for loop i think, read all work trips
        for each work trip, check if the employee_id given to check 
        is in the crew of any trips happening at a certain day/interval
        which is given. 
        '''
        return True

    def validate_trip_validity(self, work_trip):
        '''wait for ValidationService to be implemented
        A simple way to do this would be to obtain the members_crew of the work_trip and splitting
        the employee id's into a list, by splitting at the comma (split(,)). 
        Then iterating through the employee id's and gather all the pilots and flight attendants
        into seperate lists, using the is_pilot and is_flight_attendant which can be fetched
        in the LogicLayerAPI.
        and then using the is_captain and is senior flight attendant
        of LogicLayerAPI. ()'''
        # implement with import random 50 50 chance of returning true or false
        # each work trip should have at least two pilots (one being a captain)
        # and at least one flight attendant (one being a senior attendant).

        zero_to_one = randint(0, 1)
        if zero_to_one == 0:
            return False
        else:
            return True

    def work_trip_validity_period(self, weekly_or_daily, start_date):
        '''
        :param weekly_or_daily: weekly or daily validity period
        :param start_date: The start date of the period, in string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"

        Returns, return: List of WorkTrip objects with additional field "validity" set to True or False.
        '''
        # should obtain weekly or daily work trips in a period, and uses the validation test to check if it is valid
        # now need to fetch all work trips in the period
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
        start_date = start_date.date()
        all_work_trips = self.list_all_work_trips()
        work_trips_in_period = []
        if weekly_or_daily.lower() == "weekly":
            end_date = start_date + timedelta(days=7)
            for trip in all_work_trips:
                if start_date <= trip.departure_datetime.date() <= end_date:
                    trip.validity = self.validate_trip_validity(trip)
                    work_trips_in_period.append(trip)

        elif weekly_or_daily.lower() == "daily":
            for trip in all_work_trips:
                if trip.departure_datetime.date() == start_date:
                    trip.validity = self.validate_trip_validity(trip)
                    work_trips_in_period.append(trip)
        else:
            raise ValueError("Invalid input for weekly_or_daily")

        return work_trips_in_period

    def create_recurring_work_trips(self, work_trip_id, weekly_or_daily, number_of_recurrences):
        '''
        Creates recurring WorkTrips of given WorkTrip either weekly or daily for a certain amount of times.

        :param work_trip_id: The ID of the work trip to be copied
        :param weekly_or_daily: A string either "weekly" or "daily"
        :param number_of_recurrunces: The number of times the work trip should be copied, (x days or x weeks)
        '''
        # takes in either weekly or daily, and number of recurrences and work trip to be repeated

        # need to first obtain dates to be repeated and then use timedelta to add 1 day to it or 7 days.

        # first need to find the corresponding trip id
        all_work_trips = self.work_trip_data.read_all_work_trips()
        trip_found = False
        for trip in all_work_trips:
            if trip.id == work_trip_id:
                trip_found = True
                for i in range(number_of_recurrences):
                    # need to take out the seconds
                    if weekly_or_daily.lower() == "weekly":
                        new_departure_datetime = trip.departure_datetime + \
                            timedelta(days=7+7*i)
                        new_return_datetime = trip.return_datetime + \
                            timedelta(days=7+7*i)
                    elif weekly_or_daily.lower() == "daily":
                        new_departure_datetime = trip.departure_datetime + \
                            timedelta(days=1+1*i)
                        new_return_datetime = trip.return_datetime + \
                            timedelta(days=1+1*i)
                    else:
                        raise ValueError("Invalid input for weekly_or_daily")
                    self.add_work_trip(
                        trip.destination, self.correct_datetime_format(new_departure_datetime), self.correct_datetime_format(new_return_datetime))

        if not trip_found:
            raise ValueError(
                f"WorkTrip with ID {work_trip_id} not found in CSV")

    def correct_datetime_format(self, datetime_str):
        '''Helper function for create_recurring_work_trips to correct datetime format'''
        return datetime.strftime(datetime_str, '%Y-%m-%d %H:%M')

    def list_all_busy_employees(self, string_date):
        '''
        List all employees who are working at a certain date. 

        :param string_date: The date to check, in string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13" 

        Returns, return: a list of employee ids busy on the date

        '''
        start_date = datetime.strptime(string_date, '%Y-%m-%d %H:%M')
        start_date = start_date.date()
        all_work_trips = self.work_trip_data.read_all_work_trips()
        crew_members_list = []
        for trip in all_work_trips:
            if start_date == trip.departure_datetime.date():
                # need to do a for loop for all employees
                # changing crew_members to list, need to first check if empty
                if not trip.crew_members == "":
                    crew_members_list = trip.crew_members.split(',')

        return crew_members_list

    def list_all_available_employees(self, string_date):
        '''
        List all employees who are not working at a certain date. 

        :param string_date: The date to check, in string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13" 

        Returns, return: a list of employee ids busy on the date

        '''

        busy_employees = self.list_all_busy_employees(string_date)

        all_employees = self.work_trip_data.read_all_employees()

        all_employee_ids = []

        for emp in all_employees:

            all_employee_ids.append(emp.id)

        available_employees = []

        for emp in all_employee_ids:
            if not emp in busy_employees:
                available_employees.append(emp)

        return available_employees

    def list_employees_working_and_destinations(self, string_date):
        '''
        Lists all employee id's who are working on given date and to which destination they're going.

        :param string_date: The date to check, in string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13" 

        Returns, return: a list of dictionaries, with the employee_id and destination for given day.
        '''
        start_date = datetime.strptime(string_date, '%Y-%m-%d %H:%M')
        start_date = start_date.date()
        # need to find all work trips with this departure date
        all_work_trips_in_day = []
        all_work_trips = self.list_all_work_trips()
        for trip in all_work_trips:
            if start_date == trip.departure_datetime.date():
                # need to do a for loop for all employees

                # changing crew_members to list, need to first check if empty
                if not trip.crew_members == "":
                    crew_members_list = trip.crew_members.split(',')

                    for member in crew_members_list:
                        all_work_trips_in_day.append(
                            {'employee_id': str(member), 'destination': trip.destination})

        return all_work_trips_in_day

    def all_work_trips_of_employee(self, employee_id, string_date):
        '''
        Returns all work trips of employee id in week, the date given is the 
        start of the week that is searched. Example: 2004-6-6 14:00, search range
        is 2004-6-6 14:00 - 2004-6-13 14:00.

        :param employee_id: ID of the employee to check.
        :param employee_id: string date start of the week to check.
        '''
        start_date = start_date = datetime.strptime(
            string_date, '%Y-%m-%d %H:%M')
        start_date = start_date.date()

        end_date = start_date + timedelta(days=7)

        all_work_trips = self.list_all_work_trips()
        employee_work_trips = []

        # need to first get list of employees

        for trip in all_work_trips:
            if start_date <= trip.departure_datetime.date() <= end_date:
                # changing crew_members to list, need to first check if empty
                if not trip.crew_members == "":
                    crew_members_list = trip.crew_members.split(',')
                    if employee_id in crew_members_list or str(int(employee_id)) in crew_members_list:
                        employee_work_trips.append(trip)

        return employee_work_trips

        # if start_date <= trip.departure_datetime.date() <= end_date:

    def get_work_trip_by_flight_number(self, flight_number):
        '''
        Returns work trip by flight number.

        :param flight_number: Flight number to check.
        '''
        all_work_trips = self.work_trip_data.read_all_work_trips()
        for trip in all_work_trips:
            if trip.flight_number_start == flight_number or trip.flight_number_end == flight_number:
                return trip

        return None
