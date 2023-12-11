class Flight:
    def __init__(self, flight_number, start_from, start_datetime, end_at, arrival_datetime, airplane_id, capacity, tickets_sold):
        self.flight_number = flight_number
        self.start_from = start_from
        self.start_datetime = start_datetime
        self.end_at = end_at
        self.arrival_datetime = arrival_datetime
        self.airplane_id = airplane_id
        self.capacity = capacity
        self.tickets_sold = tickets_sold
