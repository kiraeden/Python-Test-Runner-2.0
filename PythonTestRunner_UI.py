# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PythonTestRunner_UI.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1030, 697)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(621, 80))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox_11 = QtGui.QGroupBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.groupBox_11.setMinimumSize(QtCore.QSize(301, 31))
        self.groupBox_11.setTitle(_fromUtf8(""))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.runCount = QtGui.QSpinBox(self.groupBox_11)
        self.runCount.setGeometry(QtCore.QRect(230, 7, 61, 22))
        self.runCount.setObjectName(_fromUtf8("runCount"))
        self.label_2 = QtGui.QLabel(self.groupBox_11)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.rerunCB = QtGui.QCheckBox(self.groupBox_11)
        self.rerunCB.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.rerunCB.setObjectName(_fromUtf8("rerunCB"))
        self.gridLayout_3.addWidget(self.groupBox_11, 0, 1, 1, 1)
        self.mainFolderEdit = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFolderEdit.sizePolicy().hasHeightForWidth())
        self.mainFolderEdit.setSizePolicy(sizePolicy)
        self.mainFolderEdit.setMinimumSize(QtCore.QSize(560, 20))
        self.mainFolderEdit.setObjectName(_fromUtf8("mainFolderEdit"))
        self.gridLayout_3.addWidget(self.mainFolderEdit, 1, 0, 1, 2)
        self.folderBtn = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderBtn.sizePolicy().hasHeightForWidth())
        self.folderBtn.setSizePolicy(sizePolicy)
        self.folderBtn.setMinimumSize(QtCore.QSize(41, 23))
        self.folderBtn.setObjectName(_fromUtf8("folderBtn"))
        self.gridLayout_3.addWidget(self.folderBtn, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(621, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(181, 31))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.runNum = QtGui.QLabel(self.groupBox_3)
        self.runNum.setGeometry(QtCore.QRect(141, 8, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.runNum.setFont(font)
        self.runNum.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.runNum.setObjectName(_fromUtf8("runNum"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 8, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(121, 31))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.failNum = QtGui.QLabel(self.groupBox_6)
        self.failNum.setGeometry(QtCore.QRect(82, 5, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.failNum.setFont(font)
        self.failNum.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.failNum.setObjectName(_fromUtf8("failNum"))
        self.label_5 = QtGui.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(10, 5, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setMinimumSize(QtCore.QSize(121, 31))
        self.groupBox_9.setTitle(_fromUtf8(""))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.notRunNum = QtGui.QLabel(self.groupBox_9)
        self.notRunNum.setGeometry(QtCore.QRect(87, 7, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.notRunNum.setFont(font)
        self.notRunNum.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.notRunNum.setObjectName(_fromUtf8("notRunNum"))
        self.label_14 = QtGui.QLabel(self.groupBox_9)
        self.label_14.setGeometry(QtCore.QRect(2, 7, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.groupBox_9, 0, 2, 1, 1)
        self.runBtn = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy)
        self.runBtn.setMinimumSize(QtCore.QSize(91, 31))
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.gridLayout.addWidget(self.runBtn, 0, 3, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(181, 31))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.completeNum = QtGui.QLabel(self.groupBox_4)
        self.completeNum.setGeometry(QtCore.QRect(142, 8, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.completeNum.setFont(font)
        self.completeNum.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.completeNum.setObjectName(_fromUtf8("completeNum"))
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(8, 8, 120, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMinimumSize(QtCore.QSize(121, 31))
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.errorNum = QtGui.QLabel(self.groupBox_7)
        self.errorNum.setGeometry(QtCore.QRect(82, 7, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.errorNum.setFont(font)
        self.errorNum.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.errorNum.setObjectName(_fromUtf8("errorNum"))
        self.label_11 = QtGui.QLabel(self.groupBox_7)
        self.label_11.setGeometry(QtCore.QRect(10, 8, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.groupBox_7, 1, 1, 1, 1)
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setMinimumSize(QtCore.QSize(291, 61))
        self.groupBox_10.setTitle(_fromUtf8(""))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.debugList = QtGui.QTextBrowser(self.groupBox_10)
        self.debugList.setGeometry(QtCore.QRect(0, 20, 291, 41))
        self.debugList.setObjectName(_fromUtf8("debugList"))
        self.label_4 = QtGui.QLabel(self.groupBox_10)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.groupBox_10, 1, 2, 2, 2)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(181, 31))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_16 = QtGui.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(14, 7, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.testNum = QtGui.QLabel(self.groupBox_5)
        self.testNum.setGeometry(QtCore.QRect(141, 7, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.testNum.setFont(font)
        self.testNum.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.testNum.setObjectName(_fromUtf8("testNum"))
        self.gridLayout.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setMinimumSize(QtCore.QSize(121, 31))
        self.groupBox_8.setTitle(_fromUtf8(""))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.warningNum = QtGui.QLabel(self.groupBox_8)
        self.warningNum.setGeometry(QtCore.QRect(82, 5, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.warningNum.setFont(font)
        self.warningNum.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.warningNum.setObjectName(_fromUtf8("warningNum"))
        self.label_7 = QtGui.QLabel(self.groupBox_8)
        self.label_7.setGeometry(QtCore.QRect(5, 5, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.groupBox_8, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.treeWidget = QtGui.QTreeWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setTabKeyNavigation(True)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropOverwriteMode(True)
        self.treeWidget.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.treeWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("Tests"))
        self.treeWidget.headerItem().setText(1, _fromUtf8("Time"))
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(50)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.treeWidget.header().setStretchLastSection(False)
        self.detailPane = QtGui.QTextBrowser(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailPane.sizePolicy().hasHeightForWidth())
        self.detailPane.setSizePolicy(sizePolicy)
        self.detailPane.setMinimumSize(QtCore.QSize(0, 0))
        self.detailPane.setObjectName(_fromUtf8("detailPane"))
        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuAdvanced = QtGui.QMenu(self.menubar)
        self.menuAdvanced.setObjectName(_fromUtf8("menuAdvanced"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Selected_Test = QtGui.QAction(MainWindow)
        self.actionSave_Selected_Test.setObjectName(_fromUtf8("actionSave_Selected_Test"))
        self.actionSave_Un_selected_Test = QtGui.QAction(MainWindow)
        self.actionSave_Un_selected_Test.setObjectName(_fromUtf8("actionSave_Un_selected_Test"))
        self.actionSave_Selected_Suite_Time = QtGui.QAction(MainWindow)
        self.actionSave_Selected_Suite_Time.setObjectName(_fromUtf8("actionSave_Selected_Suite_Time"))
        self.actionLoad_Test_List_To_Select = QtGui.QAction(MainWindow)
        self.actionLoad_Test_List_To_Select.setObjectName(_fromUtf8("actionLoad_Test_List_To_Select"))
        self.actionLoad_Test_List_to_Un_select = QtGui.QAction(MainWindow)
        self.actionLoad_Test_List_to_Un_select.setObjectName(_fromUtf8("actionLoad_Test_List_to_Un_select"))
        self.actionOpen_Test_Session = QtGui.QAction(MainWindow)
        self.actionOpen_Test_Session.setObjectName(_fromUtf8("actionOpen_Test_Session"))
        self.actionSave_Test_Session = QtGui.QAction(MainWindow)
        self.actionSave_Test_Session.setObjectName(_fromUtf8("actionSave_Test_Session"))
        self.actionConsole_Log = QtGui.QAction(MainWindow)
        self.actionConsole_Log.setObjectName(_fromUtf8("actionConsole_Log"))
        self.actionMeter_Builders = QtGui.QAction(MainWindow)
        self.actionMeter_Builders.setObjectName(_fromUtf8("actionMeter_Builders"))
        self.actionTest_Station = QtGui.QAction(MainWindow)
        self.actionTest_Station.setObjectName(_fromUtf8("actionTest_Station"))
        self.actionFilter_Suites_By_Author = QtGui.QAction(MainWindow)
        self.actionFilter_Suites_By_Author.setObjectName(_fromUtf8("actionFilter_Suites_By_Author"))
        self.actionAdvanced_Load_Tests = QtGui.QAction(MainWindow)
        self.actionAdvanced_Load_Tests.setObjectName(_fromUtf8("actionAdvanced_Load_Tests"))
        self.actionSave_De_selected_Tests = QtGui.QAction(MainWindow)
        self.actionSave_De_selected_Tests.setObjectName(_fromUtf8("actionSave_De_selected_Tests"))
        self.actionHelp_Topics = QtGui.QAction(MainWindow)
        self.actionHelp_Topics.setObjectName(_fromUtf8("actionHelp_Topics"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSort_By_Suite_Name = QtGui.QAction(MainWindow)
        self.actionSort_By_Suite_Name.setObjectName(_fromUtf8("actionSort_By_Suite_Name"))
        self.actionSort_By_Time_Ascending = QtGui.QAction(MainWindow)
        self.actionSort_By_Time_Ascending.setObjectName(_fromUtf8("actionSort_By_Time_Ascending"))
        self.actionSort_By_Time_Descending = QtGui.QAction(MainWindow)
        self.actionSort_By_Time_Descending.setObjectName(_fromUtf8("actionSort_By_Time_Descending"))
        self.actionExpand_All = QtGui.QAction(MainWindow)
        self.actionExpand_All.setObjectName(_fromUtf8("actionExpand_All"))
        self.actionClose_All = QtGui.QAction(MainWindow)
        self.actionClose_All.setObjectName(_fromUtf8("actionClose_All"))
        self.actionUnselect_All = QtGui.QAction(MainWindow)
        self.actionUnselect_All.setObjectName(_fromUtf8("actionUnselect_All"))
        self.actionDatabase_Override_Info = QtGui.QAction(MainWindow)
        self.actionDatabase_Override_Info.setObjectName(_fromUtf8("actionDatabase_Override_Info"))
        self.actionShow_Loop_Tests = QtGui.QAction(MainWindow)
        self.actionShow_Loop_Tests.setObjectName(_fromUtf8("actionShow_Loop_Tests"))
        self.menuFile.addAction(self.actionSave_Selected_Test)
        self.menuFile.addAction(self.actionSave_Un_selected_Test)
        self.menuFile.addAction(self.actionSave_Selected_Suite_Time)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad_Test_List_To_Select)
        self.menuFile.addAction(self.actionLoad_Test_List_to_Un_select)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Test_Session)
        self.menuFile.addAction(self.actionSave_Test_Session)
        self.menuView.addAction(self.actionConsole_Log)
        self.menuView.addAction(self.actionShow_Loop_Tests)
        self.menuAdvanced.addAction(self.actionAdvanced_Load_Tests)
        self.menuAdvanced.addSeparator()
        self.menuAdvanced.addAction(self.actionSave_De_selected_Tests)
        self.menuAdvanced.addAction(self.actionDatabase_Override_Info)
        self.menuHelp.addAction(self.actionHelp_Topics)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAdvanced.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Set base path for project:", None))
        self.label_2.setText(_translate("MainWindow", "Run Count", None))
        self.rerunCB.setText(_translate("MainWindow", "Re-Run Failed Tests", None))
        self.folderBtn.setText(_translate("MainWindow", "...", None))
        self.groupBox.setTitle(_translate("MainWindow", "Test Session Status", None))
        self.runNum.setText(_translate("MainWindow", "0", None))
        self.label_6.setText(_translate("MainWindow", "Selected To Run:", None))
        self.failNum.setText(_translate("MainWindow", "0", None))
        self.label_5.setText(_translate("MainWindow", "Failures:", None))
        self.notRunNum.setText(_translate("MainWindow", "0", None))
        self.label_14.setText(_translate("MainWindow", "Not Tested:", None))
        self.runBtn.setText(_translate("MainWindow", "Run", None))
        self.completeNum.setText(_translate("MainWindow", "0", None))
        self.label_9.setText(_translate("MainWindow", "Tests Completed:", None))
        self.errorNum.setText(_translate("MainWindow", "0", None))
        self.label_11.setText(_translate("MainWindow", "Errors:", None))
        self.label_4.setText(_translate("MainWindow", "Debug Tests:", None))
        self.label_16.setText(_translate("MainWindow", "Total # of tests:", None))
        self.testNum.setText(_translate("MainWindow", "0", None))
        self.warningNum.setText(_translate("MainWindow", "0", None))
        self.label_7.setText(_translate("MainWindow", "Warnings:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuAdvanced.setTitle(_translate("MainWindow", "Advanced", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionSave_Selected_Test.setText(_translate("MainWindow", "Save Selected Test", None))
        self.actionSave_Un_selected_Test.setText(_translate("MainWindow", "Save Un-selected Test", None))
        self.actionSave_Selected_Suite_Time.setText(_translate("MainWindow", "Save Selected Suite Time", None))
        self.actionLoad_Test_List_To_Select.setText(_translate("MainWindow", "Load Test List To Select", None))
        self.actionLoad_Test_List_to_Un_select.setText(_translate("MainWindow", "Load Test List to Un-select", None))
        self.actionOpen_Test_Session.setText(_translate("MainWindow", "Open Test Session", None))
        self.actionSave_Test_Session.setText(_translate("MainWindow", "Save Test Session", None))
        self.actionConsole_Log.setText(_translate("MainWindow", "Show Console Log", None))
        self.actionMeter_Builders.setText(_translate("MainWindow", "Meter Builders", None))
        self.actionTest_Station.setText(_translate("MainWindow", "Test Station", None))
        self.actionFilter_Suites_By_Author.setText(_translate("MainWindow", "Filter Suites By Author", None))
        self.actionAdvanced_Load_Tests.setText(_translate("MainWindow", "Advanced Load Tests", None))
        self.actionSave_De_selected_Tests.setText(_translate("MainWindow", "Save De-selected Tests", None))
        self.actionHelp_Topics.setText(_translate("MainWindow", "Help Topics", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionSort_By_Suite_Name.setText(_translate("MainWindow", "Sort By Suite Name", None))
        self.actionSort_By_Time_Ascending.setText(_translate("MainWindow", "Sort By Time (Ascending)", None))
        self.actionSort_By_Time_Descending.setText(_translate("MainWindow", "Sort By Time (Descending)", None))
        self.actionExpand_All.setText(_translate("MainWindow", "Expand All", None))
        self.actionClose_All.setText(_translate("MainWindow", "Close All", None))
        self.actionUnselect_All.setText(_translate("MainWindow", "Unselect All", None))
        self.actionDatabase_Override_Info.setText(_translate("MainWindow", "Database Override Info", None))
        self.actionShow_Loop_Tests.setText(_translate("MainWindow", "Show Loop Test Window", None))

