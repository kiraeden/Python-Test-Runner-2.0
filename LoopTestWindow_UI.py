# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoopTestWindow.ui'
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

class Ui_LoopTestWindow(object):
    def setupUi(self, LoopTestWindow):
        LoopTestWindow.setObjectName(_fromUtf8("LoopTestWindow"))
        LoopTestWindow.resize(648, 440)
        self.gridLayout = QtGui.QGridLayout(LoopTestWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(LoopTestWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.clearBtn = QtGui.QPushButton(LoopTestWindow)
        self.clearBtn.setObjectName(_fromUtf8("clearBtn"))
        self.gridLayout.addWidget(self.clearBtn, 1, 0, 1, 1)
        self.closeBtn = QtGui.QPushButton(LoopTestWindow)
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))
        self.gridLayout.addWidget(self.closeBtn, 1, 1, 1, 1)

        self.retranslateUi(LoopTestWindow)
        QtCore.QMetaObject.connectSlotsByName(LoopTestWindow)

    def retranslateUi(self, LoopTestWindow):
        LoopTestWindow.setWindowTitle(_translate("LoopTestWindow", "Form", None))
        self.clearBtn.setText(_translate("LoopTestWindow", "Clear", None))
        self.closeBtn.setText(_translate("LoopTestWindow", "Close", None))

