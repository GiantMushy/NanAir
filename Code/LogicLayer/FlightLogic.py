from DataLayer.DataLayerAPI import DataLayerAPI
from LogicLayer.AirplaneTypeLogic import AirplaneTypeLogic
import ast
from Models.Flight import Flight
from datetime import datetime


class FlightLogic:
    def __init__(self):
        self.data = DataLayerAPI()
        self.airplane_type_logic = AirplaneTypeLogic()

    def list_all_flights(self):
        '''
        Returns, return: List of Flight objects.
        '''
        return self.data.read_all_flights()

    def add_flight(self, **kwargs):
        """
        Adds a new airplane to the system.
        Validates required fields before adding.

        :raises ValueError: If required fields are missing or empty.
        """
        required_fields = ['flight_number', 'start_from',
                           'start_datetime', 'end_at', 'arrival_datetime', 'airplane_id', 'capacity']

        if any(kwargs.get(field) is None or kwargs.get(field) == '' for field in required_fields):
            raise ValueError("Required fields cannot be empty.")

        kwargs['tickets_sold'] = 0

        new_flight = Flight(**kwargs)
        self.data.add_flight(new_flight)

    def get_flight_by_id(self, flight_number):
        '''
        :param flight_id: ID of the flight to find
        Returns, return: Flight object with the given id.
        '''
        for flight in self.list_all_flights():
            if flight.flight_number == flight_number:
                return flight

    def get_all_flights_by_destination_id(self, destination_id):
        '''
        :param destination_id: ID of the destination to find
        Returns, return: List of Flight objects with the given destination id.
        '''
        # flight number is on this format NAXX where XX is always the destination id
        flights = []
        for flight in self.list_all_flights():
            if int(flight.flight_number[2:4]) == int(destination_id):
                flights.append(flight)

        return flights

    def change_sold_tickets(self, flight_number, tickets_sold):
        '''
        :param flight_number: Number of the flight to change
        :param tickets_sold: Number of tickets sold to add to flight
        '''
        upd_flight = self.get_flight_by_id(flight_number)
        upd_flight.tickets_sold = int(
            upd_flight.tickets_sold)+int(tickets_sold)
        all_flights = self.list_all_flights()
        new_flight_objects = []
        for flight in all_flights:
            if flight.flight_number == flight_number:
                new_flight_objects.append(upd_flight)
            else:
                new_flight_objects.append(flight)

        self.data.modify_flight_data(new_flight_objects)

        # TODO: make airplane types, and stop adding more sold seats then airplane type has

    def get_sold_tickets(self, flight_number):
        '''
        :param flight_number: Number of the flight to get sold tickets from

        Returns, return: string number of sold tickets
        '''
        flight = self.get_flight_by_id(flight_number)
        return str(flight.tickets_sold)

    def get_available_tickets(self, flight_number):
        '''
        :param flight_number: Number of the flight to get available tickets from

        Returns, return: string number of available tickets
        '''
        flight = self.get_flight_by_id(flight_number)
        return str(int(flight.capacity)-int(flight.tickets_sold))

    def is_airplane_available(self, airplane_id, departure_datetime, return_datetime):
        '''
        :param airplane_id: ID of the airplane to check
        :param departure_datetime: datetime of departure
        :param return_datetime: datetime of return

        Returns, return: boolean if airplane is available
        '''
        # get all flights with the airplane id
        flights = self.data.read_all_flights()
        departure_datetime = self.date_string_to_datetime(departure_datetime)
        return_datetime = self.date_string_to_datetime(return_datetime)
        for flight in flights:
            if flight.airplane_id == airplane_id:
                # check if the flight is between the departure and return datetime
                if departure_datetime >= self.date_string_to_datetime(flight.start_datetime) and departure_datetime <= self.date_string_to_datetime(flight.arrival_datetime):
                    return False
        return True

    def date_string_to_datetime(self, date_string):
        '''
        :param date_string: string of date in format %Y-%m-%d %H:%M

        Returns, return: datetime object of the string
        '''
        return datetime.strptime(date_string, '%Y-%m-%d %H:%M')

    def is_airplane_in_use(self, airplane_id):
        '''
        :param airplane_id: ID of the airplane to check

        Returns, return: flight object if airplane is in use, None otherwise
        '''
        now = datetime.now()
        flights = self.data.read_all_flights()
        for flight in flights:
            if flight.airplane_id == airplane_id:
                if now >= self.date_string_to_datetime(flight.start_datetime) and now <= self.date_string_to_datetime(flight.arrival_datetime):
                    return flight

        return None
