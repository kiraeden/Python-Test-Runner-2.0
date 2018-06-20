'''
Created on May 16, 2017

@author: LockwoodE
'''
import LoopTestWindow_UI
import sys, os
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QAbstractItemView, QTableWidgetItem, QColor, QApplication
import webbrowser

class Loop_Test(QWidget, LoopTestWindow_UI.Ui_LoopTestWindow):
    def __init__(self):
        super(Loop_Test, self).__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Loop Test Results")
        
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["Test Name"])
        
        self.clearBtn.clicked.connect(self.clear_window)
        self.closeBtn.clicked.connect(self.close_window)
        
        self.tableWidget.itemClicked.connect(self.OpenResultFile)
        
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger(0))
        
        
        #self.update_table({"C:\\file.py*:.test7" : [("<PASSED>", "C:\\BGInfoInstallLog.txt"), ("<PASS-WR>", "C:\\"), ("<FAILED>", "C:\\"), ("<ERROR>", "C:\\")]})
        
    def close_window(self):
        self.hide()
        
    def clear_window(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Test Name"])
        self.tableWidget.setRowCount(0)
    
    def OpenResultFile(self, item):
        if (not item == None) and (not item.column() == 0):
            webbrowser.open(os.path.normpath(item.toolTip()))
    
    def update_table(self, results):
        self.clear_window()
        numRows = 0
        self.tableWidget.setRowCount(len(results.keys()))
        for key, val in results.items():
            if (len(val) + 1) > self.tableWidget.columnCount():
                self.tableWidget.setColumnCount(len(val) + 1)
            self.tableWidget.setItem(numRows, 0, QTableWidgetItem(self.breakDownTestName(key)))
            self.tableWidget.item(numRows, 0).setTextAlignment(Qt.AlignCenter)
            for i in range(0, len(val)):
                self.tableWidget.setItem(numRows, i+1, QTableWidgetItem(val[i][0]))
                self.tableWidget.item(numRows, i+1).setToolTip(val[i][1])
                self.tableWidget.item(numRows, i+1).setBackground(self.getQColor(val[i][0]))
                self.tableWidget.item(numRows, i+1).setTextAlignment(Qt.AlignCenter)
                
            numRows += 1
        
        numCols = self.tableWidget.columnCount()
        header = ["Test Name"]
        for col in range(1, numCols):
            header.append("Run " + str(col))
            
        self.tableWidget.setHorizontalHeaderLabels(header)
              
        self.tableWidget.resizeColumnsToContents()
                
    def getQColor(self, result):
        if result == "<PASSED>":
            return QColor(0, 255, 0)
        elif result == "<ERROR> ":
            return QColor(255, 0, 0)
        elif result == "<PASS-WR>":
            return QColor(255, 255, 0)
        elif result == "<FAILED>":
            return QColor(255, 123, 0)
        else:
            return QColor(255, 255, 255)
    def breakDownTestName(self, testCall):
        currTestName = testCall.split(".")
        currTestName = currTestName[1]
        return currTestName
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Loop_Test(2)
    form.show()
    
    app.exec_()