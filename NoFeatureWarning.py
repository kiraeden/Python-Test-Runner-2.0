'''
Created on Dec 31, 2015

@author: LockwoodE
'''

from PyQt4.QtGui import QWidget
import NoFeatureWindow

class NoFeature(QWidget, NoFeatureWindow.Ui_NoFeature):
    def __init__(self):
        super(NoFeature, self).__init__()
        
        self.setupUi(self)
        
        self.closeBtn.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        self.close()