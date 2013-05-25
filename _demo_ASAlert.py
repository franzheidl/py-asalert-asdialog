from PyASAlert import ASAlert

testAlert = ASAlert(application="System Events", title="ASALert", message="This AppleScript alert is brought to you by Python.", buttons="Cancel, OK", cancelButton="Cancel", defaultButton="OK")
print "Alert result: ", testAlert.result()
print "Alert button returned: ", testAlert.buttonReturned()
print "Alert canceled: ", testAlert.canceled()