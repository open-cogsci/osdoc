title: Creating an extension

[TOC]


## What is an OpenSesame extension?

*Extensions* add arbitrary functionality to the OpenSesame user interface. For example, an extension can add a new entry to the main toolbar or the menubar. To add functionality that you can use in experiments, you need a *plugin*:

- %link:plugin%


## Relevant files

Let's assume that your extension is called `my_extension`. In that case, your extension corresponds to a folder called `my_extension`, which contains at least the following 2 files:

	MyExtension/
		info.yaml
		MyExtension.py


## Extension information

Extension information is defined in `info.yaml`. This works the same way as for plugins, with the exception that you don't define any controls. For more information, see:

- %link:plugin%


## Writing the extension code

The main extension code is placed in `MyExtension.py`. This file has one class, `MyExtension` (the same name as the file), which inherits `libqtopensesame.extensions.BaseExtension`. So a basic (non-functional) extension class looks like this:

~~~ .python
from libqtopensesame.extensions import BaseExtension


class MyExtension(BaseExtension):

	pass
~~~


### Activating an extension through the menu/ toolbar

An extension can appear in the menu or main toolbar of OpenSesame. This requires that you define several fields in `info.yaml`:

~~~ .yaml
label: Example extension
icon: go-next
tooltip: Some tooltip
menu:
  index: 0
  separator_after: false
  separator_before: false
  submenu: Example
toolbar:
  index: -1
  separator_after: false
  separator_before: true
~~~

The `label` is the text that will appear in the menu. The `icon` is a [freedesktop-compliant icon name][icon-spec] that specifies the icon that will appear in the menu and/ or toolbar. The `index` gives the position of the extension in the menu/ toolbar, and works like a `list` index. That is, negative values are relative to the last entry, where -1 puts your extension at the end.

To have your extension respond to menu/ toolbar activation, implement the `activate()` method:

~~~ .python
from libopensesame.oslogging import oslogger
from libqtopensesame.extensions import BaseExtension


class MyExtension(BaseExtension):

	def activate(self):

		oslogger.info('My extension was activated!')
~~~


### Listening for events

OpenSesame fires events whenever something important happens. For example, the `save_experiment` event is fired when an experiment is saved. To have your extension listen to an event, simply implement a method with the name `event_[event name]`.

~~~ .python
from libopensesame.oslogging import oslogger
from libqtopensesame.extensions import BaseExtension


class MyExtension(BaseExtension):

	def event_save_experiment(self, path):

		oslogger.info(f'Event fired: save_experiment(path={path})')
~~~

Note that some events take keyword arguments, such as `path` in the case of `save_experiment`. The keyword signature of your function must match the expected keyword signature. A list of events can be found in the [example extension](https://github.com/smathot/opensesame-extension-example/blob/master/opensesame_extensions/example_extension/example_extension.py).


## Writing a setup.py and uploading to PyPi

See:

- %link:plugin%
- <https://github.com/smathot/opensesame-extension-example>

## Examples

For a working example, see:

- <https://github.com/smathot/opensesame-extension-example>

- Other examples can be found in the `opensesame_extensions` folder included with OpenSesame.

[example]: https://github.com/smathot/OpenSesame/tree/master/extensions/example
[icon-spec]: http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html


## Event overview

This overview lists all events that are fired somewhere in the code, and that your extenstion can therefore listen to by implementing the corresponding `event_[eventname]()` functions.

%-- include: include/events.md --%
