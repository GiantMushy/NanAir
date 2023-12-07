from LogicLayer import EmployeeManagerLogic


class ValidationService:    
    def get_mock_work_trips(self):        
        """Temporary method to return detailed mock destinations."""         
        mock_worktrips = [{'id': '001', 'destination': "{'country': 'Greenland', 'airport': 'Nuuk Airport', 'flight_time': '3h', 'distance_from_iceland': '1500km', 'contact_name': 'John Nuuk', 'emergency_phone': '765467'}", 'departure_datetime': datetime.datetime(2012, 11, 14, 14, 32), 'return_datetime': datetime.datetime(2012, 11, 14, 20, 32), 'crew_members': ''},    
                      {'id': '002', 'destination': "{'country': 'Greenland', 'airport': 'Nuuk Airport', 'flight_time': '3h', 'distance_from_iceland': '1500km', 'contact_name': 'John Nuuk', 'emergency_phone': '765467'}", 'departure_datetime': datetime.datetime(2011, 11, 14, 14, 32), 'return_datetime': datetime.datetime(2011, 11, 14, 20, 32), 'crew_members': '001,002,003'}]  
        return mock_worktrips

    def validate_work_trip(self, trip):
        pass

    def validate_employee_availability(self, employee):
        pass
