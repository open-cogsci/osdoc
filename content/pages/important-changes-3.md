title: Important changes in OpenSesame 3

[TOC]


## Changes in 3.2

OpenSesame 3.2 brings several major improvements that make it even easier to develop experiments. OpenSesame 3.2 is fully backwards compatible with 3.1.


### A better, PEP-8-compliant Python API

PEP-8 is a style guide for Python. Much modern Python software follows the PEP-8 guidelines—but, for historical reasons, OpenSesame didn't. As of 3.2, the public API now follows the guideline that the names of classes (and factory functions that generate classes) should be `CamelCase`, while names of objects and functions should be `underscore_case`. Practically speaking, this means that you now create `Canvas` object as follows:

~~~ .python
my_canvas = Canvas() # Note the capital C!
my_canvas.fixdot()
my_canvas.show())
~~~

Of course, the old `underscore_case` names are still available as aliases, so backwards compatibility is preserved.

The API for forms has also been simplified. You no longer need to import `libopensesame.widgets`, and you no longer need to pass `exp` as the first argument:

~~~ .python
form = Form()
button = Button(text=u'Ok!')
form.set_widget(button, (0, 0))
form._exec()
~~~


### Improvements to the sketchpad and Canvas

#### Access and modify Canvas elements

Elements of a `Canvas` are now objects that can be named, accessed, and modified. This means that you no longer need to redraw an entire canvas to change a single element. For example, you can draw a rotating arm as follows:

~~~ .python
my_canvas = Canvas()
my_canvas['arm'] = Line(0, 0, 0, 0)
for x, y in xy_circle(n=100, rho=100):
	my_canvas['arm'].ex = x
	my_canvas['arm'].ey = y
	my_canvas.show()
	clock.sleep(10)
~~~

The SKETCHPAD also allows you to name elements.

For more information, see:

- %link:canvas%


#### Improved support for HTML and non-Latin script

Text is now rendered by Qt, which is a modern library (the same library that is also used for the graphical interface). This means that you can now use real HTML in your text. This also means that left-to-right script and other non-Latin scripts are rendered much better.


#### Images can be rotated

Images can now be rotated. This work both in SKETCHPAD items and `Canvas` objects.


#### Work with polar coordinates

If you right-click on a SKETCHPAD elements, you can select 'Specify polar coordinates'. This allows you to calculate cartesian (x, y) coordinates based on polar coordinates, which is especially useful if you want to create circular configurations.


### Form improvements

#### Improved form performance

Forms are now much faster when using the *psycho* and *xpyriment* backends. This is due to the fact that `Canvas` elements can now be updated individually, as described above.


#### Validation of form input

You can now validate the input of a form; that is, you can prevent a form from closing until certain criteria are met. In addition, you can exclude characters as input from `TextInput` widgets.

For more information, see:

- %link:manual/forms/validation%


### Keyboard Improvements

#### Support for key-release events

The `Keyboard()` object now has a `get_key_release()` function, which allows you to collect key releases. Due to limitations of the underlying libraries, the function has two important limitations:

- The returned `key` may be incorrect on non-QWERTY keyboard layouts
- The function has not been implemented for the *psycho* backend

For more information, see:

- %link:manual/response/keyboard%


### Mouse Improvements

#### Support for mouse-release events

The `Mouse()` object now has a `get_click_release()` function, which allows you to collect mouse-click releases. This function is currently not implemented for the *psycho* backend.

For more information, see:

- %link:manual/response/mouse%

#### Use sketchpads to define regions of interest

You can now define a linked SKETCHPAD in a `mouse_response` item. If you do this, the names of the elements on the SKETCHPAD will be automatically used as regions of interest (ROIs) for the mouse clicks.


## Changes in 3.1

OpenSesame 3.1 brings many improvements that make it even easier to develop experiments. OpenSesame 3.1 is fully backwards compatible with 3.0.

### A new look!

