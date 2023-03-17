title: Creating an extension

[TOC]


## What is an OpenSesame extension?

*Extensions* add arbitrary functionality to the OpenSesame user interface. For example, an extension can add a new entry to the main toolbar or the menubar. (To add functionality that you can use in experiments, you need a [plugin](%url:plugin%).)


## Relevant files

One or more extensions are put together in an extension package, which is always a subpackage of `opensesame_extensions` (which is itself a so-called implicit namespace package, but that's a technical detail that is not very important). Let's say that your extension package is called `example`, and that it contains a single extension (there can be more) called `example_extension`. This would correspond to the following file-and-folder structure:

```
opensesame_extensions/
    example/
        __init__.py               # can be empty but must exist
        example_extension/
            __init__.py           # contains extension information
            example_extension.py  # contains extension class
```


## Extension information

Extension information is defined in the `__init__.py` of the extension module, so in our example this is `opensesesame_extensions/example/example_extension/__init__.py`.

```python
"""A docstring with a description of the extension"""

# A standard icon name
# - <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>
icon = 'applications-accessories'
# The label and the tooltip are used to create the default action, which is
# insert into the menu and/ or toolbar (or neither)
label = "Example extension"
tooltip = "Example tooltip"
menu = {
    "index": -1,
    "separator_before": True,
    "separator_after": True,
    "submenu": "Example"
}
toolbar = {
    "index": -1,
    "separator_before": True,
    "separator_after": True
}
# Settings are perstistently stored in the cfg object
settings = {
    "example_setting": "example value"
}
```

An extension can appear in the menu or main toolbar of OpenSesame. This requires that you define several fields in `__init__.py` as shown above:

- The `label` is the text that will appear in the menu.
- The `icon` is a [freedesktop-compliant icon name][icon-spec] that specifies the icon that will appear in the menu and/ or toolbar.
- The `index` gives the position of the extension in the menu/ toolbar, and works like a `list` index. That is, negative values are relative to the last entry, where -1 puts your extension at the end.

To have your extension respond to menu/ toolbar activation, implement the `activate()` method as shown below in the extension code below.


## Writing the extension code

The main extension code is placed in `[extension_name].py`. This file generally contains only a single class named `[ExtensionName].py`, that is, a class with the CamelCase equivalent of the plugin name, which inherits `libqtopensesame.extensions.BaseExtension`. So a basic (non-functional) extension class looks like this:

~~~ .python
from libopensesame.py3compat import *
from libopensesame.oslogging import oslogger
from libqtopensesame.extensions import BaseExtension


class ExampleExtension(BaseExtension):
    """An example extension that lists several common events. The class name
    should be the CamelCase version of the folder_name and file_name. So in
    this case both the extension folder (which is a Python package) and the
    .py file (which is a Python module) are called example_extension, whereas
    the class is called ExampleExtension.
    """

    def activate(self):
        oslogger.debug('example_extension extension activated')

    def event_save_experiment(self, path):
        oslogger.debug(f'Event fired: save_experiment(path={path})')

    # See example_extension source code for more event listeners
~~~


## Listening for events

OpenSesame fires events whenever something important happens. For example, the `save_experiment` event is fired when an experiment is saved. To have your extension listen to an event, simply implement a method with the name `event_[event name]` as shown above.

Note that some events take keyword arguments, such as `path` in the case of `save_experiment`. The keyword signature of your function must match the expected keyword signature. See the Event overview below for a full list of events and expected keywords.


## Building a package and uploading to pypi

Building an extensin package and uploading it to `pypi` works the same way as it does for plugins:

- %link:plugin%
- <https://github.com/open-cogsci/opensesame-extension-example>

## Examples

For a working example, see:

- <https://github.com/open-cogsci/opensesame-extension-example>

Other examples can be found in the `opensesame_extensions` folder of the OpenSesame source code:

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_extensions/core>

[example]: https://github.com/open-cogsci/OpenSesame/tree/master/extensions/example
[icon-spec]: http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html


## Event overview

This overview lists all events that are fired somewhere in the code, and that your extenstion can therefore listen to by implementing the corresponding `event_[eventname]()` functions.

%-- include: include/events.md --%
