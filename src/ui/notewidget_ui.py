# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp_resources/notewidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoteWidget(object):
    def setupUi(self, NoteWidget):
        NoteWidget.setObjectName("NoteWidget")
        NoteWidget.resize(643, 425)
        self.verticalLayout = QtWidgets.QVBoxLayout(NoteWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, 10)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newNoteBtn = QtWidgets.QPushButton(NoteWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newNoteBtn.sizePolicy().hasHeightForWidth())
        self.newNoteBtn.setSizePolicy(sizePolicy)
        self.newNoteBtn.setObjectName("newNoteBtn")
        self.horizontalLayout.addWidget(self.newNoteBtn)
        self.saveBtn = QtWidgets.QPushButton(NoteWidget)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.modeBtns = QtWidgets.QStackedWidget(NoteWidget)
        self.modeBtns.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeBtns.sizePolicy().hasHeightForWidth())
        self.modeBtns.setSizePolicy(sizePolicy)
        self.modeBtns.setObjectName("modeBtns")
        self.horizontalLayout.addWidget(self.modeBtns)
        self.deteleBtn = QtWidgets.QPushButton(NoteWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deteleBtn.sizePolicy().hasHeightForWidth())
        self.deteleBtn.setSizePolicy(sizePolicy)
        self.deteleBtn.setObjectName("deteleBtn")
        self.horizontalLayout.addWidget(self.deteleBtn)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 15)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(NoteWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.noteContent = QtWidgets.QStackedWidget(NoteWidget)
        self.noteContent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.noteContent.setObjectName("noteContent")
        self.verticalLayout.addWidget(self.noteContent)

        self.retranslateUi(NoteWidget)
        self.modeBtns.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(NoteWidget)

    def retranslateUi(self, NoteWidget):
        _translate = QtCore.QCoreApplication.translate
        NoteWidget.setWindowTitle(_translate("NoteWidget", "Form"))
        self.newNoteBtn.setText(_translate("NoteWidget", "New note"))
        self.saveBtn.setText(_translate("NoteWidget", "Save"))
        self.deteleBtn.setText(_translate("NoteWidget", "Delete"))
        self.label.setText(_translate("NoteWidget", "Labels:"))
