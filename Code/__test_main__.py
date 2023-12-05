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
    city = input("Enter City: ")
    airport = input("Enter Airport: ")
    country = input("Enter Country: ")
    distance = int(input("Enter Distance (km): "))
    travel_time = int(input("Enter Travel Time (minutes): "))
    contact_name = input("Enter Contact Name: ")
    contact_phone_number = input("Enter Contact Phone Number: ")

    destination_manager.add_destination(city, airport, country, distance, travel_time, contact_name, contact_phone_number)
    print("Destination added successfully!")

def list_all_destinations(destination_manager):
    # Call the logic function to list all destinations
    destinations = destination_manager.list_all_destinations()
    print("\nAll Destinations:")
    for dest in destinations:
        print(dest.__dict__)


if __name__ == "__main__":
    main()
