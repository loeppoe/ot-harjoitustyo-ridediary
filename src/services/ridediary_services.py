from entities.ride import Ride
from entities.rider import Rider

class RidediaryService:
    def __init__(self):
        self._user = None
        self._rides = []

    def create_ride(self, date, horse, teacher, stable):
        ride = Ride(date, horse, teacher, stable)
        self._rides.append(ride)

    def get_rides(self):
        return self._rides

    def delete_ride(self):
        None

ridediary_service = RidediaryService()
    
