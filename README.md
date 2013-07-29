#PyASAlert, PyASDialog
***Simple Python wrappers for AppleScript Alerts and Dialogs.***

These wrappers implement all the options and parameters of their AppleScript counterparts, if these are multi-worded in AS they're camelcased in PyASAlert and PyASDialog. Have a look below for the details.

Or you might just have a look at and run `_demo_*.*.py` and take it from there.


##PyASAlert

![PyASAlert Screenshot](http://github.com/franzheidl/py-asalert-asdialog/raw/master/screenshots/PyASAlert.png)

### Usage


	from PyASAlert import ASAlert

	myAlert = ASAlert()


ASAlert takes the following keyword arguments (all optional):

##### title (string)
The alert title, displayed in bold type.

##### message (string)
The alert message text.

##### buttons (string)
The buttons you want the alert to show, max. 3. If you specify three buttons, the first will be on the left side of the alert, the others on the right. Defaults to OK as default Button actionable by Enter/Return key if not specified.

##### displayAs (string)
The alert type, can be "informational", "warning", and "critical", whereas "critical" looks identical to "informational".

##### defaultButton (string or integer)
The default, Enter/Return-actionable button. Defaults to ok if not specified and no buttons have been specified either, if you have specified buttons but no default button, none of them will be the default button. To specify a default button with your custom buttons use either name or index.

##### cancelButton (string or integer)
The button to cancel the alert. Only sensible if you have specified a button for canceling, otherwise ignored. Specify name or index.

##### givingUpAfter (string or integer)
The number of seconds after which you want the alert to disappear if the user didn't click a button.

##### application (string)
The application you want to tell to display the dialog, defaults to Finder.

#### Example

    myAlert = Alert(application="System Events",
    	title="Hi!",
    	message="Some Message for you here",
    	buttons="OK, Stop this, Cancel",
    	displayAs="warning",
    	defaultButton="Stop this",
    	cancelButton=3,
    	givingUpAfter=15)

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

##### text (string)
The text you want the dialog to display.

##### title (string)
The title of the dialog as shown in the title bar.

##### application (string)
The name of the application you want to display the dialog, defaults to System Events.

##### defaultAnswer (string)
The string you want to prefill a text input field with. Pass empty string for an empty input field.

##### hiddenAnswer (string)
The hidden (displayed as bullets) string you want to prefill a text input with. Pass empty string for empty input field (User input in this field will still be displayed as bullets).

##### buttons (string)
The buttons you want for your dialog. Defaults to Cancel and OK.

##### defaultButton (string or integer)
The default, Enter/Return-actionable button. Defaults to ok if not specified and no buttons have been specified either, if you have specified buttons but no default button, none of them will be the default button. To specify a default button with your custom buttons use either name or index.

##### cancelButton (string or integer)
The button to cancel the dialog. Only sensible if you have specified a button for canceling, otherwise ignored. Specify name or index.

##### icon (string)
A custom icon you want your dialog to display. Specify an .icns file.

##### givingUpAfter (string or integer)
The number of seconds after which you want the dialog to disappear if the user didn't click a button.

#### Example

	myDialog = ASDialog(title="My Dialog",
		text"Type Something:",
		defaultAnswer="",
		buttons="Cancel, Agree, Decline")


### Accessing the Dialog Result, Methods
The result from a dialog can be accessed as a Python dict by calling

	myDialog.result()

The returned dict is the equivalent to the Applescript record that holds the dialog result (with the added value of canceled=True in case the dialog was canceled)

There are multiple convenience methods to further process the result of your dialog in Python:

	myDialog.buttonReturned()

returns the text of the button the user clicked as string, unless the user canceled, which can be tested for with

	myDialog.canceled()

which returns True if the dialog was canceled, otherwise False.

If your dialog uses a text input (defaultAnswer or hiddenAnswer), the returned text can be retrieved like this:

	myDialog.textReturned()


## PyASOpenFileDialog

Implements an AppleScript "choose file" dialog, returns either a list of path(s) or False in case the user cancelled the dialog. It does NOT read the file or return its contents.

### Usage

	from PyASOpenFileDialog import ASOpenFileDialog
	
	myOpenFileDialog = ASOpenFileDialog()

ASOpenFileDialog takes the following keyword arguments (all optional):

##### application (string)
The name of the application you want to display the dialog, defaults to System Events.

##### prompt (string)
An optional message to appear on the dialog.

##### type (string)
The type of files that can be opened using the dialog, other types will be disabled. If not set, any type of file can be accessed. 

##### defaultLocation (string)
The default location the dialog opens at. Defaults to system behavior.

##### invisibles (bool or bool as string)
Toggle display of invisibles files, defaults to False.

##### multipleSelectionsAllowed (bool or bool as string)
Toggle whether multiple files can be accessed, defaults to False. If set to true, the dialog will return a list of paths.

##### showingPackageContents (bool or bool as string)
Toggle whether files inside application packages can be accessed. Defaults to False.

##### Example

	myOpenFile = ASOPenFileDialog(type="public.plain-text",
		invisibles= True,
		multipleSelectionsAllowed = True)

### Accessing the Dialog Result, Methods

The result from a Choose File Dialog can be accessed using

	myOpenFile.result()
	
The dialog object as a Python dict can be accessed with 

	myOpenFile.dialog
	
To test whether the user canceled the dialog or not use

	myOpenFile.canceled()


## PyASSaveFileDialog

Implements an AppleScipt "choose file name" dialog, returns either a path or False in case the user cancelled the dialog. It does NOT actually write a file, it just gives you the file path the user chose to save to.

### Usage
	
	from PyASSaveFileDialog import ASSaveFileDialog
	
	mySaveFileDialog = ASSaveFileDialog()
	
ASSaveFileDialog takes the following keyword arguments (all optional):

##### application (string)
The name of the application you want to display the dialog, defaults to System Events.

##### prompt (string)
An optional message you want to appear on the dialog.

##### defaultName (string)
The name of the file to appear in the input by default. Defaults to Untitled (or its equivalent in the respective system language).

##### defaultLocation (string)
The default location the dialog opens at. Defaults to system behavior.

##### Example

	mySaveFileDialog = ASSaveFileDialog(defaultName="Untitled.txt")

### Accessing the Dialog Result, Methods

The result from a Choose File Dialog can be accessed using

	mySaveFileDialog.result()
	
The dialog object as a Python dict can be accessed with 

	mySaveFileDialog.dialog
	
To test whether the user canceled the dialog or not use

	mySaveFileDialog.canceled()


## PyASChooseFolderDialog

Implements an Applescript "choose folder" dialog, returns either a directoy path or False.

### Usage

	from PyASChooseFolderDialog import ASChooseFolderDialog
	
	myChooseFolderDialog = ASChooseFolderDialog()
	
ASChooseFolderDialog takes the following keyword arguments (all optional):

##### application (string)
The name of the application you want to display the dialog, defaults to System Events.

##### prompt (string)
An optional message you want to appear on the dialog.

##### defaultLocation (string)
The default location the dialog opens at. Defaults to system behavior.

##### invisibles (bool or bool as string)
Toggle display of invisibles files, defaults to False.

##### multipleSelectionsAllowed (bool or bool as string)
Toggle whether multiple folders can be accessed, defaults to False. If set to true, the dialog will return a list of paths.

##### showingPackageContents (bool or bool as string)
Toggle whether folders inside application packages can be accessed. Defaults to False.

##### Example

	myChooseFolderDialog = ASChooseFolderDialog(defaultLocation="~/Documents/")

### Accessing the Dialog Result, Methods

The result from a Choose Folder Dialog can be accessed using

	myChooseFolderDialog.result()
	
The dialog object as a Python dict can be accessed with 

	myChooseFolderDialog.dialog
	
To test whether the user canceled the dialog or not use

	myChooseFolderDialog.canceled()


## PyASChooseApplicationDialog

Implements an AppleScript "choose application" dialog, returns a path to an application or False.

### Usage
	from PyAsChooseApplicationDialog import ASChooseApplicationDialog
	
	myChooseApplicationDialog = ASChooseApplicationDialog()
	
ASChooseApplicationDialog atkes the following keyword arguments (all optional):

##### application (string)
The name of the application you want to display the dialog, defaults to System Events.

##### title (string)
A custom title for the dialog, defaults to "Choose Application:"

##### prompt (string)
An optional message you want to appear on the dialog

##### multipleSelectionAllowed (bool or bool as string)
Toggle whether multiple applications can be selected or only one. If set to true, the dialog will return a list of applications, otherwise the name of the chosen application as string.

##### as ("paths" or "names")
Toggle whether to return application name(s) or paths(s), defaults to "names"

#### Example

	myChooseApplicationDialog(multipleSelectionsAllowed=True, returnAs="paths")



### Acessing the Dialog Result, Methods

The result from a Choose Application Dialog can be accessed using

	myChooseApplicationDialog.result()
	
The dialog object as a Python dict can be accessed with 

	myChooseApplicationDialog.dialog
	
To test whether the user canceled the dialog or not use

	myChooseApplicationDialog.canceled()



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