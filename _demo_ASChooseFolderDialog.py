from PyASChooseFolderDialog import ASChooseFolderDialog

testChooseFolder = ASChooseFolderDialog(multipleSelectionsAllowed=True, defaultLocation="~/Documents/Projects/RoboFont")

print "Dialog: ", testChooseFolder
print "Dialog Object: ", testChooseFolder.dialog
print "Dialog Result: ", testChooseFolder.result()
print "Dialog canceled: ", testChooseFolder.canceled()
