from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QInputDialog

from src.controller import Controller
from src.controller.models.labelmodel import Label
from src.controller.models.notemodel import Note
from src.notewidget import NoteWidget
from src.ui.mainwindow_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.resize(1024, 600)
        self.controller = Controller()

        self.notes_widget = NoteWidget(parent=self)

        self.init_ui()

        self.update_labels()

        self.note_btn = {}

    def init_ui(self):
        self.ui.setupUi(self)
        self.resize(1024, 600)

        self.ui.horizontalLayout.addWidget(self.notes_widget)
        self.ui.horizontalLayout.setStretch(0, 2)
        self.ui.horizontalLayout.setStretch(1, 3)
        self.ui.horizontalLayout.setStretch(2, 8)

        self.ui.newLabelBtn.clicked.connect(self.create_label)
        self.ui.labelsListWidget.itemDoubleClicked.connect(self.label_clicked)
        self.ui.deleteLabelBtn.clicked.connect(self.delete_label)
        self.notes_widget.note_created.connect(self.create_note)
        self.notes_widget.note_saved.connect(self.save_note)

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
            self.controller.save_label(Label(text))
        self.update_labels()

    def delete_label(self):
        labels = self.controller.get_labels()
        text, ok = QInputDialog.getItem(None, 'Delete label', 'Select label', (label.name for label in labels))
        label_to_del = next((label for label in labels if text in label.name), None)
        if ok and label_to_del is not None:
            self.controller.delete_label(label_to_del.id)

        self.update_labels()

    def create_note(self):
        note = self.controller.save_note(Note(name="untiled", content=""))
        self.notes_widget.set_note(note)

    def save_note(self, note: Note):
        self.controller.save_note(note)

    def label_clicked(self, item: QListWidgetItem) -> None:
        # self.ui.notesLabel.setText(item.text())
        # TODO: fetching notes
        pass
