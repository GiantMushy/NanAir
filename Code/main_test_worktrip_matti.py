from DataLayer.DataLayerAPI import DataLayerAPI
from Models.WorkTrip import WorkTrip
from datetime import datetime, timedelta


def main():
    work_trip_data = DataLayerAPI()

    destinations = work_trip_data.get_mock_destinations()

    for dest in destinations:
        print(dest)

    new_work_trip = WorkTrip(
        "001", destinations[0], '2012-11-14 14:32', '2012-11-14 17:32')

    work_trip_data.add_work_trip(new_work_trip)

    work_trips = work_trip_data.read_all_work_trips()

    for trip in work_trips:
        print(trip.__dict__)

    print("\ntesting datetime")
    print(datetime(2012, 11, 14, 14, 32))


if __name__ == "__main__":
    main()
