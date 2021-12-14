from tkinter import ttk, constants
from services.ridediary_services import ridediary_service


class RidesView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._rides = open("rides.txt", "r+")

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_new_ride(self):
        date_header = ttk.Label(master=self._root, text="Päivämäärä")
        horse_header = ttk.Label(master=self._root, text="Hevonen")
        instructor_header = ttk.Label(
            master=self._root, text="Opettaja/Valmentaja")
        stable_header = ttk.Label(master=self._root, text="Talli")

        self._new_date = ttk.Entry(master=self._root)
        self._new_horse = ttk.Entry(master=self._root)
        self._new_instructor = ttk.Entry(master=self._root)
        self._new_stable = ttk.Entry(master=self._root)

        new_ride_button = ttk.Button(
            master=self._root, text="Uusi merkintä", command=self._handle_new_ride_button)

        date_header.grid(row=1, column=0)
        horse_header.grid(row=1, column=1)
        instructor_header.grid(row=1, column=2)
        stable_header.grid(row=1, column=3)

        self._new_date.grid(row=2, column=0)
        self._new_horse.grid(row=2, column=1)
        self._new_instructor.grid(row=2, column=2)
        self._new_stable.grid(row=2, column=3)
        new_ride_button.grid(row=2, column=4)

    def _handle_new_ride_button(self):
        date = self._new_date.get()
        horse = self._new_horse.get()
        instructor = self._new_instructor.get()
        stable = self._new_stable.get()
        ride = [date, horse, instructor, stable]

        if len(ride) == 4:
            ridediary_service.create_ride(date, horse, instructor, stable)
            self._rides_list_view()
            self._new_date.delete(0, constants.END)
            self._new_horse.delete(0, constants.END)
            self._new_instructor.delete(0, constants.END)
            self._new_stable.delete(0, constants.END)

    def _rides_list_view(self):
        rowlet = 5
        rides = self._rides.readlines()

        for ride in rides:
            index = rides.index(ride)
            index_place = ttk.Label(master=self._root, text=index)
            ride_place = ttk.Label(master=self._root, text=ride)

            index_place.grid(row=rowlet, column=0)
            ride_place.grid(row=rowlet, column=1, columnspan=2)
            rowlet += 1

    def _delete_ride(self):
        self._index_delete_ride = ttk.Entry(master=self._root)
        delete_ride_button = ttk.Button(
            master=self._root, text="Poista", command=self._handle_delete_ride)
        label = ttk.Label(master=self._root, text="Poistettava indeksi:")

        label.grid(row=3, column=0)
        self._index_delete_ride.grid(row=4, column=0)
        delete_ride_button.grid(row=4, column=1)

    def _handle_delete_ride(self):
        delete_index = self._index_delete_ride.get()
        if delete_index:
            ridediary_service.delete_ride(delete_index)
            self._rides_list_view()
            self._index_delete_ride.delete(0, constants.END)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._create_new_ride()
        self._rides_list_view()
        self._delete_ride()
