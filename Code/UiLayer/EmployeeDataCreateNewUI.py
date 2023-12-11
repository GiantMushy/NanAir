from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI
from Code.UiLayer.PrintFunctions import PrintFunctions

class EmployeeDataCreateNewUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.new_employee = []

    def input_employee_type(self):
        '''Print sequence for Creating a new Employee : Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Name", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("--> Input Employee Type (Pilot/Flight Attendant)"))
        print(self.PrintUi.allign_left("    Employee Role"))
        print(self.PrintUi.allign_left("    Employee Name"))
        print(self.PrintUi.allign_left("    Social Security Number"))
        print(self.PrintUi.allign_left("    Phone Number"))
        print(self.PrintUi.allign_left("    Home Address"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_employee_role(self):
        '''Print sequence for Creating a new Employee : Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Name", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_employee[0]}"))
        print(self.PrintUi.allign_left("--> Input Employee Role (Captain/Co Pilot, Senior/Flight Attendant)"))
        print(self.PrintUi.allign_left("    Employee Name"))
        print(self.PrintUi.allign_left("    Social Security Number"))
        print(self.PrintUi.allign_left("    Phone Number"))
        print(self.PrintUi.allign_left("    Home Address"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_name(self):
        '''Print sequence for Creating a new Employee : Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Name", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_employee[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        print(self.PrintUi.allign_left("--> Input Employee Name"))
        print(self.PrintUi.allign_left("    Social Security Number"))
        print(self.PrintUi.allign_left("    Phone Number"))
        print(self.PrintUi.allign_left("    Home Address"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_SSN(self):
        '''Print sequence for Creating a new Employee : Social Security Number'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input SSN", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_employee[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left("--> Social Security Number (xxxxxx xxxx)"))
        print(self.PrintUi.allign_left("    Phone Number"))
        print(self.PrintUi.allign_left("    Home Address"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_phone(self):
        '''Print sequence for Creating a new Employee : Phone number'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Phone Number", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_employee[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left("--> Input Phone Number"))
        print(self.PrintUi.allign_left("    Home Address"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_address(self):
        '''Print sequence for Creating a new Employee : Home Address'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Address", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_employee[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left("--> Input Home Address (Street, Number)"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_email(self):
        '''Print sequence for Creating a new Employee : Email'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Email", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_employee[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[5]}"))
        print(self.PrintUi.allign_left("--> Input Email Address"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_home_phone(self):
        '''Print sequence for Creating a new Employee : Home Phone'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    {self.new_employee[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[5]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[6]}"))
        print(self.PrintUi.allign_left("--> Input Home Phone (optional)"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def new_created(self):
        '''Print sequence when a new Employee has been created'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("New Employee Created:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"Employee Type:    {self.new_employee[0]}"))
        print(self.PrintUi.allign_left(f"Employee Role:    {self.new_employee[1]}"))
        print(self.PrintUi.allign_left(f"         Name:    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"          SSN:    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(f"        Phone:    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left(f"      Address:    {self.new_employee[5]}"))
        print(self.PrintUi.allign_left(f"        Email:    {self.new_employee[6]}"))
        print(self.PrintUi.allign_left(f"   Home Phone:    {self.new_employee[7]}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 1 : Remake Employee (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Save and Create Another Employee"))
        print(self.PrintUi.allign_left(" 3 : Save and Return to the Employee Database Menu"))
        print(self.PrintUi.allign_left(" 4 : Discard and Return to the Employee Database Menu"))
        print(self.PrintUi.end_line())

    def create_new_sequence(self):
        n = 1
        input_check = True
        while n < 9:
            if n == 1:
                self.input_employee_type()
                data = input("Enter Employee Type: ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_employee_type(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 2:
                self.input_employee_role()
                data = input("Enter Employee Role: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_employee_role(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 3:
                self.input_name()
                data = input("Enter Name: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_name(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 4:
                self.input_SSN()
                data = input("Enter Social Security Number: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_social_security_number(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False
                
            elif n == 5:
                self.input_phone()
                data = input("Enter Phone number: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_contact_phone_number(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 6:
                self.input_address()
                data = input("Enter Address: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_address(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 7:
                self.input_email()
                data = input("Enter Email: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_email(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            elif n == 8:
                self.input_home_phone()
                data = input("Enter Home Phone: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                try:
                    self.Logic.is_home_phone(data)
                    input_check = True
                except ValueError as e:
                    print(f"Error: {e}")
                    input_check = False

            if input_check:
                self.new_employee.append(data)
                n += 1

    def input_prompt(self):
        '''Starting function for creating a new Employee'''
        self.create_new_sequence()
        while True:
            self.new_created()
            command = input("Enter command: ")
            if command == "1":
                self.new_employee = []
                self.create_new_sequence()
            elif command == "2":
                try:
                    self.Logic.add_employee(self.new_employee[0], self.new_employee[1], name=self.new_employee[2], social_security_number=self.new_employee[3],
                                            mobile_phone_number=self.new_employee[4], address=self.new_employee[5], email_address=self.new_employee[6], home_phone_number=self.new_employee[7])
                except ValueError as e:
                    print(f"Error: {e}")
                self.new_employee = []
                self.create_new_sequence()
            elif command == "3":
                try:
                    self.Logic.add_employee(self.new_employee[0], self.new_employee[1], name=self.new_employee[2], social_security_number=self.new_employee[3],
                                            mobile_phone_number=self.new_employee[4], address=self.new_employee[5], email_address=self.new_employee[6], home_phone_number=self.new_employee[7])
                    break
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "4":
                break    
            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")