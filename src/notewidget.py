from enum import Enum

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QTextBrowser

from src.controller.models.notemodel import Note
from src.ui.notewidget_ui import Ui_NoteWidget


class NoteState(Enum):
    RENDER = 0
    EDIT = 1


class NoteWidget(QWidget):
    note_created = pyqtSignal()
    note_saved = pyqtSignal(Note)

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.ui = Ui_NoteWidget()

        self.textBrowser = QTextBrowser(self)
        self.textEdit = QTextEdit(self)

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

        self.ui.titleEdit.setPlaceholderText('Input title')

        self.ui.modeBtns.addWidget(edit_btn)
        self.ui.modeBtns.addWidget(render_btn)

        self.ui.noteContent.addWidget(self.textBrowser)
        self.ui.noteContent.addWidget(self.textEdit)

        self.ui.newNoteBtn.clicked.connect(lambda: self.note_created.emit())
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
            self.note.name = self.ui.titleEdit.text()
            self.note.content = self.textEdit.toMarkdown()
            self.note_saved.emit(self.note)
