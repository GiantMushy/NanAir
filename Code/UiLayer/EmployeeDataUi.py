#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions
from UiLayer.EmployeeDataCreateNewUI import EmployeeDataCreateNewUI
from UiLayer.EmployeeDataEditUI import EmployeeDataEditUI

class EmployeeDataUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()

    def employee_data_output(self):
        '''Print sequence for the Employee Data Menu'''
        data = [{'id': '001', 'name': 'Matti', 'social_security_number': '611563-4242', 'address': 'Mac street 1', 'mobile_phone_number': '6686453441', 'email_address': 'example71@gmail.com', 'home_phone_number': ''},
                {'id': '002', 'name': 'Sara', 'social_security_number': '430730-9923', 'address': 'Microsoft street 1', 'mobile_phone_number': '1358799863', 'email_address': 'example55@gmail.com', 'home_phone_number': ''},
                {'id': '003', 'name': 'Raggi', 'social_security_number': '164862-8280', 'address': 'AMZN street 1', 'mobile_phone_number': '9861589627', 'email_address': 'example38@gmail.com', 'home_phone_number': ''},
                {'id': '004', 'name': 'Banani', 'social_security_number': '347784-3214', 'address': 'FB street 1', 'mobile_phone_number': '3550569113', 'email_address': 'example35@gmail.com', 'home_phone_number': ''},
                {'id': '005', 'name': 'Epli', 'social_security_number': '628896-8506', 'address': 'Apple street 1', 'mobile_phone_number': '1002571434', 'email_address': 'example87@gmail.com', 'home_phone_number': ''},
                {'id': '006', 'name': 'Matti', 'social_security_number': '611563-4242', 'address': 'Mac street 1', 'mobile_phone_number': '6686453441', 'email_address': 'example71@gmail.com', 'home_phone_number': ''},
                {'id': '007', 'name': 'Raggi', 'social_security_number': '164862-8280', 'address': 'AMZN street 1', 'mobile_phone_number': '9861589627', 'email_address': 'example38@gmail.com', 'home_phone_number': ''},
                {'id': '008', 'name': 'Banani', 'social_security_number': '347784-3214', 'address': 'FB street 1', 'mobile_phone_number': '3550569113', 'email_address': 'example35@gmail.com', 'home_phone_number': ''},
                {'id': '009', 'name': 'Epli', 'social_security_number': '628896-8506', 'address': 'Apple street 1', 'mobile_phone_number': '1002571434', 'email_address': 'example87@gmail.com', 'home_phone_number': ''},
                {'id': '010', 'name': 'Matti', 'social_security_number': '611563-4242', 'address': 'Mac street 1', 'mobile_phone_number': '6686453441', 'email_address': 'example71@gmail.com', 'home_phone_number': ''},
                {'id': '011', 'name': 'Sara', 'social_security_number': '430730-9923', 'address': 'Microsoft street 1', 'mobile_phone_number': '1358799863', 'email_address': 'example55@gmail.com', 'home_phone_number': ''},
                {'id': '012', 'name': 'Raggi', 'social_security_number': '164862-8280', 'address': 'AMZN street 1', 'mobile_phone_number': '9861589627', 'email_address': 'example38@gmail.com', 'home_phone_number': ''},
                {'id': '013', 'name': 'Banani', 'social_security_number': '347784-3214', 'address': 'FB street 1', 'mobile_phone_number': '3550569113', 'email_address': 'example35@gmail.com', 'home_phone_number': ''},
                {'id': '014', 'name': 'Epli', 'social_security_number': '628896-8506', 'address': 'Apple street 1', 'mobile_phone_number': '1002571434', 'email_address': 'example87@gmail.com', 'home_phone_number': ''},
                {'id': '015', 'name': 'Matti', 'social_security_number': '611563-4242', 'address': 'Mac street 1', 'mobile_phone_number': '6686453441', 'email_address': 'example71@gmail.com', 'home_phone_number': ''},
                {'id': '016', 'name': 'Sara', 'social_security_number': '430730-9923', 'address': 'Microsoft street 1', 'mobile_phone_number': '1358799863', 'email_address': 'example55@gmail.com', 'home_phone_number': ''},
                {'id': '017', 'name': 'Raggi', 'social_security_number': '164862-8280', 'address': 'AMZN street 1', 'mobile_phone_number': '9861589627', 'email_address': 'example38@gmail.com', 'home_phone_number': ''},
                {'id': '018', 'name': 'Banani', 'social_security_number': '347784-3214', 'address': 'FB street 1', 'mobile_phone_number': '3550569113', 'email_address': 'example35@gmail.com', 'home_phone_number': ''},
                {'id': '019', 'name': 'Epli', 'social_security_number': '628896-8506', 'address': 'Apple street 1', 'mobile_phone_number': '1002571434', 'email_address': 'example87@gmail.com', 'home_phone_number': ''},
                {'id': '020', 'name': 'Matti', 'social_security_number': '611563-4242', 'address': 'Mac street 1', 'mobile_phone_number': '6686453441', 'email_address': 'example71@gmail.com', 'home_phone_number': ''}]


        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("List of Employees"))
        print(self.PrintUi.empty_line())
        self.PrintUi.print_employee_table(data, 15)
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 0 : Back                     00 : Create New Employee                  <ID> : Edit Employee Data"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for EmployeeDataUI'''
        while True:
            self.employee_data_output()
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "00":
                create_new = EmployeeDataCreateNewUI()
                create_new.input_prompt()
            elif command == "1": #make it take employee data
                edit = EmployeeDataEditUI([])
                edit.input_prompt()
            else:
                print("Invalid input, try again")