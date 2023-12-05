import csv
import os
from Models.Destination import Destination


class Destination_Data:
    def __init__(self, filename='DataLayer/Repository/Destination.csv'):
        """
        Initialize the DestinationData with the path to CSV file with destination data.
        """
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        Check if CSV file exists, creating one if not
        """

        directory = os.path.dirname(self.filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=[
                                        'City', 'Airport', 'Country', 'Distance', 'Travel_Time', 'Contact_Name', 'Contact_Phone_Number'])
                writer.writeheader()

    def read_all_destinations(self):
        """
        Read all destinations from the CSV file and return them as a list of Destination objects.
        :return: List of Destination objects.
        """
        destinations = []
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    destinations.append(Destination(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.filename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return destinations

    def add_destination(self, destination):
        """
        Add a new destination to the CSV file.
        :param destination: Destination object to be added.
        """
        required_fields = ['City', 'Airport', 'Country', 'Distance',
                           'Travel_Time', 'Contact_Name', 'Contact_Phone_Number']

        # checking for missing required fields
        for field in required_fields:
            if getattr(destination, field, None) is None:
                raise ValueError(
                    f"Missing required destination field: {field}")

        try:
            with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=required_fields)
                writer.writerow(destination.__dict__)
        except Exception as e:
            raise Exception(f"An error occurred while writing to file: {e}")

    def update_destination(self, destination):
        """
        Update an existing destination in the CSV file.
        :param destination: Destination object to be updated.
        """
        required_fields = ['City', 'Airport', 'Country', 'Distance',
                        'Travel_Time', 'Contact_Name', 'Contact_Phone_Number']

        # checking for missing required fields
        for field in required_fields:
            if getattr(destination, field, None) is None:
                raise ValueError(
                    f"Missing required destination field: {field}")

        try:
            with open(self.filename, mode='r+', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                destinations = []
                destination_exists = False

                for row in reader:
                    if row['City'] == destination.City:
                        destinations.append(destination.__dict__)
                        destination_exists = True
                    else:
                        destinations.append(row)

                if not destination_exists:
                    raise ValueError(f"Destination with City {destination.City} does not exist.")

                file.seek(0)
                writer = csv.DictWriter(file, fieldnames=required_fields)
                writer.writeheader()
                writer.writerows(destinations)
        except Exception as e:
            raise Exception(f"An error occurred while writing to file: {e}")