class WorkTrip:
    def __init__(self, id, destination, departure_datetime, return_datetime, airplane, flight_number_start, flight_number_end, crew_members=None):
        self.id = id
        self.destination = destination
        self.departure_datetime = departure_datetime
        self.return_datetime = return_datetime
        self.airplane = airplane
        self.flight_number_start = flight_number_start
        self.flight_number_end = flight_number_end
        self.crew_members = crew_members if crew_members else ""

    def __str__(self):
        return f"id: {self.id}, destination: {self.destination}, departure_datetime: {self.departure_datetime}, return_datetime: {self.return_datetime}, crew_members: {self.crew_members}"