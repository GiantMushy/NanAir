import csv
import os
from Code.Models.AirplaneType import AirplaneType


class AirplaneTypeData:
    def __init__(self, airplane_type_filename='Code/DataLayer/Repository/AirplaneType.csv'):
        self.airplane_type_filename = airplane_type_filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        Check if CSV files exist, creating them if not with headers.
        """
        self.create_file_if_not_exists(self.airplane_type_filename, [
                                       'type', 'manufacturer', 'capacity'])

    def create_file_if_not_exists(self, filename, fieldnames):
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    def read_all_airplane_types(self):
        """
        Read all airplane_type type from the airplane_type type CSV file and return them as a list of airplane_type type objects.

        Returns, return: List of airplane_type type objects.
        """
        airplane_type = []
        try:
            with open(self.airplane_type_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    airplane_type.append(AirplaneType(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.airplane_type_filename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return airplane_type

    def add_airplane_type(self, airplane_type):
        """
        Add a new airplane_type to the CSV file.

        :param airplane_type: airplane_type object to be added.
        """

        try:
            with open(self.airplane_type_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=airplane_type.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(airplane_type.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def modify_airplane_type_data(self, updated_airplane_types):
        """
        Write the updated list of airplane_types to the CSV file.

        :param updated_airplane_types: List of airplane_type objects with updated information.
        """
        try:
            with open(self.airplane_type_filename, mode='w', newline='', encoding='utf-8') as file:
                if updated_airplane_types:
                    writer = csv.DictWriter(
                        file, fieldnames=updated_airplane_types[0].__dict__.keys())
                    writer.writeheader()
                    for emp in updated_airplane_types:
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
