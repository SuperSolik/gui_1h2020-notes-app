from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QFrame, \
    QSizePolicy


class NotePreviewWidget(QFrame):
    def __init__(self, note, parent=None):
        super(QWidget, self).__init__(parent=parent)
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(QLabel(note.name))
        sep = QWidget()
        sep.setFixedHeight(2);
        sep.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed);
        sep.setStyleSheet("background-color: #c0c0c0;")
        self.layout().addWidget(sep)
        self.layout().addWidget(QLabel(note.content))

        self.setFrameStyle(QFrame.StyledPanel)
