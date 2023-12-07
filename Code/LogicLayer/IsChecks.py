from DataLayer.DataLayerAPI import DataLayerAPI
class IsChecks:
    def __init__(self):
        self.destination_data = DataLayerAPI()
        self.punc = '-_'

    def is_city(self, City):
        if not City or not City.replace(" ", "").isalpha():
            raise ValueError("City must be a non-empty string of alphabetic characters")

    def is_airport(self, Airport):
        if not Airport or not Airport.replace(" ", "").isalpha():
            raise ValueError("Airport must be a non-empty string of alphabetic characters")

    def is_country(self, Country):
        if not Country or not Country.replace(" ", "").isalpha():
            raise ValueError("Country must be a non-empty string of alphabetic characters")

    def is_distance(self, Distance):
        if not Distance.isdigit():
            raise ValueError("Distance must be a positive integer")
        try:
            Distance = int(Distance)
        except ValueError:
            raise ValueError("Distance must be numeric")
        if Distance > 20000:
            raise ValueError("Distance must be less than 20,000km (half the circumference of the Earth)")

    def is_travel_time(self, Travel_Time):
        if not Travel_Time.isdigit():
            raise ValueError("Travel Time must be a positive integer")
        try:
            Travel_Time = int(Travel_Time)
        except:
            raise ValueError("Travel Time and must be numeric")

    def is_contact_name(self, Contact_Name):
        if not Contact_Name or not Contact_Name.replace(" ", "").isalpha():
            raise ValueError("Contact Name must be a non-empty string of alphabetic characters")

    def is_contact_phone_number(self, Contact_Phone_Number):
        if not Contact_Phone_Number.replace(" ", "").isdigit():
            raise ValueError("Contact Phone Number must be a positive integer")
        try:
            Contact_Phone_Number = int(Contact_Phone_Number.replace(" ", ""))
        except:
            raise ValueError("Contact Phone Number must be numeric")

    def is_name(self, Name):
        if not Name or not Name.replace(" ", "").isalpha():
            raise ValueError("Name must be a non-empty string of alphabetic characters")

    def is_current_location(self, Current_Location):
        if not Current_Location or not Current_Location.replace(" ", "").isalpha():
            raise ValueError("Current Location must be a non-empty string of alphabetic characters")

    def is_social_security_number(self, social_security_number):
        if not social_security_number.replace(" ", "").isdigit():
            raise ValueError("social_security_number must be a positive integer")
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
            raise ValueError("Birth dat in social_security_number is too young or not born yet")
        
    def is_type(self, Type):
        if not Type:
            raise ValueError("Type must be a non-empty string")

    def is_manufacturer(self, Manufacturer):
        if not Manufacturer or not Manufacturer.replace(" ", "").isalpha():
            raise ValueError("Manufacturer must be a non-empty string of alphabetic characters")

    def is_capacity(self, Capacity):
        if not Capacity.isdigit():
            raise ValueError("Capacity must be a positive integer")
        try:
            Capacity = int(Capacity)
        except ValueError:
            raise ValueError("Capacity must be numeric")
        if Capacity > 853:
            raise ValueError("No plane in the world has a seat capacity of more than 853")

    def is_address(self, adress):
        if not adress or not adress.replace(" ", "").isalpha():
            raise ValueError("Address must be a non-empty string of alphabetic characters")

    def is_email(self, Email):
        if not Email or not Email.replace(" ", "").strip("@.").isalpha():
            raise ValueError("Email must be a non-empty string of alphabetic characters")

    def is_employee_type(self, employee_type):
        if not employee_type:
            raise ValueError("Employee Type field cannot be empty")
        input_str = employee_type.replace(" ", "").strip(self.punc).lower()
        if input_str != "pilot" and input_str != "flightattendant":
            raise ValueError("Employee Type must be either 'Pilot' or 'Flight Attendant'")

    def is_employee_role(self, employee_role):
        if not employee_role:
            raise ValueError("Employee Role field cannot be empty")
        input_str = employee_role.replace(" ", "").strip(self.punc).lower()
        if input_str != "captain" and input_str != "copilot" and input_str != "seniorflightattendant" and input_str != "flightattendant":
            raise ValueError("Employee Role must be either 'Captain','Co-Pilot','Senior Flight Attendant' or 'Flight Attendant'")