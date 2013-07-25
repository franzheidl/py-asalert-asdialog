# PyASSaveFileDialog
# A simple Python wrapper for an AppleScript Open File alert.
# Franz Heidl 2013
# http://github.com/franzheidl/py-asalert-asdialog
# MIT license.



import os
import subprocess

class ASSaveFileDialog():
    
    def __init__(self, **kwargs):
        
        self.dialog = {}
        self.dialogString = 'set theFile to choose file name'
        
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
            
            
        if "defaultName" in kwargs.keys():
            self.defaultName = kwargs["defaultName"]
            self.dialog["defaultName"] = self.defaultName
            self.dialogString += (' default name ' + '\"' + self.defaultName + '\"')
            
        if "defaultLocation" in kwargs.keys():
            if os.path.exists(kwargs["defaultLocation"]):
                self.defaultLocation = kwargs["defaultLocation"]
                self.dialog["defaultLocation"] = self.defaultLocation
                if not self.defaultLocation.startswith("/"):
                    self.defaultLocation = "/" + self.defaultLocation
                self.dialogString += (' default location (POSIX file \"' + self.defaultLocation + '\" as alias)')
            
        
        self._result = self.displaySaveFileDialog(self.applicationString, self.dialogString)
        
        # coerce to posix unless dialog was cancelled:
        if self._result != "False":
            self._result = self._result.split(":")
            self._result = self._result[1:]
            self._result = "/".join(res for res in self._result if res)
            if not self._result.startswith("/"):
                self._result = "/" + self._result
            
        else:
            self.dialog["cancelled"] = True
        self.dialog["result"] = self._result
        
            
    def displaySaveFileDialog(self, theApplication, theDialog):
        self.output = subprocess.check_output(['osascript',
            '-e', theApplication,
            '-e', 'activate',
            '-e', 'try',
            '-e', theDialog,
            '-e', 'set theFile to theFile as text',
            '-e', 'on error number -128',
            '-e', 'set theFile to \"False\"',
            '-e', 'end try',
            '-e', 'return theFile',
            '-e', 'end tell'])
        return self.output.strip()
        
        
    def result(self):
        if self._result:
            return self.dialog["result"]
        else:
            return False
            
    
    def __repr__(self):
        return self.result()
    