# PyASChooseFolderDialog
# A simple Python wrapper for an AppleScript Choose Folder dialog.
# Franz Heidl 2013
# http://github.com/franzheidl/py-asalert-asdialog
# MIT license.

import os
import subprocess


class ASChooseFolderDialog:
    
    def __init__(self, **kwargs):
        
        self.dialog = {}
        self.dialogString = 'set theFolder to choose folder'
        
        if "application" in kwargs.keys():
            self.application = kwargs["application"]
        else:
            self.application = "System Events"
        self.dialog["application"] = self.application
        self.applicationString = 'tell application \"' + self.application + '\"'
        
        
        if "prompt" in kwargs.keys():
            self.prompt = kwargs["prompt"]
            self.dialog["prompt"] = self.prompt
            self.dialogString += (' with prompt ' + '\"' + self.prompt + '\"')
            
        
        if "invisibles" in kwargs.keys():
            iv = kwargs["invisibles"]
            if iv == True or iv == "True":
                self.invisibles = kwargs["invisibles"]
                self.dialog["invisibles"] = True
                self.dialogString += ' invisibles true'
            else:
                self.invisibles = False
                self.dialog["invisibles"] = self.invisibles
                self.dialogString += ' invisibles false'
                
        
        if "multipleSelectionsAllowed" in kwargs.keys():
            mSA = kwargs["multipleSelectionsAllowed"]
            if mSA == True or mSA == "True":
                self.multipleSelectionsAllowed = kwargs["multipleSelectionsAllowed"]
                self.dialog["multipleSelectionsAllowed"] = True
                self.dialogString += ' with multiple selections allowed'
            else:
                self.multipleSelectionsAllowed = kwargs["multipleSelectionsAllowed"]
                self.dialog["multipleSelectionsAllowed"] = False
                
        
        if "showingPackageContents" in kwargs.keys():
            sPC = kwargs["showingPackageContents"]
            if sPC == True or sPC == "True":
                self.showingPackageContents = kwargs["showingPackageContents"]
                self.dialog["showingPackageContents"] = True
                self.dialogString += ' showing package contents'
            else:
                self.showingPackageContents = kwargs["showingPackageContents"]
                self.dialog["showingPackageContents"] = False
    
                
        self._result = self.displayChooseFolderDialog(self.applicationString, self.dialogString)
               
    
    def displayChooseFolderDialog(self, theApplication, theDialog):
        self.output = subprocess.check_output(['osascript',
            '-e', theApplication,
            '-e', 'activate',
            '-e', 'try',
            '-e', theDialog,
            '-e', 'set theFolder to (POSIX path of theFolder as text)',
            '-e', 'on error number -128',
            '-e', 'set theFolder to \"False\"',
            '-e', 'end try',
            '-e', 'return theFolder',
            '-e', 'end tell'])
        return self.output.strip()
        
        
    def result(self):
        if self._result:
            return self._result
        else:
            return False
            
            
    def cancelled(self):
        if self._result:
            if self._result == "False":
                return True
            else:
                return False
            
    
    def __repr__(self):
        return self.result()
            