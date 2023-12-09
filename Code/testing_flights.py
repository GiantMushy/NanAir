from LogicLayer.LogicLayerAPI import LogicLayerAPI
from datetime import datetime, timedelta


def main():
    logic = LogicLayerAPI()

    # add pilot objects

    logic.add_employee("pilot", "Captain", airplane_type="AKN-77", name="Matthíass",
                       social_security_number="69699696969",
                       mobile_phone_number="8547345",
                       address="Oldugrandi",
                       email_address="fun@gmail.com")

    print("Added Mr.Matti as captain successfully!")

    print("\n Adding airplanes for checks..")
    # Airbus-330,AKN-77

    logic.add_airplane_type(
        type="AKN-77", manufacturer="Boeing", capacity="300")
    logic.add_airplane(name="Katla", type="AKN-77")
    logic.add_airplane(name="Sara", type="AKN-77")

    print("\n Airplane Katla and Sara added successfully!")

    print("\n Adding destinations for checks..")
    logic.add_destination(city="Matta city", airport="Matti airport", country="Mattaland",
                          distance='6', travel_time='200',	contact_name="Helgi", contact_phone_number="9876543")

    print("\n Destination Matta city added successfully!")
    # now the question is how worktrips should work
    # we now need to choose an airplane for a worktrip, however
    # that doesnt get added to the worktrip object, it gets added to the 2 flight objects
    # that get created, in work_trip_logic.py,
    # what connects the Flight object to the WorkTrip object is the flight numbers of the two flights
    # so we need to create the flights first, then create the worktrip

    # fyrir work trip þarf að slá inn
    # áfangastað
    # brottför frá íslandi
    # brottför frá áfangastað
    # flugvélatýpu (úr lista)

    # það verður hægt að endurtaka þá vinnuferð

    # þetta eru allar upplýsingarnar sem við fáum,

    # skref 1, láta add_work_trip taka inn flugvélina sem flýgur

    # núna er hægt að búa til vinnuferðir
    # virknin sem við þurfum að bæta við er að það eru flug í hverri vinnuferð
    # með flugnúmerum

    print("test adding worktrip")
    # find destination object to add to work trip
    destinations = logic.list_all_destinations()
    # use airplane id 001 for worktrip
    logic.add_work_trip(
        "02", '2032-11-14 14:32', '2032-11-14 22:32', '001')

    print("\n Worktrip added successfully!")

    # listing all work trips
    print("\n Listing all work trips")
    work_trips = logic.list_all_work_trips()
    for trip in work_trips:
        print(trip.__dict__)

    # listing all flights
    print("\n Listing all flights")
    flights = logic.list_all_flights()
    for flight in flights:
        print(flight.__dict__)

    # add new destination
    print("\n Adding new destination")
    logic.add_destination(city="New city", airport="New airport", country="New country",
                          distance='6', travel_time='200',	contact_name="Helgi", contact_phone_number="9876543")

    print("\n New destination added successfully!")

    # adding new worktrip to new destination
    print("\n Adding new worktrip to new destination")
    # use airplane id 001 for worktrip
    logic.add_work_trip(
        "02", '2032-11-15 14:32', '2032-11-15 22:32', '001')

    logic.add_work_trip(
        "02", '2032-11-16 14:32', '2032-11-16 22:32', '001')

    logic.add_crew_member("001", "001")

    logic.change_sold_tickets("NA020", "50")

    # print(logic.all_work_trips_of_employee("001"))

    print("\n 50 sold tickets added!")
    print("\n Getting sold tickets for flight NA020")
    print(logic.get_sold_tickets("NA020"))
    print("\n Getting available tickets for flight NA020")
    print(logic.get_available_tickets("NA020"))

    wttest = logic.work_trip_validity_period("weekly", '2032-11-15 14:32')
    for trip in wttest:
        print(trip.__dict__)

    print("\n Testing listing all flights")
    all_airplanes = logic.list_airplanes_detailed()

    for airplane in all_airplanes:
        print(airplane.__dict__)


if __name__ == "__main__":
    main()
