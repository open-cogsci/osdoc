title: Creating a plugin

[TOC]


## What is an OpenSesame plugin?

*Plugins* are extra items that appear in the OpenSesame item toolbar. Plugins add functionality that you can use in experiments. (To add functionality to the OpenSesame user interface, you need an [*extension*](%url:extension%).)



## Relevant files

One or more plugins are put together in a plugin package, which is always a subpackage of `opensesame_plugins` (which is itself a so-called implicit namespace package, but that's a technical detail that is not very important). Let's say that your plugin package is called `example`, and that it contains a single plugin (there can be more) called `example_plugin`. This would correspond to the following file-and-folder structure:

```
opensesame_plugins/
    example/
        __init__.py                  # can be empty but must exist
        example_plugin/
            __init__.py              # contains plugin information
            example_plugin.py        # contains plugin class
            example_plugin.png       # 16 x 16 icon (optional)
            example_plugin_large.png # 32 x 32 icon (optional)
            example_plugin.md        # Help file in Markdown format (optional)
```

## Icons

Each plug-in needs an icon, which you can specify in one of two ways:

- Include two icon files in the plugin folder as shown above:
    - A 16x16 px png file called `[plugin_name].png`; and
    - A 32x32 px png file called `[plugin_name]_large.png`.
- Or specify an `icon` name in the plugin information (`__init__.py`). If you do this, the plugin icon will be taken from the icon theme.


## Help file

You can provide a help file in Markdown or HTML format. To add a Markdown help file, simply create a file called `[plugin_name].md` in the plugin folder. For an HTML help file, create a file called `[plugin_name].html`. Markdown format is preferred, because it is easier to read. Strictly speaking, the help file is optional, and your plugin will work without it. However, an informative help file is an essential part of a good plugin.


## Defining the GUI

The plugin information (`__init__.py`) defines (at least) a docstring, a `category` variable, and a `controls` variable.

The `controls` variable is a list of `dict` elements that define the GUI controls. The most important fields are:

- `type` specifies the type of the control. Possible values:
	- `checkbox` is a checkable box (`QtGui.QCheckBox`)
	- `color_edit` is a color-selection widget (`libqtopensesame.widgets.color_edit.ColorEdit`)
	- `combobox` is a drop-down box with multiple options (`QtGui.QComboBox`)
	- `editor` is a multiline text editor (using PyQode)
	- `filepool` is a file-selection widget (`QtGui.QLineEdit`)
	- `line_edit` is a single-line text input (`QtGui.QLineEdit`)
	- `spinbox` is a text-based numeric-value selector (`QtGui.QSpinBox`)
	- `slider` is a sliding numeric-value selector (`QtGui.QSlider`)
	- `text` is a non-interactive text string (`QtGui.QLabel`)
- `var` specifies the name of the variable that should be set using the control (not applicable if `type` is `text`).
- `label` specifies the text label for the control.
- `name` (optional) specifies under which name the widget should be added to the plugin object, so that it can be referred to as `self.[name]`.
- `tooltip` (optional) an informative tooltip.


```python
"""A docstring with a description of the plugin"""

# The category determines the group for the plugin in the item toolbar
category = "Visual stimuli"
# Defines the GUI controls
controls = [
    {
        "type": "checkbox",
        "var": "checkbox",
        "label": "Example checkbox",
        "name": "checkbox_widget",
        "tooltip": "An example checkbox"
    }, {
        "type": "color_edit",
        "var": "color",
        "label": "Color",
        "name": "color_widget",
        "tooltip": "An example color edit"
    }
]
```

See the [example](#examples) plugin for a list of all controls and options.


## Writing the plugin code

The main plugin code is placed in `[plugin_name].py`. This file generally contains only a single class named `[PluginName].py`, that is, a class with the CamelCase equivalent of the plugin name, which inherits from `libopensesame.item.Item`. A basic plugin class looks like this:


```python
from libopensesame.py3compat import *
from libopensesame.item import Item
from libqtopensesame.items.qtautoplugin import QtAutoPlugin
from openexp.canvas import Canvas


class ExamplePlugin(Item):
    """An example plugin that shows a simple canvas. The class name
    should be the CamelCase version of the folder_name and file_name. So in
    this case both the plugin folder (which is a Python package) and the
    .py file (which is a Python module) are called example_plugin, whereas
    the class is called ExamplePlugin.
    """
    def reset(self):
        """Resets plug-in to initial values."""
        # Here we provide default values for the variables that are specified
        # in __init__.py. If you do not provide default values, the plug-in
        # will work, but the variables will be undefined when they are not
        # explicitly # set in the GUI.
        self.var.checkbox = 'yes'  # yes = checked, no = unchecked
        self.var.color = 'white'
        self.var.option = 'Option 1'
        self.var.file = ''
        self.var.text = 'Default text'
        self.var.spinbox_value = 1
        self.var.slider_value = 1
        self.var.script = 'print(10)'

    def prepare(self):
        """The preparation phase of the plug-in goes here."""
        # Call the parent constructor.
        super().prepare()
        # Here simply prepare a canvas with a fixatio dot.
        self.c = Canvas(self.experiment)
        self.c.fixdot()

    def run(self):
        """The run phase of the plug-in goes here."""
        # self.set_item_onset() sets the time_[item name] variable. Optionally,
        # you can pass a timestamp, such as returned by canvas.show().
        self.set_item_onset(self.c.show())
```


If you want to implement custom GUI controls for your plugin, you also need to implement a `Qt[PluginName]` class in the same file. This is illustrated in the [example](#examples) plugin. If you don't implement this class, a default GUI will be created based on the controls as defined in `__init__.py`.


## Experimental variables

Experimental variables are properties of the `var` object. An example is `self.var.my_line_edit_var` from the example above. These variables that define the plugin, and are parsed to and from the OpenSesame script. See also:

- %link:manual/variables%


## Building a package and uploading to pypi

The easiest way to build a package for your plugin is by defined a `pyproject.toml` file and using `poetry` to build the package and upload it to `pypi`.

- <https://python-poetry.org/>

An example `pyproject.toml` file looks as follows:

```toml
[tool.poetry]
name = "opensesame-plugin-example"
version = "0.0.1"
description = "An example plugin for OpenSesame"
authors = ["Sebastiaan Mathôt <s.mathot@cogsci.nl>"]
readme = "readme.md"
packages = [
    {include = "opensesame_plugins"},
]

[tool.poetry.dependencies]
python = ">= 3.7"
opensesame-core = ">= 4.0.0a0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Once you have add this file to the root folder of your plugin code, you can build a `.whl` package by running:

```bash
poetry build
```

Once you have succesfully built a package, create an account on <https://pypi.org/>, create an API token for your account, and authenticate `poetry` like this:

```bash
poetry config pypi-token.pypi [api_token]
```

Once this is done, you can publish your package to PyPi by running the following command:

```bash
poetry publish
```


Your users will now be able to pip-install your plugin!

```bash
pip install opensesame-plugin-example
```


## Examples

For a working example, see:

- <https://github.com/open-cogsci/opensesame-plugin-example>

Other examples can be found in the `opensesame_plugins` folder of the OpenSesame source code:

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_plugins/core>
