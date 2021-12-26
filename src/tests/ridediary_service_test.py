import unittest
from entities.ride import Ride
from services.ridediaryservicestest import RidediaryServiceTest


class TestRide(unittest.TestCase):
    def setUp(self):
        date = "12.3."
        horse = "Polle"
        teacher = "Ope"
        stable = "Talli"
        self.ride = Ride(date, horse, teacher, stable)

    def test_created_ride_looks_right(self):
        self.assertEqual(str(self.ride), "12.3. - Polle - Ope - Talli")


class TestRidediaryService(unittest.TestCase):
    def setUp(self):
        self.ridediary_service = RidediaryServiceTest()

    def test_create_ride(self):
        None

    def test_get_rides(self):
        None

    def test_delete_ride(self):
        None
