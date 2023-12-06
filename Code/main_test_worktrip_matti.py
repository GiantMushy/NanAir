from DataLayer.DataLayerAPI import DataLayerAPI
from datetime import datetime, timedelta


def main():
    work_trip_data = DataLayerAPI()

    destinations = work_trip_data.get_mock_destinations()

    for dest in destinations:
        print(dest)


if __name__ == "__main__":
    main()
