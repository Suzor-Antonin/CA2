from django.test import TestCase
from .models import Building


class BuildingModelTests(TestCase):

    # negative test
    def test_number_floors_can_be_less_than_one(self):
        """If there is a building, its number of floors cannot be less than 1.
        The case of negative floors number is taken care of by the `PositiveSmallIntegerField`.
        We still need to ensure that a building cannot have a number of floors equal to 0."""
        building_zero_floors = Building.objects.create(floors=0)
        self.assertTrue(building_zero_floors.floors > 0)

    # positive test
    def test_address_function_works_correctly(self):
        """Testing whether the get_address2 works properly or not."""
        sample_building = Building.objects.create(country="Country name", city="City name", street="Street name", number="15")
        self.assertTrue(sample_building.get_address2() == "Country name, City name, Street name, 15")
