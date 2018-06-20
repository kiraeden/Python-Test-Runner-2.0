# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Override_Window.ui'
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

class Ui_DBOverride(object):
    def setupUi(self, DBOverride):
        DBOverride.setObjectName(_fromUtf8("DBOverride"))
        DBOverride.resize(531, 326)
        self.label = QtGui.QLabel(DBOverride)
        self.label.setGeometry(QtCore.QRect(80, 10, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(DBOverride)
        self.comboBox.setGeometry(QtCore.QRect(210, 79, 201, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_2 = QtGui.QLabel(DBOverride)
        self.label_2.setGeometry(QtCore.QRect(109, 80, 91, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(DBOverride)
        self.label_3.setGeometry(QtCore.QRect(101, 120, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Version_Field = QtGui.QLineEdit(DBOverride)
        self.Version_Field.setGeometry(QtCore.QRect(210, 120, 113, 20))
        self.Version_Field.setObjectName(_fromUtf8("Version_Field"))
        self.label_4 = QtGui.QLabel(DBOverride)
        self.label_4.setGeometry(QtCore.QRect(96, 150, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Revision_Field = QtGui.QLineEdit(DBOverride)
        self.Revision_Field.setGeometry(QtCore.QRect(210, 150, 113, 20))
        self.Revision_Field.setText(_fromUtf8(""))
        self.Revision_Field.setObjectName(_fromUtf8("Revision_Field"))
        self.OK_Button = QtGui.QPushButton(DBOverride)
        self.OK_Button.setGeometry(QtCore.QRect(160, 270, 81, 41))
        self.OK_Button.setObjectName(_fromUtf8("OK_Button"))
        self.Cancel_Button = QtGui.QPushButton(DBOverride)
        self.Cancel_Button.setGeometry(QtCore.QRect(290, 270, 81, 41))
        self.Cancel_Button.setObjectName(_fromUtf8("Cancel_Button"))
        self.label_5 = QtGui.QLabel(DBOverride)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 481, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(DBOverride)
        QtCore.QMetaObject.connectSlotsByName(DBOverride)

    def retranslateUi(self, DBOverride):
        DBOverride.setWindowTitle(_translate("DBOverride", "Database Override", None))
        self.label.setText(_translate("DBOverride", "Database Storage Information Override", None))
        self.label_2.setText(_translate("DBOverride", "Product Name: ", None))
        self.label_3.setText(_translate("DBOverride", "Product Version:", None))
        self.label_4.setText(_translate("DBOverride", "Product Revision:", None))
        self.OK_Button.setText(_translate("DBOverride", "Ok", None))
        self.Cancel_Button.setText(_translate("DBOverride", "Cancel", None))
        self.label_5.setText(_translate("DBOverride", "The purpose of this window is to allow the user to override any automatic meter version detection once it\'s implemented. Until such features are implemented and functional, this page will serve as the setup location for the database.", None))

