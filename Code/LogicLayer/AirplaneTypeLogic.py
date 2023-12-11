from Code.DataLayer.DataLayerAPI import DataLayerAPI
from Code.Models.AirplaneType import AirplaneType


class AirplaneTypeLogic:
    def __init__(self):
        self.airplane_type_data = DataLayerAPI()

    def add_airplane_type(self, **kwargs):
        """
        Adds a new airplane type to the system.
        Validates required fields before adding.

        :param kwargs: Attributes of the airplane type.
        :raises ValueError: If required fields are missing or empty.
        """
        required_fields = ['type', 'manufacturer', 'capacity']
        if any(kwargs.get(field) is None or kwargs.get(field) == '' for field in required_fields):
            raise ValueError("Required fields cannot be empty.")

        # if same type already added to sytem raise error
        for airplane in self.list_all_airplane_types():
            if airplane.type == kwargs['type']:
                raise ValueError("Airplane type already exists.")

        # add general employee information
        new_airplane_type = AirplaneType(**kwargs)
        self.airplane_type_data.add_airplane_type(new_airplane_type)

    def list_all_airplane_types(self):
        """Returns a list of all airplane types."""
        return self.airplane_type_data.read_all_airplane_types()

    def find_type_data(self, airplane_type):
        """
        Finds an airplane type object by their type.

        :param airplane_type: type of the airplane to find.
        Returns, return: airplane object if found, None otherwise.
        """
        for airplane in self.list_all_airplane_types():
            if airplane.type == airplane_type:
                return airplane
        return None

    # B-requirements will be implemented  here.
