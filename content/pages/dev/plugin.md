title: Creating a plugin
reviewed: false

[TOC]

## Relevant files

Let's assume that your plug-in is called `my_plugin`. In that case, your plug-in corresponds to a folder called `my_plugin`, containing at least the following 5 files:

	my_plugin/
		info.yaml
		my_plugin.md
		my_plugin.png
		my_plugin_large.png
		my_plugin.py

## Icons

Your plug-in needs two icons. A small 16x16-pixel icon, which is called `my_plugin.png` and is shown in the overview area, and a larger 32x32-pixel icon, which is called `my_plugin_large.png`. These files need to be placed directly in the plug-in folder.

## Help file

You can provide a help file in [Markdown] or [HTML] format. To add a Markdown help file, simply create a file called `my_plugin.md` in the plug-in folder. For an HTML help file, create a file called `my_plugin.html`. Markdown format is preferred, because it is easier to read. Strictly speaking, the help file is optional, and your plug-in will work without it. However, an informative help file is an essential part of a good plug-in.

## Defining the GUI

The GUI is defined in a file called `info.yaml`[^json]. [YAML] is an easily readable format, and provides a quick and straight-forward way to define your plug-in controls, and specify various kinds of information. Make sure that your file is syntactically valid YAML, for example using a validator such as [yamllint.com].

The following top-level fields are used to show plug-in information by the plug-in and extension manager: `author`, `url`, `version`. and `description`. Another important field is `category`, which specifies in which group the plug-in should appear in the item toolbar (e.g. 'Visual stimuli', etc.). Finally, the `priority` field determines the order in which plug-ins are loaded, where high priority values are loaded last.

The `control` field contains a list of controls. Each control is itself an object that has various fields. The most important fields are:

- `type` specifies the type of the control. Possible values:
	- `checkbox` is a checkable box (`QtGui.QCheckBox`)
	- `color_edit` is a color-select widget (`libqtopensesame.widgets.color_edit`)
	- `combobox` is a drop-down box with multiple options (`QtGui.QComboBox`)
	- `editor` is a multiline text editor (`libqtopensesame.widgets.inline_editor`)
	- `filepool` is a file-select widget (`QtGui.QLineEdit`)
	- `line_edit` is a single-line text input (`QtGui.QLineEdit`)
	- `spinbox` is a text-based numeric-value selector (`QtGui.QSpinBox`)
	- `slider` is a sliding numeric-value selector (`QtGui.QSlider`)
	- `text` is a non-interactive text string (`QtGui.QLabel`)
- `var` specifies the name of the variable that should be set using the control (not applicable if `type` is `text`).
- `label` specifies the text label for the control.
- `name` (optional) specifies under which name the widget should be added to the plug-in object, so that it can be referred to as `self.[name]`.
- `tooltip` (optional) an informative tooltip.

~~~ .yaml
author: Your name
category: Some category
description: This is my plug-in
url: http://your.website
controls:
-
    label: My line edit control
    name: line_edit_widget
    tooltip: You can type something here
    type: line_edit
    var: my_line_edit_var
-
    label: My line checkbox control
    name: checkbox_widget
    tooltip: You can type something here
    type: checkbox
    var: my_checkbox_var
~~~

See the `auto_example` [example](#examples) for a full list of all controls and options.

## Writing the main plug-in code

The main plug-in code is placed in `my_plugin.py`. This file has two classes: The first is `my_plugin`, which contains the runtime part of the plug-in. The second is `qtmy_plugin`, which controls the GUI and is almost empty in most cases, because the controls are defined in `info.yaml`. In many cases, you will only be concerned with three methods:

- `my_plugin.reset()` is where you specify default values for the plug-in variables.
- `my_plugin.prepare()` is where you implement the prepare phase of your plug-in. It is good practice to move as much functionality as possible into `prepare()`, so that the time-critical run phase goes as smooth as possible.
- `my_plugin.run()` is where you implement the run phase of your plug-in.

A very simple example looks like this (see the [examples](#examples) for more realistic examples):

~~~ .python
# Import Python 3 compatibility functions
from libopensesame.py3compat import *
# Import the required modules.
from libopensesame import debug
from libopensesame.item import item
from libqtopensesame.items.qtautoplugin import qtautoplugin

class my_plugin(item):

	description = u'Plug-in description'

	def reset(self):

		# Set default experimental variables and values
		self.var.my_line_edit_var = u'some default'
		self.var.my_checkbox_var = u'some default'
		# Debugging output is only visible when OpenSesame is started with the
		# --debug argument.
		debug.msg(u'My plug-in has been initialized!')

	def prepare(self):

		# Call parent functions.
		item.prepare(self)
		# Prepare your plug-in here.

	def run(self):

		# Record the timestamp of the plug-in execution.
		self.set_item_onset()
		# Run your plug-in here.

class qtmy_plugin(my_plugin, qtautoplugin):

	def __init__(self, name, experiment, script=None):

		# Call parent constructors.
		my_plugin.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
~~~

## Experimental variables

Experimental variables are properties of the `var` object. An example is `self.var.my_line_edit_var` from the example above. These variables that define the plug-in, and are parsed to and from the OpenSesame script.

## Examples

- the [`auto_example`][auto_example] plug-in is a dummy plug-in that contains a lot of information, and a detailed `info.json` that you can use as a basis for your own plug-in.
- the [`fixation_dot`][fixation_dot] plug-in is a simple, but functional example.

[^json]: In OpenSesame 2.8.3, plug-in information was stored in `info.json`. This still works, but for newer plug-ins it is recommend to use `info.yaml`, because YAML-syntax is simpler than JSON-syntax. (In fact, JSON is a specific case of YAML.)

[auto_example]: https://github.com/smathot/OpenSesame/tree/master/plugins/auto_example
[fixation_dot]: https://github.com/smathot/OpenSesame/tree/master/plugins/fixation_dot
[html]: http://en.wikipedia.org/wiki/HTML#Markup
[yaml]: http://en.wikipedia.org/wiki/YAML
[yamllint.com]: http://yamllint.com/
[markdown]: http://daringfireball.net/projects/markdown/syntax
