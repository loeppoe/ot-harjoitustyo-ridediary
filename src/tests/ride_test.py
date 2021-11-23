import unittest
from entities.ride import Ride

class TestRide(unittest.TestCase):
    def setUp(self):
        date = "12.3."
        horse = "Polle"
        teacher = "Ope"
        stable = "Talli"
        self.ride = Ride(date, horse, teacher, stable)

    def test_created_ride_looks_right(self):
        self.assertEqual(str(self.ride), "12.3. - Polle - Ope - Talli")