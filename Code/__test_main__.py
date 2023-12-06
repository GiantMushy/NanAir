from LogicLayer.DestinationLogic import DestinationManagerLogic

def main():
    destination_manager = DestinationManagerLogic()

    while True:
        print("\n------ Destination Management System ------")
        print("1. Add Destination")
        print("2. List All Destinations")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_destination(destination_manager)
        elif choice == "2":
            list_all_destinations(destination_manager)
        elif choice == "0":
            print("Exiting the Destination Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def add_destination(destination_manager):
    # Get input from the user and call the appropriate logic function
    while True:
        try:
            city = input("Enter City: ")
            destination_manager.is_destination(city)
            break
        except ValueError as error:
            print("ValueError:", error)
    while True:
        try:
            airport = input("Enter Airport: ")
            destination_manager.is_airport(airport)
            break
        except ValueError as error:
            print("ValueError:", error)
    while True:
        try:
            country = input("Enter Country: ")
            destination_manager.is_country(country)
            break
        except ValueError as error:
            print("ValueError:", error)
    while True:
        try:
            distance = input("Enter Distance (km): ")
            destination_manager.is_distance(distance)
            break
        except ValueError as error:
            print("ValueError:", error)  
    while True:
        try:
            travel_time = input("Enter Travel Time (minutes): ")    
            destination_manager.is_travel_time(travel_time)
            break
        except ValueError as error:
            print("ValueError:", error) 
    while True:
        try:
            contact_name = input("Enter Contact Name: ")
            destination_manager.is_contact_name(contact_name)
            break
        except ValueError as error:
            print("ValueError:", error)
    while True:    
        try: 
            contact_phone_number = input("Enter Contact Phone Number: ")
            destination_manager.is_contact_phone_number(contact_phone_number)
            break
        except ValueError as error:
            print("ValueError:", error)
    while True:    
        try:
            destination_manager.add_new_destination(city, airport, country, distance, travel_time, contact_name, contact_phone_number)
            print("Destination added successfully!")
            break
        except Exception as error:
            print("Exception:", error)


def list_all_destinations(destination_manager):
    # Call the logic function to list all destinations
    destinations = destination_manager.list_all_destinations()
    print("\nAll Destinations:")
    for dest in destinations:
        print(dest.__dict__)


if __name__ == "__main__":
    main()