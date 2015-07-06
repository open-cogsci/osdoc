---
layout: osdoc
title: Important changes in 3.0
group: Miscellaneous
permalink: /important-changes-3/
---

OpenSesame 3.0.X brings many improvements that make it even easier to develop experiments. But these changes may take some getting used to. Almost all changes are backwards compatible, that is, you can still use old way. However, a handful of changes are backwards incompatible, and it's especially important to be aware of those.

%--
toc:
 mindepth: 2
--%

## Backwards incompatible changes

### Sampler properties

The `sampler` object has a number of properties that were previously functions. This concerns `sampler.fade_in`, `sampler.pan`, `sampler.pitch`, and `sampler.volume`. For more information, see:

- [/python/sampler/#backwards-incompatible-changes-from-29-to-30](/python/sampler/#backwards-incompatible-changes-from-29-to-30)

## Simplified Python API

### No more self and exp

It is no longer necessary to prefix `self.` or `exp.` when calling commonly used functions. For example, to pause for a second, you now simply run:

~~~ .python
sleep(1000)
~~~

For a list of common functions, see:

- [/python/common/](/python/common/)

### Easy getting and setting of experimental variables

The old way of using `self.get()` to get, and `exp.set()` to set experimental variables has been replaced by a far simpler syntax. For example, to set the variable `condition`, so that you can refer to it as `[condition]` in `sketchpad`s, etc.:

~~~ .python
var.condition = 'easy`'
~~~

And to get an experimental variable that was, for example, defined in a `loop`:

~~~ .python
print('Condition is %s' % var.condition)
~~~

For more information, see:

- [/python/var/](/python/var/)

### No more from openexp.* import *

It is no longer necessary to import `openexp` classes, and to pass `exp` as the first argument. Instead, to create a `canvas` object, you can simply do:

~~~ .python
my_canvas = canvas()
~~~

There are similar factory functions (as these are called) for `keyboard`, `mouse`, and `sampler`.

For more information, see:

- [/python/common/](/python/common/)

### The synth is now a sampler

The `synth` is no longer a class of its own. Instead, it's a function that returns a `sampler` object that has been filled with a synthesized sample.

## Consistent coordinates

Previously, OpenSesame used mixed, and inconsistent screen coordinates: `0,0` was the display top-left when using Python code, and the display center when working in `sketchpad` items etc. As of 3.0, the display center is always `0,0`, also in Python code. If you want to switch back to the old behavior, you can disable the 'Uniform coordinates' option in the general tab. (This will be disabled when you open an old experiment.)
