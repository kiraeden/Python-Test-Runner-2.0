# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PTR_About_Window.ui'
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

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName(_fromUtf8("AboutWindow"))
        AboutWindow.resize(590, 457)
        self.closeWindow = QtGui.QPushButton(AboutWindow)
        self.closeWindow.setGeometry(QtCore.QRect(250, 390, 91, 51))
        self.closeWindow.setObjectName(_fromUtf8("closeWindow"))
        self.label = QtGui.QLabel(AboutWindow)
        self.label.setGeometry(QtCore.QRect(150, 0, 290, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AboutWindow)
        self.label_2.setGeometry(QtCore.QRect(140, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(AboutWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 571, 279))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(AboutWindow)
        self.line.setGeometry(QtCore.QRect(0, 80, 591, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_4 = QtGui.QLabel(AboutWindow)
        self.label_4.setGeometry(QtCore.QRect(270, 62, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About Window", None))
        self.closeWindow.setText(_translate("AboutWindow", "OK", None))
        self.label.setText(_translate("AboutWindow", "Python Test Runner", None))
        self.label_2.setText(_translate("AboutWindow", "Version: 1.0.0", None))
        self.label_3.setText(_translate("AboutWindow", "Python Test Runner is a custom program created for internal use by Elster/Honeywell employees. The purpose of this program, per its name, is to run python tests and report/save their results.\n"
"\n"
"This program was created using Python Version 3.4.3 and PyQt Version 4.11.4. This program was written without a license to Qt or PyQt and thus cannot be sold or otherwise commercialised. If this program is shared for use it must have the source code available with it per the requirements of the GPL license applied to Qt/PyQt. The Author makes no guarantees of functionality of the program nor of compatibility with any system. This program is supplied without warranty and is supplied \"as is\" to the end user.", None))
        self.label_4.setText(_translate("AboutWindow", "Author: Ethan Lockwood", None))

