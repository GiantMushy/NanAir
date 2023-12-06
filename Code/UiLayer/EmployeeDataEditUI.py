from LogicLayer.LogicLayerAPI import LogicLayerAPI #Wrapper
from UiLayer.PrintFunctions import PrintFunctions

class EmployeeDataEditUI:
    def __init__(self, employee = []):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.employee = employee

    def employee_data_edit_output(self):
        '''Print sequence for editing Employee Data (initial)'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Edit > " + self.employee['name'], "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Employee Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"  : Name                  {self.employee['name']}"))
        print(self.PrintUi.allign_left(f"  : SSN                   {self.employee['social_security_number']}"))
        print(self.PrintUi.allign_left(f"1 : Phone                 {self.employee['mobile_phone_number']}"))
        print(self.PrintUi.allign_left(f"2 : Address               {self.employee['address']}"))
        print(self.PrintUi.allign_left(f"3 : Email                 {self.employee['email_address']}"))
        print(self.PrintUi.allign_left(f"4 : Home Phone            {self.employee['home_phone_number']}"))
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
        print(self.PrintUi.allign_left(" 0 : Back          q : Exit"))
        print(self.PrintUi.end_line())

    def edit_data(self, changed_data):
        '''Print sequence for editing Employee Data'''
        self.PrintUi.logo()
        self.PrintUi.print_header(f"Employee Database Menu > Edit > {self.employee['name']} > {changed_data}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Employee Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Name                  {self.employee['name']}"))
        print(self.PrintUi.allign_left(f"    SSN                   {self.employee['social_security_number']}"))
        print(self.PrintUi.allign_left(f"    Phone                 {self.employee['mobile_phone_number']}"))
        print(self.PrintUi.allign_left(f"    Address               {self.employee['address']}"))
        print(self.PrintUi.allign_left(f"    Email                 {self.employee['email_address']}"))
        print(self.PrintUi.allign_left(f"    Home Phone            {self.employee['home_phone_number']}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Input new {changed_data}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(""))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for editing Employee Data'''
        while True:
            self.employee_data_edit_output()
            command = input("Enter you command: ")            

            if command == "0":
                break
            elif command == "1":
                self.edit_data("Phone")
                command = input("Input new Phone number: ")
                try:
                    self.Logic.modify_employee(self.employee['id'], mobile_phone_number = command)
                except ValueError as e:
                    print(f"Error: {e}")
                
            elif command == "2":
                self.edit_data("Address")
                command = input("Input new Address: ")
                try:
                    self.Logic.modify_employee(self.employee['id'], address = command)
                except ValueError as e:
                    print(f"Error: {e}")
                
            elif command == "3":
                self.edit_data("Email")
                command = input("Input new Email: ")
                try:
                    self.Logic.modify_employee(self.employee['id'], email_address = command)
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "4":
                self.edit_data("Home Phone")
                command = input("Input new Home Phone: ")
                try:
                    self.Logic.modify_employee(self.employee['id'], home_phone_number = command)
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "q":
                exit()
            else:
                print("Invalid input, try again")