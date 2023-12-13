import csv
import os
from Code.Models.Airplane import Airplane


class AirplaneData:
    def __init__(self, airplanes_filename='Code/DataLayer/Repository/Airplanes.csv'):
        self.airplanes_filename = airplanes_filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        Check if CSV files exist, creating them if not with headers.
        """
        self.create_file_if_not_exists(self.airplanes_filename, [
                                       'id', 'name', 'type'])

    def create_file_if_not_exists(self, filename, fieldnames):
        '''
        Creates file with given fieldnames if it doesnt exist.
        '''
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    def read_all_airplanes(self):
        """
        Read all airplanes from the Airplanes CSV file and return them as a list of airplanes objects.

        Returns, return: List of airplanes objects.
        """
        airplanes = []
        try:
            with open(self.airplanes_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    airplanes.append(Airplane(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.airplanes_filename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return airplanes

    def add_airplane(self, airplanes):
        """
        Add a new airplane to the CSV file.

        :param airplanes: airplanes object to be added.
        """

        try:
            with open(self.airplanes_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=airplanes.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(airplanes.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def modify_airplane_data(self, updated_airplaness):
        """
        Write the updated list of airplaness to the CSV file.

        :param updated_airplaness: List of airplanes objects with updated information.
        """
        try:
            with open(self.airplanes_filename, mode='w', newline='', encoding='utf-8') as file:
                if updated_airplaness:
                    writer = csv.DictWriter(
                        file, fieldnames=updated_airplaness[0].__dict__.keys())
                    writer.writeheader()
                    for emp in updated_airplaness:
                        writer.writerow(emp.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def add_record(self, filename, record):
        '''
        Adds a new record to the CSV file.
        '''
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
