class WorkTrip:
    def __init__(self, id, destination, departure_datetime, return_datetime, crew_members=None):
        self.id = id
        self.destination = destination
        self.departure_datetime = departure_datetime
        self.return_datetime = return_datetime
        self.crew_members = crew_members if crew_members else ""
