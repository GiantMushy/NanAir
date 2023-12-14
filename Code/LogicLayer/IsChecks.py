from datetime import datetime, timedelta


class IsChecks:
    def __init__(self):
        self.punc = '-_'
        self.all_punc = '''!"#$%&\'(')*+,-./:;<=>?@[\\]^_`{|}~¨°'''

    def is_city(self, City):
        if not City or not City.replace(" ", "").isalpha():
            raise ValueError(
                "City must be a non-empty string of alphabetic characters")
        if "  " in City:
            raise ValueError("City cannot contain two or more spaces")

    def is_airport(self, Airport):
        if not Airport or not Airport.replace(" ", "").isalpha():
            raise ValueError(
                "Airport must be a non-empty string of alphabetic characters")
        if not len(Airport) == 3:
            raise ValueError(
                "Airport name must be input as the 3 letter abbreviation (ex. LAX, KEF)")
        if "  " in Airport:
            raise ValueError("Airport cannot contain two or more spaces")

    def is_country(self, Country):
        if not Country or not Country.replace(" ", "").isalpha():
            raise ValueError(
                "Country must be a non-empty string of alphabetic characters")
        if "  " in Country:
            raise ValueError("Country cannot contain two or more spaces")

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
        if (str(Distance))[0] == "0":
            raise ValueError("Distance cannot start with 0")

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
        if (str(travel_time))[0] == 0:
            raise ValueError("Travel time cannot start with 0")

    def is_contact_name(self, Contact_Name):
        if not Contact_Name or not Contact_Name.replace(" ", "").isalpha():
            raise ValueError(
                "Contact Name must be a non-empty string of alphabetic characters")
        if "  " in Contact_Name:
            raise ValueError("Contact Name cannot contain two or more spaces")

    def is_contact_phone_number(self, Contact_Phone_Number):
        # strip "+"" only from the first character if that is the case
        if "  " in Contact_Phone_Number:
            raise ValueError(
                "Contact Phone Number cannot contain two or more spaces")
        Contact_Phone_Number = Contact_Phone_Number.replace(" ", "")
        if Contact_Phone_Number[0:1] == "+":
            Contact_Phone_Number = Contact_Phone_Number[1:] # strips away "+" only from the first character if that is the case
        if not Contact_Phone_Number.replace(" ", "").isdigit():
            raise ValueError("Phone Number must be a positive integer")
        # checks if the number has 10 digits maximum
        if not int(Contact_Phone_Number) <= 9999999999:
            raise ValueError("Phone Number must be 10 digits maximum")
        if not int(Contact_Phone_Number) >= 100:
            raise ValueError("Phone Number must be 3 digits minimum")

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
        if "  " in Name:
            raise ValueError("Name cannot contain two or more spaces")

    def is_current_location(self, Current_Location):
        if not Current_Location or not Current_Location.replace(" ", "").isalpha():
            raise ValueError(
                "Current Location must be a non-empty string of alphabetic characters")
        if not len(Current_Location) < 20:
            raise ValueError("Manufacturer must be less than 20 characters")
        if "  " in Current_Location:
            raise ValueError(
                "Current location cannot contain two or more spaces")

    def is_social_security_number(self, social_security_number):
        if not social_security_number.replace("-", "").replace(" ", "").isdigit():
            raise ValueError(
                "social_security_number must be a positive integer")
        if "  " in social_security_number:
            raise ValueError("Social security number cannot contain two or more spaces")
        social_security_number = social_security_number.replace(" ", "").replace("-", "")

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
        if int(social_security_number[0:2]) > 30 and int(social_security_number[3]) == 4 or int(social_security_number[0:2]) > 30 and int(social_security_number[3]) == 6 or int(social_security_number[0:2]) > 30 and int(social_security_number[3]) == 9 or int(social_security_number[0:2]) > 30 and int(social_security_number[2:4]) == 11:
            raise ValueError("SSN must be a valid date")
        if int(social_security_number[0:2]) > 29 and int(social_security_number[3]) == 2:
            raise ValueError("SSN must be a valid date")

    def is_type(self, Type):
        if not Type:
            raise ValueError("Type must be a non-empty string")
        if "  " in Type:
            raise ValueError("Type cannot contain two or more spaces")
        if len(Type) > 15:
            raise ValueError("Type_str cannot be longer than 15 characters")

    def is_manufacturer(self, Manufacturer):
        if not Manufacturer:
            raise ValueError("Manufacturer must be a non-empty string")
        if "  " in Manufacturer:
            raise ValueError("Manufacturer cannot contain two or more spaces")
        if not Manufacturer.strip(self.punc):
            raise ValueError("Manufacturer cannot be only punctuation")
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
            raise ValueError("No plane in the world has a seat capacity of more than 853")
        if (str(Capacity))[0] == "0": # checks if the number starts with 0
            raise ValueError("Capacity cannot start with 0")


    def is_address(self, address):
        if not address:
            raise ValueError("Address must be a non-empty string")
        if "  " in address:
            raise ValueError("Address cannot contain two or more spaces")
        if len(address) > 20:
            raise ValueError("Address too long")

    def is_email(self, Email):
        if not Email:
            raise ValueError("Email must be a non-empty string")
        if " " in Email:
            raise ValueError("Email cannot contain spaces")
        if not "@" in Email:
            raise ValueError('Email must contain "@"')
        if not "." in Email:
            raise ValueError('Email must contain "."')
        if self.all_punc in Email.strip("@."):
            if len(Email) > 20:
                raise ValueError("Email is too long")

    def departure_date_past(self, departure_date):
        given_datetime = datetime.strptime(departure_date, "%Y-%m-%d")
        now = datetime.now()
        now_date = now.date()
        given_datetime = given_datetime.date()
        if given_datetime < now_date:
            raise ValueError("Date cannot be in the past")

    def departure_datetime_past(self, departure_datetime):
        given_datetime = datetime.strptime(
            departure_datetime, "%Y-%m-%d %H:%M")
        now = datetime.now()
        if given_datetime < now:
            raise ValueError("Date cannot be in the past")

    def is_return_time_dd_rd(self, input_departure_day, input_return_day):
        given_datetime = datetime.strptime(
            input_departure_day, "%Y-%m-%d %H:%M")
        given_returntime = datetime.strptime(
            input_return_day, "%Y-%m-%d %H:%M")
        if not given_datetime < given_returntime:
            raise ValueError("Return time has to be after departure time")

    def is_date(self, date):
        date = date.split('-')
        if not len(date) == 3:
            raise ValueError('Date has to be writen in the correct format (YYYY-MM-DD)')
        if not date[0].isdigit or not date[1].isdigit or not date[2].isdigit:
            raise ValueError('Date has to be (YYYY-MM-DD) with valid integers between the dashes ("-")')

    def flight_sched_destination_validation(self, departure_datetime, return_datetime, destination_obj):
        if int(destination_obj.id) == 1:
            raise ValueError("Cannot fly to HQ")

        if not destination_obj:
            raise ValueError("Destination does not exist")
        difference = datetime.strptime(
            return_datetime, "%Y-%m-%d %H:%M") - datetime.strptime(departure_datetime, "%Y-%m-%d %H:%M")
        destination_travel_time = destination_obj.travel_time
        if difference < (timedelta(minutes=int(destination_travel_time)*1) + timedelta(hours=0.99)):
            raise ValueError(
                "Time between flights is too short, allow 1 hr overhead to refuel plane abroad.")
