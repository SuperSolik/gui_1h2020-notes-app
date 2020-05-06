from enum import Enum
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QComboBox, QPushButton, \
    QTextEdit, QTextBrowser, QSpacerItem, QStackedWidget, QSizePolicy

from src.controller.models.notemodel import Note


class NoteState(Enum):
    RENDER = 0
    EDIT = 1


class NoteWidget(QWidget):
    note_created = pyqtSignal()
    note_saved = pyqtSignal(Note)

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout()

        self.note_create_btn = QPushButton('New note')
        self.note_delete_btn = QPushButton('Delete')

        self.title_edit = QLineEdit()
        self.notes_labels = QComboBox()

        self.note_buttons = QStackedWidget()
        self.note_widgets = QStackedWidget()

        self.state = NoteState.RENDER

        self.note = None

        self.init_ui()

    def init_ui(self):
        self.title_edit.setPlaceholderText('Note title')

        edit_btn = QPushButton('Edit')
        edit_btn.clicked.connect(self.edit_note)
        render_btn = QPushButton('Render')
        render_btn.clicked.connect(self.render_note)

        self.note_buttons.addWidget(edit_btn)
        self.note_buttons.addWidget(render_btn)

        self.note_buttons.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.note_widgets.addWidget(QTextBrowser())
        self.note_widgets.addWidget(QTextEdit())

        tool_bar = QHBoxLayout()
        labels_bar = QHBoxLayout()
        tool_bar.addWidget(self.note_create_btn)
        tool_bar.addItem(QSpacerItem(10, 10))
        tool_bar.addWidget(self.note_buttons)
        tool_bar.addWidget(self.note_delete_btn)
        tool_bar.setContentsMargins(0, 0, 0, 0)
        tool_bar.setSpacing(3)
        tool_bar.setStretch(0, 2)
        tool_bar.setStretch(1, 2)
        tool_bar.setStretch(2, 2)
        tool_bar.setStretch(3, 2)
        self.main_layout.addLayout(tool_bar)
        labels_bar.addWidget(self.notes_labels)
        labels_bar.addWidget(QPushButton('Edit labels'))
        labels_bar.setContentsMargins(0, 0, 0, 10)
        self.main_layout.addLayout(labels_bar)
        self.main_layout.addWidget(self.title_edit)
        self.main_layout.addWidget(self.note_widgets)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(3)
        self.setLayout(self.main_layout)

        self.note_create_btn.clicked.connect(lambda: self.note_created.emit())

    def _change_state(self, num_state: int):
        self.note_buttons.setCurrentIndex(num_state)
        self.note_widgets.setCurrentIndex(num_state)

    def edit_note(self):
        self.state = NoteState.EDIT
        self._change_state(self.state.value)

    def render_note(self):
        self.state = NoteState.RENDER
        self._change_state(self.state.value)
        text = self.note_widgets.widget(NoteState.EDIT.value).toMarkdown()
        self.note_widgets.widget(NoteState.RENDER.value).setMarkdown(text)

        self.note.name = self.title_edit.text().strip()
        self.note.content = text

        self.note_saved.emit(self.note)

    def set_note(self, note: Note):
        self.note = note
        self.title_edit.setText(note.name)
        self.note_widgets.widget(NoteState.EDIT.value).setText(note.content)
        self.render_note()
