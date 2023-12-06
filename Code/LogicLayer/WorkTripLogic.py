from DataLayer.DataLayerAPI import DataLayerAPI
from Models.WorkTrip import WorkTrip
from datetime import datetime, timedelta


class WorkTripLogic:
    def __init__(self):
        self.work_trip_data = DataLayerAPI()

    def generate_unique_work_trip_id(self):
        """
        Generates a unique work trip ID.
        If no work trips exist, starts from '001'.
        Otherwise, increments the maximum existing ID by 1.
        :return: A string representing the unique ID.
        """
        work_trips = self.work_trip_data.read_all_work_trips()
        if not work_trips:
            return "001"

        max_id = max(int(trip.id) for trip in work_trips)
        new_id = max_id + 1
        return str(new_id).zfill(3)

    def add_work_trip(self, destination, departure_datetime, return_datetime, crew_members=None):
        """
        Adds a new work trip to the system.
        Validates required fields before adding.

        :param destination: Destination of the work trip.
        :param departure_datetime: Departure date and time.
        :param return_datetime: Return date and time.
        :param crew_members: List of crew member IDs (optional).
        :raises ValueError: If required fields are missing or empty.
        """
        if not destination or not departure_datetime or not return_datetime:
            raise ValueError("Required fields cannot be empty.")

        work_trip_id = self.generate_unique_work_trip_id()
        new_work_trip = WorkTrip(
            work_trip_id, destination, departure_datetime, return_datetime, crew_members)
        self.work_trip_data.add_work_trip(new_work_trip)

    def list_all_work_trips(self):
        """Returns a list of all work trips."""
        return self.work_trip_data.read_all_work_trips()

    def get_mock_destinations(self):
        return self.work_trip_data.get_mock_destinations()
