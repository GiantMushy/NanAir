from UiLayer import EmployeeManagementUI

# this file is only for menu's who don't have any Logic functionality

# TODO: add docstrings


class MainMenus:
    def display_main_menu(self):
        while True:
            print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print("█                           Main Menu                           █")
            print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
            print("║                                                               ║")
            print("║   1 : Trip Manager                                            ║")
            print("║   2 : Human Resources                                         ║")
            print("║                                                               ║")
            print("╚═══════════════════════════════════════════════════════════════╝")

            choice = input("Enter your choice: ")
            if choice == '1':
                pass
            elif choice == '2':
                self.display_human_resources_menu()
            else:
                print("Invalid choice. Please try again.")

    def display_human_resources_menu(self):
        while True:
            print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print("█                        Human Resources                        █")
            print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
            print("║                                                               ║")
            print("║   1 : Employee Management Menu                                ║")
            print("║   2 : Destination Management Menu                             ║")
            print("║   3 : Trip Schedules (TripManagementMenu)                     ║")
            print("║   4 : Edit Employee Schedules (CrewAssignmentMenu)            ║")
            print("║   5 : Work Reports Menu                                       ║")
            print("║   6 : Airplane Database                                       ║")
            print("║                                                               ║")
            print("║   0 : Back                                                    ║")
            print("╚═══════════════════════════════════════════════════════════════╝")

            choice = input("Enter your choice: ")
            if choice == '1':
                employee_management_ui = EmployeeManagementUI.EmployeeManagement()
                employee_management_ui.display_employee_management_menu()
            elif choice == '0':
                break  # breaks current HR loop, taking it back to the MainMenu loop
            else:
                print("Invalid choice. Please try again.")
