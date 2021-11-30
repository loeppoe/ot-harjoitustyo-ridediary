from services.ridediary_services import ridediary_service


def main():
    print("komennot")
    print("0 - lopeta")
    print("1 - uusi merkintä")
    print("2 - hae kaikki merkinnät")
    print("3 - poista merkintä indeksistä")

    while True:
        command = str(input("Anna komento"))
        if command == "0":
            break

        if command == "1":
            date = str(input("Pvm:"))
            horse = str(input("Hevonen:"))
            teacher = str(input("Opettaja:"))
            stable = str(input("Talli:"))
            ridediary_service.create_ride(date, horse, teacher, stable)

        if command == "2":
            rides = ridediary_service.get_rides()
            for ride in rides:
                print(ride)

        if command == "3":
            i = int(input("Poistettava indeksi:"))
            ridediary_service.delete_ride(i)

        else:
            continue


if __name__ == "__main__":
    main()
