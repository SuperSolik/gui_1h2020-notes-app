from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QInputDialog

from src.controller import Controller
from src.ui.mainwindow_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.resize(1024, 600)
        self.controller = Controller()

        self.init_ui()

        self.update_labels()

    def init_ui(self):
        self.ui.setupUi(self)
        self.resize(1024, 600)
        self.ui.newNoteBtn.clicked.connect(self.create_note)
        self.ui.newLabelBtn.clicked.connect(self.create_label)
        self.ui.labelsListWidget.itemDoubleClicked.connect(self.label_clicked)
        self.ui.deleteLabelBtn.clicked.connect(self.delete_label)

    def update_labels(self) -> None:
        labels = self.controller.get_labels()
        self.ui.labelsListWidget.clear()
        # first fake label, by clicking on it just fetch all notes
        item = QListWidgetItem("All notes")
        setattr(item, 'id', -1)
        self.ui.labelsListWidget.addItem(item)

        for label in labels:
            item = QListWidgetItem(f'{label.name}')
            setattr(item, 'id', label.id)
            self.ui.labelsListWidget.addItem(item)

    def create_label(self):
        text, ok = QInputDialog.getText(None, 'Dialog', 'Input label name:')
        if ok:
            self.controller.create_label(text)
        self.update_labels()

    def delete_label(self):
        labels = self.controller.get_labels()
        text, ok = QInputDialog.getItem(None, 'Delete label', 'Select label', (label.name for label in labels))
        label_to_del = next((label for label in labels if text in label.name), None)
        if ok and label_to_del is not None:
            self.controller.delete_label(label_to_del.id)

        self.update_labels()

    def create_note(self):
        pass

    def label_clicked(self, item: QListWidgetItem) -> None:
        self.ui.notesLabel.setText(item.text())
        # TODO: fetching notes
