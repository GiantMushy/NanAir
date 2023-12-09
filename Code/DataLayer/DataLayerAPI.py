from DataLayer.EmployeeData import EmployeeData
from DataLayer.WorkTripData import WorkTripData
from DataLayer.DestinationData import DestinationData
from DataLayer.AirplaneData import AirplaneData
from DataLayer.FlightData import FlightData
from DataLayer.AirplaneTypeData import AirplaneTypeData


class DataLayerAPI:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.work_trip_data = WorkTripData()
        self.destination_data = DestinationData()
        self.airplane_data = AirplaneData()
        self.flight_data = FlightData()
        self.airplane_type_data = AirplaneTypeData()

    ################################## Employee Data Functions ###################################
    def read_all_employees(self):
        '''
        Read all employees from the Employee CSV file and return them as a list of Employee objects.

        Returns, return: List of Employee objects.
        '''
        return self.employee_data.read_all_employees()

    def read_all_pilots(self):
        '''
        Read all pilots from the Pilot CSV file and return them as a list of Pilot objects.

        Returns, return: List of Pilot objects.
        '''
        return self.employee_data.read_all_pilots()

    def read_all_flight_attendants(self):
        '''
        Read all flight attendants from the FlightAttendant CSV file and return them as a list of FlightAttendant objects.

        Return, return: List of FlightAttendant objects.
        '''
        return self.employee_data.read_all_flight_attendants()

    def add_employee(self, employee):
        '''
        Add a new employee to the CSV file.

        :param employee: Employee object to be added.
        '''
        self.employee_data.add_employee(employee)

    def modify_employee_data(self, updated_employees):
        '''
        Write the updated list of employees to the CSV file.

        :param updated_employees: List of Employee objects with updated information.
        '''
        self.employee_data.modify_employee_data(updated_employees)

    def add_pilot(self, pilot):
        '''
        Add a new pilot to the Pilot CSV file.

        :param pilot: Pilot object to be added.
        '''
        self.employee_data.add_pilot(pilot)

    def add_flight_attendant(self, flight_attendant):
        '''
        Add a new flight attendant to the FlightAttendant CSV file.

        :param flight_attendant: FlightAttendant object to be added.
        '''
        self.employee_data.add_flight_attendant(flight_attendant)

    ################# WorkTripData #################
    def read_all_work_trips(self):
        '''
        Returns a list of WorkTrip objects.

        Returns, list: A list of WorkTrip objects.
        '''
        return self.work_trip_data.read_all_work_trips()

    def add_work_trip(self, work_trip):
        '''
        Add a new work tirp to the CSV file.

        :param work_trip: WorkTrip object to be added.
        '''
        self.work_trip_data.add_work_trip(work_trip)

    def update_work_trip_data(self, updated_work_trips):
        '''
        Writing updated list of Work Trips after editing

        :param updated_work_trips: updated WorkTrip objects to write.
        '''
        self.work_trip_data.update_work_trip_data(updated_work_trips)

    ################################## Destination Data Functions ###################################

    def read_all_destinations(self):
        """
        Read all destination from the Destination CSV file and return them as a list of Destination objects.
        :return: List of Destination objects.
        """
        return self.destination_data.read_all_destinations()

    def add_destination(self, destination):
        """
        Add a new destination to the CSV file.
        :param destination: Destination object to be added.
        """
        self.destination_data.add_destination(destination)

    ################################## Airplane Data Functions ###################################

    def read_all_airplanes(self):
        """
        Read all airplane from the Airplane CSV file and return them as a list of Airplane objects.
        :return: List of airplane objects.
        """
        return self.airplane_data.read_all_airplanes()

    def add_airplane(self, airplane):
        """
        Add a new airplane to the CSV file.
        :param airplane: Airplane object to be added.
        """
        self.airplane_data.add_airplane(airplane)

    def modify_airplane_data(self, updated_airplanes):
        """
        Write the updated list of airplanes to the CSV file.
        :param updated_airplanes: List of airplane objects with updated information.
        """
        self.airplane_data.modify_airplane_data(updated_airplanes)
    ################################## Flight Data ###################################

    def read_all_flights(self):
        """
        Read all Flights from the Flight CSV file and return them as a list of Flight objects.

        Returns, return: List of Flight objects.
        """
        return self.flight_data.read_all_flights()

    def add_flight(self, flight):
        """
        Add a new Flight to the CSV file.

        :param Flight: Flight object to be added.
        """
        self.flight_data.add_flight(flight)

    def modify_flight_data(self, updated_flights):
        '''
        Write the updated list of flights to the CSV file.

        :param updated_employees: List of Flight objects with updated information.
        '''
        self.flight_data.modify_flight_data(updated_flights)

    ################################## AirplaneType Data ###################################

    def read_all_airplane_types(self):
        """
        Read all airplane_type type from the airplane_type type CSV file and return them as a list of airplane_type type objects.

        Returns, return: List of airplane_type type objects.
        """
        return self.airplane_type_data.read_all_airplane_types()

    def add_airplane_type(self, airplane_type):
        """
        Add a new airplane_type to the CSV file.

        :param airplane_type: airplane_type object to be added.
        """
        self.airplane_type_data.add_airplane_type(airplane_type)

    def modify_airplane_type_data(self, updated_airplane_types):
        """
        Write the updated list of airplane_types to the CSV file.

        :param updated_airplane_types: List of airplane_type objects with updated information.
        """
        self.airplane_type_data.modify_airplane_type_data(
            updated_airplane_types)
