from Code.DataLayer.DataLayerAPI import DataLayerAPI

from Code.LogicLayer.IsChecks import IsChecks

def test_is_checks():
    # Create an instance of IsChecks
    is_checks = IsChecks()

    try:
        is_checks.is_return_time_dd_rd("2023-12-12 19:00", "2023-12-12 21:00")
        print("")
        print(" ------")
        print("|passed|")
        print(" ------")
        print("")

    except ValueError as e:
        print("")
        print(f"failed: {e}")
        print("")

def main():
    test_is_checks()

if __name__ == "__main__":
    main()
