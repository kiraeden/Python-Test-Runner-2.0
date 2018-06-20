'''
Created on Dec 16, 2015

@author: LockwoodE
'''

from PyQt4.QtGui import QWidget, QFileDialog
from PyQt4.QtCore import QFile, QIODevice, QSettings, pyqtSignal
import ConsoleLog_UI
import Option_Window, Log_Search
import Logging_Module
import sys
from io import StringIO

class ConsoleLog(QWidget, ConsoleLog_UI.Ui_ConsoleLog):
    def __init__(self, parent):
        super(ConsoleLog, self).__init__()
        self.settings = QSettings("Honeywell", "ConsoleLog")
        if not self.settings.value("geometry") == None:
            self.restoreGeometry(self.settings.value("geometry"))
        self.setupUi(self)
        
        self.optionWindow = Option_Window.ConLogOption(parent)
        self.searchWindow = Log_Search.LogSearchWindow(self)
        
        self.outputBuffer = StringIO()
        self.stdout_redirector = OutputRedirector(sys.stdout, parent)
        self.stderr_redirector = OutputRedirector(sys.stderr, parent)
        self.stdout_redirector.fp = self.outputBuffer
        self.stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = self.stdout_redirector
        sys.stderr = self.stderr_redirector
                
        self.searchLogBtn.clicked.connect(self.searchLog)
        self.clearLogBtn.clicked.connect(self.clearLog)
        self.printLogBtn.clicked.connect(self.printLog)
        self.optionBtn.clicked.connect(self.optionDialog)
        self.saveLogBtn.clicked.connect(self.saveLog)
        
        self.parent = parent
        
        self.parent.newLogData.connect(self.handleLogString)
        self.parent.resetConsole.connect(self.reset)
        
        self.optionWindow.newLogPath.connect(self.newLog)
        
        self.logger = Logging_Module.PTR_Logging_Module()
        
    def closeEvent(self, event):
        self.optionWindow.close()
        self.searchWindow.close()
        self.settings.setValue("geometry", self.saveGeometry())
        QWidget.closeEvent(self, event)
    
    def reset(self):
        self.clearLog()
        self.logger.logFileBaseName()
    
    def handleLogString(self, logString):
        #if not len(logString) == 0:
        #    if not logString == "\n":
        try:
            self.consoleLogTxt.append(logString.strip("\n"))
            self.logger.handleLogStrings(logString)
        except:
            pass
    
    def newLog(self, value):
        self.logger.initLogPaths(value)
    
    def searchLog(self):
        self.searchWindow.show()
    
    def clearLog(self):
        self.consoleLogTxt.clear()
        
    def printLog(self):
        #need to find a way to print the log, this also needs a confirmation checkbox
        self.consoleLogTxt.append("Temp test data\n")
    
    def optionDialog(self):
        #need a window that lets the user set the output points for the log files.
        self.optionWindow.show()
    
    def searchDialog(self):
        self.searchWindow.show()
        
    def saveLog(self):
        #need to make a way to save the log file.
        QFD = QFileDialog(self)
        f = QFD.getSaveFileName(self, "Save the Current Log...", "C:\\", "*.log")
        if not "." in f:
            f += ".log"
        file = QFile(f)
        file.open(QIODevice.ReadWrite)
        file.write(self.consoleLogTxt.toPlainText())
        file.close()
        
class OutputRedirector(object):
    
    logData = pyqtSignal(str)
    
    def __init__(self, fp, parent):
        self.fp = fp
        self.parent = parent

    def write(self, s):
        try:
            self.parent.newLogData.emit(str(s))
        except:
            pass

    def writelines(self, lines):
        try:
            self.parent.newLogData.emit(str(lines))
        except:
            pass
        
    def flush(self):
        self.fp.flush()