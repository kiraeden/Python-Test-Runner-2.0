# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoFeatureWindow.ui'
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

class Ui_NoFeature(object):
    def setupUi(self, NoFeature):
        NoFeature.setObjectName(_fromUtf8("NoFeature"))
        NoFeature.resize(400, 183)
        self.label = QtGui.QLabel(NoFeature)
        self.label.setGeometry(QtCore.QRect(30, 90, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(NoFeature)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.closeBtn = QtGui.QPushButton(NoFeature)
        self.closeBtn.setGeometry(QtCore.QRect(155, 134, 101, 31))
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))

        self.retranslateUi(NoFeature)
        QtCore.QMetaObject.connectSlotsByName(NoFeature)

    def retranslateUi(self, NoFeature):
        NoFeature.setWindowTitle(_translate("NoFeature", "No Feature Exists", None))
        self.label.setText(_translate("NoFeature", "This feature is not yet implemented.", None))
        self.label_2.setText(_translate("NoFeature", "Sorry!", None))
        self.closeBtn.setText(_translate("NoFeature", "Close", None))

