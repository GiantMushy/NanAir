#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class EmployeeDataCreateNewUI:
    def __init__(self):
        self.PrintUi = PrintFunctions()
        self.new_employee = []

    def input_name(self):
        '''Print sequence for Creating a new Employee : Name'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Create New > Input Name", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Creating New Employee"))
        print(self.PrintUi.empty_line())
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
        print(self.PrintUi.allign_left("--> Input Phone Number (xxx xxxx)"))
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
        print(self.PrintUi.allign_left("--> Input Home Phone"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
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
        print(self.PrintUi.allign_left(f"    {self.new_employee[0]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[1]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[2]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[3]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[4]}"))
        print(self.PrintUi.allign_left(f"    {self.new_employee[5]}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(" 1 : Remake Employee (if incorrect data was input)"))
        print(self.PrintUi.allign_left(" 2 : Create Another Employee"))
        print(self.PrintUi.allign_left(" 0 : Return to the Employee Database Menu"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for creating a new Employee'''
        n = 1
        while n < 7:
            if n == 1:
                self.input_name()
                data = input("Enter name: ")
                #------------Ask Logic if input actualy a name--------------
            elif n == 2:
                self.input_SSN()
                data = input("Enter SSN: ")
                #------------Ask Logic if input actualy a valid SSN--------------
            elif n == 3:
                self.input_phone()
                data = input("Enter Phone: ")
                #------------Ask Logic if input actualy a phone number--------------
            elif n == 4:
                self.input_address()
                data = input("Enter Address: ")
                #------------Ask Logic if input actualy an address--------------
            elif n == 5:
                self.input_email()
                data = input("Enter Email: ")
                #------------Ask Logic if input actualy an email--------------
            elif n == 6:
                self.input_home_phone()
                data = input("Enter Home Phone: ")
                if data == "":
                    data = "--Not Given--"
                #------------Ask Logic if input actualy a phone number--------------
            self.new_employee.append(data)
            n += 1
        
        while True:
            self.new_created()
            command = input("Enter command: ")
            if command == "0":
                #--------------------send data to Logic-----------------------
                ####-----NEEDS FIXING: Back doesnt always go to EmployeeData after multiple employee creations-----####
                break
            elif command == "1":
                self.new_employee = []
                self.input_prompt()
            elif command == "2":
                #--------------------send data to Logic-----------------------
                self.new_employee = []
                self.input_prompt()
            else:
                print("Invalid input, try again")