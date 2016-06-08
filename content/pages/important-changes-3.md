title: Important changes in 3.0

OpenSesame 3.0 has brought many improvements that make it even easier to develop experiments. Most changes are backwards compatible. That is, you can still do things the old way. However, a handful of changes are backwards incompatible, and it's important to be aware of those.

[TOC]

## Backwards incompatible changes

### Sampler properties

The SAMPLER object has a number of properties that were previously functions. This concerns:

- `sampler.fade_in`
- `sampler.pan`
- `sampler.pitch`
- `sampler.volume`

For more information, see:

- %link:sampler%

### CSS3-compatible colors

You can now use CSS3-compatible color specifications, as described here:

- %link:canvas%

If you use color names (e.g. 'red', 'green', etc.), this may result in slightly different colors. For example, according to CSS3, 'green' is `#008000` instead (as was the case previously) of `#00FF00`.

## New file format (.osexp)

OpenSesame now saves experiments in `.osexp` format. Of course, you can still open the old formats (`.opensesame` and `.opensesame.tar.gz`). For more information, see:

- %link:fileformat%

## Simplified Python API

### No more self and exp

It is no longer necessary to prefix `self.` or `exp.` when calling commonly used functions. For example, this will programmatically set the subject number to 2:

~~~ .python
set_subject_nr(2)
~~~

For a list of common functions, see:

- %link:common%

### The `var` object: Easy getting and setting of experimental variables

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

### The `clock` object: Time functions

Time functions are now available through the `clock` object:

~~~ .python
print('Current timestamp: %s' % clock.time())
clock.sleep(1000) # Sleep for 1 s
~~~

For more information, see:

- %link:clock%

### The `pool` object: Accessing the file pool

The file pool is now accessible through the `pool` object, which supports a `dict`-like interface (but is not really a Python `dict`):

~~~ .python
path = pool['image.png']
print('The full path to image.png is: %s' % path)
~~~

For more information, see:

- %link:pool%

### No more from openexp.* import *

It is no longer necessary to import `openexp` classes, and to pass `exp` as the first argument. Instead, to create a `canvas` object, you can simply do:

~~~ .python
my_canvas = canvas()
~~~

There are similar factory functions (as these are called) for `keyboard`, `mouse`, and SAMPLER.

For more information, see:

- %link:common%

### The synth is now a sampler

The SYNTH is no longer a class of its own. Instead, it's a function that returns a SAMPLER object that has been filled with a synthesized sample.

## User-interface improvements

### An IPython debug window

IPython, an interactive Python terminal for scientific computing, is now used for the debug window.

### A live variable inspector

The variable inspector now shows the actual values of your variables while your experiment is running, and after your experiment has finished.

### Undo

You can finally undo actions!

### A new color scheme

The default color scheme is now *Monokai*. Again a dark color scheme, but with a higher contrast than the previous default, *Solarized*. This increased should increase legibility. And it looks good!

## Consistent coordinates

Previously, OpenSesame used mixed, inconsistent screen coordinates: `0,0` was the display top-left when using Python code, and the display center when working in SKETCHPAD items etc. As of 3.0, the display center is always `0,0`, also in Python code.

If you want to switch back to the old behavior, you can disable the 'Uniform coordinates' option in the general tab. For backwards compatibility, 'Uniform coordinates' are automatically disabled when you open an old experiment.

## Using Python in text strings

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

## Support for Python 3

OpenSesame now supports Python >= 3.4. However, many of OpenSesame's dependencies, notably PsychoPy and Expyriment, are Python 2-only. Therefore, Python 2.7 remains the default version of Python.
