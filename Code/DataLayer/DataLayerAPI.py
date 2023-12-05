from DataLayer.EmployeeData import EmployeeData


class DataLayerAPI:
    def __init__(self):
        self.employee_data = EmployeeData()

    def read_all_employees(self):
        return self.employee_data.read_all_employees()

    def read_all_pilots(self):
        return self.employee_data.read_all_pilots()

    def read_all_flight_attendants(self):
        return self.employee_data.read_all_flight_attendants()

    def add_employee(self, employee):
        self.employee_data.add_employee(employee)

    def modify_employee_data(self, updated_employees):
        self.employee_data.modify_employee_data(updated_employees)
