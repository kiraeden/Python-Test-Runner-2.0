#-----------------------------------------------------------------------------------------------------------------------------------------------------
#                                                           PYTHON TEST RUNNER
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#
#    Author: Ethan Lockwood
#
#    Python Version Required: 3.4.4
#    UI Made using PYQT4
#
#    Description: This is the code for the Python Test Runner Tool, which is the Python version of DV Test Runner. This program runs python unittests
#    via the nose testing framework (which implements the default python unittest framework
#
#-----------------------------------------------------------------------------------------------------------------------------------------------------

import os, sys, traceback, re, ast
import IconCollection, Console_Log, NoFeatureWarning, AdvancedLoadTests, AboutWindow, FolderSelection #, Override_Window, PySQL_Connector # these are the UI\Local files.
from PyQt4.QtGui import QMainWindow, QFileDialog, QApplication, QTreeWidgetItem, QHeaderView, QIcon, QLabel,\
    QBrush, QColor
from PyQt4.QtCore import Qt, pyqtSignal, QSettings, QObject, QTimer, SIGNAL, QThread
from time import strftime
from collections import OrderedDict
import Loop_Test
import PythonTestRunner_UI
import TestRunnerModule
from Registry_Access_Module import Reg_Access

class PythonTestRunner(QMainWindow, PythonTestRunner_UI.Ui_MainWindow, QApplication):
    #The line below is the signal point which the Console Log Window is getting result data from.
    newLogData = pyqtSignal(str)
    resetConsole = pyqtSignal()
    
    #This function sets up all the button calls and variables (it is called once when the window is made).
    def __init__(self):
        super(PythonTestRunner, self).__init__()
        
        self.settings = QSettings("Honeywell", "PythonTestRunner")
        if not self.settings.value("geometry") == None:
            self.restoreGeometry(self.settings.value("geometry"))
        if not self.settings.value("windowState") == None:
            self.restoreState(self.settings.value("windowState"))
            
        self.setupUi(self) #this creates the actual window'
        self.treeWidget.header().setResizeMode(0, QHeaderView.Stretch)
        
        self.testRunList = OrderedDict({})
        
        self.registry = Reg_Access()
        
        self.about = AboutWindow.AboutWindow()
        
        self.testTimeRemaining = 0 #total time in seconds that the test has remaining
        self.totalTestTime = 0 #total time in seconds that the current test run has been going for
        self.HOUR = 0 #timer hour value
        self.MINUTE = 0 #timer minute value
        self.SECOND = 0 #time second value
        
        self.timeLabel = QLabel(None)
        self.statusbar.addPermanentWidget(self.timeLabel) #creates the bottom right timer display
        self.timeLabel.setText("Time Remaining: 00:00:00")
        self.timeNegative = False #the floor operation for the clock breaks on negative values, so I have it do abs math with a negative sign added. Negative state is tracked by this value.
        
        self.testingStarted = False #this value enables/disables the timer ticks.
        
        self.log_window = None #empty variable so I can enable access to the console log methods once it's instantiated later.
        self.expansionLock = False #if set, will disable the treeWidget from expanding when a selection is made, this maintains the expansion state when check states are changed
        self.testCount = 0 #Tracks the total number of tests loaded.
        self.selTestCount = 0 #tracks the total number of tests selected by the user.
        self.testsDoneCount = 0 #tracks the tests that have been finished in a particular run
        self.testsNotRunCount = 0 #tracks the tests not run.
        self.warningCount = 0 #tracks the number of warnings across all tests
        self.errorCount = 0 #tracks the total error count across all tests
        self.failureCount = 0 #tracks the total failure count across all tests.
        
        self.totalTimeSelected = 0 #sum of the total time in minutes that the selected tests report from their docstring.
        
        self.no_feature = None
        self.alt_window = None
        
        self.currentTestDir = "C:\\" #the default start point for the test folder, used when the registry hasn't been setup yet.
        
        self.sortToggle = True #Toggle value to tell the sort by name function which way to sort.
        
        #self.optionWindow = ConLogOption(self)
        self.icon = IconCollection.Icons()
        
        self.log_window = Console_Log.ConsoleLog(self)
        
        self.folderList = []
        self.folderLevelNodes = []
        
        self.initMainFolder()
        
        self.testResultList = OrderedDict({})
        self.debug_test_list = []
        self.rerunList = []
        
        self.loopTestResults = OrderedDict({})
        
        #self.thread_1 = None
        self.qt_object = QObject()
        
        self.stopTests = False
        
        self.loopTest = Loop_Test.Loop_Test()
        
        self.root = self.addNode(self.treeWidget, self.icon.getIcon(5), "Generic", "", False, True)
        
        self.treeWidget.itemChanged.connect(self.handleItemChanged)
        self.treeWidget.itemSelectionChanged.connect(self.showToolTip)
        
        self.alt_window = AdvancedLoadTests.AdvancedTestLoader(self)
        
        #QObject.connect(self.qt_object, SIGNAL("done"), self.rerunTests)
        
        self.mainFolderEdit.returnPressed.connect(self.useExistingFolder)
        
        #Database Information Objects
        #shouldn't need any of this to operate database now...
        
        #Menu Buttons
        #File Menu
        self.actionSave_Selected_Test.triggered.connect(self.saveSelectedTests)
        self.actionSave_Un_selected_Test.triggered.connect(self.noFeature)
        self.actionSave_Selected_Suite_Time.triggered.connect(self.noFeature)
        self.actionLoad_Test_List_To_Select.triggered.connect(self.noFeature)
        self.actionLoad_Test_List_to_Un_select.triggered.connect(self.noFeature)
        self.actionOpen_Test_Session.triggered.connect(self.noFeature)
        self.actionSave_Test_Session.triggered.connect(self.noFeature)
        
        #View Menu
        self.actionConsole_Log.triggered.connect(self.showConsoleLog)
        self.actionShow_Loop_Tests.triggered.connect(self.showLoopTestWindow)
        
        #Advanced Menu
        self.actionAdvanced_Load_Tests.triggered.connect(self.advancedTestLoader)
        self.actionSave_De_selected_Tests.triggered.connect(self.noFeature)
        self.actionDatabase_Override_Info.triggered.connect(self.noFeature)#self.overrideDatabaseWindow)
        
        #Help Menu
        self.actionHelp_Topics.triggered.connect(self.noFeature)
        self.actionAbout.triggered.connect(self.aboutWindow)
        
        #Window Buttons
        self.runBtn.clicked.connect(self.runBtnSwitch)
        self.folderBtn.clicked.connect(self.getFolder)
        
        #Right Click Context Menu
        #To add further right click menu options: In Qt Designer, View > Action Editor, click Add Action and set the name of the action
        self.treeWidget.addAction(self.actionSort_By_Suite_Name)
        self.treeWidget.addAction(self.actionSort_By_Time_Ascending)
        self.treeWidget.addAction(self.actionSort_By_Time_Descending)
        self.treeWidget.addAction(self.actionClose_All)
        self.treeWidget.addAction(self.actionExpand_All)
        self.treeWidget.addAction(self.actionUnselect_All)
        
        self.actionSort_By_Suite_Name.triggered.connect(self.sortByName)
        self.actionSort_By_Time_Ascending.triggered.connect(self.sortTimeAsc)
        self.actionSort_By_Time_Descending.triggered.connect(self.sortTimeDesc)
        self.actionClose_All.triggered.connect(self.closeAll)
        self.actionExpand_All.triggered.connect(self.expandAll)
        self.actionUnselect_All.triggered.connect(self.uncheckAll)
        #End Menu Buttons
        
        #Create the testing thread and connect it's signals.
        self.TestRunner = TestRunnerModule.TestInterface(self)
        #self.testing_thread = QThread()
        #self.TestRunner.moveToThread(self.testing_thread)
        self.TestRunner.start()
        
        self.TestRunner.endSignal.connect(self.endTestRun)
        self.TestRunner.resultSignal.connect(self.parseResults)
        
        QObject.connect(self.qt_object, SIGNAL("start"), self.TestRunner.startTests)
        
        self.commandLineCall()
    
    def commandLineCall(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == "load_and_run":
                #Command Line Call: python main.py load_and_run C:\top\level\path\of\py\test\files C:\path\to\test\selection\list
                test_path = os.path.normpath(sys.argv[2])
                sel_list_path = os.path.normpath(sys.argv[3])
                self.mainFolderEdit.setText(test_path) #this sets the path in the entry field.
                self.useExistingFolder() #this will take the path and build the tree structure of the tests.
                self.alt_window.fileEntry.setText(sel_list_path)
                self.alt_window.loadTestList()
                self.runBtnSwitch()
    
    def notify(self, *args, **kwargs):
        try:
            return QApplication.notify(self, *args, **kwargs)
        except Exception as e:
            print(e)
            return False
        
    #this method is an override of the default closeEvent method and includes a means to save the window size/location as well as close the console log window when the main window is closed.
    
    def closeEvent(self, event):
        self.closeConsoleLog()
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        QMainWindow.closeEvent(self, event)
        sys.exit(0)
    
    #setter function to allow the override window to set the necessary values to define the product being tested.
    
    def set_Database_Values(self, Version, Revision, Product):
        self.ProductVersion = Version
        self.ProductRevision = Revision
        self.ProductName = Product
    
    #window function to open the override options pane
    '''
    def overrideDatabaseWindow(self):
        self.DBOverride = Override_Window.Override_Window(self)
        self.DBOverride.show()
    '''
        
    #this function gets the log paths from the registry if they already exist and sets them to C:\ if they do not.
    
    def saveSelectedTests(self):
        testList = []
        fileName = QFileDialog.getSaveFileName(self, caption='Save File Name', directory='C:\\', filter='*.txt')
        if not ".txt" in fileName.lower():
            fileName = fileName + ".txt"
        
        for suite in range(0, self.root.childCount()):
            suiteFolder = self.root.child(suite)
            for module in range(0, suiteFolder.childCount()):
                testModule = suiteFolder.child(module)
                for childNum in range(0, testModule.childCount()):
                    leaf = testModule.child(childNum)
                    if leaf.childCount() == 0:
                        if leaf.checkState(0) == Qt.Checked:
                            testList.append(str(testModule.text(0).replace(".py", "") + "," + leaf.text(0)))
        
        try:
            with open(os.path.normpath(fileName), "w") as f:
                for item in testList:
                    f.write(item + "\n")
            f.close()
        except FileNotFoundError:
            print("File Not Found Error: " + fileName)
        except:
            print("Error: " + sys.exc_info())
    
    def initMainFolder(self):
        name0 = "TEST_FOLDER_PATH"
        lastUsed = self.registry.readRegistry(name0)
        if lastUsed:
            self.mainFolderEdit.setText(lastUsed)
        
    def noFeature(self):
        self.no_feature = NoFeatureWarning.NoFeature()
        self.no_feature.show()
        
    def advancedTestLoader(self):
        self.alt_window.show()
        
    def consoleLogWindow(self):
        self.log_window.show()
    
    def multiFolderSelection(self, folderPath):
        self.folderWindow = FolderSelection.FolderSelector(folderPath)
        self.folderWindow.folderListUpdate.connect(self.updateFolderList)
        self.folderWindow.show()
    
    def updateFolderList(self, folderList):
        self.folderList = folderList
        self.debugList.clear()
        self.debug_test_list.clear()
        self.testCount = 0
        
        folderPath = self.mainFolderEdit.text()
        
        self.root = self.addNode(self.treeWidget, self.icon.getIcon(5), folderPath, "", False, True)
        
        if not self.folderList == []:
            for folder in self.folderList:
                node = self.addNode(self.root, self.icon.getIcon(5), folder, "", True, False)
                self.folderLevelNodes.append(node)
                self.buildTreeList(folder, node)
        
        self.testNum.setNum(self.testCount)
        
        for item in self.folderLevelNodes:
            self.getFolderTime(item)
        
    def closeConsoleLog(self):
        self.log_window.close()
    
    #BEGIN RIGHT CLICK MENU FUNCTIONS:
    
    def sortByName(self):
        self.treeWidget.setSortingEnabled(True)
        if self.sortToggle:
            self.treeWidget.sortByColumn(0, Qt.SortOrder(Qt.AscendingOrder))
        else:
            self.treeWidget.sortByColumn(0, Qt.SortOrder(Qt.DescendingOrder))
        self.treeWidget.setSortingEnabled(False)
        self.sortToggle = not self.sortToggle
    
    def sortTimeAsc(self):
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.sortByColumn(1, Qt.SortOrder(Qt.AscendingOrder))
        self.treeWidget.setSortingEnabled(False)
        
    def sortTimeDesc(self):
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.sortByColumn(1, Qt.SortOrder(Qt.DescendingOrder))
        self.treeWidget.setSortingEnabled(False) 
    
    def expandAll(self):
        self.treeWidget.expandAll()
    
    def closeAll(self):
        self.treeWidget.collapseAll()
        
    def uncheckAll(self):
        self.expansionLock = True #this value prevents our checkbox signals from expanding/collapsing the tree
        self.root.setCheckState(0, Qt.Checked)
        self.root.setCheckState(0, Qt.Unchecked)
        self.selTestCount = 0
        self.runNum.setNum(self.selTestCount)
        self.expansionLock = False
        self.totalTimeSelected = 0
    
    #END RIGHT CLICK MENU FUNCTIONS
    
    #BEGIN TIMER FUNCTIONS
    
    def timerTick(self):
        if self.testingStarted:
            self.testTimeRemaining -= 1
            self.totalTestTime += 1
            self.setTime(self.testTimeRemaining)
            self.timeLabel.setText("Time Remaining: " + self.getTime())
        
    def setTime(self, time):
        self.HOUR, self.MINUTE, self.SECOND = self.convertTime(time)
    
    def convertTime(self, timeInSeconds):
        if timeInSeconds < 0:
            timeInSeconds = abs(timeInSeconds)
            self.timeNegative = True
        else:
            self.timeNegative = False
        hour = timeInSeconds // 3600
        minute = (timeInSeconds - (hour * 3600)) // 60
        second = timeInSeconds - (hour * 3600) - (minute * 60)
        return (hour, minute, second)
        
    def getTime(self):
        this_time = "%02d:%02d:%02d" % (self.HOUR, self.MINUTE, self.SECOND)
        if self.timeNegative:
            return ("-" + this_time)
        else:
            return this_time
    
    #END TIMER FUNCTIONS
    
    #The function below controls the operation of the checkboxes and how the nodes expand/collapse as well as the test selected #
    
    def handleItemChanged(self, item, column):
        childCount = item.childCount()
        if item.checkState(column) == Qt.Checked:
            if childCount == 0:
                self.selTestCount += 1
                self.totalTimeSelected += self.getTimeData(item)
            else:
                for i in range(0, childCount):
                    child = item.child(i)
                    child.setCheckState(0, Qt.Checked)
                    if not self.expansionLock:
                        child.setExpanded(True)
                        item.setExpanded(True)
        elif item.checkState(column) == Qt.Unchecked:
            if childCount == 0:
                self.selTestCount -= 1
                self.totalTimeSelected -= self.getTimeData(item)
            else:
                for i in range(0, childCount):
                    child = item.child(i)
                    child.setCheckState(0, Qt.Unchecked)
                    if not self.expansionLock:
                        child.setExpanded(False)
                        item.setExpanded(False)
        self.runNum.setNum(self.selTestCount)
        self.statusbar.showMessage("Time selected: %02d:%02d:%02d" % self.convertTime(self.totalTimeSelected * 60), 0)
    
    def getTimeData(self, node):
        if node.data(1, Qt.ToolTipRole) == None: #time related
            return 0
        else:
            return int(node.data(1, Qt.ToolTipRole)) #time related
        
    #this function takes the time for individual tests and puts it in the detail pane.
    
    def showToolTip(self):
        info = ""
        self.detailPane.setText(info)
        node = self.treeWidget.selectedItems()
        if node:
            if not node[0].data(1, Qt.UserRole) == "" and not node[0].data(1, Qt.UserRole) == None:
                info += node[0].data(1, Qt.UserRole)
                self.detailPane.setText(str(node[0].data(0, Qt.UserRole)) + "\n---------------\n" + info)
    
    #This function gets the folder the user wants the test finder to start at then starts the tree builder.
    
    def getFolder(self):
        testLookupPath = self.mainFolderEdit.text()
        
        if testLookupPath == "":
            testLookupPath = "C:\\"
        
        folderPath = QFileDialog.getExistingDirectory(self, "Select directory", testLookupPath, QFileDialog.ShowDirsOnly)
        
        if not folderPath == "":
            self.folderLevelNodes = []
            self.registry.writeRegistry("TEST_FOLDER_PATH", folderPath)
            self.mainFolderEdit.setText(folderPath)
    
            self.treeWidget.clear()
            
            self.multiFolderSelection(folderPath)
    
    def useExistingFolder(self):
        folderPath = self.mainFolderEdit.text()
        self.registry.writeRegistry("TEST_FOLDER_PATH", folderPath)
        
        self.treeWidget.clear()
        
        self.root = self.addNode(self.treeWidget, self.icon.getIcon(5), folderPath, "", False, True)
        sub_node = self.addNode(self.root, self.icon.getIcon(5), folderPath, "", True, False)
        
        self.testCount = 0
        
        self.debugList.clear()
        self.debug_test_list.clear()
        
        self.buildTreeList(folderPath, sub_node)
        self.testNum.setNum(self.testCount)
        
    # This function builds the actual tree by searching for python files, then parses the file data into a list of files.
        
    def buildTreeList(self, folderPath, node):
        self.treeWidget.blockSignals(True) #begins signal blocking to ignore time changes during the list build.
        for dirpath, _, filenames in os.walk(folderPath):
            for filename in [f for f in filenames if f.endswith(".py")]:
                if not filename == "__init__.py":
                    self.getTestData(os.path.normpath(dirpath + "\\" + filename), node) #newNode
        self.selTestCount = 0
        self.runNum.setNum(self.selTestCount)
        self.totalTimeSelected = 0
        self.statusbar.showMessage("Time selected: " + str(self.totalTimeSelected), 0)
        self.showDebugList()
        self.treeWidget.blockSignals(False) #ends the signal blocking to allow time changes to occur.
    
    # This function uses the AST module to retrieve the docstring (comments) and function names so they can be loaded into the UI.
    
    def getTestData(self, testPath, node):
        try:
            fd = open(testPath, "r+")
            file_contents = fd.read()
        except Exception as e:
            self.detailPane.setText("The file " + testPath + " failed to open or read because of " + str(e) + "\n" + self.detailPane.toPlainText())
            return None
        
        try:
            module = ast.parse(file_contents)
        except Exception as e:
            self.detailPane.setText("Parsing of " + testPath + " failed because of " + str(e) + "\n" + self.detailPane.toPlainText())
            return None
        
        parentNode = self.addNode(node, self.icon.getIcon(5), str(os.path.basename(testPath)), "", True)
        
        className = None
        modDescription = ast.get_docstring(module)
        
        parentNode.setData(1, Qt.UserRole, modDescription)
        
        function_definitions = []
        class_function_definitions = []
        
        for node in module.body:
            if isinstance(node, ast.ClassDef):
                className = node.name
                for cNode in node.body:
                    if isinstance(cNode, ast.FunctionDef):
                        class_function_definitions.append(cNode)
                self.breakdownFunction(class_function_definitions, parentNode, className, testPath)
                class_function_definitions = []
                
            elif isinstance(node, ast.FunctionDef):
                function_definitions.append(node)
                
        if len(function_definitions) > 0:
            self.breakdownFunction(function_definitions, parentNode, className, testPath)
    
    def breakdownFunction(self, function_definitions, parentNode, className, testPath):
        testNode = None
        for f in function_definitions:
            if not (isinstance(f, ast.Assert) or isinstance(f, ast.Expr)):
                testName = str(f.name)
                if self.ignoreXTest(testName):
                    description = ast.get_docstring(f)
                    if not self.checkDebug(description):
                        self.testCount += 1
                        self.testNum.setNum(self.testCount)
                        data = (testPath, className, testName)
                        testNode = self.addNode(parentNode, self.icon.getIcon(4), testName, data)
                        if not description == None:
                            timeData = self.parseDesc(str(description))
                            if timeData == None:
                                testNode.setData(1, Qt.ToolTipRole, "0") #time related
                            else:
                                testNode.setData(1, Qt.ToolTipRole, str(timeData)) #time related   
                            fixtureData = self.parseFixtureName(str(description))
                            if not fixtureData == None:
                                if not self.isFixtureInList(fixtureData):
                                    testNode.setBackground(0, QBrush(QColor(255,0,0,255), Qt.SolidPattern))
                                    testNode.setBackground(1, QBrush(QColor(255,0,0,255), Qt.SolidPattern))
                        testNode.setData(1, Qt.UserRole, description)
                    else:
                        self.debug_test_list.append(className + "." + testName)
        if not parentNode == None:
            self.updateNode(parentNode, None, "", "", self.getParentTime(parentNode))
    
    #xTest_Ignore function performs a regular expression to avoid X'd out tests in a python file.
    
    def ignoreXTest(self, functionName):
        functionName = functionName.lower()
        rg = re.compile('(\Atest_.*)', re.IGNORECASE|re.DOTALL)
        m = rg.search(functionName)
        if not m == None:
            return True
        else:
            return False
    
    def checkDebug(self, docstring):
        if not docstring == None:
            docstring = docstring.lower()
            rg = re.compile('(debug_test\s*=\s*true)', re.IGNORECASE|re.DOTALL)
            m = rg.search(docstring)
            if not m == None:
                return True
            else:
                return False
        else:
            return False
        
    def showDebugList(self):
        for test in self.debug_test_list:
            self.debugList.append(test)
    #ParseDesc function performs a regular expresseion on the docstring to retrieve the time value.
    #If you want a different Time = differentiation, change test_time in the string below to a new value.
            
    def parseDesc(self, desc):
        rg = re.compile('\s*?(test_time\s*=+\s*)([0-9]+)', re.IGNORECASE|re.DOTALL)
        m = rg.search(desc)
        if not m == None:
            var2 = m.group(2)
            
            return var2
        else:
            return None
        
    def parseFixtureName(self, desc):
        rg = re.compile('\s*?(test_fixture\s*=+\s*)([0-9a-zA-Z, ]+)', re.IGNORECASE|re.DOTALL)
        m = rg.search(desc)
        if not m == None:
            var2 = m.group(2)
            return var2
        else:
            return None
        
    def isFixtureInList(self, fixtureStr):
        '''
        if there is a list and the computer name is not on it, then we mark the tree node red to indicate that the test should not be run on the fixture.
        if there is no list, we do nothing
        if there is a list and the computer name is on it, we do nothing
        '''
        fixtures = []
        computerName = os.environ['COMPUTERNAME']
        if "," in fixtureStr:
            fixtures = fixtureStr.split(",")
        else:
            fixtures.append(fixtureStr.strip())
        for fixture in fixtures:
            if fixture.strip() == computerName:
                return True
        return False
    
    # This method calculates the total time for the parent node based on the individual test times.
    
    def getParentTime(self, node):
        time = 0
        num = node.childCount()
        if num > 0:
            if node.child(0).childCount() > 0:
                totalTime = 0
                for k in range(0, node.childCount()):
                    time = self.getParentTime(node.child(k))
                    #if the class node timing data is desired, it is computed at this point
                    totalTime += time
                return totalTime
            else:
                for i in range(0, num):
                    val = node.child(i).data(1, Qt.ToolTipRole)
                    if not val == None:
                        time += int(val)
                node.setData(1, Qt.ToolTipRole, time) #time related
                return time
        else:
            return 0
    #this method gets the folder level time total for the tests beneath the folder node and places it in the toolTip for the folder node.
    
    def getFolderTime(self, node):
        time = 0
        num = node.childCount()
        if num > 0:
            for k in range(0, node.childCount()):
                if(not node.child(k).data(1, Qt.ToolTipRole) == None):
                    time += node.child(k).data(1, Qt.ToolTipRole)
            
        node.setData(1, Qt.ToolTipRole, time)
        node.setData(1, Qt.DisplayRole, time)
    
    # This function adds a node to the tree and sets the various properties of that node.
    
    def addNode(self, parent, icon_, text="", data="", isParent = False, isRoot = False):
        node = QTreeWidgetItem(parent)
        node.setText(0, text)
        node.setCheckState(0, Qt.Unchecked)
        node.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        if isRoot:
            node.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDropEnabled)
        if isParent:
            node.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
        node.setData(0, Qt.UserRole, data)
        node.setIcon(0, icon_)
        return node
    
    # this method is used to update specific values of a given node such as it's icon, text value, data value, or time value.
    
    def updateNode(self, node, icon_=None, text="", data="", time_=-1):
        if not text == "":
            node.setText(0, text)
        if not data == "":
            node.setData(0, Qt.UserRole, data)
        if not icon_ == None:
            node.setIcon(0, icon_)
        if time_ >= 0:
            node.setData(1, Qt.DisplayRole, time_)
    
    def resetTestStats(self):
        self.completeNum.setNum(0)
        self.testsDoneCount = self.failureCount = self.errorCount = self.warningCount = 0
        self.warningNum.setNum(0)
        self.failNum.setNum(0)
        self.errorNum.setNum(0)
        self.notRunNum.setNum(0)
        self.resetIcons()
        self.testsNotRunCount = 0
        self.stopTests = False
        self.testNum.setNum(self.testCount)
        self.testResultList = OrderedDict({})
        self.testRunList.clear()
        self.testTimeRemaining = self.totalTimeSelected * 60
        self.testingStarted = True
        self.resetConsole.emit()
        
    #the following method is called by the Run button and calls the entire test runner operation as a separate thread.
    #Once pressed the button changes function to become a "Stop" button and will tell the test run to stop at the end of the next test.
    
    def runBtnSwitch(self):
        self.treeWidget.blockSignals(True) #prevents time and other values from updating. Stops time re-add during successive runs.
        if self.runBtn.text() == "Run":
            self.resetTestStats()
            self.runBtn.setText("Stop")
            self.getTestsToRun()
            self.treeWidget.blockSignals(False) #prevents time and other values from updating. Stops time re-add during successive runs.
            
            if not self.TestRunner.isRunning():
                self.TestRunner.start()
            QObject.emit(self.qt_object, SIGNAL("start"))
                
        elif self.runBtn.text() == "Stop":
            self.TestRunner.stop_test_run()
            self.stopTests = True
            self.testingStarted = False
            self.runBtn.setText("Kill")
        
        elif self.runBtn.text() == "Kill":
            self.TestRunner.terminate()
            self.TestRunner.wait()
            self.endTestRun()
            
    #This method resets the various values we use during test runs and then steps through the tree to run each test.
    def getTestsToRun(self):
        self.startTestSessionHeader()
        for suite_level in range(0, self.root.childCount()):
            suiteFolder = self.root.child(suite_level)
            for module_level in range(0, suiteFolder.childCount()):
                testModule = suiteFolder.child(module_level)
                test_name_list = []
                module_path = ""
                addTestList = True
                for class_level in range(0, testModule.childCount()):
                    test_level = testModule.child(class_level)
                    if test_level.childCount() == 0:
                        if test_level.checkState(0) == Qt.Checked:
                            node_data = test_level.data(0, Qt.UserRole) #retrieves the tuple from the test_level node
                            module_path = node_data[0] #gets the full module file path from the tuple
                            moduleName = os.path.basename(module_path) #gets the base .py name from the full module file path
                            moduleName = moduleName.strip(".py") #strips the .py from the full module file path
                            
                            if not node_data[1] == None: # makes sure there is a class present in the file
                                test_name_list.append(node_data[1] + "." + node_data[2]) # appends <class_name>.<test name> to the list of tests to run
                            
                                self.newLogData.emit("\t" + moduleName + " -> " + node_data[2] + "\n")
                            else:
                                self.detailPane.setText("The test script {} was skipped because there was no class present ".format(moduleName) + "\n" + self.detailPane.toPlainText())
                                addTestList = False
                            self.testResultList[moduleName + "." + node_data[2]] = 4
                if not module_path == "" and addTestList:
                    if len(test_name_list) > 0:
                        self.testRunList[module_path] = (test_name_list, testModule)
        self.endTestSessionHeader()
        
        
    def endTestRun(self):
        self.treeWidget.blockSignals(True) #prevents time and other values from updating. Stops time re-add during successive runs.
        self.finalResults()
        self.createSumFile()
        self.runBtn.setText("Run")
        self.log_window.logger.copyLogToNetwork()
        self.testingStarted = False
        self.timeLabel.setText("Testing finished in: %02d:%02d:%02d" % self.convertTime(self.totalTestTime))
        self.testTimeRemaining = 0
        self.totalTestTime = 0
        self.treeWidget.blockSignals(False) #prevents time and other values from updating. Stops time re-add during successive runs.
        
        self.rerunTests()
        
    def rerunTests(self):
        #self.treeWidget.blockSignals(True) #ends the signal blocking that prevents the time changes from occurring.
        if (self.runCount.value() > 0) and (not self.stopTests):
            self.runCount.setValue(self.runCount.value() - 1)
            if not len(self.testResultList) == 0:
                self.totalTimeSelected = 0 #clear time here so that later selections/de-selections will re-add time correctly.
                #check if the passing or failing tests are what the user wants to rerun.
                if self.rerunCB.checkState() == Qt.Checked:
                    self.rerunList = [name for name, result in self.testResultList.items() if result < 2]
                    #load the passing tests back in.
                    if not len(self.rerunList) == 0:
                        self.selTestCount = 0
                        self.runNum.setNum(self.selTestCount)
                        self.statusbar.showMessage("Time selected: " + str(self.totalTimeSelected), 0)
                        #load the passing tests back in
                        self.treeHunt()
                    else:
                        self.stopTests = True
                        
                self.testResultList.clear()
                self.rerunList.clear()
                self.runBtnSwitch()
        else:
            self.testResultList.clear()
            self.loopTestResults.clear()
            try:
                self.TestRunner.terminate()
                self.TestRunner.wait()
            except:
                pass
    
    def showLoopTestWindow(self):
        '''
            This function toggles the Loop Test Window to be shown or hidden.
            
            Args:
                None
            
            Returns:
                None
                
            Raises:
                None
        '''
        if self.loopTest.isVisible():
            self.loopTest.hide()
        else:
            self.loopTest.show()
    
    def treeHunt(self):
        '''
            This function searches down the QTreeWidget from the root item to find and deselect each test then run testListCheck on that item.
            
            Args:
                None
            
            Returns:
                None
                
            Raises:
                None
        '''
        for suite in range(0, self.root.childCount()):
            suiteFolder = self.root.child(suite)
            for module in range(0, suiteFolder.childCount()):
                testModule = suiteFolder.child(module)
                for childNum in range(0, testModule.childCount()):
                    leaf = testModule.child(childNum)
                    if leaf.childCount() == 0:
                        leaf.setCheckState(0, Qt.Unchecked)
                        self.testListCheck(testModule, leaf)
    
    def testListCheck(self, parent, child):
        '''
            This function determines if a given test is part of the tests to be rerun, and selects it if it is.
            
            Args:
                parent - the module QTreeWidgetItem in the QTreeWidget
                child - the test level QTreeWidgetItem
                
            Returns:
                None
                
            Raises:
                None
        '''
        testName = parent.data(0, Qt.DisplayRole).strip(".py") + "." + child.data(0, Qt.DisplayRole)
        for name in self.rerunList:
            if testName == name:
                child.setCheckState(0, Qt.Checked)
    
    def parseResults(self, results):
        '''
            This function handles the parsing of the results sent directly to it from the TestRunnerModule.
            
            Args:
                results - the results of a test as a tuple of (test_result, test|module.class)
                
            Returns:
                None
                
            Raises:
                None
        '''
        self.treeWidget.blockSignals(True)
        testResult, testName, moduleName = self.parseUnittestResult(results)
        self.updateResultCounts(testResult)
        currentTestNode = self.getCurrentTestNode(testName, moduleName)
        if not currentTestNode == None:
            currentTestNode.setIcon(0, self.icon.getIcon(testResult))    
        
        self.testResultList[moduleName + "." + testName] = testResult
        
        self.sendResults(moduleName + "." + testName, testResult)
        self.treeWidget.blockSignals(False)
            
    def getCurrentTestNode(self, testName, moduleName):
        '''
            This function finds the specific test node that was run so that results can be assigned.
            
            Args:
                testName - the full test name of the test that just ended.
                
            Returns:
                testNode - This is the QTreeWidgetItem that the testName argument corresponds to.
                
            Raises:
                None
        '''
        moduleList = self.treeWidget.findItems(moduleName + ".py", Qt.MatchExactly | Qt.MatchRecursive)
        testList = self.treeWidget.findItems(testName, Qt.MatchExactly | Qt.MatchRecursive)
        for node in moduleList:
            for test in testList:
                if test.parent() == node:
                    return test
        '''
        if len(items) > 0:
            for node in items:
                for i in range(0, node.childCount()):
                    if 
                if len(testNode) == 1:
                    if testNode[0].data(0, Qt.DisplayRole) == testName:
                        return testNode
        '''
        
    def parseUnittestResult(self, results):
        '''
            This function takes the tuple received from the TestRunnerModule and breaks it down into the result and the test/module names.
            
            Args:
                results - the full result tuple that was received by parseResults
                
            Returns
                test_result - The Error/Fail/Pass/Pass-warning result of the test represented as 0/1/2/3 respectively.
                testName - The name of the test that was run.
                moduleName - The module name of the test that was run.
        '''
        unittest_string = str(results[1])
        unittest_string = unittest_string.split("(")
        testName = unittest_string[0].strip()
        temp = unittest_string[1].replace(")", "")
        moduleClass = temp.split(".")
        moduleName = moduleClass[0].strip()
        
        return results[0], testName, moduleName
    
    def convertResultValues(self, resultNum):
        result_dict = {0 : "<ERROR>", 1 : "<FAILED>", 2 : "<PASSED>", 3 : "<PASS-WR>", 4 : "<NOT RUN>"}
        return result_dict[resultNum]
    
    def updateResultCounts(self, result):
        if result == 0:
            self.errorCount += 1
            self.errorNum.setNum(self.errorCount)
        if result == 1:
            self.failureCount += 1
            self.failNum.setNum(self.failureCount)
        if result == 3:
            self.warningCount += 1
            self.warningNum.setNum(self.warningCount)
        if result == 4:
            self.testsNotRunCount += 1
            self.notRunNum.setNum(self.testsNotRunCount)
        self.testsDoneCount += 1
        self.completeNum.setNum(self.testsDoneCount)
    
    #this method updates the final test result display points in the GUI main window, such as the icons and the numerical result values.
    
    def sendResults(self, testName, result):
        fileName = self.log_window.logger.getLocalLogPath() + "\\" + self.log_window.logger.getLogFileBase() + ".log" #self.localLogPath + "\\" +  self.logFileBase + ".log"
        fileName = os.path.normpath(fileName)
        
        self.loopTestResults.setdefault(testName, [])
        self.loopTestResults[testName].append((self.convertResultValues(result), fileName))
        
        try:
            self.loopTest.update_table(self.loopTestResults)
        except Exception as e:
            self.detailPane.setText(str(e) + "\n" + self.detailPane.toPlainText())
    
    #this function captures the names of the tests that were not run
    
    def notRunCounter(self):
        self.testsNotRunCount += 1
        self.notRunNum.setNum(self.testsNotRunCount)
    
    def resetIcons(self):
        mycount = 0
        for suite in range(0, self.root.childCount()):
            suiteFolder = self.root.child(suite)
            for module in range(0, suiteFolder.childCount()):
                testModule = suiteFolder.child(module)
                for childNum in range(0, testModule.childCount()):
                    leaf = testModule.child(childNum)
                    if leaf.childCount() == 0:
                        self.updateNode(leaf, self.icon.getIcon(4))
                        if leaf.checkState(0) == Qt.Checked:
                            mycount += 1
        self.selTestCount = mycount
        self.runNum.setNum(self.selTestCount)
    
    #this function creates the information at the top of the log file and console log detailing the conditions of the test.
    
    def startTestSessionHeader(self):
        testHeader = strftime("%d.%m.%y %H:%M:%S")
        testHeader += "\n--------------- Test Session Information ---------------\n"
        testHeader += "PyTestRunner Session\t[" + strftime("%d/%m/%y %H:%M:%S") + "]\n\n"
        testHeader += "Installed Components:\n\n"
        testHeader += "\tPyTestRunner:\t {}\n\n".format(self.about.version)
        testHeader += "Selected Tests:\n"
        self.newLogData.emit(testHeader)
    
    def endTestSessionHeader(self):
        
        testHeader = "--------------------------------------------------------\n\n"
        testHeader += "--------------- Running ProjectInfo.exe ---------------\n\n"
        testHeader += "--------------- Begin Test Run ---------------\n\n"
        self.newLogData.emit(testHeader)
    
    #Similar to how TestSessionInfo works, this function gets the end results summary into the logs
    
    def finalResults(self):
        #End results compilation for the console log/log file
        endSession = ""
        endSession += "\n--------------------------------------------------------\n"
        endSession += "PyTestRunner Session Summary\n"
        endSession += "\nTest Results:\n\n"
        for test, result in self.testResultList.items():
            if result == 4:
                self.notRunCounter()
                self.sendResults(test, result)
            testName = test.replace(".", " -> ")
            endSession += self.convertResultValues(result) + "\t" + testName + "\n"
        endSession += "\n--------------------------------------------------------\n"
        self.newLogData.emit(endSession)
    
    '''
    def pushResultsToDB(self):
        if not self.ProductName == None:
            SQL_Connection = PySQL_Connector.PySQL()
            
            tableName = self.ProductName + "_" + self.ProductVersion + "_" + self.ProductRevision
            
            firmware = (self.ProductVersion + "." + self.ProductRevision)
            
            self.currentTestSuite = self.currentTestSuite.strip(".py")
            
            SQL_Connection.SendResultsToDB(tableName, self.currentTestSuite, self.currentTestName, self.currentTestResult, firmware, self.computerName, self.currentTestStart, self.currentTestEnd, self.currentTestDuration, self.networkFilePath, "1.0")
    '''
    
    def createSumFile(self):
        sumData = ""
        fileName = self.log_window.logger.getLocalLogPath() + "\\" + self.log_window.logger.getLogFileBase() + ".sum" #self.localLogPath + "\\" +  self.logFileBase + ".sum"
        fileName = os.path.normpath(fileName)
        try:
            f = open(fileName, 'a+')
            for test, result in self.testResultList.items():
                parts = test.split(".")
                testModule = parts[0]
                testName = parts[1]
                
                if result == "<PASSED>" or result == "<PASS-WR>":
                    baseResult = "PASS"
                    sumData += baseResult + " , " + testModule + "." + testName + ", " + testName + " Test  -  " + result + "\n"
                elif result == "<FAILED>" or result == "<ERROR>":
                    baseResult = "FAIL"          
                    sumData += baseResult + " , " + testModule + "." + testName + ", " + testName + " Test  -  " + result + "\n"

            f.write(sumData)
            f.close()
        except FileNotFoundError:
            print("File Not Found Error in createSumFile() using: " + fileName)
        except:
            print("Unknown Error Occurred createSumFile(): " + str(sys.exc_info()))
    
    def showConsoleLog(self):
        self.consoleLogWindow()
    
    def aboutWindow(self):
        self.about.show()

# this function is what starts the entire execution chain.
        
def main():
    try:
        app = QApplication([])
        app_icon = QIcon()
        app_icon.addFile('PTR_ICON.ico')
        app.setWindowIcon(app_icon)
        form = PythonTestRunner()
        form.setWindowTitle('Python Test Runner')
        
        timer = QTimer()
        timer.setInterval(1000)
        timer.timeout.connect(form.timerTick)
        timer.start()
        
        form.consoleLogWindow()
        form.show()
        app.exec_()
    except KeyboardInterrupt:
        print("Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)
        
if __name__ == '__main__':
    main()