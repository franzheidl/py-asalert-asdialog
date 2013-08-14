# PyASChooseApplicationDialog
# A simple Python wrapper for an AppleScript Choose Application dialog.
# Franz Heidl 2013
# http://github.com/franzheidl/py-asalert-asdialog
# MIT license.

import subprocess


class ASChooseApplicationDialog:
    
    def __init__(self, **kwargs):
        
        self.dialog = {}
        self.dialogString = 'set theApp to choose application'
        
        if "application" in kwargs.keys():
            self.application = kwargs["application"]
        else:
            self.application = "System Events"
        self.dialog["application"] = self.application
        self.applicationString = 'tell application \"' + self.application + '\"'
        
        if "returnAs" in kwargs.keys() and kwargs["returnAs"] == "paths":
            self.returnAs = "paths"
            self.dialog["returnAs"] = self.returnAs
            self.dialogString += ' as alias'
        else:
            self.returnAs = "names"
        
        if 'title' in kwargs.keys():
            self.title = kwargs["title"]
            self.dialog["title"] = self.title
            self.dialogString += ' with prompt ' + '\"' + self.title + '\"'
            
            
        if "prompt" in kwargs.keys():
            self.prompt = kwargs["prompt"]
            self.dialog["prompt"] = self.prompt
            self.dialogString += (' with prompt ' + '\"' + self.prompt + '\"')
           
            
        if "multipleSelectionsAllowed" in kwargs.keys():
            mSA = kwargs["multipleSelectionsAllowed"]
            if mSA == True or mSA == "True":
                self.multipleSelectionsAllowed = kwargs["multipleSelectionsAllowed"]
                self.dialog["multipleSelectionsAllowed"] = True
                self.dialogString += ' with multiple selections allowed'
            else:
                self.multipleSelectionsAllowed = kwargs["multipleSelectionsAllowed"]
                self.dialog["multipleSelectionsAllowed"] = False
        
        
        
        
            
        self._result = self.displayChooseApplicationDialog(self.applicationString, self.dialogString)
        self.dialog["result"] = self._result
        
        
        
    def displayChooseApplicationDialog(self, theApplication, theDialog):
        if self.returnAs == "paths":
            self.output = subprocess.check_output(['osascript',
                '-e', 'set theAppPaths to {}',
                '-e', theApplication,
                '-e', 'activate',
                '-e', 'try',
                '-e', theDialog,
                '-e', 'if class of theApp is text',
                '-e', 'set theAppPaths to POSIX path of (theApp as alias)',
                '-e', 'else if class of theApp is list',
                '-e', 'repeat with anApp in theApp',
                '-e', 'set theAppPaths to theAppPaths & POSIX path of (anApp as alias)',
                '-e', 'end repeat',
                '-e', 'end if',
                '-e', 'on error number -128',
                '-e', 'set theAppPaths to \"False\"',
                '-e', 'end try',
                '-e', 'return theAppPaths',
                '-e', 'end tell'])
        else:
            self.output = subprocess.check_output(['osascript',
                '-e', theApplication,
                '-e', 'activate',
                '-e', 'try',
                '-e', theDialog,
                '-e', 'on error number -128',
                '-e', 'set theApp to \"False\"',
                '-e', 'end try',
                '-e', 'return theApp',
                '-e', 'end tell'])
            
        appsString = self.output.strip()
        if appsString != "False":
            if len(appsString.split(", ")) > 1:
                apps = appsString.split(", ")
            else:
                apps = appsString
        else:
            apps = "False"
            

            
        return apps
        
    
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
        return self.dialog.result()
        
            