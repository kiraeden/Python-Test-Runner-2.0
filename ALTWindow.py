# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ALTWindow.ui'
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
        Form.resize(939, 211)
        self.fileEntry = QtGui.QLineEdit(Form)
        self.fileEntry.setGeometry(QtCore.QRect(10, 40, 871, 20))
        self.fileEntry.setObjectName(_fromUtf8("fileEntry"))
        self.findFileBtn = QtGui.QToolButton(Form)
        self.findFileBtn.setGeometry(QtCore.QRect(890, 40, 41, 21))
        self.findFileBtn.setObjectName(_fromUtf8("findFileBtn"))
        self.timeLimitCB = QtGui.QCheckBox(Form)
        self.timeLimitCB.setGeometry(QtCore.QRect(288, 80, 101, 21))
        self.timeLimitCB.setObjectName(_fromUtf8("timeLimitCB"))
        self.timeEdit = QtGui.QLineEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(478, 80, 61, 20))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(550, 79, 121, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.removeTestsCB = QtGui.QCheckBox(Form)
        self.removeTestsCB.setGeometry(QtCore.QRect(288, 119, 141, 17))
        self.removeTestsCB.setObjectName(_fromUtf8("removeTestsCB"))
        self.hasCompCB = QtGui.QCheckBox(Form)
        self.hasCompCB.setGeometry(QtCore.QRect(480, 119, 161, 17))
        self.hasCompCB.setObjectName(_fromUtf8("hasCompCB"))
        self.loadBtn = QtGui.QPushButton(Form)
        self.loadBtn.setGeometry(QtCore.QRect(381, 160, 71, 41))
        self.loadBtn.setObjectName(_fromUtf8("loadBtn"))
        self.cancelBtn = QtGui.QPushButton(Form)
        self.cancelBtn.setGeometry(QtCore.QRect(479, 160, 71, 41))
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(13, 20, 171, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.findFileBtn.setText(_translate("Form", "...", None))
        self.timeLimitCB.setText(_translate("Form", "Enable Time Limit", None))
        self.label.setText(_translate("Form", "Max Run Time (hours)", None))
        self.removeTestsCB.setText(_translate("Form", "Remove Tests From File", None))
        self.hasCompCB.setText(_translate("Form", ".txt file has Computer Name", None))
        self.loadBtn.setText(_translate("Form", "Load Tests", None))
        self.cancelBtn.setText(_translate("Form", "Cancel", None))
        self.label_2.setText(_translate("Form", "Test Source Path and File", None))

