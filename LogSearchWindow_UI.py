# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogSearchWindow.ui'
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

class Ui_Find(object):
    def setupUi(self, Find):
        Find.setObjectName(_fromUtf8("Find"))
        Find.resize(536, 191)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Find.sizePolicy().hasHeightForWidth())
        Find.setSizePolicy(sizePolicy)
        self.searchField = QtGui.QTextEdit(Find)
        self.searchField.setGeometry(QtCore.QRect(10, 10, 520, 91))
        self.searchField.setObjectName(_fromUtf8("searchField"))
        self.findErrorBtn = QtGui.QPushButton(Find)
        self.findErrorBtn.setGeometry(QtCore.QRect(10, 110, 81, 23))
        self.findErrorBtn.setObjectName(_fromUtf8("findErrorBtn"))
        self.findFailBtn = QtGui.QPushButton(Find)
        self.findFailBtn.setGeometry(QtCore.QRect(120, 110, 81, 23))
        self.findFailBtn.setObjectName(_fromUtf8("findFailBtn"))
        self.findWarnBtn = QtGui.QPushButton(Find)
        self.findWarnBtn.setGeometry(QtCore.QRect(230, 110, 81, 23))
        self.findWarnBtn.setObjectName(_fromUtf8("findWarnBtn"))
        self.findPassBtn = QtGui.QPushButton(Find)
        self.findPassBtn.setGeometry(QtCore.QRect(340, 110, 81, 23))
        self.findPassBtn.setObjectName(_fromUtf8("findPassBtn"))
        self.findTestBtn = QtGui.QPushButton(Find)
        self.findTestBtn.setGeometry(QtCore.QRect(450, 110, 81, 23))
        self.findTestBtn.setObjectName(_fromUtf8("findTestBtn"))
        self.findNextBtn = QtGui.QPushButton(Find)
        self.findNextBtn.setGeometry(QtCore.QRect(20, 150, 101, 31))
        self.findNextBtn.setObjectName(_fromUtf8("findNextBtn"))
        self.moveTopBtn = QtGui.QPushButton(Find)
        self.moveTopBtn.setGeometry(QtCore.QRect(150, 150, 101, 31))
        self.moveTopBtn.setObjectName(_fromUtf8("moveTopBtn"))
        self.moveBotBtn = QtGui.QPushButton(Find)
        self.moveBotBtn.setGeometry(QtCore.QRect(280, 150, 101, 31))
        self.moveBotBtn.setObjectName(_fromUtf8("moveBotBtn"))
        self.cancelBtn = QtGui.QPushButton(Find)
        self.cancelBtn.setGeometry(QtCore.QRect(410, 150, 101, 31))
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))

        self.retranslateUi(Find)
        QtCore.QMetaObject.connectSlotsByName(Find)

    def retranslateUi(self, Find):
        Find.setWindowTitle(_translate("Find", "Find", None))
        self.findErrorBtn.setText(_translate("Find", "<Error", None))
        self.findFailBtn.setText(_translate("Find", "<Fail", None))
        self.findWarnBtn.setText(_translate("Find", "<Warning", None))
        self.findPassBtn.setText(_translate("Find", "<Pass", None))
        self.findTestBtn.setText(_translate("Find", "Test_", None))
        self.findNextBtn.setText(_translate("Find", "Find Next", None))
        self.moveTopBtn.setText(_translate("Find", "Move To Top", None))
        self.moveBotBtn.setText(_translate("Find", "Move To Bottom", None))
        self.cancelBtn.setText(_translate("Find", "Cancel", None))

