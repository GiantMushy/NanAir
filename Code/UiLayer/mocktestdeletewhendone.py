from LogicLayer.AirplainesLogicLayer import AirplaineManagerLogic
import random

def generate_random_airplane_name():
    # Generate a random airplane name for testing
    return f"Plane{random.randint(100, 999)}"

def add_sample_airplanes(logic):
    airplane_details = [
        ("Boeing 747", "Reykjavik", "Commercial", "Boeing", 400),
        ("Airbus A320", "Nuuk", "Commercial", "Airbus", 180),
        # Add more sample airplanes as needed
    ]

    for name, location, type, manufacturer, capacity in airplane_details:
        try:
            logic.AddAirplaine(name, location, type, manufacturer, capacity)
            print(f"Added airplane named {name}")
        except Exception as e:
            print(f"Error occurred while adding airplane named {name}: {e}")

def test_list_all_airplanes():
    logic = AirplaineManagerLogic()
    airplanes = logic.get_all_airplanes()
    print("\nList of All Airplanes:")
    for airplane in airplanes:
        print(airplane)

def run_tests():
    logic = AirplaineManagerLogic()

    # Test adding sample airplanes
    add_sample_airplanes(logic)

    # Test listing all airplanes
    test_list_all_airplanes()

    print("\nSuccessfully ran all tests")

if __name__ == "__main__":
    run_tests()
