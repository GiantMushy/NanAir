import csv
import os
from Models.AirplaineModel import Airplaine




class AirplaineData:
    def __init__(self):
        self.file_name = "files/airplaines.csv"
    def get_all_airplaines(self):
        ret_lis = []
        with open('airplaines.csv', newline='', endcoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_lis.append((row["name"], row["CurrentLocation"], row["Type"], row["Manufacturer"], row["Capacity"]))
                #print(row['first_name'], row['last_name'])
            return ret_lis
        
        """Initialize the AirplaineData with the path to CSV file with airplaine data"""
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        self.create_file_if_not_exists(self.employee_filename, ['NameOfPlane', 'CurrentLocation', 'Type',
                                                                'Manufacturer', 'Capacity',])
        self.create_file_if_not_exists(self.Airplaine_filename, [
                                       'type'])
        

    def create_file_if_not_exists(self, filename, fieldnames):
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    def read_all_airplaines(self):
        """
        Read all Airplaines from the Airplaine CSV file and return them as a list of Airplaine objects.
        :return: List of Airplaine objects.
        """
        Airplaine = []
        try:
            with open(self.airplaine_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    airplaine.append(Airplaine(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.employee_filename} does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
        return airplaine

    def read_all_pilots(self):
        """
        Read all pilots from the Pilot CSV file and return them as a list of Pilot objects.
        :return: List of Pilot objects.
        """
        pilots = []
        try:
            with open(self.pilot_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    pilots.append(Pilot(**row))
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file {self.airplaine_filename} does not exist.")
        except Exception as e:
            raise Exception(
                f"An error occurred while reading the Airplaine file: {e}")
        return pilots

    def add_employee(self, airplaine):
        """
        Add a new airplaine to the CSV file.
        :param airplaine: Airplaine object to be added.
        """

        try:
            with open(self.airplaine_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=airplaine.__dict__.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(airplaine.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    def modify_airplaine_data(self, updated_employees):
        """
        Write the updated list of airplaines to the CSV file.
        :param updated_employees: List of airplaine objects with updated information.
        """
        try:
            with open(self.airplaine_filename, mode='w', newline='', encoding='utf-8') as file:
                if updated_employees:
                    writer = csv.DictWriter(
                        file, fieldnames=updated_employees[0].__dict__.keys())
                    writer.writeheader()
                    for emp in updated_airplaines:
                        writer.writerow(emp.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the file: {e}")

    