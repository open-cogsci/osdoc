---
layout: osdoc
title: About Python inline code
group: Python inline code
permalink: /about/
---

In OpenSesame you can create complex experiments using only the graphical user interface (GUI), but you will inevitably encounter situations in which the functionality provided by the GUI is insufficient. In these cases you can use the `inline_script` item to add Python code to your experiment.

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## Learning Python

### Code Academy

The Python track at Code Academy is an excellent way to get started with Python:

- <http://www.codecademy.com/tracks/python>

### A Byte of Python

A good free E-book to learn Python for non-programmers is "A Byte of Python", by Swaroop. Make sure to get the version for Python 2, which is what OpenSesame uses.

- ["A Byte of Python"][swaroop] by Swaroop [[Download PDF for Python 2.X]][swaroop-direct]

### Think Python

Another good free E-Book is "Think Python", by Allen B. Downey. This book should work for Python 2 as well as Python 3.

- ["Think Python"][downey] by Allen B. Downey [[Download PDF]][downey-direct]

## Python in the OpenSesame GUI

### The `inline_script` item

In order to use Python code you need to add an `inline_script` item to your experiment. You can do this by dragging the Python icon (the blue/yellow icon) from the item toolbar into the experiment sequence. After you have done this you will see something like %FigInlineScript.

%--
figure:
 id: FigInlineScript
 source: inline-script.png
 caption: The `inline_script` item.
--%

As you can see, the `inline_script` item consists of two tabs: one for the prepare phase and one for the run phase. The prepare phase is executed first, to allow items to prepare for the time critical run phase. It is good practice to construct `canvas` objects, `sampler` objects, etc. during the prepare phase, so that they can be presented without delay during the run phase. But this is only convention, you can execute arbitrary Python code during both phases. For more information about the prepare-run strategy, see:

- [/usage/prepare-run/](/usage/prepare-run/)

The scripts that you enter are used as the body of two functions of the inline_script class:

{% highlight python %}
class inline_script:
   def prepare(self):
      # Your prepare script goes here
   def run(self):
      # Your run script goes here
{% endhighlight %}

This is important to know, because it explains why you can use commands such as:

{% highlight python %}
self.sleep(1000)
{% endhighlight %}

This works, because `sleep()` is a function of the `inline_script` object. For a full list of available functions, see:

- [/python/inline-script/](/python/inline-script/)

### Loop tables and conditional ("if") statements

You can use single-line Python statements also where you would normally type static values or use the OpenSesame square-brackets notation to indicate values (i.e. `[my_var]`). To do so, you need to add an `=` prefix. For example, you can use the following Python script as a run-if statement (see also %FigRunIf):

{% highlight python %}
=self.get('correct') == 1 and self.get('response_time') < 1000
{% endhighlight %}

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: Using Python script in the run-if statement of a `sequence` item.
--%

For more information about conditional ("if") statements, see:

- [/usage/variables-and-conditional-statements/#using-conditional-if-statements](/usage/variables-and-conditional-statements/#using-conditional-if-statements)

Similarly, you can use single-line Python statements to define variables in `loop` tables. For example, if you want the variable `duration` to have a random value between 0 and 1000, you can use the following statement (all functions from the `math` and `random` modules are available; see also %FigLoopTable):

{% highlight python %}
=randint(0, 1000)
{% endhighlight %}

%--
figure:
 id: FigLoopTable
 source: loop-table.png
 caption: Using Python script to define variables in a `loop` table.
--%

### The debug window

OpenSesame reroutes the standard output to the debug window, which you can activate using Control + D or through the menu (Menu -> View -> Show debug window; see %FigDebugNormal). You can print to the debug window using the Python print statement:

{% highlight python %}
print "This will appear in the debug window!"
{% endhighlight %}

%--
figure:
 id: FigDebugNormal
 source: debug-window.png
 caption: The debug window.
--%

## Things to know

### The `exp` and `win` variables

There are two special variables in an `inline_script`: `exp` and `win`. Actually, there is nothing too special about these variables. They are simply synonyms for `self.experiment` and `self.experiment.window`, respectively. `exp` is the `experiment` object, which is described [here][experiment], and you will use it often to access variables and functions. `win` is the window handle, which is dependent on the back-end that is used, and you will generally use only in special cases.

### Getting and setting experimental variables

For information about getting and setting experimental variables in an `inline_script`, see here:

- [/usage/variables-and-conditional-statements/#getting-and-setting-variables-in-inline_script-items](/usage/variables-and-conditional-statements/#getting-and-setting-variables-in-inline_script-items)

### Sharing variables and modules between `inline_script`s

Variables defined in one `inline_scrip`t are accessible in all other `inline_script`s. Therefore, if, for example, you want to prepare a `canvas` object in the prepare phase of an `inline_script` and show it in the run phase, there is no need to declare the object `global` or to store it as a property of the `exp` object. You can simply construct the `canvas` in one `inline_script` ...

{% highlight python %}
from openexp.canvas import canvas
my_canvas = canvas(exp)
my_canvas.fixdot()
{% endhighlight %}

... and show it in another `inline_script` ...

{% highlight python %}
my_canvas.show()
{% endhighlight %}

The same principle applies to functions and modules: Once you have defined a function or imported a module in one `inline_script`, it will be accessible in other `inline_scripts` as well. In other words, variables, functions, and modules are shared between `inline_script`s.

## Modules for display presentation, response collection, etc.

### `openexp` (Native OpenSesame modules)

OpenSesame comes with a set of Python modules for presenting stimuli, handling input, etc. These modules work with all back-ends. The full API (i.e., a list of functions) can be found here:

- [/python/canvas](/python/canvas) for display presentation
- [/python/keyboard](/python/keyboard) for response collection using the keyboard
- [/python/mouse](/python/mouse) for response collection using the mouse
- [/python/sampler](/python/sampler) for sound sample playback
- [/python/synth](/python/synth) for sound synthesis and playback

### `psychopy`

If you are using the *psycho* back-end, you can directly use the various [PsychoPy] modules. For more information, see:

- [/back-ends/psycho](/back-ends/psycho)

### `expyriment`

If you are using the *xpyriment* back-end, you can directly use the various [Expyriment] modules. For more information, see:

- [/back-ends/xpyriment](/back-ends/xpyriment)

### `pygame`

If you are using the *legacy*, *droid*, or *xpyriment* (only with "Use OpenGL" set to "no") back-end, you can directly use the various [PyGame] modules. For more information, see:

- [/back-ends/legacy/](/back-ends/legacy)

[python]: http://www.python.org/
[inline-script]: /python/inline-script
[experiment]: /python/experiment
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
