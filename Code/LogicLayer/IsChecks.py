from DataLayer.DataLayerAPI import DataLayerAPI


class IsChecks:
    def __init__(self):
        self.destination_data = DataLayerAPI()
        self.punc = '-_'

    def is_city(self, City):
        if not City or not City.replace(" ", "").isalpha():
            raise ValueError(
                "City must be a non-empty string of alphabetic characters")

    def is_airport(self, Airport):
        if not Airport or not Airport.replace(" ", "").isalpha():
            raise ValueError(
                "Airport must be a non-empty string of alphabetic characters")
        if len(Airport) > 3:
            raise ValueError(
                "Airport name must be input as the 3 letter abbreviation (ex. LAX, KEF)")

    def is_country(self, Country):
        if not Country or not Country.replace(" ", "").isalpha():
            raise ValueError(
                "Country must be a non-empty string of alphabetic characters")

    def is_distance(self, Distance):
        if not Distance.isdigit():
            raise ValueError("Distance must be a positive integer")
        try:
            Distance = int(Distance)
        except ValueError:
            raise ValueError("Distance must be numeric")
        if Distance > 20000:
            raise ValueError(
                "Distance must be less than 20,000km (half the circumference of the Earth)")

    def is_travel_time(self, Travel_Time):
        if not Travel_Time.isdigit():
            raise ValueError("Travel Time must be a positive integer")
        try:
            Travel_Time = int(Travel_Time)
        except:
            raise ValueError("Travel Time and must be numeric")
        travel_time = int(Travel_Time)
        if travel_time > 1120:
            raise ValueError(
                "Longest Commercial Flight in the world is/was 1120min, be realistic")

    def is_contact_name(self, Contact_Name):
        if not Contact_Name or not Contact_Name.replace(" ", "").isalpha():
            raise ValueError(
                "Contact Name must be a non-empty string of alphabetic characters")

    def is_contact_phone_number(self, Contact_Phone_Number):
        # strip "+"" only from the first character if that is the case
        Contact_Phone_Number = Contact_Phone_Number.replace(" ", "")
        if Contact_Phone_Number[0:1] == "+":
            Contact_Phone_Number = Contact_Phone_Number[1:]
        if not Contact_Phone_Number.replace(" ", "").isdigit():
            raise ValueError("Phone Number must be a positive integer")
        # checks if the number has 10 digits maximum
        if not int(Contact_Phone_Number) <= 9999999999:
            raise ValueError("Phone Number must be 10 digits maximum")
        try:
            Contact_Phone_Number = int(Contact_Phone_Number.replace(" ", ""))
        except:
            raise ValueError("Phone Number must be numeric")

    def is_home_phone(self, home_phone):
        if not home_phone:
            pass
        else:
            home_phone = self.is_contact_phone_number(home_phone)

    def is_name(self, Name):
        if not Name:
            raise ValueError("Name must be a non-empty string")
        if not Name.replace(" ", "").isalpha():
            raise ValueError(
                "Get out of here 'X Æ A-12' We dont allow numbers or symbols in our names")

    def is_current_location(self, Current_Location):
        if not Current_Location or not Current_Location.replace(" ", "").isalpha():
            raise ValueError(
                "Current Location must be a non-empty string of alphabetic characters")
        if not len(Current_Location) < 20:
            raise ValueError("Manufacturer must be less than 20 characters")

    def is_social_security_number(self, social_security_number):
        if not social_security_number.replace(" ", "").isdigit():
            raise ValueError(
                "social_security_number must be a positive integer")
        social_security_number = social_security_number.replace(" ", "")
        try:
            social_security_number_int = int(social_security_number)
        except:
            raise ValueError("social_security_number must be numeric")
        if len(social_security_number) != 10:
            raise ValueError("social_security_number must be 10 digits")
        if int(social_security_number[0:2]) > 31 or int(social_security_number[2:4]) > 12 or (social_security_number[-1] != "0" and social_security_number[-1] != "9"):
            raise ValueError("social_security_number must be a valid date")
        if int(social_security_number[4:6]) > 10 and social_security_number[-1] == "0":
            raise ValueError(
                "Birth dat in social_security_number is too young or not born yet")
        if int(social_security_number[0:2]) > 30 and int(social_security_number[3]) == 4 or int(social_security_number[3]) == 6 or int(social_security_number[3]) == 9 or int(social_security_number[2:4]) == 11:
            raise ValueError("SSN must be a valid date")
        if int(social_security_number[0:2]) > 29 and int(social_security_number[3]) == 2:
            raise ValueError("SSN must be a valid date")

    def is_type(self, Type):
        if not Type:
            raise ValueError("Type must be a non-empty string")
        if len(Type) > 15:
            raise ValueError("Type_str cannot be longer than 15 characters")

    def is_manufacturer(self, Manufacturer):
        if not Manufacturer:
            raise ValueError("Manufacturer must be a non-empty string")
        if len(Manufacturer) > 20:
            raise ValueError(
                "Manufacturer name cannot be longer than 20 characters")

    def is_capacity(self, Capacity):
        if not Capacity.isdigit():
            raise ValueError("Capacity must be a positive integer")
        try:
            Capacity = int(Capacity)
        except ValueError:
            raise ValueError("Capacity must be numeric")
        if Capacity > 853:
            raise ValueError(
                "No plane in the world has a seat capacity of more than 853")

    def is_address(self, address):
        if not address:
            raise ValueError("Address must be a non-empty string")
        if len(address) > 20:
            raise ValueError("Address too long")

    def is_email(self, Email):
        if not Email:
            raise ValueError("Email must be a non-empty string")
        if len(Email) > 20:
            raise ValueError("Email is too long")

    def is_employee_type(self, employee_type):
        if not employee_type:
            raise ValueError("Employee Type field cannot be empty")
        input_str = employee_type.replace(" ", "").strip(self.punc).lower()
        if input_str != "pilot" and input_str != "flightattendant":
            raise ValueError(
                "Employee Type must be either 'Pilot' or 'Flight Attendant'")

    def is_employee_role(self, employee_role):
        if not employee_role:
            raise ValueError("Employee Role field cannot be empty")
        input_str = employee_role.replace(" ", "").strip(self.punc).lower()
        if input_str != "captain" and input_str != "copilot" and input_str != "seniorflightattendant" and input_str != "flightattendant":
            raise ValueError(
                "Employee Role must be either 'Captain','Co-Pilot','Senior Flight Attendant' or 'Flight Attendant'")