OpenSesame has a new icon theme, based on [Moka](https://snwh.org/moka) by Sam Hewitt. In addition, the user interface has been redesigned based on consistent human-interface guidelines. We hope you like the new look as much as we do!

### A redesigned loop

The LOOP is now easier to use, and allows you to constrain randomization; this makes it possible, for example, to prevent the same stimulus from occurring twice in a row.

For more information, see:

- %link:loop%

### Coroutines: doing things in parallel

The COROUTINES plugin is now included by default. COROUTINES allows you to run multiple other items in parallel; this makes it possible, for example, to continuously collect key presses while presenting a series of SKETCHPADs.

For more information, see:

- %link:coroutines%

### Open Science Framework integration

You can now log into the [Open Science Framework](http://osf.io) (OSF) from within OpenSesame, and effortlessly synchronize experiments and data between your computer and the OSF. Thanks to the [Center for Open Science](http://cos.io/) for supporting this functionality!

For more information, see:

- %link:osf%

### A responses object

There is a new standard Python object: `responses`. This keeps track of all responses that have been collected during the experiment.

For more information, see:

- %link:responses%

## Changes in 3.0

OpenSesame 3.0 has brought many improvements that make it even easier to develop experiments. Most changes are backwards compatible. That is, you can still do things the old way. However, a handful of changes are backwards incompatible, and it's important to be aware of those.

### Backwards incompatible changes

#### Sampler properties

The SAMPLER object has a number of properties that were previously functions. This concerns:

- `sampler.fade_in`
- `sampler.pan`
- `sampler.pitch`
- `sampler.volume`

For more information, see:

- %link:sampler%

#### CSS3-compatible colors

You can now use CSS3-compatible color specifications, as described here:

- %link:canvas%

If you use color names (e.g. 'red', 'green', etc.), this may result in slightly different colors. For example, according to CSS3, 'green' is `#008000` instead (as was the case previously) of `#00FF00`.

### New file format (.osexp)

OpenSesame now saves experiments in `.osexp` format. Of course, you can still open the old formats (`.opensesame` and `.opensesame.tar.gz`). For more information, see:

- %link:fileformat%

### Simplified Python API

#### No more self and exp

It is no longer necessary to prefix `self.` or `exp.` when calling commonly used functions. For example, this will programmatically set the subject number to 2:

~~~ .python
set_subject_nr(2)
~~~

For a list of common functions, see:

- %link:common%

#### The `var` object: Easy getting and setting of experimental variables

The old way of using `self.get()` to get, and `exp.set()` to set experimental variables has been replaced by a simpler syntax. For example, to set the variable `condition`, so that you can refer to it as `[condition]` in SKETCHPADs, etc.:

~~~ .python
var.condition = 'easy`'
~~~

And to get an experimental variable `condition` that was, for example, defined in a LOOP:

~~~ .python
print('Condition is %s' % var.condition)
~~~

For more information, see:

- %link:var%

#### The `clock` object: Time functions

Time functions are now available through the `clock` object:

~~~ .python
print('Current timestamp: %s' % clock.time())
clock.sleep(1000) # Sleep for 1 s
~~~

For more information, see:

- %link:clock%

#### The `pool` object: Accessing the file pool

The file pool is now accessible through the `pool` object, which supports a `dict`-like interface (but is not really a Python `dict`):

~~~ .python
path = pool['image.png']
print('The full path to image.png is: %s' % path)
~~~

For more information, see:

- %link:pool%

#### No more from openexp.* import *

It is no longer necessary to import `openexp` classes, and to pass `exp` as the first argument. Instead, to create a `canvas` object, you can simply do:

~~~ .python
my_canvas = canvas()
~~~

There are similar factory functions (as these are called) for `keyboard`, `mouse`, and SAMPLER.

For more information, see:

- %link:common%

#### The synth is now a sampler

The SYNTH is no longer a class of its own. Instead, it's a function that returns a SAMPLER object that has been filled with a synthesized sample.

### User-interface improvements

#### An IPython debug window

IPython, an interactive Python terminal for scientific computing, is now used for the debug window.

#### A live variable inspector

The variable inspector now shows the actual values of your variables while your experiment is running, and after your experiment has finished.

#### Undo

You can finally undo actions!

#### A new color scheme

The default color scheme is now *Monokai*. Again a dark color scheme, but with a higher contrast than the previous default, *Solarized*. This increased should increase legibility. And it looks good!

### Consistent coordinates

Previously, OpenSesame used mixed, inconsistent screen coordinates: `0,0` was the display top-left when using Python code, and the display center when working in SKETCHPAD items etc. As of 3.0, the display center is always `0,0`, also in Python code.

If you want to switch back to the old behavior, you can disable the 'Uniform coordinates' option in the general tab. For backwards compatibility, 'Uniform coordinates' are automatically disabled when you open an old experiment.

### Using Python in text strings

You can now embed Python in text strings using the `[=...]` syntax. For example, the following text string in a SKETCHPAD:

~~~
Two times two equals [=2*2]
~~~

... will show:

~~~
Two times two equals 4
~~~

For more information, see:

- %link:text%

### Support for Python 3

OpenSesame now supports Python >= 3.4. However, many of OpenSesame's dependencies, notably PsychoPy and Expyriment, are Python 2-only. Therefore, Python 2.7 remains the default version of Python.
