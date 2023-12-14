from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI  # Wrapper
from Code.UiLayer.PrintFunctions import PrintFunctions


class EmployeeDataEditUI:
    def __init__(self, employee_id=""):
        self.PrintUi = PrintFunctions()
        self.Logic = LogicLayerAPI()
        self.employee_id = employee_id

    def employee_data_edit_output(self):
        '''Print sequence for editing Employee Data (initial)'''
        self.PrintUi.logo()
        self.PrintUi.print_header(
            "Employee Database Menu > View/Edit > " + self.PrintUi.auto_shorten_name(self.employee['name'], 25), "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Employee Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    Role                  {self.employee['role']}"))
        print(self.PrintUi.allign_left(
            f"    Name                  {self.PrintUi.auto_shorten_name(self.employee['name'],25)}"))
        print(self.PrintUi.allign_left(
            f"    SSN                   {self.employee['social_security_number']}"))
        print(self.PrintUi.allign_left(
            f"1 : Phone                 {self.employee['mobile_phone_number']}"))
        print(self.PrintUi.allign_left(
            f"2 : Address               {self.employee['address']}"))
        print(self.PrintUi.allign_left(
            f"3 : Email                 {self.PrintUi.auto_shorten_name(self.employee['email_address'],25)}"))
        print(self.PrintUi.allign_left(
            f"4 : Home Phone            {self.employee['home_phone_number']}"))
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
        self.PrintUi.print_header(
            f"Employee Database Menu > Edit > {self.employee['name']} > {changed_data}", "left")
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left("Employee Data:"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(
            f"    Role                  {self.employee['role']}"))
        print(self.PrintUi.allign_left(
            f"    Name                  {self.PrintUi.auto_shorten_name(self.employee['name'],25)}"))
        print(self.PrintUi.allign_left(
            f"    SSN                   {self.employee['social_security_number']}"))
        print(self.PrintUi.allign_left(
            f"    Phone                 {self.employee['mobile_phone_number']}"))
        print(self.PrintUi.allign_left(
            f"    Address               {self.employee['address']}"))
        print(self.PrintUi.allign_left(
            f"    Email                 {self.PrintUi.auto_shorten_name(self.employee['email_address'],25)}"))
        print(self.PrintUi.allign_left(
            f"    Home Phone            {self.employee['home_phone_number']}"))
        print(self.PrintUi.empty_line())
        print(self.PrintUi.empty_line())
        print(self.PrintUi.allign_left(f"    Input new {changed_data}"))

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
            input_check = False
            employee_obj = self.Logic.find_employee_by_id_detailed(
                self.employee_id)
            self.employee = self.Logic.object_to_dict(employee_obj)
            self.employee_data_edit_output()
            command = input("Enter you command: ").lower()

            if command == "0":
                break
            elif command == "1":
                self.edit_data("Phone")
                while not input_check:  # input check becomes True once a valid input is entered
                    command = input("Input new Phone number: ")
                    if command == "q":
                        print("Goodbye")
                        exit()
                    try:
                        self.Logic.is_contact_phone_number(command)
                        input_check = True
                        try:
                            self.Logic.modify_employee(
                                self.employee['id'], mobile_phone_number=command)
                        except ValueError as e:
                            print(f"Error: {e}")
                    except ValueError as e:
                        print(f"Error: {e}")
                        input_check = False

            elif command == "2":
                self.edit_data("Address")
                while not input_check:
                    command = input("Input new Address: ")
                    if command == "q":
                        print("Goodbye")
                        exit()
                    try:
                        self.Logic.is_address(command)
                        input_check = True
                        try:
                            self.Logic.modify_employee(
                                self.employee['id'], address=command)
                        except ValueError as e:
                            print(f"Error: {e}")
                    except ValueError as e:
                        print(f"Error: {e}")
                        input_check = False

            elif command == "3":
                self.edit_data("Email")
                while not input_check:
                    command = input("Input new Email: ")
                    if command == "q":
                        print("Goodbye")
                        exit()
                    try:
                        self.Logic.is_email(command)
                        input_check = True
                        try:
                            self.Logic.modify_employee(
                                self.employee['id'], email_address=command)
                        except ValueError as e:
                            print(f"Error: {e}")
                    except ValueError as e:
                        print(f"Error: {e}")
                        input_check = False

            elif command == "4":
                self.edit_data("Home Phone")
                while not input_check:
                    command = input("Input new Phone number: ")
                    if command == "q":
                        print("Goodbye")
                        exit()
                    try:
                        self.Logic.is_home_phone(command)
                        input_check = True
                        try:
                            self.Logic.modify_employee(
                                self.employee['id'], home_phone_number=command)
                        except ValueError as e:
                            print(f"Error: {e}")
                    except ValueError as e:
                        print(f"Error: {e}")
                        input_check = False

            elif command == "q":
                print("Goodbye")
                exit()
            else:
                print("Invalid input, try again")
