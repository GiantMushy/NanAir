import csv
import os
from Models.Flight import Flight


class FlightData:
    def __init__(self, flight_filename='DataLayer/Repository/Flight.csv'):
        self.flight_filename = flight_filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        Check if CSV files exist, creating them if not with headers.
        """
        self.create_file_if_not_exists(self.flight_filename, [
                                       'flight_number', 'start_from', 'start_datetime', 'end_at', 'arrival_datetime', 'airplane_id', 'capacity', 'tickets_sold'])

    def create_file_if_not_exists(self, filename, fieldnames):
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    def read_all_flights(self):
        """
        Read all Flights from the Flight CSV file and return them as a list of Flight objects.

        Returns, return: List of Flight objects.
        """
        flights = []
        try:
            with open(self.flight_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    flights.append(Flight(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.flight_filename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return flights

    def add_flight(self, flight):
        """
        Add a new Flight to the CSV file.

        :param Flight: Flight object to be added.
        """

        try:
            with open(self.flight_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=flight.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(flight.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def modify_flight_data(self, updated_flights):
        '''
        Write the updated list of flights to the CSV file.

        :param updated_employees: List of Flight objects with updated information.
        '''
        try:
            with open(self.flight_filename, mode='w', newline='', encoding='utf-8') as file:
                if updated_flights:
                    writer = csv.DictWriter(
                        file, fieldnames=updated_flights[0].__dict__.keys())
                    writer.writeheader()
                    for flight in updated_flights:
                        writer.writerow(flight.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")
