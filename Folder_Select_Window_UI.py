# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Folder_Select_Window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(561, 433)
        self.folderTreeWidget = QtGui.QTreeWidget(Form)
        self.folderTreeWidget.setGeometry(QtCore.QRect(20, 60, 521, 321))
        self.folderTreeWidget.setObjectName(_fromUtf8("folderTreeWidget"))
        self.folderTreeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.ok_btn = QtGui.QPushButton(Form)
        self.ok_btn.setGeometry(QtCore.QRect(130, 400, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(Form)
        self.cancel_btn.setGeometry(QtCore.QRect(350, 400, 75, 23))
        self.cancel_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Folder Selection", None))
        self.label.setText(_translate("Form", "Select Folder(s):", None))
        self.ok_btn.setText(_translate("Form", "Ok", None))
        self.cancel_btn.setText(_translate("Form", "Cancel", None))

