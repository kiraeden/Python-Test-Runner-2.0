'''
Created on Mar 2, 2016

@author: LockwoodE
'''

import ast, os

class DocstringReader():
    def __init__(self, pyTestFile):
        self.fileName = os.path.normpath("C:\\PTR_Tests\\test_1_folder\\test_1.py")
    
    def importDoc(self):
        print("Getting Doc...")
        fd = open(self.fileName, "r+")
        file_contents = fd.read()
        module = ast.parse(file_contents)
        
        function_definitions = []
        for node in module.body:
            if isinstance(node, ast.ClassDef):
                for cNode in node.body:
                    if isinstance(cNode, ast.FunctionDef):
                        function_definitions.append(cNode)
        
        print(str(function_definitions))
        
        for f in function_definitions:
            print(f.name)
            print(ast.get_docstring(f))
            
if __name__ == "__main__":
    this = DocstringReader(None)
    this.importDoc()