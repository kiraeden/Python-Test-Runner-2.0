'''
Created on Dec 16, 2015

@author: LockwoodE
'''

from PyQt4.QtGui import QFileDialog, QDialog
from PyQt4.QtCore import pyqtSignal
from Registry_Access_Module import Reg_Access
import ConsoleLogOption_UI
import os

class ConLogOption(QDialog, ConsoleLogOption_UI.Ui_ConLogOptWindow):
    
    newLogPath = pyqtSignal(tuple)
    def __init__(self, parent):
        super(ConLogOption, self).__init__()
        self.setupUi(self)
        
        self.localLog = ""
        self.networkLog = ""
        self.basepathname = "C:\\"
        
        self.registry = Reg_Access()
        
        self.initFields()
        result = self.registry.readRegistry("LOCAL_LOG_PATH")
        if result:
            self.logPath.setText(result)
        else:
            self.logPath.setText(self.basepathname)
            
        result = self.registry.readRegistry("NETWORK_LOG_PATH")
        if result:
            self.networkPath.setText(result)
        else:
            self.networkPath.setText(self.basepathname)
        
        self.okBtn.clicked.connect(self.acceptInput)
        self.cancelBtn.clicked.connect(self.closeWindow)
        self.filePushBtn.clicked.connect(self.fileNetPush)
        self.logFileBtn.clicked.connect(self.selLogPath)
        self.netwPathBtn.clicked.connect(self.selNetworkPath)
        
        self.parent = parent
        
        #self.fontCB.clicked.connect()
    
    def closeEvent(self, event):
        self.localLog = self.registry.readRegistry("LOCAL_LOG_PATH")
        self.networkLog = self.registry.readRegistry("NETWORK_LOG_PATH")
        if self.localLog:
            self.logPath.setText(self.localLog)
        else:
            self.logPath.setText(self.basepathname)
        if self.networkLog:
            self.networkPath.setText(self.networkLog)
        else:
            self.logPath.setText(self.basepathname)
    
    def initFields(self):
        name0 = "LOCAL_LOG_PATH"
        name1 = "NETWORK_LOG_PATH"
        local = self.registry.readRegistry(name0)
        
        if local:
            self.localLog = local
        else:
            self.registry.writeRegistry(name0, self.basepathname)
            self.localLog = self.basepathname
            
        network = self.registry.readRegistry(name1)
        
        if network:
            self.networkLog = network
        else:
            self.registry.writeRegistry(name1, self.basepathname)
            self.networkLog = self.basepathname
    
    def fileNetPush(self):
        print("This button does nothing currently.")
        #self.parent.copyLogToNetwork()
    
    def closeWindow(self):
        self.localLog = self.registry.readRegistry("LOCAL_LOG_PATH")
        self.networkLog = self.registry.readRegistry("NETWORK_LOG_PATH")
        self.close()
    
    def acceptInput(self):
        # I could emit all the changes here when the OK button is pressed.
        
        if self.logPath.text() != self.localLog:
            self.localLog = self.logPath.text()
        
        if self.networkPath.text() != self.networkLog:
            self.networkLog = self.networkPath.text()
        
        self.registry.writeRegistry("LOCAL_LOG_PATH", self.localLog)
        self.registry.writeRegistry("NETWORK_LOG_PATH", self.networkLog)
        self.newLogPath.emit((self.localLog, self.networkLog))
        self.close()
        
    def selLogPath(self):
        filePath = QFileDialog.getExistingDirectory(self, "Select directory", self.localLog, QFileDialog.ShowDirsOnly)
        self.logPath.setText(filePath)
        self.localLog = filePath
    
    def selNetworkPath(self):
        
        filePath = QFileDialog.getExistingDirectory(self, "Select directory", self.networkLog, QFileDialog.ShowDirsOnly)
        self.networkPath.setText(filePath)
        self.networkLog = filePath