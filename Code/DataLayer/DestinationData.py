import csv
import os
from Models.Destination import Destination


class DestinationData:
    def __init__(self, destinations_filename='DataLayer/Repository/Destinations.csv'):
        self.destinations_filename = destinations_filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        Check if CSV files exist, creating them if not with headers.
        """
        self.create_file_if_not_exists(self.destinations_filename, ['id', 'city', 'airport','country', 'distance', 'travel_time',
                                                                     'contact_name', 'contact_phone_number'])
    def create_file_if_not_exists(self, filename, fieldnames):
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    def read_all_destinations(self):
        """
        Read all Destinationss from the Destinations CSV file and return them as a list of Destinations objects.
        :return: List of Destinations objects.
        """
        destinations = []
        try:
            with open(self.destinations_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    destinations.append(Destination(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.destinations_filename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return destinations

    def add_destination(self, destinations):
        """
        Add a new Destinations to the CSV file.
        :param Destinations: Destinations object to be added.
        """

        try:
            with open(self.destinations_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=destinations.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(destinations.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def add_record(self, filename, record):
        try:
            with open(filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=record.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(record.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")
