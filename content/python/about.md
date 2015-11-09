---
layout: osdoc
title: About Python
group: Python inline code
permalink: /about/
---

In OpenSesame you can create complex experiments using only the graphical user interface (GUI). But you will sometimes encounter situations in which the functionality provided by the GUI is insufficient. In these cases you can add Python code to your experiment.

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## Learning Python

- __Code Academy__ -- The Python track at Code Academy is an excellent way to get started with Python:
    - <http://www.codecademy.com/tracks/python>
- __A Byte of Python__ -- A good free E-book to learn Python for non-programmers is "A Byte of Python", by Swaroop. Make sure to get the version for Python 2, which is what OpenSesame uses.
    - ["A Byte of Python"][swaroop] by Swaroop [[Download PDF for Python 2.X]][swaroop-direct]
- __Think Python__ -- Another good free E-Book is "Think Python", by Allen B. Downey. This book should work for Python 2 as well as Python 3.
    - ["Think Python"][downey] by Allen B. Downey [[Download PDF]][downey-direct]

## Python in the OpenSesame GUI

### Screencast

%--
video:
 source: youtube
 id: VidTutorial30
 videoid: sEjQlYCmY_w
 width: 640
 height: 360
 caption: |
  A screencast that the demonstrates the basics of using Python inline script in OpenSesame.
--%

### A single Python workspace

All Python code is executed in a single Python workspace. This means that variables that have been defined in one `inline_script` are accessible in all other `inline_script`s, as well as in Python statements that are embedded in run-if statements and text strings. The same principle applies to modules: once `import`ed, they are available everywhere.

For example, you can simply construct the `canvas` in one `inline_script` ...

~~~ .python
my_canvas = canvas()
my_canvas.fixdot()
~~~

... and show it in another `inline_script` ...

~~~ .python
my_canvas.show()
~~~

### Inline_script items

In order to use Python code you need to add an `inline_script` item to your experiment. You can do this by dragging the Python icon (the blue/yellow icon) from the item toolbar into the experiment sequence. After you have done this you will see something like %FigInlineScript.

%--
figure:
 id: FigInlineScript
 source: inline-script.png
 caption: The `inline_script` item.
--%

As you can see, the `inline_script` item consists of two tabs: one for the prepare phase and one for the run phase. The prepare phase is executed first, to allow items to prepare for the time critical run phase. It is good practice to construct `canvas` objects, `sampler` objects, etc. during the prepare phase, so that they can be presented without delay during the run phase. But this is only convention; you can execute arbitrary Python code during both phases.

For more information about the prepare-run strategy, see:

- [/usage/prepare-run/](/usage/prepare-run/)

### Loop tables and conditional ("if") statements

You can use single-line Python statements also where you would normally type static values, or would use the OpenSesame square-brackets notation to indicate values (i.e. `[my_var]`). To do so, you need to add an `=` prefix. For example, you can use the following Python script as a run-if statement (see also %FigRunIf):

~~~ .python
=var.correct == 1 and var.response_time < 1000
~~~

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: Using Python script in the run-if statement of a `sequence` item.
--%

For more information about conditional ("if") statements, see:

