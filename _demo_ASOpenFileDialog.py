from PyASOpenFileDialog import ASOpenFileDialog

testOpenFileDialog = ASOpenFileDialog(multipleSelectionsAllowed="True")

print "Dialog: ", testOpenFileDialog
print "Dialog Object: ", testOpenFileDialog.dialog
print "Dialog Result: ", testOpenFileDialog.result()
print "Dialog canceled: ", testOpenFileDialog.canceled()
