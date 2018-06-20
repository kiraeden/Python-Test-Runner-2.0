'''
Created on Jul 14, 2017

@author: Ethan Lockwood
'''
from unittest import makeSuite
from unittest import TestResult
import unittest
import os, sys, ast, datetime
from PyQt4.QtCore import pyqtSlot, QThread, pyqtSignal

class TestInterface(QThread):
    '''
    The TestInterface is the QThread worker class that operates the test run process given a list of tests. It signals its results back to main for processing.
    Two signals exist from this class that go back to the main:
        endSignal - informs the main program that the current test run has completed.
        resultSignal - sends the result of a test to the main in the form of a tuple of (result, test)
    '''
    endSignal = pyqtSignal()
    resultSignal = pyqtSignal(tuple)
    
    def __init__(self, parent):
        super(TestInterface, self).__init__(parent)
        self.test_loader = unittest.TestLoader()
        self.parent = parent
        #self.testDict = testDict
        self.runner = FWVTestRunner(stream=sys.stdout, verbosity=1, resultSignal=self.resultSignal)

    @pyqtSlot()
    def startTests(self):
        '''
        This function loops through the given list of tests and calls the primary test run function.
        '''
        self.runner.result.shouldStop = False
        if isinstance(self.parent.testRunList, dict):
            if len(self.parent.testRunList.keys()) > 0:
                for modPath, testInfo in self.parent.testRunList.items():
                    self.run_selected_tests_from_suite(modPath, testInfo[0])
        self.endSignal.emit()
            
    def run_whole_test_suite(self, testSuiteModule):
        '''
        This function takes in a module object and tries to run all the tests underneath.
        - currently unused since run_selected_tests_from_suite is capable of handling the job without additional logic.
        '''
        try:
            sys.path.append(os.path.dirname(testSuiteModule))
            testImport = __import__(os.path.basename(testSuiteModule).strip(".py"))
            self.runner.run(makeSuite(self.get_class_name(testSuiteModule, testImport)))
        except Exception as e:
            print(e)
    
    def run_selected_tests_from_suite(self, testSuiteModule, testList):
        '''
        This function takes a string representing the module and a list of test names and tries to run all the given tests.
        '''
        try:
            sys.path.append(os.path.dirname(testSuiteModule))
            testImport = __import__(os.path.basename(testSuiteModule).strip(".py"))
            test_suite = self.test_loader.loadTestsFromNames(testList, module=testImport)
            self.runner.run(test_suite)
        except Exception as e:
            print(e)
    
    def get_class_name(self, testFile, testImport):
        '''
        This function uses the ast library to find the unittest.TestCase class in the given module.
        - Currently this is unused because it's only called by run_whole_test_suite
        '''
        try:
            fd = open(testFile)
            contents = fd.read()
            module = ast.parse(contents)
            for node in module.body:
                if isinstance(node, ast.ClassDef):
                    testClassObj = getattr(testImport, node.name)
                    if issubclass(testClassObj, unittest.TestCase):
                        fd.close()
                        return testClassObj
                    else:
                        print("Test Module {} does not have a class that subclasses unittest.TestCase, test was not able to be imported.")
                        return None
        except Exception as e:
            print(e)
        
    def stop_test_run(self):
        '''
        Passes a call through to the FWVTestRunner object to ask the current test run to stop at the end of the current test.
        '''
        self.runner.stop_tests()

class _TestResult(TestResult):
    '''
    This class extends the existing unittest.TestResult class to enable me to signal out the results directly.
    '''
    def __init__(self, verbosity=1, outputBuffer=None, resultSignal=None):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.outputBuffer = outputBuffer
        self.resultSignal = resultSignal

    def startTest(self, test):
        print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")
        print("Starting test {}".format(test))
        print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")
        TestResult.startTest(self, test)

    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        if self.checkWarnings(test):
            self.resultSignal.emit((3, str(test)))
            print("\n<PASS-WR> - {}\n".format(test))
        else:
            self.resultSignal.emit((2, str(test)))
            print("\n<PASSED> - {}\n".format(test))
        self.clearWarnings(test)
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        self.resultSignal.emit((0, str(test)))
        print("\n<ERROR> occurred in {}, reason: {}\n".format(test, _exc_str))
        self.clearWarnings(test)
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        self.resultSignal.emit((1, str(test)))
        print("\n<FAILED> {}, reason {}\n".format(test, _exc_str))
        self.clearWarnings(test)
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')
            
    def checkWarnings(self, test):
        module = sys.modules[test.__module__]
        try:
            if len(module.__warningregistry__) > 0:
                #print(module.__warningregistry__)
                for key, _ in module.__warningregistry__.items():
                    if isinstance(key, tuple):
                        print("<WARNING> - {} on line # {} in test: {}".format(key[0], key[2], str(test)))
                return True
            else:
                return False
        except:
            return False
    
    def clearWarnings(self, test):
        module = sys.modules[test.__module__]
        try:
            if len(module.__warningregistry__) > 0:
                module.__warningregistry__ = {}
                return True
        except:
            return False
         
class FWVTestRunner():
    '''
    This class is a custom unittest TestRunner that handles creating my custom TestResult class and handles stopping test runs.
    '''
    def __init__(self, stream=sys.stdout, verbosity=1, resultSignal=None):
        self.result = _TestResult(verbosity, stream, resultSignal)
        self.startTime = datetime.datetime.now()

    def run(self, test):
        '''
        Run the given test case or test suite.
        '''
        print("\nBeginning of Test Suite...\n")
        try:
            test(self.result)
        except Exception as e:
            print(e)
        print("\nEnd of Test Suite\n")
        
        self.stopTime = datetime.datetime.now()
        print('\nTime Elapsed: {}'.format(self.stopTime-self.startTime))
    
    def stop_tests(self):
        '''
        Passes a call through to the _TestResult object to ask the test run to stop after the current test.
        '''
        self.result.stop()
            
if __name__ == "__main__":
    PTR = TestInterface()
    PTR.run_selected_tests_from_suite(os.path.normpath("C:\\PTR_Tests\\VirtualMachineTests\\BasicVMTests.py"), ["BasicVMTests.test_custom_imports"])