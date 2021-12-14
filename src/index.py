from tkinter import Tk
from ui.userinterface import UI


def main():
    window = Tk()
    window.title("Ratsastuspäiväkirja")

    Ui = UI(window) # pylint: disable=invalid-name
    Ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
