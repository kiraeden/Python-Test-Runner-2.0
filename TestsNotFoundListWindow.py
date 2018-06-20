'''
Created on Sep 5, 2017

@author: Ethan Lockwood
'''

import TestsNotFoundList_UI
from PyQt4.QtGui import QWidget

class TestsNotFound(QWidget, TestsNotFoundList_UI.Ui_Form):
    def __init__(self):
        super(TestsNotFound, self).__init__()
        self.setupUi(self)
        
    def close(self):
        self.textBrowser.clear()
        
    def showTestList(self, testList):
        for test in testList:
            self.textBrowser.setText(self.textBrowser.toPlainText() + str(test) + "\n")