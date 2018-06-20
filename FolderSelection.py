'''
Created on Feb 15, 2017

@author: LockwoodE
'''

import os
import Folder_Select_Window_UI
from PyQt4.QtGui import QWidget, QTreeWidgetItem
from PyQt4.Qt import Qt
from PyQt4.QtCore import pyqtSignal

class FolderSelector(QWidget, Folder_Select_Window_UI.Ui_Form):
    
    folderListUpdate = pyqtSignal(list)
    
    def __init__(self, root_folder):
        super(FolderSelector, self).__init__()
        self.setupUi(self)
        
        self.root = self.addNode(self.folderTreeWidget, root_folder, root_folder)
        
        self.makeFirstLevelTree(root_folder, self.root)
        
        self.testPathList = []
        
        self.rootPath = root_folder
        
        self.ok_btn.clicked.connect(self.OkButtonCode)
        self.cancel_btn.clicked.connect(self.cancelButton)
        
        self.folderTreeWidget.itemExpanded.connect(self.makeFolderTree)
        self.folderTreeWidget.itemCollapsed.connect(self.removeNodes)
    
    # This function adds a node to the tree and sets the various properties of that node.
    
    def addNode(self, parent, text="", data=""):
        node = QTreeWidgetItem(parent)
        node.setText(0, text)
        node.setCheckState(0, Qt.Unchecked)
        node.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        node.setData(0, Qt.UserRole, data)
        return node
    
    def cancelButton(self):
        self.folderListUpdate.emit([self.rootPath])
        self.close()
    
    def OkButtonCode(self):
        self.getCheckedPaths()
        self.folderListUpdate.emit(self.testPathList)
        self.close()
    
    def makeFirstLevelTree(self, folderPath, node):
        for name in os.listdir(folderPath):
            currDir = os.path.join(folderPath, name)
            if not name in [".svn"]:
                if os.path.isdir(currDir):
                    node = self.addNode(node, name, currDir)
                    if not ([d for d in os.listdir(currDir) if os.path.isdir(os.path.join(currDir, d))] == []):
                        self.addNode(node, "...", "...")
                    node = node.parent()
    
    def makeFolderTree(self, node):
        if not node == self.root:
            if node.child(0).text(0) == "...":
                node.removeChild(node.child(0))
            folderPath = node.data(0, Qt.UserRole)
            for name in os.listdir(folderPath):
                currDir = os.path.join(folderPath, name)
                if not name in [".svn"]:
                    if os.path.isdir(currDir):
                        node = self.addNode(node, name, currDir)
                        if not ([d for d in os.listdir(currDir) if os.path.isdir(os.path.join(currDir, d))] == []):
                            self.addNode(node, "...", "...")
                        node = node.parent()
    
    def removeNodes(self, node):
        if not node == self.root:
            for _ in range(0, node.childCount()):
                node.removeChild(node.child(0))
            self.addNode(node, "...", "...")
            
    def getCheckedPaths(self, node=None):
        if node == None:
            node = self.root
            if node.checkState(0) == Qt.Checked:
                self.testPathList.append(node.data(0, Qt.UserRole))
        if node.childCount() > 0:
            for i in range(0, node.childCount()):
                if node.child(i).checkState(0) == Qt.Checked:
                    self.testPathList.append(node.child(i).data(0, Qt.UserRole))
                if node.child(i).childCount() > 0:
                    self.getCheckedPaths(node.child(i))
