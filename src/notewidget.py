from enum import Enum
from typing import Tuple

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QTextBrowser, QSpacerItem

from src.checkable_combobox import CheckableComboBox
from src.controller.models.labelmodel import Label
from src.controller.models.notemodel import Note
from src.ui.notewidget_ui import Ui_NoteWidget


class NoteState(Enum):
    RENDER = 0
    EDIT = 1


class NoteWidget(QWidget):
    note_created = pyqtSignal()
    note_saved = pyqtSignal(tuple)
    note_deleted = pyqtSignal(Note)

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.ui = Ui_NoteWidget()

        self.textBrowser = QTextBrowser(self)
        self.textEdit = QTextEdit(self)
        self.labels_box = CheckableComboBox(self)

        self.state = NoteState.RENDER
        self.note = None
        self.init_ui()
        self.render_note()

    def init_ui(self):
        self.ui.setupUi(self)

        edit_btn = QPushButton('Edit')
        edit_btn.clicked.connect(self.edit_note)
        render_btn = QPushButton('Render')
        render_btn.clicked.connect(self.render_note)

        self.ui.horizontalLayout_2.addWidget(self.labels_box)
        self.ui.horizontalLayout_2.addItem(QSpacerItem(10, 10))
        self.ui.horizontalLayout_2.setStretch(0, 0)
        self.ui.horizontalLayout_2.setStretch(1, 3)
        self.ui.horizontalLayout_2.setStretch(2, 8)

        self.ui.titleEdit.setPlaceholderText('Input title')

        self.ui.modeBtns.addWidget(edit_btn)
        self.ui.modeBtns.addWidget(render_btn)

        self.ui.noteContent.addWidget(self.textBrowser)
        self.ui.noteContent.addWidget(self.textEdit)

        self.ui.newNoteBtn.clicked.connect(lambda: self.note_created.emit())
        self.ui.deteleBtn.clicked.connect(lambda: self.note_deleted.emit(self.note) if self.note else None)
        self.ui.saveBtn.clicked.connect(self.save_note)

    def _change_state(self, num_state: int):
        self.ui.modeBtns.setCurrentIndex(num_state)
        self.ui.noteContent.setCurrentIndex(num_state)

    def edit_note(self):
        self.state = NoteState.EDIT
        self.ui.titleEdit.setEnabled(True)
        self._change_state(self.state.value)

    def render_note(self):
        self.state = NoteState.RENDER
        self.ui.titleEdit.setDisabled(True)
        text = self.textEdit.toMarkdown()
        self.textBrowser.setMarkdown(text)
        self._change_state(self.state.value)

    def set_note(self, note: Note):
        self.note = note
        self.ui.titleEdit.setText(note.name)
        self.textEdit.setText(note.content)
        self.render_note()

    def save_note(self):
        if self.note is not None:
            self.note.name = self.ui.titleEdit.text().strip()
            self.note.content = self.textEdit.toMarkdown().strip()
            self.note_saved.emit((self.note, self.labels_box.currentData()))

    def update_labels(self, labels: Tuple[Label], active_labels: Tuple[Label]):
        self.labels_box.clear()
        for label in labels:
            checked = label in active_labels
            self.labels_box.addItem(label.name, None, checked)
