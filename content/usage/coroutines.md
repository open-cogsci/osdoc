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

Coroutines allow multiple items to run simultaneously--or, to be more exact, they allow items to run in rapid alternation in a way that, to the user, looks like simultaneous execution.

The coroutines interface looks as follows:

%--
figure:
 source: FigCoroutinesInterface.png
 caption: The interface of the coroutines plug-in.
 id: FigCoroutinesInterface
--%

As you can see, the `coroutines` plug-in looks similar to the `sequence` item, but has a few extra options:

- *Duration* indicates the total duration of the coroutines.
- *Generator function name (optional)* indicates the name of a generator function that has been defined in an inline_script. (See [Writing a coroutine generator function][])
- Each item has a *Start time* and an *End time*. The end time does not apply to one-shot items; for example, `sketchpad`s show a display and terminate immediately, so the end time is not applicable.

Specifically, this example (from the [stop-signal-task example](https://github.com/smathot/opensesame_coroutines/tree/master/examples)) does the following:

- It shows a target display immediately
- If the `stop_after` variable is not empty, it shows the stop_signal display after an interval specified by the `stop_after` variable.
- During the entire (2000 ms) interval, a keyboard response is collected.

## Installing the coroutines plug-in

You can download the `coroutines` plug-in from:

- <https://github.com/smathot/opensesame_coroutines/releases>

... and install it as described here:

- [/plugins/installation](/plugins/installation)

## Supported items

Currently, the following items are supported:

- `keyboard_response`
- `sketchpad`
- `inline_script` (see [Writing a coroutine generator function][])

## Technical: How do coroutines work?

Technically, coroutines are [generators](https://en.wikipedia.org/wiki/Generator_(computer_programming)). Generators are functions that can suspend their execution (i.e., they `yield`) and resume later on; therefore, multiple generators can run in a rapidly alternating suspend-resume cycle. This trick is sometimes called *weightless threading*, because it has most of benefits or real threading, without any of the overhead or (potential) instability.

Coroutines do *not* use threading or multiprocessing.

## Writing a coroutine generator function

In the coroutines plug-in, you can indicate the name of a generator function that you have defined in an `inline_script`. This generator needs to work in a particular way that is illustrated in the example below:

~~~ .python
def my_coroutine():

	"""
	This is an example generator coroutines that keeps track of
	how many cycles it goes through.
	"""

	# All initialization stuff goes here
	i = 0
	yield # Now yield to signal the end of the preparation

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
