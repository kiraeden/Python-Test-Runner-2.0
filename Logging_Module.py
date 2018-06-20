'''
Created on Aug 14, 2017

@author: Ethan Lockwood

@description: This module handles the logging functions of the Python Test Runner
'''

import os, sys, time
from shutil import copy
from Registry_Access_Module import Reg_Access

class PTR_Logging_Module():
    def __init__(self):
        self.localLogPath = ""
        self.networkLogPath = ""
        self.logFileBase = ""
        self.registry = Reg_Access()
        self.initLogPaths()
    
    #Placeholder function for sending log strings from the console log to their files.
    
    def handleLogStrings(self, logString):
        self.logResults(logString)
    
    def initLogPaths(self, optional_paths=None):
        name0 = "LOCAL_LOG_PATH"
        name1 = "NETWORK_LOG_PATH"
        basePathName = os.path.normpath("C:\\")
        local = self.registry.readRegistry(name0)
        if local:
            self.localLogPath = local
        network = self.registry.readRegistry(name1)
        if network:
            self.networkLogPath = network
        else:
            self.registry.writeRegistry(name0, basePathName)
            self.registry.writeRegistry(name1, basePathName)
            if optional_paths == None:
                self.localLogPath = basePathName
                self.networkLogPath = basePathName
            else:
                self.localLogPath = optional_paths[0]
                self.networkLogPath = optional_paths[1]
            
    # this function creates the log file and writes the result data to the file.
    
    def logResults(self, resultString):
        #the actual results get pushed to a file here.
        fileName = self.localLogPath + "\\" +  self.logFileBase + ".log"
        fileName = os.path.normpath(fileName)
        try:
            f = open(fileName, 'a+')
            f.write(resultString)
            f.close()
        except Exception as e:
            #This print was removed because it causes an infinite loop when an error occurs.
            pass
            #print(e)
            
    #This function performs a copy of the log file created to the network at the end of the test run (it doesn't necessarily have to be to a network location).
    def copyLogToNetwork(self):
        #copies the result log files to the network
        fileName = self.localLogPath + "\\" + self.logFileBase + ".log"
        fileName = os.path.normpath(fileName)
        sumFileName = self.localLogPath + "\\" + self.logFileBase + ".sum"
        sumFileName = os.path.normpath(sumFileName)
        
        self.networkFilePath = os.path.normpath(self.networkLogPath + "\\" + self.logFileBase + ".log")
        networkSumFilePath = os.path.normpath(self.networkLogPath + "\\" + self.logFileBase + ".sum")
        
        try:
            copy(fileName, self.networkFilePath)
        except Exception as e:
            print(e)
            
        try:
            copy(sumFileName, networkSumFilePath)
        except Exception as e:
            print(e)
    
    #this function computes the basename for the log files and sets it to a global value for consistency later.
    
    def logFileBaseName(self):
        #Builds the base file name to be used on all output files.
        fileName = ""
        fileName += "PyTestRun"
        fileName += self.dateStamp() + "_"
        self.computerName = os.environ['COMPUTERNAME']
        fileName += str(self.computerName).upper()
        self.logFileBase = fileName
    
    def dateStamp(self):
        dstamp = "["
        dstamp += time.strftime("%d-%m-%y")
        dstamp += "]["
        dstamp += time.strftime("%I %M %S %p")
        dstamp += "]"
        return dstamp
    
    def getLogFileBase(self):
        return self.logFileBase
    
    def getLocalLogPath(self):
        return self.localLogPath
    
    def getNetworkLogPath(self):
        return self.networkLogPath