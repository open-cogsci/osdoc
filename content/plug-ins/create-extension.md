---
layout: osdoc
title: Creating an extension
group: Plug-ins and extensions
permalink: /create-extension/
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## Relevant files

Let's assume that your extension is called `my_extension`. In that case, your extension corresponds to a folder called `my_extension`, containing at least the following 2 files:

	my_extension/
		info.yaml
		my_extension.py

## Extension information

Extension information is defined in `info.yaml`. This works the same way as for plug-ins, with the exception that you don't define any controls. For more information, see:

- [/plug-ins/create-plug-in/#defining-the-gui](/plug-ins/create-plug-in/#defining-the-gui)

## Writing the extension code

The main extension code is placed in `my_extension.py`. This file has one class, `my_extension`, which inherits `libqtopensesame.extensions.base_extension.base_extension`. So a basic (non-functional) extension class looks like this:

{% highlight python %}
from libqtopensesame.extensions import base_extension

class my_extension(base_extension):

	pass
{% endhighlight %}

### Activating an extension through the menu/ toolbar

An extension can appear in the menu or main toolbar of OpenSesame. This requires that you define several fields in `info.yaml`:

{% highlight yaml %}
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
{% endhighlight %}

The `label` is the text that will appear in the menu. The `icon` is a [freedesktop-compliant icon name][icon-spec] that specifies the icon that will appear in the menu and/ or toolbar. The `index` gives the position of the extension in the menu/ toolbar, and works like a `list` index. That is, negative values are relative to the last entry, where -1 puts your extension at the end.

To have your extension respond to menu/ toolbar activation, implement the `activate()` method:

{% highlight python %}
from libopensesame import debug
from libqtopensesame.extensions import base_extension

class my_extension(base_extension):

	def activate(self):

		debug.msg(u'My extension was activated!')
{% endhighlight %}

### Listening for events

OpenSesame fires events whenever something important happens. For example, the `save_experiment` event is fired when an experiment is saved. To have your extension listen to an event, simply implement a method with the name `event_[event name]`.

{% highlight python %}
from libopensesame import debug
from libqtopensesame.extensions import base_extension

class my_extension(base_extension):

	def event_save_experiment(self, path):

		debug.msg(u'Event fired: save_experiment(path=%s)' % path)
{% endhighlight %}

Note that some events take keyword arguments, such as `path` in the case of `save_experiment`. The keyword signature of your function must match the expected keyword signature. A list of events can be found in the [example] extension.

## Examples

- The [`example`][example] extension is a dummy extension that demonstrates how to implement a basic extension.
- Other examples can be found in the `extensions` folder included with OpenSesame.

[example]: https://github.com/smathot/OpenSesame/tree/master/extensions/example
[icon-spec]: http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html
