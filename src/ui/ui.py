from ui.rides_view import RidesView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_rides_view()

    def _show_rides_view(self):
        self._current_view = RidesView(self._root)
        self._current_view.pack
