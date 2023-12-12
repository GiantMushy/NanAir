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
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Employee Type", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            "--> Input Employee Type (1: for Pilot, 2: for Flight Attendant)"))
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

    def which_role_to_display(self, employee_type):
        '''which roles to display to choose from'''
        if employee_type == "pilot":
            return "(Input 1: for Captain, 2: for Co-Pilot)"
        elif employee_type == "flight_attendant":
            return "(Input 1: for Senior Flight Attendant, 2: for Flight Attendant)"

    def input_employee_role(self):
        '''Print sequence for Creating a new Employee : Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Input Employee Role", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    {self.clean_employee_type(self.new_employee[0])}"))
        print(self.PrintUi.allign_left(
            "--> Input Employee Role "+self.which_role_to_display(self.new_employee[0])))
        if self.new_employee[0] == "pilot":
            print(self.PrintUi.allign_left("    Airplane Type"))
        print(self.PrintUi.allign_left("    Employee Name"))
        print(self.PrintUi.allign_left("    Social Security Number"))
        print(self.PrintUi.allign_left("    Phone Number"))
        print(self.PrintUi.allign_left("    Home Address"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        if not self.new_employee[0] == "pilot":
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

    def input_airplane_type(self):
        '''Print sequence for Creating a new Employee : Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Input Airplane Type", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"Choose Pilot's license by inputting the airplane type"))
        print(self.PrintUi.empty_line())
        if self.Logic.list_all_airplane_types() == []:
            print(self.PrintUi.allign_left(
                "It seems that there are no airplane types in the database, please add some airplanes before creating a pilot."))
            print(self.PrintUi.allign_left(
                "Enter '0' to skip this step for now, but you won't be able to create a pilot without a license."))
            for i in range(10):
                print(self.PrintUi.empty_line())

        else:
            self.PrintUi.print_airplane_type_table(
                self.Logic.object_list_to_dict_list((self.Logic.list_all_airplane_types())), 12)
        print(self.PrintUi.end_line())

    def input_name(self):
        '''Print sequence for Creating a new Employee : Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Input Name", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    {self.clean_employee_type(self.new_employee[0])}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        if self.new_employee[0] == "pilot":
            print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left("--> Input Employee Name"))
        print(self.PrintUi.allign_left("    Social Security Number"))
        print(self.PrintUi.allign_left("    Phone Number"))
        print(self.PrintUi.allign_left("    Home Address"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        if not self.new_employee[0] == "pilot":
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
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Input SSN", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    {self.clean_employee_type(self.new_employee[0])}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        if self.new_employee[0] == "pilot":
            print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(
            "--> Social Security Number (xxxxxx xxxx)"))
        print(self.PrintUi.allign_left("    Phone Number"))
        print(self.PrintUi.allign_left("    Home Address"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        if not self.new_employee[0] == "pilot":
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
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Input Phone Number", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    {self.clean_employee_type(self.new_employee[0])}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        if self.new_employee[0] == "pilot":
            print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left("--> Input Phone Number"))
        print(self.PrintUi.allign_left("    Home Address"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        if not self.new_employee[0] == "pilot":
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
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Input Address", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    {self.clean_employee_type(self.new_employee[0])}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        if self.new_employee[0] == "pilot":
            print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[5]}"))
        print(self.PrintUi.allign_left("--> Input Home Address (Street, Number)"))
        print(self.PrintUi.allign_left("    Email"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        if not self.new_employee[0] == "pilot":
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
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Input Email", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    {self.clean_employee_type(self.new_employee[0])}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        if self.new_employee[0] == "pilot":
            print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[5]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[6]}"))
        print(self.PrintUi.allign_left("--> Input Email Address"))
        print(self.PrintUi.allign_left("    Home Phone"))
        print(self.PrintUi.empty_line())
        if not self.new_employee[0] == "pilot":
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
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Input Home Phone", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    {self.clean_employee_type(self.new_employee[0])}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        if self.new_employee[0] == "pilot":
            print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[5]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[6]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[7]}"))
        print(self.PrintUi.allign_left("--> Input Home Phone (optional)"))

        print(self.PrintUi.empty_line())
        if not self.new_employee[0] == "pilot":
            print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def clean_employee_type(self, employee_type):
        if employee_type == "pilot":
            return "Creating: Pilot"
        elif employee_type == "flight_attendant":
            return "Creating: Flight Attendant"

    def clean_employee_type_2(self, employee_type):
        if employee_type == "pilot":
            return "Pilot"
        elif employee_type == "flight_attendant":
            return "Flight Attendant"

    def new_created(self):
        '''Print sequence when a new Employee has been created'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Employee Database Menu > Create New > Confirm", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("New Employee Created:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"Employee Type:    {self.clean_employee_type_2(self.new_employee[0])}"))
        print(self.PrintUi.allign_left(
            f"Employee Role:    {self.new_employee[1]}"))
        if self.new_employee[0] == "pilot":
            print(self.PrintUi.allign_left(
                f"Pilot License:    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(
            f"         Name:    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(
            f"          SSN:    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left(
            f"        Phone:    {self.new_employee[5]}"))
        print(self.PrintUi.allign_left(
            f"      Address:    {self.new_employee[6]}"))
        print(self.PrintUi.allign_left(
            f"        Email:    {self.new_employee[7]}"))
        print(self.PrintUi.allign_left(
            f"   Home Phone:    {self.new_employee[8]}"))
        print(self.PrintUi.empty_line())
        if not self.new_employee[0] == "pilot":
            print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            " 1 : Remake Employee (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Save and Create Another Employee"))
        print(self.PrintUi.allign_left(
            " 3 : Save and Return to the Employee Database Menu"))
        print(self.PrintUi.allign_left(
            " 4 : Discard and Return to the Employee Database Menu"))
        print(self.PrintUi.end_line())

    def create_new_sequence(self):
        n = 1
        while n < 10:
            input_check = True
            if n == 1:
                self.input_employee_type()
                data = input("Enter Employee Type (1 or 2): ").lower()
                if data == "q":
                    print("Goodbye")
                    exit()
                elif data == "1":
                    data = "pilot"
                elif data == "2":
                    data = "flight_attendant"
                else:
                    print(
                        "Invalid input, input 1 or 2, choosing a pilot or flight_attendant respectively.")
                    input_check = False

            elif n == 2:
                self.input_employee_role()
                data = input("Enter Employee Role (1 or 2: ")
                if data == "q":
                    print("Goodbye")
                    exit()
                if self.new_employee[0] == "pilot":
                    if data == "1":
                        data = "Captain"
                    elif data == "2":
                        data = "Co-Pilot"
                    else:
                        print(
                            "Invalid input, input 1 or 2, choosing a captain or co_pilot respectively.")
                        input_check = False

                elif self.new_employee[0] == "flight_attendant":
                    if data == "1":
                        data = "Senior Flight Attendant"
                    elif data == "2":
                        data = "Flight Attendant"
                    else:
                        print(
                            "Invalid input, input 1 or 2, choosing a Senior Flight Attendant or Flight Attendant Respectively.")
                        input_check = False

            elif n == 3:
                if self.new_employee[0] == 'pilot':
                    self.input_airplane_type()
                    data = input("Enter Airplane Type: ")
                    if data == "q":
                        print("Goodbye")
                        exit()
                    elif data == "0":
                        data = ""
                    elif self.Logic.find_type_data(data) == None:
                        print(
                            "Invalid airplane type input, please choose type from provided list.")
                        input_check = False
                else:
                    data = ""

            elif n == 4:
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

            elif n == 5:
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

            elif n == 6:
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

            elif n == 7:
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

            elif n == 8:
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

            elif n == 9:
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
                    self.Logic.add_employee(self.new_employee[0],
                                            self.new_employee[1],
                                            airplane_type=self.new_employee[2],
                                            name=self.new_employee[3],
                                            social_security_number=self.new_employee[4],
                                            mobile_phone_number=self.new_employee[5],
                                            address=self.new_employee[6],
                                            email_address=self.new_employee[7],
                                            home_phone_number=self.new_employee[8])
                except ValueError as e:
                    print(f"Error: {e}")
                self.new_employee = []
                self.create_new_sequence()
            elif command == "3":
                try:
                    self.Logic.add_employee(self.new_employee[0],
                                            self.new_employee[1],
                                            airplane_type=self.new_employee[2],
                                            name=self.new_employee[3],
                                            social_security_number=self.new_employee[4],
                                            mobile_phone_number=self.new_employee[5],
                                            address=self.new_employee[6],
                                            email_address=self.new_employee[7],
                                            home_phone_number=self.new_employee[8])
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
