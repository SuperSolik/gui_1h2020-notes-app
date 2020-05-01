from PyQt5 import QtWidgets

from src.controller import Controller
from src.controller.models.labelmodel import Label
from src.controller.models.notemodel import Note
from src.interfaces.iview import IView
from src.ui.mainwindow_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, IView):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = Controller(self)

        print(self.controller.get_labels())
        print(self.controller.get_notes())
