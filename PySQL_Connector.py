'''
Created on Jun 28, 2016

@author: LockwoodE
'''

import mysql.connector
from mysql.connector import errorcode

#Problem to solve: to enable the Python test runner to put data in the database in such a way as to be usable by the database, I will need the Product name, Firmware Version and Firmware Revision.

class PySQL():
    def __init__(self):
        
        self.cnx = None
        self.cursor = None
        
        try:
            self.cnx = mysql.connector.connect(user = "root", password="L0rdGabenIsMySavior", host="127.0.0.1", database = "test_results", port="3307")
            self.cursor = self.cnx.cursor()
        
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Bad Username or Password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            if not self.cnx == None:
                self.cnx.close()
        
    def endDBSession(self):
        self.cnx.close()
    
    def SendResultsToDB(self, tableName, test_suite, test_name, test_result, test_firmware, test_machine, test_start, test_end, test_duration, test_log_location, testVersion):
        test_results = "INSERT INTO " + tableName + "() VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        results_data = (test_suite, test_name, test_result, test_machine, test_start, test_end, "Auto", test_log_location, test_duration)
        
        self.cursor.execute(test_results, results_data)
        self.cnx.commit()
        
    def Get_Product_Names(self):
        try:
            self.cursor.fetchall() #clears the results queue, if this isn't done, Mysql may spit back an error.
        except:
            pass
        self.cnx.connect(user='root', database='products')
        self.cursor = self.cnx.cursor()
        
        query = "SELECT product_name FROM product_list"
        self.cursor.execute(query)
        
        return self.cursor.fetchall()
            