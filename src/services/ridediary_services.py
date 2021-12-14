from entities.ride import Ride


class RidediaryService:
    """ Sovelluslogiikasta vastaava luokka."""

    def __init__(self):
        """ Luokan konstruktori. Luo sovelluslogiikasta vastaavan olion."""
        
        self._user = None
        self._rides = open("rides.txt", "a+")

    def create_ride(self, date, horse, teacher, stable):
        """ Luo uuden ride-olion ja kirjoittaa sen tiedostoon.
        
        Args:
            date: päivämäärä
            horse: hevonen
            teacher: opettaja/valmentaja
            stable: talli/paikka"""
        
        ride = Ride(date, horse, teacher, stable)
        self._rides.write(str(ride) + "\n")

    def get_rides(self):
        """ Palauttaa tiedostossa olevat ride-oliot"""
        return self._rides.readlines()

    def delete_ride(self, i):
        """ Poistaa rivin tiedostosta indeksin perusteella."""
        
        rides = open("rides.txt", "r")
        lines = rides.readlines()
        rides.close()
        del lines[int(i)]
        new_file = open("rides.txt", "w+")
        for line in lines:
            new_file.write(line)
        new_file.close()


ridediary_service = RidediaryService()
