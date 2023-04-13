title: About Python

In OpenSesame you can create complex experiments using only the graphical user interface (GUI). But you will sometimes encounter situations in which the functionality provided by the GUI is insufficient. In these cases you can add Python code to your experiment.

Python is not supported in online experiments with OSWeb. If you need to run your experiment online, you have to use [JavaScript](%url:manual/javascript/about%) instead.

[TOC]

## Learning Python

You can find a set of basic tutorials and exercises to get you started with Python at <https://pythontutorials.eu/>.


## Python in the OpenSesame GUI

### A single Python workspace

All Python code is executed in a single Python workspace. This means that variables that have been defined in one INLINE_SCRIPT are accessible in all other INLINE_SCRIPTs, as well as in Python statements that are embedded in run-if statements and text strings. The same principle applies to modules: once `import`ed, they are available everywhere.

For example, you can simply construct the `Canvas` in one INLINE_SCRIPT ...

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
~~~

... and show it in another INLINE_SCRIPT ...

~~~ .python
my_canvas.show()
~~~

### Inline_script items

In order to use Python code you need to add an INLINE_SCRIPT item to your experiment. You can do this by dragging the Python icon (the blue/yellow icon) from the item toolbar into the experiment sequence. After you have done this you will see something like %FigInlineScript.

%--
figure:
 id: FigInlineScript
 source: inline-script.png
 caption: The INLINE_SCRIPT item.
--%

As you can see, the INLINE_SCRIPT item consists of two tabs: one for the Prepare phase and one for the Run phase. The Prepare phase is executed first, to allow items to prepare for the time-critical run phase. It is good practice to construct `Canvas` objects, `Sampler` objects, etc. during the Prepare phase, so that they can be presented without delay during the Run phase. But this is only convention; you can execute arbitrary Python code during both phases.

For more information about the prepare-run strategy, see:

- %link:prepare-run%


### Conditional ("if") expressions

You can use single-line Python expressions in conditional expressions. For example, you can use the following Python script as a run-if expression (see also %FigRunIf):

~~~ .python
correct == 1 and response_time < 1000
~~~

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: Using Python script in the run-if statement of a SEQUENCE item.
--%

For more information about conditional ("if") expressions, see:

- %link:manual/variables%


### Python in text strings

You can embed Python statements in text strings using the `{...} syntax. This works for simple variable references, but also for single-line expressions. For example, you could the following text to a SKETCHPAD:

```text
The resolution is {width} x {height} px, which is a total of {width * height} pixels
```

Depending on your experiment's resolution, this might evaluate to:

```text
The resolution is 1024 x 768 px, which is a total of 786432 pixels
```

For more information about variables and text, see:

- %link:manual/variables%
- %link:manual/stimuli/text%


### The Jupyter console (debug window)

OpenSesame reroutes the standard output to the console (or: debug window), which you can activate using Control + D or through the menu (Menu -> View -> Show debug window; see %FigDebugNormal). You can print to the console using `print()`.

~~~ .python
print('This will appear in the debug window!')
~~~

The console is also an interactive Python interpreter powered by [project Jupyter](https://jupyter.org).


## Things to know

### Common functions

Many common functions are directly available in an INLINE_SCRIPT item, without the need to import anything. For example:

~~~ .python
# `Canvas()` is a factory function that returns a `Canvas` object
fixdot_canvas = Canvas()
if sometimes(): # Sometimes the fixdot is green
    fixdot_canvas.fixdot(color='green')
else: # Sometimes it is red
    fixdot_canvas.fixdot(color='red')
fixdot_canvas.show()
~~~

For a list of common functions, see:

- %link:manual/python/common%


### The `var` object: Access to experimental variables

__Version note__ As of OpenSesame 4.0, all experimental variables are available as globals. This means that you no longer need the `var` object.
{:.page-notification}

You can access experimental variables through the `var` object:

~~~ .python
# Get an experimental variable
print('my_variable is: %s' % var.my_variable)
# Set an experimental variable
var.my_variable = 'my_value'
~~~

A full overview of the `var` object can be found here:

- %link:manual/python/var%


### The `clock` object: Time functions

Basic time functions are available through the `clock` object:

~~~ .python
# Get the current timestamp
t = clock.time()
# Wait for 1 s
clock.sleep(1000)
~~~

A full overview of the `clock` object can be found here:

- %link:manual/python/clock%


### The `log` object: Data logging

Data logging is available through the `log` object:

~~~ .python
# Write one line of text
log.write('My custom log message')
# Write all variables
log.write_vars()
~~~

A full overview of the `log` object can be found here:

- %link:manual/python/log%


### The `pool` object: Access to the file pool

You get the full path to a file in the file pool through the `pool` object:

~~~ .python
# Show an image from the file pool
path = pool['img.png']
my_canvas = Canvas()
my_canvas.image(path)
my_canvas.show()
~~~

A full overview of the `pool` object can be found here:

- %link:manual/python/pool%


### The `responses` object: Access to participant responses

The `responses` object keeps track of all participant responses that have been collected during the experiment. For example, to list the correctness of all responses so far:

~~~ .python
for response in responses:
	print(response.correct)
~~~

A full overview of the `responses` object can be found here:

- %link:manual/python/responses%


### The `Canvas` class: Presenting visual stimuli

The `Canvas` class is used to present visual stimuli. For example, you can show a fixation dot as follows:

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

A full overview of the `Canvas` class can be found here:

- %link:manual/python/canvas%


### The `Keyboard` class: Collecting key presses

The `Keyboard` class is used to collect key presses. For example, to collect a key press with a timeout of 1000 ms:

~~~ .python
my_keyboard = Keyboard(timeout=1000)
key, time = my_keyboard.get_key()
~~~

A full overview of the `Keyboard` class can be found here:

- %link:manual/python/keyboard%


### The `Mouse` class: Collecting mouse clicks and screen touches

The `Mouse` class is used to collect mouse clicks and screen touches. (OpenSesame makes no distinction between the two.) For example, to collect a mouse click with a timeout of 1000 ms:

~~~ .python
my_mouse = Mouse(timeout=1000)
button, position, time = my_mouse.get_click()
~~~

A full overview of the `Mouse` class can be found here:

- %link:manual/python/mouse%


### The `Sampler` class: Sound playback

The `Sampler` class is used to play back sound samples. For example, to play back a simple beep:

~~~ .python
my_sampler = Sampler()
my_sampler.play()
~~~

A full overview of the `Sampler` class can be found here:

- %link:manual/python/sampler%


## Alternative modules for display presentation, response collection, etc.


### `psychopy`

If you are using the *psycho* backend, you can directly use the various [PsychoPy] modules. For more information, see:

- %link:backends%


### `expyriment`

If you are using the *xpyriment* backend, you can directly use the various [Expyriment] modules. For more information, see:

- %link:backends%

### `pygame`

If you are using the *legacy*, *droid*, or *xpyriment* (only with "Use OpenGL" set to "no") backend, you can directly use the various [PyGame] modules. For more information, see:

- %link:backends%


[python]: http://www.python.org/
[backends]: /backends/about-backends
[ipython]: http://ipython.org/
[swaroop]: http://www.swaroopch.com/notes/Python
[swaroop-direct]: http://www.ibiblio.org/swaroopch/byteofpython/files/120/byteofpython_120.pdf
[downey]: http://www.greenteapress.com/thinkpython/
[downey-direct]: http://www.greenteapress.com/thinkpython/thinkpython.pdf
[opensesamerun]: /usage/opensesamerun/
[psychopy]: http://www.psychopy.org/
[expyriment]: http://www.expyriment.org/
[pygame]: http://www.pygame.org/
