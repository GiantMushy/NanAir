from Code.LogicLayer.LogicLayerAPI import LogicLayerAPI
from datetime import datetime, timedelta
import random


logic = LogicLayerAPI()


def generate_random_phone():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])


def generate_random_ssn():
    return f"{random.randint(100000, 999999)}-{random.randint(1000, 9999)}"


def add_sample_employees():
    '''
    When adding employees, the following changes have been done, a pilot flies a certain airplane type, which can't be None if employee 
    type is pilot. A flight attendant has no airplane type, and can and should be None.
    '''

    employee_details_pilots = [
        ('pilot', 'Captain', 'AKN-77', 'Matti', "Mac street 1"),
        ('pilot', 'Co-Pilot', 'AKN-77', 'Sara', "Microsoft street 1"),

    ]

    employ_details_flight_attendants = [
        ('flight_attendant', 'Senior Flight Attendant', 'Raggi', "AMZN street 1"),
        ('flight_attendant', 'Flight Attendant', 'Banani', "FB street 1"),
        ('flight_attendant', 'Flight attendant', 'Epli', "Apple street 1")
    ]

    for employee_type, employee_role, name, address in employ_details_flight_attendants:
        try:
            logic.add_employee(
                employee_type,
                employee_role,
                name=name,
                social_security_number=generate_random_ssn(),
                mobile_phone_number=generate_random_phone(),
                address=address,
                email_address=f"example{random.randint(1, 100)}@gmail.com"
            )
            print(f"Added {employee_type} named {name}")
        except Exception as e:
            print(
                f"Error occurred while adding {employee_type} named {name}: {e}")

    for employee_type, employee_role, airplane_type, name, address in employee_details_pilots:
        try:
            logic.add_employee(
                employee_type,
                employee_role,
                airplane_type=airplane_type,
                name=name,
                social_security_number=generate_random_ssn(),
                mobile_phone_number=generate_random_phone(),
                address=address,
                email_address=f"example{random.randint(1, 100)}@gmail.com"
            )
            print(f"Added {employee_type} named {name}")
        except Exception as e:
            print(
                f"Error occurred while adding {employee_type} named {name}: {e}")


def add_airplanes():
    '''It is simportant that the airplane type exists before adding an airplane.
    The reason is to obtain the capacity of the airplane type, we don't want same types of airplanes
    to have different capacities becauses of user input. This way a type is only added once'''

    logic.add_airplane_type(
        type="AKN-77", manufacturer="Boeing", capacity="300")
    logic.add_airplane(name="Katla", type="AKN-77")
    logic.add_airplane(name="Sara", type="AKN-77")


def add_destinations():
    '''
    first step when creating a worktrip is to have destinations created already.
    A thing that was required to do was to always create one destination, the headquarters or RKV. So when listing destinations
    it will always be there.
    '''
    logic.add_destination(city="Matta city", airport="Matti airport", country="Mattaland",
                          distance='6', travel_time='40',	contact_name="Helgi", contact_phone_number="9876543")
    logic.add_destination(city="London", airport="Heathrow", country="England", distance='6',
                          travel_time='40',	contact_name="Helgi", contact_phone_number="9876543")


def add_work_trips():
    '''
    When adding work trips, the main functionality is the two flights that are created for each trip.
    '''
    departure_date_time_now = datetime.now() + timedelta(minutes=1)
    return_datetime_now = departure_date_time_now + timedelta(hours=6)
    departure_date_time_str = departure_date_time_now.strftime(
        '%Y-%m-%d %H:%M')
    return_datetime_str = return_datetime_now.strftime('%Y-%m-%d %H:%M')

    logic.add_work_trip("02", departure_date_time_str,
                        return_datetime_str, "001")

    departure_date_time_now = datetime.now() + timedelta(minutes=3)
    return_datetime_now = departure_date_time_now + timedelta(hours=6)
    departure_date_time_str = departure_date_time_now.strftime(
        '%Y-%m-%d %H:%M')
    return_datetime_str = return_datetime_now.strftime('%Y-%m-%d %H:%M')

    logic.add_work_trip("03", departure_date_time_str,
                        return_datetime_str, "002")


def list_object(list_of_dicts):
    for obj in list_of_dicts:
        if isinstance(obj, dict):
            print_dict_in_readable_format(obj)
        else:
            print_dict_in_readable_format(obj.__dict__)
        print("\n")


def print_dict_in_readable_format(data_dict):
    max_key_length = 0
    for key in data_dict.keys():
        if len(f"{key}") > max_key_length:
            max_key_length = len(f"{key}")

    for key, value in data_dict.items():
        key_str = f"{key}".ljust(max_key_length)

        # check if nested dict
        if isinstance(value, dict):
            print_dict_in_readable_format(value)
        else:
            print(f"{key_str} : {value}")


def add_crew_member_wt():
    '''
    When adding crew members to a work trip, the following changes have been done, a pilot flies a certain airplane type, which can't be None if employee 
    type is pilot. A flight attendant has no airplane type, and can and should be None.
    '''
    logic.add_crew_member("001", "004")
    logic.add_crew_member("001", "002")
    logic.add_crew_member("001", "004")


