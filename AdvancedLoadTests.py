'''
Created on Dec 30, 2015

@author: LockwoodE
'''
import os, sys
import ALTWindow, TestsNotFoundListWindow
from PyQt4.QtGui import QWidget, QFileDialog
from PyQt4.Qt import Qt

class AdvancedTestLoader(QWidget, ALTWindow.Ui_Form):
    
    def __init__(self, parent):
        super(AdvancedTestLoader, self).__init__()
        self.setupUi(self)
        
        self.cancelBtn.clicked.connect(self.closeWindow)
        self.findFileBtn.clicked.connect(self.getFile)
        self.loadBtn.clicked.connect(self.loadTestList)
        
        self.parent = parent
        
        self.testsNotFoundWindow = TestsNotFoundListWindow.TestsNotFound()
        
        self.importFileName = ""
        
        self.timeLimit = 0
        self.timeCheck = False
        self.timeSum = 0
        self.removeTests = False
        self.hasCompName = False
        
    def loadTestList(self):
        
        if(self.timeLimitCB.checkState() == Qt.Checked):
            self.timeLimit = int(self.timeEdit.text())
            self.timeCheck = True
        if(self.removeTestsCB.checkState() == Qt.Checked):
            self.removeTests = True
        if(self.hasCompCB.checkState() == Qt.Checked):
            self.hasCompName = True
        
        computerName = os.environ['COMPUTERNAME']
        if self.hasCompName:
            if computerName in self.fileEntry:
                self.treeHunt(self.parent.root)
        else:     
            self.treeHunt(self.parent.root)
        
        if self.removeTests:
            with open(os.path.normpath(self.fileEntry.text()), "w") as f:
                for item in self.importList:
                    f.write(item + "\n")
            f.close()
        self.close()
        
    #given the number of operations this could lead to, scanning the file more than once could become n^2 vs log(n) for this function. So the best option may be to read in the entire list,
    #delete the file, then recreate the file via the list of items I read in from the file, minus the items taken out if the user requests test removal from the list.
    
        
    def treeHunt(self, node):
        #steps through the test tree list down to each lead node then performs testListCheck
        treeList = []
        for suite in range(0, node.childCount()):
            suiteFolder = node.child(suite)
            for childNum in range(0, suiteFolder.childCount()):
                module = suiteFolder.child(childNum)
                for testNum in range(0, module.childCount()):
                    leaf = module.child(testNum)
                    if leaf.childCount() == 0:
                        testName = module.text(0).replace(".py","") + "," + leaf.text(0)
                        treeList.append((testName, leaf))
                        #self.testListCheck(module, leaf)
        self.testListCheck(treeList, self.testListImport())
    
    def testListCheck(self, treeList, importList):
        #checks a given node's testClass,testName against each line of the imported text list of test names.
        #test list's passed must be of the form CLASSNAME,TESTNAME
        testNotFoundList = []
        found = False
        for name in importList:
            for item in treeList:
                if item[0] == name:
                    if self.timeCheck:
                        if (self.timeSum + int(item[1].data(1, Qt.ToolTipRole))) <= self.timeLimit:  
                            item[1].setCheckState(0, Qt.Checked)
                            item[1].setExpanded(True)
                            item[1].parent().setExpanded(True)
                            #parent.setCheckState(0, Qt.Checked)
                            self.parent.root.setExpanded(True)
                            self.timeSum += int(item[1].data(1, Qt.ToolTipRole))
                    else:
                        item[1].setCheckState(0, Qt.Checked)
                        item[1].setExpanded(True)
                        item[1].parent().setExpanded(True)
                        #parent.setCheckState(0, Qt.Checked)
                        self.parent.root.setExpanded(True)
                    found = True
                    break
            if not found:
                testNotFoundList.append(name)
            found = False
        self.showTestsNotFound(testNotFoundList)
    
    def showTestsNotFound(self, testsNotFoundList):
        self.testsNotFoundWindow.textBrowser.clear()
        self.testsNotFoundWindow.showTestList(testsNotFoundList)
        self.testsNotFoundWindow.show()
    
    def testListImport(self):
        importList = []
        try:
            with open(os.path.normpath(self.fileEntry.text()), 'r+') as f:
                for line in f:
                    importList.append(str(line).strip())
                f.close()
                
            if self.removeTests:
                os.remove(os.path.normpath(self.fileEntry.text()))
                
        except FileNotFoundError:
            print("File Not Found Error Occurred in Advanced Load Tests...")
        except:
            print("Unknown Error Occurred: " + sys.exc_info())
        return importList
            
    def getFile(self):
        self.importFileName = QFileDialog.getOpenFileName(self, caption='Select a List of Tests...', directory='C:\\', filter='*.txt')
        self.fileEntry.setText(self.importFileName)
    
    def closeWindow(self):
        self.close()