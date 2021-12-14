class Ride:
    """Luokka, jolla luodaan Ride-olio
    """

    def __init__(self, date, horse, teacher, stable):
        """Luokan konstruktori, jolla luodaan Ride-olio

        Args:
        date: päivämäärä
        horse: hevonen
        teacher: opettaja/valmentaja
        stable: talli/paikka
        """
        self.date = date
        self.horse = horse
        self.teacher = teacher
        self.stable = stable

    def __str__(self):
        """Muodostaa ride-oliosta merkkijonon.
        
        Returns:
        Merkkijonon, joka kertoo ride-olion sisällön
        """
        return f"{self.date} - {self.horse} - {self.teacher} - {self.stable}"
