from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFontMetrics, QFont
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QFrame

from src.controller.models.notemodel import Note


class NotePreviewWidget(QFrame):
    note_passed = pyqtSignal(Note)

    def __init__(self, note, parent=None):
        super(QWidget, self).__init__(parent=parent)
        layout = QVBoxLayout()
        layout.setSpacing(0)
        self.setLayout(layout)
        self.note = note

        name_label = QLabel()
        content_label = QLabel()
        content_label.setFont(QFont('ubuntu', 12, QFont.Normal))
        # name_label.setFrameStyle(QFrame.StyledPanel)

        self.layout().addWidget(name_label)
        self.layout().addWidget(content_label)
        self.setText()
        self.setCursor(Qt.PointingHandCursor)

    def getNote(self):
        return self.note

    def mouseDoubleClickEvent(self, e: QtGui.QMouseEvent):
        self.note_passed.emit(self.note)
        e.accept()

    def setText(self):
        name_label = self.layout().itemAt(0).widget()
        content_label = self.layout().itemAt(1).widget()

        metrics = QFontMetrics(name_label.font())
        elided_name = metrics.elidedText(self.note.name, Qt.ElideRight, self.width())
        name_label.setText(elided_name)

        elided_content = metrics.elidedText(self.note.content, Qt.ElideRight, self.width())
        content_label.setText(elided_content)

    def resizeEvent(self, e: QtGui.QResizeEvent):
        self.setText()
        super().resizeEvent(e)

