---
layout: osdoc
title: Coroutines (running items simultaneously)
group: Usage
permalink: /coroutines/
---

Currently, coroutines are under active development, and are only available through an experimental plug-in. The goal is to integrate coroutines into the main OpenSesame code for 3.1. Until then, functionality may change in a backwards-incompatible way.
{: .page-notification}

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## What are coroutines?

Coroutines allow multiple items to run simultaneously--or, to be more exact, they allow items to run in rapid alternation in a way that looks like simultaneous execution. Only some items are supported (see [Supported items]).

## Installing the coroutines plug-in

You can download the `coroutines` plug-in from:

- <https://github.com/smathot/opensesame_coroutines/releases>

... and install it as described here:

- [/plugins/installation](/plugins/installation)

## Using coroutines

You can use coroutines through the `coroutines` plug-in (see %FigCoroutinesInterface).

%--
figure:
 source: FigCoroutinesInterface.png
 caption: The interface of the coroutines plug-in.
 id: FigCoroutinesInterface
--%

As you can see, the `coroutines` plug-in looks similar to the `sequence` item, but has a few extra options:

- *Duration* indicates the total duration of the coroutines.
- *Generator function name (optional)* indicates the name of a generator function that has been defined in an inline_script (see [Writing a custom coroutine][]).
- Each item has a *Start time*. Most items also have an *End time*. The end time does not apply to one-shot items; for example, `sketchpad`s show a display and terminate immediately, so they have no end time.

Specifically, the example from %FigCoroutinesInterface (from the [stop-signal-task example](https://github.com/smathot/opensesame_coroutines/tree/master/examples)) does the following:

- It shows a target display immediately.
- If the `stop_after` variable is not empty, it shows the stop_signal display after an interval specified by the `stop_after` variable.
- During the entire (2000 ms) interval, a keyboard response is collected.

The temporal flow is controlled by the `coroutines` plug-in. Therefore, the timeout and duration values specified in the items are not used. For example, in %FigCoroutinesInterface, the `keyboard_response` will run for 2000 ms, regardless of the timeout that is specified in the item.

## Supported items

Currently, the following items are supported:

- `keyboard_response`
- `mouse_response`
- `sketchpad`
- `inline_script` (see [Writing a custom coroutine][])

## Writing a custom coroutine

Technically, coroutines are [generators](https://en.wikipedia.org/wiki/Generator_(computer_programming)). Generators are functions that can suspend their execution (i.e., they `yield`) and resume later on; therefore, multiple generators can run in a rapidly alternating suspend-resume cycle. This trick is sometimes called *weightless threading*, because it has most of benefits of real threading, without any of the overhead or (potential) instability. Coroutines *do not* use threading or multiprocessing.

In the coroutines plug-in, you can indicate the name of a generator function that you have defined in an `inline_script`. This generator needs to work in a particular way (as illustrated in the examples below):

- It must initialize and then `yield`. This first `yield` returns nothing.
- It may loop while `yield`ing on every iteration. The loop breaks when:
  - The coroutine should end; or
  - When the `yield` returns `False`; this is the `coroutine` plug-in's way to signal the end of the coroutine.
- No time-consuming things should happen between `yield` statements, except during initialization.

The first and simplest option is to write a one-shot coroutine. This is a function that is called once to prepare itself, once to execute, and then terminates. For example:

~~~ .python
def my_oneshot_coroutine():

	"""
	This is an example of a one-shot generator coroutine.
	"""

	# All initialization stuff goes here
	print('Initialize!')
	# Now yield to signal the end of the preparation
	yield
	# Do something here and terminate
	print('Stopped!')
~~~

A more complicated example is a coroutine that prepares itself, is then called repeatedly (and keeps track of how often), and then terminates:

~~~ .python
def my_coroutine():

	"""
	This is an example of a generator coroutine that keeps track of
	how many cycles it goes through.
	"""

	# All initialization stuff goes here
	i = 0
	# Now yield to signal the end of the preparation
	yield

	# Enter an infinite loop
	while True:
		# Do some important stuff here. This should not be
		# too time consuming; otherwise you will block the
		# other items of the coroutines.
		i += 1
		# Yield to give other items an opportunity to execute,
		# and receive a boolean that indicates whether we
		# should keep going
		keep_going = yield
		if not keep_going:
			break

	# We are done!
	print('Stopped after %d cycles!' % i)
~~~
