class Ride:
    def __init__(self, date, horse, teacher, stable):
        self.date = date
        self.horse = horse
        self.teacher = teacher
        self.stable = stable

    def __str__(self):
        return f"{self.date} - {self.horse} - {self.teacher} - {self.stable}"
