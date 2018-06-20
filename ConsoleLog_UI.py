# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConsoleLog.ui'
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

class Ui_ConsoleLog(object):
    def setupUi(self, ConsoleLog):
        ConsoleLog.setObjectName(_fromUtf8("ConsoleLog"))
        ConsoleLog.resize(1022, 712)
        self.gridLayout = QtGui.QGridLayout(ConsoleLog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(ConsoleLog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(450, 91))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.saveLogBtn = QtGui.QToolButton(self.groupBox)
        self.saveLogBtn.setGeometry(QtCore.QRect(0, 0, 81, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Art_Assets/saveIcon.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveLogBtn.setIcon(icon)
        self.saveLogBtn.setIconSize(QtCore.QSize(50, 50))
        self.saveLogBtn.setShortcut(_fromUtf8(""))
        self.saveLogBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.saveLogBtn.setAutoRaise(False)
        self.saveLogBtn.setObjectName(_fromUtf8("saveLogBtn"))
        self.clearLogBtn = QtGui.QToolButton(self.groupBox)
        self.clearLogBtn.setGeometry(QtCore.QRect(90, 0, 81, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Art_Assets/clearLogIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearLogBtn.setIcon(icon1)
        self.clearLogBtn.setIconSize(QtCore.QSize(50, 50))
        self.clearLogBtn.setShortcut(_fromUtf8(""))
        self.clearLogBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.clearLogBtn.setAutoRaise(False)
        self.clearLogBtn.setObjectName(_fromUtf8("clearLogBtn"))
        self.printLogBtn = QtGui.QToolButton(self.groupBox)
        self.printLogBtn.setGeometry(QtCore.QRect(180, 0, 81, 81))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Art_Assets/printIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printLogBtn.setIcon(icon2)
        self.printLogBtn.setIconSize(QtCore.QSize(50, 50))
        self.printLogBtn.setShortcut(_fromUtf8(""))
        self.printLogBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.printLogBtn.setAutoRaise(False)
        self.printLogBtn.setObjectName(_fromUtf8("printLogBtn"))
        self.optionBtn = QtGui.QToolButton(self.groupBox)
        self.optionBtn.setGeometry(QtCore.QRect(270, 0, 81, 81))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Art_Assets/optionIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optionBtn.setIcon(icon3)
        self.optionBtn.setIconSize(QtCore.QSize(50, 50))
        self.optionBtn.setShortcut(_fromUtf8(""))
        self.optionBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.optionBtn.setAutoRaise(False)
        self.optionBtn.setObjectName(_fromUtf8("optionBtn"))
        self.searchLogBtn = QtGui.QToolButton(self.groupBox)
        self.searchLogBtn.setGeometry(QtCore.QRect(360, 0, 81, 81))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Art_Assets/searchIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchLogBtn.setIcon(icon4)
        self.searchLogBtn.setIconSize(QtCore.QSize(50, 50))
        self.searchLogBtn.setShortcut(_fromUtf8(""))
        self.searchLogBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.searchLogBtn.setAutoRaise(False)
        self.searchLogBtn.setObjectName(_fromUtf8("searchLogBtn"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.consoleLogTxt = QtGui.QTextBrowser(ConsoleLog)
        self.consoleLogTxt.setMinimumSize(QtCore.QSize(400, 400))
        self.consoleLogTxt.setObjectName(_fromUtf8("consoleLogTxt"))
        self.gridLayout.addWidget(self.consoleLogTxt, 1, 0, 1, 1)

        self.retranslateUi(ConsoleLog)
        QtCore.QMetaObject.connectSlotsByName(ConsoleLog)

    def retranslateUi(self, ConsoleLog):
        ConsoleLog.setWindowTitle(_translate("ConsoleLog", "Console Log", None))
        self.saveLogBtn.setText(_translate("ConsoleLog", "Save", None))
        self.clearLogBtn.setText(_translate("ConsoleLog", "Clear Log", None))
        self.printLogBtn.setText(_translate("ConsoleLog", "Print", None))
        self.optionBtn.setText(_translate("ConsoleLog", "Options", None))
        self.searchLogBtn.setText(_translate("ConsoleLog", "Search", None))

