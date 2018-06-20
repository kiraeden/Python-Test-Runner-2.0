# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConsoleLogOptions.ui'
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

class Ui_ConLogOptWindow(object):
    def setupUi(self, ConLogOptWindow):
        ConLogOptWindow.setObjectName(_fromUtf8("ConLogOptWindow"))
        ConLogOptWindow.resize(1035, 240)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConLogOptWindow.sizePolicy().hasHeightForWidth())
        ConLogOptWindow.setSizePolicy(sizePolicy)
        ConLogOptWindow.setMinimumSize(QtCore.QSize(1035, 240))
        font = QtGui.QFont()
        font.setPointSize(12)
        ConLogOptWindow.setFont(font)
        self.logPath = QtGui.QLineEdit(ConLogOptWindow)
        self.logPath.setGeometry(QtCore.QRect(10, 40, 971, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logPath.setFont(font)
        self.logPath.setObjectName(_fromUtf8("logPath"))
        self.networkPath = QtGui.QLineEdit(ConLogOptWindow)
        self.networkPath.setGeometry(QtCore.QRect(10, 100, 971, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.networkPath.setFont(font)
        self.networkPath.setObjectName(_fromUtf8("networkPath"))
        self.logFileBtn = QtGui.QToolButton(ConLogOptWindow)
        self.logFileBtn.setGeometry(QtCore.QRect(990, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.logFileBtn.setFont(font)
        self.logFileBtn.setObjectName(_fromUtf8("logFileBtn"))
        self.netwPathBtn = QtGui.QToolButton(ConLogOptWindow)
        self.netwPathBtn.setGeometry(QtCore.QRect(990, 100, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.netwPathBtn.setFont(font)
        self.netwPathBtn.setObjectName(_fromUtf8("netwPathBtn"))
        self.okBtn = QtGui.QPushButton(ConLogOptWindow)
        self.okBtn.setGeometry(QtCore.QRect(790, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.cancelBtn = QtGui.QPushButton(ConLogOptWindow)
        self.cancelBtn.setGeometry(QtCore.QRect(920, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.filePushBtn = QtGui.QPushButton(ConLogOptWindow)
        self.filePushBtn.setGeometry(QtCore.QRect(450, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.filePushBtn.setFont(font)
        self.filePushBtn.setObjectName(_fromUtf8("filePushBtn"))
        self.fontCB = QtGui.QComboBox(ConLogOptWindow)
        self.fontCB.setGeometry(QtCore.QRect(110, 190, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fontCB.setFont(font)
        self.fontCB.setObjectName(_fromUtf8("fontCB"))
        self.label = QtGui.QLabel(ConLogOptWindow)
        self.label.setGeometry(QtCore.QRect(20, 190, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(ConLogOptWindow)
        self.label_2.setGeometry(QtCore.QRect(326, 150, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(ConLogOptWindow)
        self.label_3.setGeometry(QtCore.QRect(12, 16, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(ConLogOptWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 75, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(ConLogOptWindow)
        QtCore.QMetaObject.connectSlotsByName(ConLogOptWindow)

    def retranslateUi(self, ConLogOptWindow):
        ConLogOptWindow.setWindowTitle(_translate("ConLogOptWindow", "Console Log Options", None))
        self.logFileBtn.setText(_translate("ConLogOptWindow", "...", None))
        self.netwPathBtn.setText(_translate("ConLogOptWindow", "...", None))
        self.okBtn.setText(_translate("ConLogOptWindow", "Ok", None))
        self.cancelBtn.setText(_translate("ConLogOptWindow", "Cancel", None))
        self.filePushBtn.setText(_translate("ConLogOptWindow", "GO", None))
        self.label.setText(_translate("ConLogOptWindow", "Log Font Size", None))
        self.label_2.setText(_translate("ConLogOptWindow", "Copy All Log files (Log File Path -> Storage Path)", None))
        self.label_3.setText(_translate("ConLogOptWindow", "Log File Path:", None))
        self.label_4.setText(_translate("ConLogOptWindow", "Log File Storage Path:", None))

