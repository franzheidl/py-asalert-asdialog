# PyASAlert
# A simple Python wrapper for an AppleScript alert.
# Franz Heidl 2013
# http://github.com/franzheidl/py-asalert-asdialog
# MIT license.


import subprocess


class ASAlert:
    
    def __init__(self, **kwargs):
        
        alertTypes = ["informational", "warning", "critical"]
        self.alert = {}
        
        if "application" in kwargs.keys():
            self.application = kwargs["application"]
        else:
            self.application = "Finder"
        self.alert["application"] = self.application
        self.applicationstring = 'tell application \"' + self.application + '\"'
        
        if "title" in kwargs.keys():
            self.title = kwargs["title"]
            self.alert["title"] = self.title
        else:
            self.title = " "
        self.alertstring = 'set theResult to display alert \"' + self.title + '\"'
            
        if "message" in kwargs.keys():
            self.message = kwargs["message"]
            self.alert["message"] = self.message
            self.alertstring = self.alertstring + ' message \"' + self.message + '\"'
            
        if "buttons" in kwargs.keys():
            self.buttons = (kwargs["buttons"]).split(", ")
            self.alert["buttons"] = self.buttons
            self.buttonstring = ', '.join([('\"' + button + '\"') for button in self.buttons if button])
            self.alertstring = self.alertstring + ' buttons {' + self.buttonstring + '}'
            
        
        if "displayAs" in kwargs.keys():
            if kwargs["displayAs"] in alertTypes:
                self.displayAs = kwargs["displayAs"]
                self.alert["displayAs"] = self.displayAs
                self.alertstring = self.alertstring + ' as ' + self.displayAs
            

        if "defaultButton" in kwargs.keys():
            dB = kwargs["defaultButton"]
            if isinstance(dB, str) or isinstance(dB, int):
                try:
                    if int(dB) <= len(self.buttons):
                        self.defaultButton = dB
                        self.alert["defaultButton"] = self.defaultButton
                        self.alertstring = self.alertstring + ' default button ' + str(self.defaultButton)
                except:
                    if str(dB) in self.buttons:
                        self.defaultButton = dB
                        self.alert["defaultButton"] = self.defaultButton
                        self.alertstring = self.alertstring + ' default button ' + '\"' + str(self.defaultButton) + '\"'
        
        
        if "cancelButton" in kwargs.keys():
            cB = kwargs["cancelButton"]
            if isinstance(cB, str) or isinstance(cB, int):
                try:
                    if int(cB) <= len(self.buttons):
                        self.cancelButton = cB
                        self.alert["cancelButton"] = self.cancelButton
                        self.alertstring = self.alertstring + ' cancel button ' + str(self.cancelButton)
                except:
                    if str(cB) in self.buttons:
                        self.cancelButton = cB
                        self.alert["cancelButton"] = self.cancelButton
                        self.alertstring = self.alertstring + ' cancel button ' + '\"' + str(self.cancelButton) + '\"'
                    
            
        if "givingUpAfter" in kwargs.keys():
            try:
                self.givingUpAfter = int(kwargs["givingUpAfter"])
                self.alert["givingUpAfter"] = self.givingUpAfter
                self.alertstring = self.alertstring + ' giving up after ' + str(self.givingUpAfter)
            except:
                pass
        
        
        self._result = self.displayAlert(self.applicationstring, self.alertstring)
        self.alert["result"] = self._result
        
        
        
    def displayAlert(self, tellApplication, theAlert):
        self.output = subprocess.check_output(['osascript',
            '-e', tellApplication,
            '-e', 'activate',
            '-e', 'try',
            '-e', theAlert,
            '-e', 'on error number -128',
            '-e', 'set theResult to \"canceled: True\"',
            '-e', 'end try',
            '-e', 'return theResult',
            '-e', 'end tell'])
        return self._dictify(self.output)
        
    
    def result(self):
        if self._result:
            return self._result
        else:
            return False
    
    
    def buttonReturned(self):
        if self.result:
            if "button returned" in self.result().keys():
                return (self.result())["button returned"]
            else:
                return False
        else:
            return False
    
            
    def canceled(self):
        if self.result:
            try:
                return (self.result())["canceled"]
            except KeyError:
                return False
        else:
            return False

    
    def _dictify(self, result):
        _rString = str(result).strip()
        _rPairs = _rString.split(', ')
        _rDict = {}
        for _rPair in _rPairs:
            _rPair = _rPair.split(':')
            _rDict[(_rPair[0])] = _rPair[1]
        return _rDict
        