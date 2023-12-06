import csv
import os
from Models.Destination import Destination


class DestinationData:
    def __init__(self, Destinations_filename='DataLayer/Repository/Destinations.csv'):
        self.Destinations_filename = Destinations_filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        Check if CSV files exist, creating them if not with headers.
        """
        self.create_file_if_not_exists(self.Destinations_filename, ['id', 'city', 'airport','country', 'distance', 'travel_time',
                                                                     'contact_name', 'contact_phone_number'])
    def create_file_if_not_exists(self, filename, fieldnames):
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    def read_all_Destinations(self):
        """
        Read all Destinationss from the Destinations CSV file and return them as a list of Destinations objects.
        :return: List of Destinations objects.
        """
        Destinationss = []
        try:
            with open(self.Destinations_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Destinationss.append(Destination(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.Destinations_filename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return Destinationss

    def add_Destinations(self, Destinations):
        """
        Add a new Destinations to the CSV file.
        :param Destinations: Destinations object to be added.
        """

        try:
            with open(self.Destinations_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=Destinations.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(Destinations.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def modify_Destinations_data(self, updated_Destinationss):
        """
        Write the updated list of Destinationss to the CSV file.
        :param updated_Destinationss: List of Destinations objects with updated information.
        """
        try:
            with open(self.Destinations_filename, mode='w', newline='', encoding='utf-8') as file:
                if updated_Destinationss:
                    writer = csv.DictWriter(
                        file, fieldnames=updated_Destinationss[0].__dict__.keys())
                    writer.writeheader()
                    for emp in updated_Destinationss:
                        writer.writerow(emp.__dict__)
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
