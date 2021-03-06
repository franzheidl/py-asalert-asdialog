from PyASAlert import ASAlert
from PyASDialog import ASDialog

testDialog = ASDialog(title="ASDIalog", text="This AppleScript dialog is brought to you by Python.\n\nSay Hi!", defaultAnswer="Hi!", icon="python.icns", buttons="Cancel, Say Hi!", defaultButton="2")
if testDialog.result():
    if testDialog.canceled():
        testAlert = ASAlert(title="ASAlert", message="User canceled.")
    elif testDialog.buttonReturned():
        testAlert = ASAlert(title="ASAlert", message=("User clicked button: " + testDialog.buttonReturned() + ", Text returned was: " + testDialog.textReturned()))
        
    print "Dialog result:", testDialog.result()
    print "Dialog canceled: ", testDialog.canceled()
    print "Dialog button returned: ",  testDialog.buttonReturned()
    print "Dialog text returned: ", testDialog.textReturned()
    
    print "Alert result: ", testAlert.result()
    print "Alert button returned:", testAlert.buttonReturned()
        