def print_all_types_of_data():
    print("Printing all types of data")
    print("Printing all airplanes")
    list_object(logic.list_airplanes_detailed())
    print("Printing all airplane types")
    list_object(logic.list_all_airplane_types())
    print("Printing all destinations")
    list_object(logic.list_all_destinations())
    print("Printing all employees")
    list_object(logic.list_all_employees())
    print("Printing all flights")
    list_object(logic.list_all_flights())
    print("Printing all work trips")
    list_object(logic.list_all_work_trips())
    print("Printing all work trip employees")
    list_object(logic.all_work_trips_of_employee("002", "2023-12-10 20:32"))
    print("Work trip validity test")
    list_object(logic.work_trip_validity_period("weekly", '2023-12-10 19:32'))
    print("Listing all employees working and their destinations")
    list_object(logic.list_employees_working_and_destinations(
        '2023-12-10 19:32'))
    print("Listing all available employees")
    all_avlb_emp = logic.list_all_available_employees('2023-12-10 19:32')
    for id in all_avlb_emp:
        print(id)
    print("listing info on employee")
    print((logic.find_employee_by_id("001")).__dict__)
    print("All pilots with licences on type AKN-77")
    list_object(logic.list_pilots_by_airplane_type("AKN-77"))
    print("Listing pilots after airplane types they're allowed to fly.")
    list_object(logic.list_pilots_sorted_by_airplane_type())


def update_emergency_contact():
    logic.update_emergency_contact("02", "Matti", "1234567")


def add_extra_airplane():
    logic.add_airplane_type(
        type="BOEING747", manufacturer="Boeing", capacity="300")
    logic.add_airplane(name="Mikki", type="BOEING747")
    logic.add_airplane(name="Karl", type="BOEING747")


def add_extra_employees():
    logic.add_employee(
        employee_type="pilot",
        employee_role="Captain",
        airplane_type="BOEING747",
        name="Mikael",
        social_security_number=generate_random_ssn(),
        mobile_phone_number=generate_random_phone(),
        address="Mikael street 1",
        email_address=f"example{random.randint(1, 100)}@gmail.com"
    )
    logic.add_employee(
        employee_type="pilot",
        employee_role="Co-Pilot",
        airplane_type="BOEING747",
        name="Karl",
        social_security_number=generate_random_ssn(),
        mobile_phone_number=generate_random_phone(),
        address="Karl street 1",
        email_address=f"example{random.randint(1, 100)}@gmail.com"
    )
    logic.add_employee(
        employee_type="flight_attendant",
        employee_role="Senior Flight Attendant",
        name="Raggi",
        social_security_number=generate_random_ssn(),
        mobile_phone_number=generate_random_phone(),
        address="Raggi street 1",
        email_address=f"example{random.randint(1, 100)}@gmail.com"
    )
    logic.add_employee(
        employee_type="flight_attendant",
        employee_role="Flight Attendant",
        name="Banani",
        social_security_number=generate_random_ssn(),
        mobile_phone_number=generate_random_phone(),
        address="Banani street 1",
        email_address=f"example{random.randint(1, 100)}@gmail.com"
    )
    logic.add_employee(
        employee_type="flight_attendant",
        employee_role="Flight Attendant",
        name="Epli",
        social_security_number=generate_random_ssn(),
        mobile_phone_number=generate_random_phone(),
        address="Epli street 1",
        email_address=f"example{random.randint(1, 100)}@gmail.com"
    )


def test_trying_to_use_airplane_twice():
    departure_date_time_now = datetime.now() + timedelta(minutes=1)
    return_datetime_now = departure_date_time_now + timedelta(hours=6)
    departure_date_time_str = departure_date_time_now.strftime(
        '%Y-%m-%d %H:%M')
    return_datetime_str = return_datetime_now.strftime('%Y-%m-%d %H:%M')

    logic.add_work_trip("02", departure_date_time_str,
                        return_datetime_str, "003")


def testing_datetime(departure_string):
    '''
    :param departure_string: string datetime on the format. In string format %Y-%m-%d %H:%M f.x. "2022-12-14 14:13"

    2023-12-10 14:50
    '''
    departure_datetime = datetime.strptime(departure_string, "%Y-%m-%d %H:%M")
    print(f"new departure datetime: {departure_datetime}")
    departure_datetime_plus_week = departure_datetime + timedelta(days=7)
    print(f"departure plus one week {departure_datetime_plus_week}")
    departure_plus_week_string = departure_datetime_plus_week.strftime(
        "%Y-%m-%d %H:%M")
    print(f"departure string: {departure_plus_week_string}")
    today = datetime.now()
    print(f"right now {today}")


def main():
    add_sample_employees()
    add_airplanes()
    add_destinations()
    add_work_trips()
    add_crew_member_wt()
    # update_emergency_contact()
    # add_extra_airplane()
    # add_extra_employees()
    # test_trying_to_use_airplane_twice()
    # testing_datetime("2023-12-15 14:50")
    print_all_types_of_data()


if __name__ == "__main__":
    main()
