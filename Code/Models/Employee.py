
class Employee:
    def __init__(self, id, name, social_security_number, address, mobile_phone_number, email_address, home_phone_number=None):
        self.id = id
        self.name = name
        self.social_security_number = social_security_number
        self.address = address
        self.mobile_phone_number = mobile_phone_number
        self.email_address = email_address
        self.home_phone_number = home_phone_number
