from src.db import Database
from src.interfaces.iview import IView


class Controller:
    def __init__(self, view: IView):
        self.view = view
        self.db = Database()
