---
layout: osdoc
title: Creating a plug-in
group: Plug-ins
permalink: /create/
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## Relevant files

Let's assume that your plug-in is called `my_plugin`. In that case, your plug-in corresponds to a folder called `my_plugin`, containing at least the following 5 files:

	my_plugin/
		info.json
		my_plugin.md
		my_plugin.png
		my_plugin_large.png
		my_plugin.py

## Icons

Your plug-in needs two icons. A small 16x16-pixel icon, which is called `my_plugin.png` and is shown in the overview area, and a larger 32x32-pixel icon, which is called `my_plugin_large.png`. These files need to be placed directly in the plug-in folder.

## Help file

You can provide a help file in [Markdown] or [HTML] format. To add a Markdown help file, simply create a file called `my_plugin.md` in the plug-in folder. For an HTML help file, create a file called `my_plugin.html`. Markdown format is generally preferred, because it is easier to read. Strictly speaking, the help file is optional, and your plug-in will work without it. However, an informative help file is an essential part of a good plug-in.

## Defining the GUI

The GUI is defined in a file called `info.json`. [JSON] is an easily readable format, and provides a quick and straight-forward way to define your plug-in controls, and specify various kinds of information. Make sure that your file is syntactically-valid JSON, for example using a validator such as [jsonlint.com].

The top-level fields, such as `author` and `url` are used to specify all kinds of information. You can add anything you like here. An important field is `category`, which specifies in which group the plug-in should appear in the item toolbar (e.g. 'Visual stimuli', etc.).

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

{% highlight javascript %}
{
	"author"	: "Your name",
	"url"		: "http://your.website",
	"category"	: "Some category",
	"comment"	: "This is my plug-in",
	"controls" : [
		{
			"type"		: "line_edit",
			"var"		: "my_var",
			"label"		: "My line edit control",
			"name"		: "line_edit_widget",
			"tooltip"	: "You can type something here"
		}
	]
}
{% endhighlight %}

See the `auto_example` [example](#examples) for a full list of all controls and options.

## Writing the main plug-in code

The main plug-in code is placed in `my_plugin.py`. This file has two classes: The first is `my_plugin`, which contains the runtime part of the plug-in. The second is `qtmy_plugin`, which controls the GUI and is almost empty in most cases, because the controls are defined in `info.json`. In many cases, you will only be concerned with three methods:

- `my_plugin.__init__()` is where you specify default values for the plug-in variables.
- `my_plugin.prepare()` is where you implement the run phase of your plug-in. It is good practice to move as much functionality as possible into `prepare()`, so that the time-critical run phase goes as smooth as possible.
- `my_plugin.run()` is where you implement the prepare phase of your plug-in.

A very simple example looks like this (see the [examples](#examples) for more realistic examples):

{% highlight python %}
# Import the required modules.
from libopensesame import debug
from libopensesame.item import item
from libqtopensesame.items.qtautoplugin import qtautoplugin

class my_plugin(item):

	description = u'Plug-in description'

	def __init__(self, name, experiment, script=None):

		# Set default values.
		self.my_var = u'some default'
		# Call the parent constructor.
		item.__init__(self, name, experiment, script)
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
		fixation_dot.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
{% endhighlight %}

## Examples

- the [`auto_example`][auto_example] plug-in is a dummy plug-in that contains a lot of information, and a detailed `info.json` that you can use as a basis for your own plug-in.
- the [`fixation_dot`][fixation_dot] plug-in is a simple, but functional example.

[auto_example]: https://github.com/smathot/OpenSesame/tree/master/plugins/auto_example
[fixation_dot]: https://github.com/smathot/OpenSesame/tree/master/plugins/fixation_dot
[html]: http://en.wikipedia.org/wiki/HTML#Markup
[json]: http://en.wikipedia.org/wiki/JSON
[jsonlint.com]: http://jsonlint.com/
[markdown]: http://daringfireball.net/projects/markdown/syntax
