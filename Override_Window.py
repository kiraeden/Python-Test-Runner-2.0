'''
Created on Aug 4, 2016

@author: LockwoodE
'''

from PyQt4.QtGui import QDialog
import PySQL_Connector
import Override_Window_UI

class Override_Window(QDialog, Override_Window_UI.Ui_DBOverride):
    def __init__(self, mainObject):
        super(Override_Window, self).__init__()
        self.setupUi(self)
        
        self.OK_Button.clicked.connect(self.acceptInput)
        self.Cancel_Button.clicked.connect(self.closeWindow)
        
        self.setup_comboBox()
        
        self.main = mainObject
    
    def closeWindow(self):
        self.close()
        
    def acceptInput(self):
        self.main.Set_Database_Values(self.Version_Field.text(), self.Revision_Field.text(), self.comboBox.currentText())
        self.close()
        
    def setup_comboBox(self):
        try:
            SQL_Connection = PySQL_Connector.PySQL()
            
            productList = SQL_Connection.Get_Product_Names()
        except:
            print("No database connection!")
            productList = None
            
        if productList != None:
            for item in productList:
                self.comboBox.addItem(str(item[0]))
        else:
            #default list of products
            self.comboBox.addItem("REX2")
            self.comboBox.addItem("REXU")
            self.comboBox.addItem("GateKeeper")
            self.comboBox.addItem("A3")
            self.comboBox.addItem("CMP")
            self.comboBox.addItem("A3NIC")
            self.comboBox.addItem("EWIC")
            self.comboBox.addItem("REXUNGC")
            self.comboBox.addItem("A3NGC")
            self.comboBox.addItem("ELI")
            self.comboBox.addItem("ZNIC")
            self.comboBox.addItem("SecondSource")
            self.comboBox.addItem("COMMS")
        