- [/usage/variables-and-conditional-statements/#using-conditional-if-statements](/usage/variables-and-conditional-statements/#using-conditional-if-statements)

Similarly, you can use single-line Python statements to define variables in `loop` tables. Let's say that you want to assign a random value between 0 and 1000 to a variable. You could this by first `import`ing the `random` in an `inline_script`. Once the `random` module is available, you could use `random.randint()` to obtain a random variable in a `loop` item:

~~~ .python
=random.randint(0, 1000)
~~~

%--
figure:
 id: FigLoopTable
 source: loop-table.png
 caption: Using Python script to define variables in a `loop` table.
--%

### Python in text strings

You can embed Python statements in text strings using the `[=...]` syntax. For example, you could the following text to a `sketchpad`:

    The resolution is [=var.width] x [=var.height] px

Depending on your experiment's resolution, this might evaluate to:

    The resolution is 1024 x 768 px

### The IPython debug window

OpenSesame reroutes the standard output to the debug window, which you can activate using Control + D or through the menu (Menu -> View -> Show debug window; see %FigDebugNormal). You can print to the debug window using the Python `print()` statement:

~~~ .python
print('This will appear in the debug window!')
~~~

If available, the debug window is an [IPython] terminal. IPython is a powerful interactive Python terminal. If IPython is not available, a simple fallback terminal will be used.

%--
figure:
 id: FigDebugNormal
 source: debug-window.png
 caption: The debug window.
--%

## Things to know

### Common functions

Many common functions are directly available in an `inline_script` item, without the need to import anything. For example:

~~~ .python
# `canvas()` is a common function that returns a `canvas` object
fixdot_canvas = canvas()
if sometimes(): # Sometimes the fixdot is green
    fixdot_canvas.fixdot(color='green')
else: # Sometimes it is red
    fixdot_canvas.fixdot(color='red')
fixdot_canvas.show()
~~~

For a list of common functions, see:

- [/python/common/](/python/common/)

### The `var` object: Access to experimental variables

You can access experimental variables through the `var` object:

~~~ .python
# Get an experimental variable
print(u'my_variable is: %s' % var.my_variable)
# Set an experimental variable
var.my_variable = u'my_value'
~~~

A full overview of the `var` object can be found here:

- [/python/var/](/python/var/)

### The `clock` object: Time functions

Basic time functions are available through the `clock` object:

~~~ .python
# Get the current timestamp
t = clock.time()
# Wait for 1 s
clock.sleep(1000)
~~~

A full overview of the `clock` object can be found here:

- [/python/clock/](/python/clock/)

### The `log` object: Data logging

Data logging is available through the `log` object:

~~~ .python
# Write one line of text
log.write(u'My custom log message')
# Write all variables
log.write_vars()
~~~

A full overview of the `log` object can be found here:

- [/python/log/](/python/log/)

### The `pool` object: Access to the file pool

You get the full path to a file in the file pool through the `pool` object:

~~~ .python
# Show an image from the file pool
path = pool['img.png']
my_canvas = canvas()
my_canvas.image(path)
my_canvas.show()
~~~

A full overview of the `pool` object can be found here:

- [/python/pool/](/python/pool/)

### The `win` object: The window handle

The `win` object is the window handle, and depends on the back-end. You will generally use the `win` object only in special cases, such as when creating PsychoPy stimuli..

## Modules for display presentation, response collection, etc.

### `openexp` (Native OpenSesame modules)

OpenSesame comes with a set of Python modules for presenting stimuli, handling input, etc. These modules work with all back-ends. The full API (i.e., a list of functions) can be found here:

- [/python/canvas](/python/canvas/) for display presentation
- [/python/keyboard](/python/keyboard/) for response collection using the keyboard
- [/python/mouse](/python/mouse/) for response collection using the mouse
- [/python/sampler](/python/sampler/) for sound playback

### `psychopy`

If you are using the *psycho* back-end, you can directly use the various [PsychoPy] modules. For more information, see:

- [/back-ends/psycho]()

### `expyriment`

If you are using the *xpyriment* back-end, you can directly use the various [Expyriment] modules. For more information, see:

- [/back-ends/xpyriment](/back-ends/xpyriment)

### `pygame`

If you are using the *legacy*, *droid*, or *xpyriment* (only with "Use OpenGL" set to "no") back-end, you can directly use the various [PyGame] modules. For more information, see:

- [/back-ends/legacy/](/back-ends/legacy)

[python]: http://www.python.org/
[canvas]: /python/canvas
[keyboard]: /python/keyboard
[mouse]: /python/mouse
[sampler]: /python/sampler
[synth]: /python/synth
[back-ends]: /back-ends/about-back-ends
[ipython]: http://ipython.org/
[swaroop]: http://www.swaroopch.com/notes/Python
[swaroop-direct]: http://www.ibiblio.org/swaroopch/byteofpython/files/120/byteofpython_120.pdf
[downey]: http://www.greenteapress.com/thinkpython/
[downey-direct]: http://www.greenteapress.com/thinkpython/thinkpython.pdf
[opensesamerun]: /usage/opensesamerun/
[psychopy]: http://www.psychopy.org/
[expyriment]: http://www.expyriment.org/
[pygame]: http://www.pygame.org/
