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

    