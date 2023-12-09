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

    # add type 330MAX
    logic.add_airplane_type(
        type="330MAX", manufacturer="Boeing", capacity="300")

    print("\n Adding airplanes for checks..")
    # Airbus-330,AKN-77
    logic.add_airplane(name="Katla", type="330MAX")
    # logic.add_airplane(name="Sara", type="AKN-77")

    # all_airplanes = logic.list_all_airplanes()
    # for plane in all_airplanes:
    #    print(plane.__dict__)


if __name__ == "__main__":
    main()
