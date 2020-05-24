from enum import Enum
from typing import Tuple

import markdown2
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QSpacerItem, QFrame, QLineEdit, QVBoxLayout

from src.checkable_combobox import CheckableComboBox
from src.controller.models.labelmodel import Label
from src.ui.notewidget_ui import Ui_NoteWidget


class NoteState(Enum):
    RENDER = 0
    EDIT = 1


class NoteWidget(QWidget):
    note_created = pyqtSignal()
    note_deleted = pyqtSignal()
    note_data_saved = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.ui = Ui_NoteWidget()

        self.textBrowser = QWebEngineView(self)

        self.titleEdit = QLineEdit(self)
        self.titleEdit.setFont(QFont('Ubuntu', 16, QFont.Bold))
        self.titleEdit.setFrame(False)
        self.titleEdit.setPlaceholderText('Input title')

        self.textEdit = QTextEdit(self)
        self.textEdit.setFont(QFont('Ubuntu', 14))
        self.textEdit.setFrameStyle(QFrame.NoFrame)
        self.textEdit.setPlaceholderText('Fill content')

        self.labels_box = CheckableComboBox(self)

        self.state = NoteState.RENDER
        self.has_content = False
        self.labels_ids_map = {}

        self.init_ui()
        self.edit_data()

    def init_ui(self):
        self.ui.setupUi(self)

        editWidget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        editWidget.setLayout(layout)

        editWidget.layout().addWidget(self.titleEdit)
        editWidget.layout().addWidget(self.textEdit)

        edit_btn = QPushButton('Edit')
        edit_btn.setCursor(Qt.PointingHandCursor)
        edit_btn.clicked.connect(self.edit_data)
        render_btn = QPushButton('Render')
        render_btn.setCursor(Qt.PointingHandCursor)
        render_btn.clicked.connect(self.render_data)

        self.ui.horizontalLayout_2.addWidget(self.labels_box)
        self.ui.horizontalLayout_2.addItem(QSpacerItem(10, 10))
        self.ui.horizontalLayout_2.setStretch(0, 0)
        self.ui.horizontalLayout_2.setStretch(1, 3)
        self.ui.horizontalLayout_2.setStretch(2, 8)

        self.ui.modeBtns.addWidget(edit_btn)
        self.ui.modeBtns.addWidget(render_btn)

        self.ui.noteContent.addWidget(self.textBrowser)
        self.ui.noteContent.addWidget(editWidget)

        self.ui.newNoteBtn.clicked.connect(lambda: self.note_created.emit())
        self.ui.deteleBtn.clicked.connect(self.delete_data)

        self.ui.saveBtn.clicked.connect(self.save_data)

    def _change_state(self, num_state: int):
        self.ui.modeBtns.setCurrentIndex(num_state)
        self.ui.noteContent.setCurrentIndex(num_state)

    def edit_data(self):
        self.state = NoteState.EDIT
        self._change_state(self.state.value)

    def render_data(self):
        self.state = NoteState.RENDER
        title = self.titleEdit.text()

        title = f'# {title}'
        content = self.textEdit.toPlainText()
        text = '  \n'.join((title, content))

        html = markdown2.markdown(text, ..., extras=['tables', 'task_list', 'cuddled-lists', 'code-friendly'])
        self.textBrowser.setHtml(html)
        self._change_state(self.state.value)

    def set_data(self, name: str, content: str):
        self.has_content = True
        self.titleEdit.setText(name)
        self.textEdit.setPlainText(content)
        self.labels_box.clear()
        self.render_data()

    def save_data(self):
        name = self.titleEdit.text().strip()
        content = self.textEdit.toPlainText()
        labels = map(lambda label: self.labels_ids_map[label], self.labels_box.currentData())
        data = {
            'name': name,
            'content': content,
            'labels': labels
        }
        self.note_data_saved.emit(data)

    def delete_data(self):
        self.textEdit.setMarkdown('')
        self.titleEdit.setText('')
        self.note_deleted.emit()
        self.render_data()
        self.has_content = False

    def update_labels(self, labels: Tuple[Label], active_labels: Tuple[Label]):
        self.labels_box.clear()
        self.labels_ids_map.clear()
        for label in labels:
            self.labels_ids_map[label.name] = label.id
            checked = label in active_labels
            self.labels_box.addItem(label.name, None, checked)
