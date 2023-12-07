from LogicLayer.LogicLayerAPI import LogicLayerAPI
from Models.WorkTrip import WorkTrip
from datetime import datetime, timedelta


def main():
    work_trip_logic = LogicLayerAPI()

    print("adding some destinations")

    work_trip_logic.add_destination(city="Matta city", airport="Matti airport", country="Mattaland",
                                    distance='6', travel_time='200',	contact_name="Helgi", contact_phone_number="9876543")

    destinations_ = work_trip_logic.list_all_destinations()

    destinations = work_trip_logic.object_list_to_dict_list(destinations_)

    for dest in destinations:
        print(dest)

    work_trip_logic.add_work_trip(
        destinations[0], '2032-11-14 14:32', '2032-11-14 17:32')

    work_trip_logic.add_work_trip(
        destinations[1], '2032-11-14 14:32', '2034-11-14 17:32', '003')

    work_trips = work_trip_logic.list_all_work_trips()

    for trip in work_trips:
        print(trip.__dict__)

    print('adding employee to worktrip')

    work_trip_logic.add_crew_member("001", "001")
    work_trip_logic.add_crew_member("001", "002")

    work_trips = work_trip_logic.list_all_work_trips()

    for trip in work_trips:
        print(trip.__dict__)

    # hopefully no problem regarding datetype
    print("testing creting reccurring worktrips daily for 15 days")
    work_trip_logic.create_recurring_work_trips("001", "daily", 15)

    print("\n lets see if it was created correctly")
    work_trips = work_trip_logic.list_all_work_trips()
    for trip in work_trips:
        print(trip.__dict__)

    print("\n testing checking validity of trips")
    work_trip_validity_test = work_trip_logic.work_trip_validity_period(
        "weekly", '2032-11-15 14:32')

    for trip in work_trip_validity_test:
        print(f"{trip.id} validity: {trip.validity}")

    print("\n Testing listing all employees working on a certain date")
    testing = work_trip_logic.list_employees_working_and_destinations(
        "2032-11-14 14:32")

    for busy_trip in testing:
        print(f"printing this busy_trip {busy_trip}")
        print(busy_trip)

    busy_employees = work_trip_logic.list_all_busy_employees(
        '2032-11-14 14:32')

    print("TESTING BUSY EMPLOYEES")
    for emp in busy_employees:
        print(f"Employee with ID {emp} is busy this day: 2032-11-14 14:32")


if __name__ == "__main__":
    main()
