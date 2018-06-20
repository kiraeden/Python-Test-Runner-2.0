'''
Created on Aug 14, 2017

@author: Ethan Lockwood
'''

import os
from winreg import OpenKey, CloseKey, CreateKey, KEY_READ, QueryValueEx, HKEY_LOCAL_MACHINE, REG_SZ, KEY_WRITE, SetValueEx

class Reg_Access():
    def readRegistry(self, value):
        REG_PATH = 'SOFTWARE\ABB\PythonTestRunner'
        try:
            root_key = OpenKey(HKEY_LOCAL_MACHINE, REG_PATH, 0, KEY_READ)
            [Pathname,_]=(QueryValueEx(root_key, value))
            CloseKey(root_key)
            if "" == Pathname:
                return False
            else:
                return Pathname
        except Exception as e:
            print("While attempting to read a registry key, the following error occurred:\n" + str(e) + "\nThis is likely because this user account does not have admin rights or Python Test Runner has not been run as administrator.\n")
            return False
    
    def writeRegistry(self, myKey, value):
        REG_PATH = 'SOFTWARE\ABB\PythonTestRunner'
        try:
            keyval=r'SOFTWARE\ABB\PythonTestRunner'
            if not os.path.exists("keyval"):
                CreateKey(HKEY_LOCAL_MACHINE,keyval)
            Registrykey= OpenKey(HKEY_LOCAL_MACHINE, REG_PATH, 0, KEY_WRITE)
            SetValueEx(Registrykey, myKey, 0, REG_SZ, value)
            CloseKey(Registrykey)
            return True
        except Exception as e:
            print("While attempting to write a registry key, the following error occurred:\n" + str(e) + "\nThis is likely because this user account does not have admin rights or Python Test Runner has not been run as administrator.\n")
            return False