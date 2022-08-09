title: Doing things in parallel


Coroutines run multiple items in parallel—or, to be more exact, they run items in rapid alternation in a way that looks parallel. Not all items support coroutines.


[TOC]


## Using coroutines

You can use coroutines through the COROUTINES plugin (see %FigCoroutinesInterface).


%--
figure:
 source: FigCoroutinesInterface.png
 caption: The interface of the coroutines plugin.
 id: FigCoroutinesInterface
--%


As you can see, the COROUTINES plugin looks similar to the SEQUENCE item, but has a few extra options:

- *Duration* indicates the total duration of the coroutines.
- *End after item (optional)* indicates that the coroutines should end when a specific item has ended. This allows you, for example, to indicate that the coroutines should end when a key press has been collected, by selecting a KEYBOARD_RESPONSE item here.
- *Generator function name (optional)* indicates the name of a generator function that has been defined in an inline_script (see Writing a custom coroutine below).
- Each item has a *Start time*. Most items also have an *End time*. The end time does not apply to one-shot items; for example, SKETCHPADs show a display and terminate immediately, so they have no end time.

Specifically, the example from %FigCoroutinesInterface (from the stop-signal-task example) does the following:

- It shows a target display immediately.
- If the `stop_after` variable is not empty, it shows the stop_signal display after an interval specified by the `stop_after` variable.
- During the entire (2000 ms) interval, a keyboard response is collected.

The temporal flow is controlled by the COROUTINES plugin. Therefore, the timeout and duration values specified in the items are not used. For example, in %FigCoroutinesInterface, the KEYBOARD_RESPONSE will run for 2000 ms, regardless of the timeout that is specified in the item.


## Supported items

Currently, the following items are supported:

- FEEDBACK
- INLINE_SCRIPT
- KEYBOARD_RESPONSE
- LOGGER
- MOUSE_RESPONSE
- SAMPLER
- SYNTH
- SKETCHPAD


## Using inline_script items in coroutines

When you use an INLINE_SCRIPT item in a COROUTINES, the Run phase works a little differently from what you might be used to. Specifically, the Run phase is executed on every iteration of the COROUTINES. In addition, the Run phase should only contain code that takes very little time to execute; this is because time-consuming operations will block the COROUTINES, thus interfering with the timing of other items in the COROUTINES as well. To end the COROUTINES, you can raise an `AbortCoroutines()` exception.

For example, say that you have a COROUTINES with two KEYBOARD_RESPONSE items, *kb1* and *kb2*, and you want to run the COROUTINES until two key presses have been collected, with a timeout of 5000 ms. You could then create the following COROUTINES structure:


%--
figure:
 source: FigCoroutinesTwoResponses.png
 caption: A coroutines that collects two keypress responses
 id: FigCoroutinesTwoResponses
--%

The *check_responses* INLINE_SCRIPT would then first set both responses variables to an empty string in the Prepare phase:

```python
# This is executed at the start of the coroutines
var.response_kb1 = ''
var.response_kb2 = ''
```

And then, in the Run phase, check if both variables have been set, and abort the coroutines if this is the case:

```python
# Values that are not an empty string are True for Python
# This code will be executed many times!
if var.response_kb1 and var.response_kb2:
    raise AbortCoroutines()
```


## Using a custom generator function in coroutines

Technically, coroutines are [generators](https://en.wikipedia.org/wiki/Generator_(computer_programming)). Generators are functions that can suspend their execution (i.e., they `yield`) and resume later on; therefore, multiple generators can run in a rapidly alternating suspend-resume cycle. This trick is sometimes called *weightless threading*, because it has most of benefits of real threading, without any of the overhead or (potential) instability. Coroutines do not use threading or multiprocessing.

In the COROUTINES plugin, you can indicate the name of a generator function that you have defined in an INLINE_SCRIPT. This generator needs to work in a particular way (as illustrated in the examples below):

- It must initialize and then `yield`. This first `yield` returns nothing.
- It may loop while `yield`ing on every iteration. The loop breaks when:
    - The coroutine should end; or
    - When the `yield` returns `False`; this is a signal from the COROUTINES plugin to the generator to signal that the coroutines ends.
    - When the generator `yields False` itself; this is a signal from the generator to the COROUTINES to signal that the coroutines ends.
    - Alternatively, the generator can `raise AbortCoroutines()` to signal that the coroutines ends.
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

Another example, which stops the coroutines when a response has been collected.

~~~ .python
def my_coroutine():

	"""
	This is an example of a generator coroutine that aborts the coroutines when
	a response has been collected.
	"""

	# To start, set response to None
	var.response = None
	yield
	# Loop while coroutines is running
	while True:
		# If response is None (i.e. no response has been collected), signal
		# True to the coroutines to indicate that, from this end, the coroutines
		# should keep going.
		signal_to_coroutines = var.response is None
		# Send the signal to the coroutines, and get a return signal. If the
		# return signal is False, we should break the loop.
		signal_from_coroutines = yield signal_to_coroutines
		if not signal_from_coroutines:
			break
~~~


## Run-if statements

The behavior of run-if statements in COROUTINES is a bit different from that in SEQUENCE items. Specifically, run-if statements in COROUTINES are evaluated during the prepare phase. See also:

- %link:prepare-run%
