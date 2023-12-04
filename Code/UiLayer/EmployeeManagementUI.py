from typing import Any
from LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic

# TODO: add docstrings, update details in presentation to match happy paths
# update list all employees to have a modifiable header


class EmployeeManagement:
    def __init__(self):
        self.employee_logic = EmployeeManagerLogic()

    def display_employee_management_menu(self):
        while True:
            print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print("█ Human Resources > Employee Management Menu                    █")
            print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
            print("║                                                               ║")
            print("║   1 : Create New Employee                                     ║")
            print("║   2 : Edit Existing Employee Data                             ║")
            print("║   3 : List All Employees                                      ║")
            print("║                                                               ║")
            print("║   0 : Back                                                    ║")
            print("╚═══════════════════════════════════════════════════════════════╝")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.register_employee()
            elif choice == '2':
                self.edit_employee_data()
            elif choice == '3':
                self.display_all_employees()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def register_employee(self):
        print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        print("█ Human Resources > Employee Management Menu > Create New       █")
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

        # gathering employee details
        name = input("Enter Employee Name: ")
        ssn = input("Enter Social Security Number (xxxxxx xxxx): ")
        phone = input("Enter Phone Number (xxx xxxx): ")
        address = input("Enter Home Address (Street, number): ")
        email = input("Enter Email (example@email.com): ")
        home_phone = input("Enter Home Phone (xxx xxxx) (optional): ")

        # create and save new employee
        try:
            self.employee_logic.add_employee(
                name, ssn, phone, address, email, home_phone)
            print("\nNew Employee Created Successfully.")
            print(f"Name: {name}")
            print(f"SSN: {ssn}")
            print(f"Phone: {phone}")
            print(f"Address: {address}")
            print(f"Email: {email}")
            print(
                f"Home Phone: {home_phone if home_phone else '--Not Given--'}")
        except ValueError as e:
            print(f"Error: {e}")

        input("\n<Enter> : Back")

    def display_all_employees(self):
        employees = self.employee_logic.list_all_employees()
        print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        print("█ List of Employees                                             █")
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("║ ID   | Name                                                   ║")
        print("║------|--------------------------------------------------------║")
        for emp in employees:
            print(f"║ {emp.id:4} | {emp.name:54} ║")
        print("╚═══════════════════════════════════════════════════════════════╝")
        input("\n<Enter> : Back")

    def edit_employee_data(self):
        self.display_all_employees()
        employee_id = input("Enter the ID of the employee to edit: ")
        employee = self.employee_logic.find_employee_by_id(employee_id)

        if employee:
            print(f"Editing data for {employee.name}")
            new_phone = input(
                "New Phone Number (leave blank to keep current): ")
            new_address = input("New Address (leave blank to keep current): ")
            new_email = input("New Email (leave blank to keep current): ")
            new_home_phone = input(
                "New Home Phone (leave blank to keep current): ")

            updates = {}
            if new_phone:
                updates['mobile_phone_number'] = new_phone
            if new_address:
                updates['address'] = new_address
            if new_email:
                updates['email_address'] = new_email
            if new_home_phone:
                updates['home_phone_number'] = new_home_phone

            self.employee_logic.modify_employee(employee_id, **updates)
            print("Employee data updated successfully.")
        else:
            print("Employee not found.")

        input("\n<Enter> : Back")
