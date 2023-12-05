#from logic_ui_wrapper import wrapper
from UiLayer.PrintFunctions import PrintFunctions

class EmployeeDataEditUI:
    def __init__(self, employee = []):
        self.PrintUi = PrintFunctions()
        #self.employee = employee
        self.employee = ["Jón Helgi", "010180 2029", "555 1234", "Flugvegur 12", "name@nanair.is", "--Not Given--"]

    def employee_data_edit_output(self):
        '''Print sequence for editing Employee Data (initial)'''
        self.PrintUi.logo()
        self.PrintUi.print_header("Employee Database Menu > Edit > " + self.employee[0], "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Employee Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"  : Name                  {self.employee[0]}"))
        print(self.PrintUi.allign_left(f"  : SSN                   {self.employee[1]}"))
        print(self.PrintUi.allign_left(f"1 : Phone                 {self.employee[2]}"))
        print(self.PrintUi.allign_left(f"2 : Address               {self.employee[3]}"))
        print(self.PrintUi.allign_left(f"3 : Email                 {self.employee[4]}"))
        print(self.PrintUi.allign_left(f"4 : Home Phone            {self.employee[5]}"))
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
        print(self.PrintUi.allign_left(" 0 : Back"))
        print(self.PrintUi.end_line())

    def edit_data(self, changed_data):
        '''Print sequence for editing Employee Data'''
        self.PrintUi.logo()
        self.PrintUi.print_header(f"Employee Database Menu > Edit > {self.employee[0]} > {changed_data}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Employee Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Name                  {self.employee[0]}"))
        print(self.PrintUi.allign_left(f"    SSN                   {self.employee[1]}"))
        print(self.PrintUi.allign_left(f"    Phone                 {self.employee[2]}"))
        print(self.PrintUi.allign_left(f"    Address               {self.employee[3]}"))
        print(self.PrintUi.allign_left(f"    Email                 {self.employee[4]}"))
        print(self.PrintUi.allign_left(f"    Home Phone            {self.employee[5]}"))
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
        print(self.PrintUi.allign_left(" 0 : Back"))
        print(self.PrintUi.end_line())

    def input_prompt(self):
        '''Starting function for editing Employee Data'''
        while True:
            self.employee_data_edit_output()
            command = input("Enter you command: ")            

            if command == "0":
                #-------------Send new Data to Logic-------------
                break
            elif command == "1":
                self.edit_data("Phone")
                command = input("Input new Phone number (xxx xxxx): ")
                #----------------------Ask Logic if actual phone number-------------------------
                self.employee[2] = command
            elif command == "2":
                self.edit_data("Address")
                command = input("Input new Address: ")
                #----------------------Ask Logic if actual Address-------------------------
                self.employee[3] = command
            elif command == "3":
                self.edit_data("Email")
                command = input("Input new Email: ")
                #----------------------Ask Logic if actual email-------------------------
                self.employee[4] = command
            elif command == "4":
                self.edit_data("Home Phone")
                command = input("Input new Phone number (xxx xxxx): ")
                #----------------------Ask Logic if actual phone number-------------------------
                self.employee[5] = command
            else:
                print("Invalid input, try again")