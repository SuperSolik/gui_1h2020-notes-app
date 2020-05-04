from enum import Enum, auto

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QComboBox, QPushButton, \
    QTextEdit, QTextBrowser


class NoteState(Enum):
    EDIT = auto()
    RENDER = auto()


class NoteWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout()
        self.title_edit = QLineEdit()
        self.notes_labels = QComboBox()

        self.state = NoteState.RENDER
        self.note_widget = {}

        self.init_ui()

    def init_ui(self):
        self.title_edit.setPlaceholderText('Note title')

        edit_btn = QPushButton('Edit')
        edit_btn.clicked.connect(self.edit_note)

        render_btn = QPushButton('Render')
        render_btn.clicked.connect(self.render_note)

        self.note_widget = {
            NoteState.EDIT: QTextEdit(),
            NoteState.RENDER: QTextBrowser()
        }

        labels_bar = QHBoxLayout()

        edit_btn = QPushButton('Edit')
        edit_btn.clicked.connect(self.edit_note)

        render_btn = QPushButton('Render')
        render_btn.clicked.connect(self.render_note)

        self.main_layout.addWidget(self.title_edit)
        labels_bar.addWidget(self.notes_labels)
        labels_bar.addWidget(QPushButton('Edit labels'))

        self.main_layout.addLayout(labels_bar)
        self.main_layout.addWidget(self.note_widget[self.state])

        self.main_layout.setContentsMargins(5, 10, 5, 0)
        self.main_layout.setSpacing(3)
        self.setLayout(self.main_layout)

    def edit_note(self):
        pass

    def render_note(self):
        pass
