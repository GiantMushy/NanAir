from LogicLayer.AirplainesLogicLayer import AirplaineManagerLogic
import random

def generate_random_airplane_name():
    #generate a random airplane name for testing
    return f"Plane{random.randint(100, 999)}"

def add_sample_airplanes(logic):
    airplane_details = [
        ("Oliver", "Reykjavik", "DHC-8-200", "De Havilland", 37),
        ("Benjamín", "Nuuk", "DHC-8-400", "De Havilland", 76),
        #add more sample airplanes as needed
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

    #test adding sample airplanes
    add_sample_airplanes(logic)

    #test listing all airplanes
    test_list_all_airplanes()

    print("\nSuccessfully ran all tests")

if __name__ == "__main__":
    run_tests()
