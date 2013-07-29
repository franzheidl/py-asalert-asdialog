# PyASChooseFolderDialog
# A simple Python wrapper for an AppleScript Choose Folder dialog.
# Franz Heidl 2013
# http://github.com/franzheidl/py-asalert-asdialog
# MIT license.


# TODO: returns HFS paths ?!? should be POSIX

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
    
                
        self._result = self.displayChooseFolderDialog(self.applicationString, self.dialogString)
        self.dialog["result"] = self._result
        
               
    
    def displayChooseFolderDialog(self, theApplication, theDialog):
        self.output = subprocess.check_output(['osascript',
            '-e', 'set theFolders to {}',
            '-e', 'set thePFolders to {}',
            '-e', theApplication,
            '-e', 'activate',
            '-e', 'try',
            '-e', theDialog,
            #'-e', 'set theFolder to (POSIX path of theFolder as text)',
            '-e', 'set theFolders to theFolders & theFolder',
            '-e', 'repeat with aFolder in theFolders',
            '-e', 'if the length of thePFolders is greater than 1 then',
            '-e', 'set thePFolders to thePFolders & \", \" & (POSIX path of aFolder) as text',
            '-e', 'else',
            '-e', 'set thePFolders to thePFolders & (POSIX path of aFolder) as text',
            '-e', 'end if',
            '-e', 'end repeat',
            '-e', 'on error number -128',
            '-e', 'set theFolder to \"False\"',
            '-e', 'end try',
            '-e', 'return theFolder',
            '-e', 'end tell'])
        pathsString = self.output.strip()
        if pathsString != "False":
            if len(pathsString.split(", ")) > 1:
                paths = pathsString.split(", ")
            else:
                paths = pathsString
        else:
            paths = "False"
        return paths
        
        
    def result(self):
        if self._result:
            return self._result
        else:
            return False
            
            
    def canceled(self):
        if self._result == "False":
            return True
        else:
            return False
            
    
    def __repr__(self):
        return self.result()
    
        
    def __str__(self):
        return str(self.result())
            