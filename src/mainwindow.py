from PyQt5 import QtWidgets

from src.ui.mainwindow_ui import Ui_MainWindow  # импорт нашего сгенерированного файла


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
