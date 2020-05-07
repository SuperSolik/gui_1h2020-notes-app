from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QInputDialog

from src.controller import Controller
from src.controller.models.labelmodel import Label
from src.controller.models.notemodel import Note
from src.notepreview import NotePreviewWidget
from src.notewidget import NoteWidget
from src.ui.mainwindow_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.resize(1024, 600)

        self.controller = Controller()
        self.notesWidget = NoteWidget(parent=self)
        self.cur_label_id = None

        self.init_ui()

        self.setWindowTitle('NOTE TAKING APP')
        self.update_labels()
        self.fetch_notes()

    def init_ui(self):
        self.ui.setupUi(self)
        self.resize(1024, 600)

        self.ui.horizontalLayout.addWidget(self.notesWidget)
        self.ui.horizontalLayout.setStretch(0, 2)
        self.ui.horizontalLayout.setStretch(1, 3)
        self.ui.horizontalLayout.setStretch(2, 8)

        self.ui.newLabelBtn.clicked.connect(self.create_label)
        self.ui.labelsListWidget.itemDoubleClicked.connect(self.label_clicked)
        self.ui.deleteLabelBtn.clicked.connect(self.delete_label)

        self.notesWidget.note_created.connect(self.create_note)
        self.notesWidget.note_saved.connect(self.save_note)
        self.notesWidget.note_deleted.connect(self.delete_note)

    def update_labels(self) -> None:
        labels = self.controller.get_labels()
        self.ui.labelsListWidget.clear()
        # first fake label, by clicking on it just fetch all notes
        item = QListWidgetItem("All notes")
        setattr(item, 'id', None)
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
        note = self.controller.save_note(Note(name="untitled", content=""))
        self.notesWidget.set_note(note)
        self.fetch_notes(self.cur_label_id)

    def save_note(self, note: Note):
        self.controller.save_note(note)
        self.fetch_notes(self.cur_label_id)

    def delete_note(self, note: Note):
        self.controller.delete_note(note.id)
        self.fetch_notes(self.cur_label_id)

    def fetch_notes(self, label_id=None):
        notes = self.controller.get_notes(label_id)
        self.ui.notesListWidget.clear()
        for note in notes:
            note_preview = NotePreviewWidget(note, self)

            note_preview.note_passed.connect(self.notesWidget.set_note)

            item = QListWidgetItem()
            item.setSizeHint(note_preview.minimumSizeHint())
            self.ui.notesListWidget.addItem(item)
            self.ui.notesListWidget.setItemWidget(item, note_preview)

    def label_clicked(self, label_item: QListWidgetItem) -> None:
        self.cur_label_id = label_item.id
        self.fetch_notes(self.cur_label_id)
