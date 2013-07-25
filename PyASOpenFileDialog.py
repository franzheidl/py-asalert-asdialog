# PyASOpenFileDialog
# A simple Python wrapper for an AppleScript Open File alert.
# Franz Heidl 2013
# http://github.com/franzheidl/py-asalert-asdialog
# MIT license.

# TODO check/fix/implement return value for multiple selections allowed

import subprocess
import os

class ASOpenFileDialog():
    
    def __init__(self, **kwargs):
        
        self.dialog = {}
        self.dialogString = 'set theFile to choose file'
        
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
            
            
        if "type" in kwargs.keys():
            self.ofType = (kwargs["type"]).split(", ")
            self.dialog["ofType"] = self.ofType
            self.ofTypeString = ', '.join([('\"' + aType + '\"') for aType in self.ofType if aType])
            self.dialogString += ' of type {' + self.ofTypeString + '}'
            
            
        if "defaultLocation" in kwargs.keys():
            if os.path.exists(kwargs["defaultLocation"]):
                self.defaultLocation = kwargs["defaultLocation"]
                self.dialog["defaultLocation"] = self.defaultLocation
                if not self.defaultLocation.startswith("/"):
                    self.defaultLocation = "/" + self.defaultLocation
                self.dialogString += (' default location (POSIX file \"' + self.defaultLocation + '\" as alias)')
          
            
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
        
        print self.dialog
        
        self._result = self.displayOpenDialog(self.applicationString, self.dialogString)
        self.dialog["result"] = self._result
        if self._result == "False":
            self.dialog["cancelled"] = True

           
        
    def displayOpenDialog(self,theApplication, theDialog):
        self.output = subprocess.check_output(['osascript',
            '-e', theApplication,
            '-e', 'activate',
            '-e', 'try',
            '-e', theDialog,
            '-e', 'set theFile to (POSIX path of theFile) as text',
            '-e', 'on error number -128',
            '-e', 'set theFile to \"False\"',
            '-e', 'end try',
            '-e', 'return theFile',
            '-e', 'end tell'])
        return self.output.strip()
    
    
    def result(self):
        if self._result:
            return self._result
        else:
            return False
    
            
    def __repr__(self):
        return self.result()
    