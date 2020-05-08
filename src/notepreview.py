from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QFrame

from src.controller.models.notemodel import Note


class NotePreviewWidget(QFrame):
    note_passed = pyqtSignal(Note)

    def __init__(self, note, parent=None):
        super(QWidget, self).__init__(parent=parent)
        self.setLayout(QVBoxLayout())
        self.note = note

        label = QLabel(note.name)
        label.setFrameStyle(QFrame.StyledPanel)

        self.layout().addWidget(label)

    def mouseDoubleClickEvent(self, e: QtGui.QMouseEvent):
        self.note_passed.emit(self.note)
        e.accept()
