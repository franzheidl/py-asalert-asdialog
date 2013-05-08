#PyASAlert, PyASDialog
***Simple Python wrappers for AppleScript Alerts and Dialogs.***


##PyASAlert

### Usage


	from PyASAlert import ASAlert
		
	myAlert = ASAlert()
	
	
ASAlert takes the following keyword arguments (all optional):
#### Parameters

##### title (string)
The alert title (displayed in bold type)

##### message (string)
The alert message text

##### buttons (string)
The buttons you want the alert to show, max. 3. If you specify three buttons, the first will be on the left side of the alert, the others on the right. Defaults to OK as default Button actionable by Enter/Return key if not specified.

##### displayAs (string)
The alert type, can be "informational", "warning", and "critical", whereas "critical" looks identical to "informational".

##### defaultButton (string or integer)
The default Enter/Return-actionable button. Defaults to ok if not specified and no buttons have been specified either, if you have specified buttons but no default button, none of them will be the default button. To specify a default button with your custom buttons use either name or index.

##### cancelButton (string or integer)
The button to cancel the alert. Only sensible if you have specified a button for canceling, otherwise ignored. Specify name or index.

##### givingUpAfter (string or integer)
The number of seconds after which you want the alert to disappear if the user didn't click a button.

##### application (string)
The application you want to tell to display the dialog, defaults to Finder.

#### Example

    myAlert = Alert(application="System Events", title="Hi!", message="Some Message for you here", buttons="OK, Stop this, Cancel", displayAs="warning", defaultButton="Stop this", cancelButton=3, givingUpAfter=15)

### Accessing the Alert Result, Methods
The result of an alert can be accessed as a Python dict by calling
	
	myAlert.result()
	
The returned dict is the Python equivalent to the AppleScript record that holds the result.

There are two convenience methods to further process the user input in Python:
	
	myAlert.buttonReturned()
returns the text of the button the user clicked as string, unless the user canceled, which can be tested for with

	myAlert.canceled()
	
which returns True if the alert was canceled, otherwise False.





## PyASDialog

![PyASDialog Screenshot](http://github.com/franzheidl/py-asalert-asdialog/raw/master/screenshots/PyASDialog.png)

### Usage


	from PyASDialog import ASDialog
	
	myDialog = ASDialog()


ASDialog takes the following keyword arguments (all optional):
#### Parameters

##### text (string)
The text you want the dialog to display.

##### title (string)
The title of the dialog

##### application (string)
The name of the application you want to display the dialog, defaults to System Events.

##### defaultAnswer (string)
The string you want to prefill a text input field with. Pass empty string for an empty input field.

##### hiddenAnswer (string)
The hidden (displayed as bullets) string you want to prefill a text input with. Pass empty string for empty input field (User input in this field will still be displayed as bullets).

##### buttons (string)
The buttons you want for your dialog. Defaults to Cancel and OK.

##### defaultButton (string or integer)
The default Enter/Return-actionable button. Defaults to ok if not specified and no buttons have been specified either, if you have specified buttons but no default button, none of them will be the default button. To specify a default button with your custom buttons use either name or index.

##### cancelButton (string or integer)
The button to cancel the dialog. Only sensible if you have specified a button for canceling, otherwise ignored. Specify name or index.

##### icon (string)
A custom icon you want your dialog to display. Specify an .icns file.

##### givingUpAfter (strong or integer)
The number of seconds after which you want the dialog to disappear if the user didn't click a button.

#### Example

	myDialog = ASDialog(title="My Dialog", text"Type Something:", defaultAnswer="", buttons="Cancel, Agree, Decline")


### Accessing the Dialog Result, Methods
The result from a dialog can be accessed as a Python dict by calling

	myDialog.result()
	
The returned dict is the equivalent to the Applescript record that holds the dialog result (with the added value of canceled=True in case the dialog was canceled)

There are multiple convenience methods to further process the result of your dialog in Python:

	myDialog.buttonReturned()
	
returns the text of the button the user clicked as string, unless the user canceled, which can be tested for with

	myDialog.canceled()
	
which returns True if the dialog was canceled, otherwise False.

If your dialog used a text input (defaultAnswer or hiddenAnswer), the returned text can be retrieved like this:

	myDialog.textReturned()
	


##The MIT License (MIT)


Copyright (c) 2013 Franz Heidl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.