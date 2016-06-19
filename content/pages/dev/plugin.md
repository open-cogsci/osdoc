title: Creating a plugin

[TOC]

## Relevant files

Let's assume that your plugin is called `my_plugin`. In that case, your plugin corresponds to a folder called `my_plugin`, containing at least the following 5 files:

	my_plugin/
		info.yaml
		my_plugin.md
		my_plugin.py

## Icons

Each plug-in needs an icon, which you can specify in one of two ways:

- Include two icon files in the plugin folder. The first should be a 16x16 px png file called `my_plugin.png`; the second should be a 32x32 px png file called `my_plugin_large.png`.
- Specify an `icon` key in `info.yaml`. If you do this, the plugin icon will be taken from the icon theme.

## Help file

You can provide a help file in [Markdown] or [HTML] format. To add a Markdown help file, simply create a file called `my_plugin.md` in the plugin folder. For an HTML help file, create a file called `my_plugin.html`. Markdown format is preferred, because it is easier to read. Strictly speaking, the help file is optional, and your plugin will work without it. However, an informative help file is an essential part of a good plugin.

## Defining the GUI

The GUI is defined in a file called `info.yaml`[^json]. [YAML] provides a straight-forward way to define your plugin controls, and specify other kinds of information. Make sure that your file is syntactically valid YAML, for example using a validator such as [yamllint.com].

The following top-level fields are used to show plugin information by the plugin and extension manager: `author`, `url`, `version`. and `description`. Another important field is `category`, which specifies in which group the plugin should appear in the item toolbar (e.g. 'Visual stimuli', etc.). The `icon` field specifies an icon name (as explained above). Finally, the `priority` field determines the order in which plugins are loaded, where high priority values are loaded last.

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
- `name` (optional) specifies under which name the widget should be added to the plugin object, so that it can be referred to as `self.[name]`.
- `tooltip` (optional) an informative tooltip.

~~~ .yaml
author: Your name
category: Some category
description: This is my plugin
icon: text-x-generic
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

## Writing the main plugin code

The main plugin code is placed in `my_plugin.py`. This file has two classes:

- `my_plugin`, which contains the runtime part of the plugin.
- `qtmy_plugin`, which controls the GUI. This class is almost empty in most cases, because the controls are defined in `info.yaml`.

In many cases, you will only be concerned with three methods:

- `my_plugin.reset()` is where you specify default values for the plugin variables.
- `my_plugin.prepare()` is where you implement the prepare phase of your plugin. It is good practice to move as much functionality as possible into `prepare()`, so that the time-critical run phase goes as smooth as possible.
- `my_plugin.run()` is where you implement the run phase of your plugin.

A very simple example looks like this (see the [examples](#examples) for more realistic examples):

~~~ .python
# Import Python 3 compatibility functions
from libopensesame.py3compat import *
# Import the required modules.
from libopensesame import debug
from libopensesame.item import item
from libqtopensesame.items.qtautoplugin import qtautoplugin

class my_plugin(item):

	description = u'plugin description'

	def reset(self):

		# Set default experimental variables and values
		self.var.my_line_edit_var = u'some default'
		self.var.my_checkbox_var = u'some default'
		# Debugging output is only visible when OpenSesame is started with the
		# --debug argument.
		debug.msg(u'My plugin has been initialized!')

	def prepare(self):

		# Call parent functions.
		item.prepare(self)
		# Prepare your plugin here.

	def run(self):

		# Record the timestamp of the plugin execution.
		self.set_item_onset()
		# Run your plugin here.

class qtmy_plugin(my_plugin, qtautoplugin):

	def __init__(self, name, experiment, script=None):

		# Call parent constructors.
		my_plugin.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
~~~

## Experimental variables

Experimental variables are properties of the `var` object. An example is `self.var.my_line_edit_var` from the example above. These variables that define the plugin, and are parsed to and from the OpenSesame script.

## Examples

- the [`auto_example`][auto_example] plugin is a dummy plugin that contains a lot of information, and a detailed `info.json` that you can use as a basis for your own plugin.
- the [`fixation_dot`][fixation_dot] plugin is a simple, but functional example.

[^json]: In OpenSesame 2.8.3, plugin information was stored in `info.json`. This still works, but for newer plugins it is recommend to use `info.yaml`, because YAML-syntax is simpler than JSON-syntax. (In fact, JSON is a specific case of YAML.)

[auto_example]: https://github.com/smathot/OpenSesame/tree/master/plugins/auto_example
[fixation_dot]: https://github.com/smathot/OpenSesame/tree/master/plugins/fixation_dot
[html]: http://en.wikipedia.org/wiki/HTML#Markup
[yaml]: http://en.wikipedia.org/wiki/YAML
[yamllint.com]: http://yamllint.com/
[markdown]: http://daringfireball.net/projects/markdown/syntax
