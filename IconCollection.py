'''
Created on Dec 10, 2015

@author: LockwoodE
'''

from PyQt4.QtGui import QIcon, QPixmap

class Icons():
    def __init__(self):
        #This module contains a series of QIcons
        
        self.iconList = []
        
        self.assetList = ["Art_Assets\errorIcon.png",
                           "Art_Assets\exIcon.png",
                           "Art_Assets\passIcon.png",
                           "Art_Assets\pwIcon.png",
                           "Art_Assets\pyScriptIcon.png",
                           "Art_Assets\pythonIcon.png",
                           "Art_Assets\warningIcon.png"
                           ]
        
        self.buildIconList(self.assetList)
        
    def getIcon(self, i):
        return self.iconList[i]
    
    def buildIconList(self, assets):
        for item in iter(assets):
            icon = QIcon()
            icon.addPixmap(QPixmap(item), QIcon.Normal, QIcon.Off)
            self.iconList.append(icon)
        