#import os
import csv
from model.employee import Employee 
class Employee_Data:
    def __init__(self):
        #print(os.get_cwe())
        self.file_name = "files/employees.csv"
    def get_all_employees(self):
        ret_lis = []
        with open('employees.csv', newline='', endcoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_lis.append(Employee(row["Name"], row["ssn"], row["phone"], row["adress"], row["email"], row["home_phone"]))
                #print(row['first_name'], row['last_name'])
            return ret_lis

    def create_employees(self, employees):
        pass
