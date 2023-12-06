import csv
import os
from Models.WorkTrip import WorkTrip
from datetime import datetime


class WorkTripData:
    def __init__(self, work_trip_filename='DataLayer/Repository/WorkTrip.csv'):
        self.work_trip_filename = work_trip_filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """Check if the WorkTrip CSV file exists, creating one if not with headers."""
        if not os.path.exists(self.work_trip_filename):
            with open(self.work_trip_filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=[
                                        'id', 'destination', 'departure_datetime', 'return_datetime', 'crew_members'])
                writer.writeheader()

    def add_work_trip(self, work_trip):
        """Add a new work trip to the CSV file."""
        try:
            with open(self.work_trip_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=work_trip.__dict__.keys())
                writer.writerow(work_trip.__dict__)
        except Exception as e:
            raise Exception(
                f"An error occurred while writing to the WorkTrip file: {e}")

    def read_all_work_trips(self):
        """
        Reads all work trips from a file and returns a list of WorkTrip objects.

        Returns:
            list: A list of WorkTrip objects representing all the work trips read from the file.
        """
        work_trips = []
        try:
            with open(self.work_trip_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Print the datetime strings for debugging
                    print("Departure:", row['departure_datetime'])
                    print("Return:", row['return_datetime'])

                    row['departure_datetime'] = datetime.strptime(
                        row['departure_datetime'], '%Y-%m-%d %H:%M')
                    row['return_datetime'] = datetime.strptime(
                        row['return_datetime'], '%Y-%m-%d %H:%M')

                    work_trips.append(WorkTrip(**row))
        except Exception as e:
            print(f"Error occurred while reading the file: {e}")
        return work_trips

    def get_mock_destinations(self):
        """Temporary method to return detailed mock destinations."""
        mock_destinations = [
            {
                "country": "Greenland",
                "airport": "Nuuk Airport",
                "flight_time": "3h",
                "distance_from_iceland": "1500km",
                "contact_name": "John Nuuk",
                "emergency_phone": "765467"
            },
            {
                "country": "Greenland",
                "airport": "Kulusuk Airport",
                "flight_time": "2h 30m",
                "distance_from_iceland": "1300km",
                "contact_name": "Anna Kulusuk",
                "emergency_phone": "65434"
            },
            {
                "country": "Faroe Islands",
                "airport": "Vágar Airport",
                "flight_time": "1h 20m",
                "distance_from_iceland": "800km",
                "contact_name": "Ólavur Þórshöfn",
                "emergency_phone": "298127"
            },
        ]
        return mock_destinations
