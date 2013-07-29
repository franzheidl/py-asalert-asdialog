from PyASSaveFileDialog import ASSaveFileDialog

testSaveDialog = ASSaveFileDialog()

print "Dialog: ", testSaveDialog
print "Dialog Object: ", testSaveDialog.dialog
print "Dialog Result: ", testSaveDialog.result()
print "Dialog canceled: ", testSaveDialog.canceled()
