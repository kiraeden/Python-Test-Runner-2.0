'''
Created on Feb 12, 2016

@author: LockwoodE
'''

from PyQt4.QtGui import QDialog, QTextCursor
import  LogSearchWindow_UI

class LogSearchWindow(QDialog, LogSearchWindow_UI.Ui_Find):
    def __init__(self, Console_Log_Obj):
        super(LogSearchWindow, self).__init__()
        self.setupUi(self)
        
        self.parent = Console_Log_Obj
        
        self.findErrorBtn.clicked.connect(self.errorSearch)
        self.findFailBtn.clicked.connect(self.failSearch)
        self.findNextBtn.clicked.connect(self.findNext)
        self.findPassBtn.clicked.connect(self.passSearch)
        self.findTestBtn.clicked.connect(self.testSearch)
        self.findWarnBtn.clicked.connect(self.warningSearch)
        self.cancelBtn.clicked.connect(self.close)
        self.moveTopBtn.clicked.connect(self.moveToTop)
        self.moveBotBtn.clicked.connect(self.moveToBottom)
        
        #self.searchField.enterEvent.connect(self.findNext)
    
    def errorSearch(self):
        self.searchField.clear()
        self.searchField.setText("<ERROR")
        self.findNext()
        #need to search the console log for <Error here.
    
    def failSearch(self):
        self.searchField.clear()
        self.searchField.setText("<FAIL")
        self.findNext()
        #need to search the console log for <Fail here.
        
    def findNext(self):
        self.parent.consoleLogTxt.find(self.searchField.toPlainText())
        #need to find the next item matching the searchField entry.
        
    def passSearch(self):
        self.searchField.clear()
        self.searchField.setText("<PASS")
        self.findNext()
        #need to find the next instance of <Pass in the console Log here.
        
    def testSearch(self):
        self.searchField.clear()
        self.searchField.setText("Test_")
        self.findNext()
        #finds the next instance of Test_ in the console log.
        
    def warningSearch(self):
        self.searchField.clear()
        self.searchField.setText("<WARNING")
        self.findNext()
        #finds the next instance of <Warning in the console log.
        
    def moveToTop(self):
        self.parent.consoleLogTxt.moveCursor(QTextCursor.Start)
        #moves the cursor and scroll point to the top of the console log window.
        
    def moveToBottom(self):
        self.parent.consoleLogTxt.moveCursor(QTextCursor.End)
        #moves the cursor and scroll point to the bottom of the console log window.
        