from LogicLayer.EmployeeManagerLogic import EmployeeManagerLogic
import random


def generate_random_phone():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])


def generate_random_ssn():
    return f"{random.randint(100000, 999999)}-{random.randint(1000, 9999)}"


def add_sample_employees(logic):
    employee_details = [
        ('pilot', 'Matti', "Mac street 1"),
        ('pilot', 'Sara', "Microsoft street 1"),
        ('flight_attendant', 'Raggi', "AMZN street 1"),
        ('flight_attendant', 'Banani', "FB street 1"),
        ('flight_attendant', 'Epli', "Apple street 1")
    ]

    for employee_type, name, address in employee_details:
        try:
            logic.add_employee(
                employee_type,
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


def test_generate_unique_employee_id():
    logic = EmployeeManagerLogic()
    new_id = logic.generate_unique_employee_id()
    assert isinstance(new_id, str), "ID should be a string"
    assert new_id.isdigit(), "ID should be numeric"
    assert len(new_id) == 3, "ID should have a length of 3"


def test_add_employee():
    logic = EmployeeManagerLogic()
    add_sample_employees(logic)


def test_list_all_employees():
    logic = EmployeeManagerLogic()
    employees = logic.list_all_employees()
    print("\nList of All Employees:")
    for emp in employees:
        print(emp.__dict__)
    assert isinstance(employees, list), "Should return a list"


def test_list_all_pilots():
    logic = EmployeeManagerLogic()
    pilots = logic.list_all_pilots()
    print("\nList of All Pilots:")
    for pilot in pilots:
        print(pilot)
    assert isinstance(pilots, list), "Should return a list"


def test_list_all_flight_attendants():
    logic = EmployeeManagerLogic()
    flight_attendants = logic.list_all_flight_attendants()
    print("\nList of All Flight Attendants:")
    for attendant in flight_attendants:
        print(attendant)
    assert isinstance(flight_attendants, list), "Should return a list"


def run_tests():
    test_generate_unique_employee_id()
    test_add_employee()
    test_list_all_employees()
    test_list_all_pilots()
    test_list_all_flight_attendants()
    print("\nSuccessfully ran all tests")


if __name__ == "__main__":
    run_tests()
