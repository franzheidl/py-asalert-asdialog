from PyASChooseApplicationDialog import ASChooseApplicationDialog

testDialog = ASChooseApplicationDialog(multipleSelectionsAllowed="True", returnAs="paths")

print "Dialog: ", testDialog
print "Dialog Object: ", testDialog.dialog
print "Dialog Result: ", testDialog.result()
print "Dialog canceled: ", testDialog.canceled()
