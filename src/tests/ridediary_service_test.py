import unittest
from entities.ride import Ride
from services.ridediary_services import RidediaryService


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
        self.ridediary_service = RidediaryService()

    def test_create_ride(self):
        self.ridediary_service.create_ride("1.1.", "Polle", "Ope", "Talli")
        rides = self.ridediary_service.get_rides()
        self.assertEqual(str(rides[0]), "1.1. - Polle - Ope - Talli")

    def test_get_rides(self):
        self.ridediary_service.create_ride("1.1.", "Polle", "Ope", "Talli")
        self.ridediary_service.create_ride("2.1.", "Pulla", "Valkku", "Talli")
        rides = self.ridediary_service.get_rides()

        self.assertEqual(len(rides), 2)
        self.assertEqual(str(rides[0]), "1.1. - Polle - Ope - Talli")
        self.assertEqual(str(rides[1]), "2.1. - Pulla - Valkku - Talli")

    def test_delete_ride(self):
        self.ridediary_service.create_ride("1.1.", "Polle", "Ope", "Talli")
        self.ridediary_service.create_ride("2.1.", "Pulla", "Valkku", "Talli")

        self.ridediary_service.delete_ride(0)
        rides = self.ridediary_service.get_rides()

        self.assertEqual(str(rides[0]), "2.1. - Pulla - Valkku - Talli")
