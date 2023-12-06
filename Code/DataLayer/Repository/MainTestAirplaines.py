from LogicLayer.AirplainesLogicLayer import AirplaineManagerLogic


def main():
    AirplaineManager = AirplaineManagerLogic()

    while True:
        print("\n------ Airplaine Overview ------")
        print("Id of airplaine")
        print("00. Add a Airplaine")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "Id of airplaine":
            UpdatedAirplaines(AirplaineManager)
        elif choice == "2":
            AddAirplaine(AirplaineManager)
        elif choice == "0":
            print("Exiting the Destination Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def AddAirplaine(AirplineManager):
    # Get input from the user and call the appropriate logic function
    while True:
        try:
            NameOfPlaine = input("Enter a Name the Airplaine")
            AirplineManager.IsNameOfPlaine(NameOfPlaine)
            break
        except ValueError as error:
            print("ValueError:", error)
    while True:
        try:
            CurrentLocation = input("Enter Current Location")
            AirplineManager.IsCurrentLocation(CurrentLocation)
            break
        except ValueError as error:
            print("ValueError:", error)
    while True:
        try:
            Type = input("Enter the type of airplaine ")
            AirplineManager.IsType(Type)
            break
        except ValueError as error:
            print("ValueError:", error)
    while True:
        try:
            Manufacturer = input("Enter the manufacturer")
            AirplineManager.IsManufacturer(Manufacturer)
            break
        except ValueError as error:
            print("ValueError:", error)  
    while True:
        try:
            Capacity = input("Enter the airplaines capacity ")    
            AirplineManager.IsCapacity(Capacity)
            break
        except ValueError as error:
            print("ValueError:", error) 
    

def UpdatedAirplaines(AirplaineManager):
    # Call the logic function to Edit airplaines information
    
    

    if __name__ == "__main__":
        main()

