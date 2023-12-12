
from Code.LogicLayer.IsChecks import IsChecks

def test_is_checks():
    # Create an instance of IsChecks
    is_checks = IsChecks()

    try:
        is_checks.is_current_location("                     ")
        print("is_social_security_number passed")
        is_checks.is_social_security_number("")
        print("is_social_security_number passed")
        is_checks.is_social_security_number(" ")
        # print("is_social_security_number passed")
        is_checks.is_social_security_number("0809042360")
        print("is_social_security_number passed")
        # is_checks.is_city("rfkb weuie")
        # print("passed")


    except ValueError as e:
        print(f"is_social_security_number failed: {e}")