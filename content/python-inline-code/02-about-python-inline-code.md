---
layout: osdoc
title: About Python inline code
group: Python inline code
permalink: /about-python-inline-code/
level: 1
sortkey: 005.002
---

In OpenSesame you can create fairly complex experiments using only the graphical user interface (GUI), but you will inevitably encounter situations in which the functionality provided by the GUI is insufficient. In these cases you can use the inline_script item to add Python code to your experiment.

You may also want to look at one of the example experiments using Python inline code, for realistic examples of inline_script items.

Overview
--------

- [Learning Python](#learning)
- [The inline_script item](#inline-script)
- [The exp and win variables](#exp-win)
- [The debug window](#debug)
- [openexp modules](#openexp)
- [Notes for 0.27.2 and later](#v0-27-2)
	- [Shared variables](#shared-variables)
	- [Transparent variables](#transparent-variables)
- [Notes for 0.27.1 and earlier](#v0-27-1)
	- [Carry-over effects between runs](#carry-over)
	- [Importing modules](#modules)
	- [Defining globally accessible functions](#functions)


Learning Python {#learning}
---------------

This tutorial assumes that you are familiar with Python. Python is a widely used, intuitive and powerful programming language. For scientists in particular, Python is attractive, because it is excellently suited for data analysis and creating experiments. In addition, Python is freely available and cross-platform.

A good free E-book to learn Python for non-programmers is "A Byte of Python", by Swaroop.  Make sure that you get the version for Python 2, which is what OpenSesame uses.

- ["A Byte of Python"][swaroop] by Swaroop [[Download PDF for Python 2.X]][swaroop-direct]

Another good free E-Book is "Think Python", by Allen B. Downey. This book should work for Python 2 as well as Python 3.

- ["Think Python"][downey] by Allen B. Downey [[Download PDF]][downey-direct]

Or you can follow one of the many other introductions to Python that are floating around on the web, such as:

- <http://docs.python.org/tutorial/>
- <http://code.google.com/edu/languages/google-python-class/index.html>
- <http://diveintopython.org/>

If you are interested in using OpenSesame in combination with PsychoPy, you may want to check out this tutorial on the GestaltRevision site (University of Leuven, Belgium): <http://gestaltrevision.be/wiki/coding>

The inline_script item {#inline-script}
----------------------

In order to use Python code you need to add an inline_script item to your experiment. You can do this by dragging the Python icon (the blue/yellow icon) from the item toolbar into the experiment sequence. After you have done this you will see something like the screenshot below.

![](/img/fig/fig5.2.1.png)

As you can see, the inline_script item consists of two tabs: one for the prepare phase and one for the run phase. The prepare phase is called first, to allow items to prepare for the time critical run phase. It is good practice to construct canvasses, sounds, etc. during the prepare phase, so that they can be presented without delay during the run phase. But this is only convention, you can execute arbitrary Python code during both phases.

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

This works, because `sleep()` is a function of the `inline_script` object. For a complete list of `inline_script` functions, see [here][inline-script].

Notes for 0.27.2 and later {#v0-27-2}
--------------------------

### Shared variables {#shared-variables}

Variables defined in one inline_script are accessible in all other inline_scripts. Therefore, if, for example, you want to prepare a `canvas` object in the prepare phase of an inline_script and show it in the run phase, there is no need to declare the object `global` or to store it as a property of the `exp` object. You can simply construct the `canvas` in one inline_script ...

{% highlight python %}
from openexp.canvas import canvas
my_canvas = canvas(exp)
my_canvas.fixdot()
{% endhighlight %}

... and show it in another inline_script ...

{% highlight python %}
my_canvas.show()
{% endhighlight %}

The same principle applies to functions and modules: Once you have defined a function or imported a module in one inline_script, it will be accessible in other inline_scripts as well. In other words, variables, functions, and modules are shared between inline_scripts.

### Transparent variables {#shared-variables}

Transparent variable management is experimental.
{: .page-notification}

In the general tab, you can enable the option 'Transparent variable management'. If enabled, experimental variables will be directly accessible in inline_script items. For example, if you have defined a variable called `my_var` in a loop item, you will be able to use that variable directly in an inline_script:
	
{% highlight python %}
print my_var
my_var = 'some value'
{% endhighlight %}

In contrast, if transparent variable management is disabled, you would need to use `self.get()` and `exp.set()`:
	
{% highlight python %}
print self.get('my_var')
exp.set('my_var', 'some value')
{% endhighlight %}

Notes for 0.27.1 and earlier {#v0-27-1}
----------------------------

### Carry-over effects between runs {#carry-over}

By default, OpenSesame executes the user interface and experimental runs in the same process. In some cases, this can give unexpected results. Let's consider Experiment A that consists (only) of the following script ...

{% highlight python %}
global my_var
my_var = 'Test!'
{% endhighlight %}

... and Experiment B that consists (only) of the following script ...

{% highlight python %}
print my_var
{% endhighlight %}

If you first run Experiments A and next run Experiment B (without closing OpenSesame), you will find that Experiment B prints out 'Test!'. This is a carry-over effect: `my_var` is set in Experiment A, but because it is declared `global` it will stay alive and also be accessible to Experiment B.

In general, such carry-over effects are harmless, but they are known to (on some systems) cause crashes when `canvas` objects are declared `global`. In general, it is therefore not advisable to declare `canvas` objects `global`. Instead, to share a `canvas` between inline_script items, you can store it as a property of `exp`:

{% highlight python %}
from openexp.canvas import canvas
exp.my_canvas = canvas(exp)
{% endhighlight %}

*Tip:* If you consistently encounter trouble when running your experiment for the second time (without closing OpenSesame), you can enable the *Run experiments in a separate process* option under *Preferences*. If you enable this option, OpenSesame will run your experiments as a separate program, using [opensesamerun][].

### Importing modules {#modules}

Because the code in an inline_script item is essentially the body of a function (see above), functions and modules may not work as you expect them to. For example, the following seemingly valid (although silly) piece of script ...

{% highlight python %}
from random import randint
def my_function():
	print 'A random integer: %d' % randint(0,10)
my_function()
{% endhighlight %}

... gives the following error:

{% highlight python %}
NameError: global name 'randint' is not defined
{% endhighlight %}

The reason that this doesn't work as you might expect is that `randint` is imported locally, in the function of which your code forms the body (see above). Therefore, you need to make `randint` global, so that it is also accessible from within other functions:

{% highlight python %}
from random import randint
global randint
def my_function():
	print 'A random integer: %d' % randint(0,10)
my_function()
{% endhighlight %}

This may be a bit confusing, but the take home message is: If you get a `NameError` for a module/ package/ function that you have imported, try declaring that module/ package/ function global, as illustrated above.

### Defining globally accessible functions {#functions}

Another neat trick is that you can declare functions global. Normally, you would not be able to define a function in one inline_script, and use it in another inline_script. By declaring a function global, you can circumvent this problem. So if you create the following inline_script ...

{% highlight python %}
# Inline_script 1
global my_global_function
def my_global_function():
	print 'You can call me anywhere!'
{% endhighlight %}

... you will be able to call `my_global_function()` in another inline_script:

{% highlight python %}
# Inline_script 2
my_global_function()
{% endhighlight %}

The exp and win variables {#exp-win}
-------------------------

In an inline_script (as of 0.25) there are two special variables: `exp` and `win`. Actually, there is nothing magical about these variables, they are simply synonyms for `self.experiment` and `self.experiment.window`, respectively. `exp` is the `experiment` object, which is described [here][experiment]. `win` is the window handle, which is dependent on the back-end that is used.

The debug window {#debug}
----------------

OpenSesame reroutes the standard output to the debug window, which you can activate using Control + D or through the menu (Menu -> View -> Show debug window). You can print to the debug window using the Python print statement:

{% highlight python %}
print "This will appear in the debug window!"
{% endhighlight %}

![](/img/fig/fig5.2.2.png)

By default, OpenSesame uses a simple, custom Python console in the debug window. However, you can also use [IPython][], which is a powerful interactive Python console. In order to do this, you need to run OpenSesame in a Python environment with IPython installed, and start OpenSesame with the command line argument `--ipython`.

![](/img/fig/fig5.2.3.png)

openexp modules {#openexp}
---------------

OpenSesame comes with a set of Python modules for presenting stimuli, handling input, etc. There are 5 such modules and the full API (i.e., a list of functions) is available:

- [openexp.canvas.canvas][canvas] for display presentation
- [openexp.keyboard.keyboard][keyboard] for response collection using the keyboard
- [openexp.mouse.mouse][mouse] for response collection using the mouse
- [openexp.sampler.sampler][sampler] for sound sample playback
- [openexp.synth.synth][synth] for sound synthesis and playback

It is perfectly possible to bypass the openexp modules and use the back-end directly. For more information, see [this article][back-ends].

[python]: http://www.python.org/
[inline-script]: /python-inline-code/inlinescript-functions
[experiment]: /python-inline-code/experiment-functions
[canvas]: /python-inline-code/canvas-functions
[keyboard]: /python-inline-code/keyboard-functions
[mouse]: /python-inline-code/mouse-functions
[sampler]: /python-inline-code/sampler-functions
[synth]: /python-inline-code/synth-functions
[back-ends]: /back-ends/about-back-ends
[ipython]: http://ipython.org/
[swaroop]: http://www.swaroopch.com/notes/Python
[swaroop-direct]: http://www.ibiblio.org/swaroopch/byteofpython/files/120/byteofpython_120.pdf
[downey]: http://www.greenteapress.com/thinkpython/
[downey-direct]: http://www.greenteapress.com/thinkpython/thinkpython.pdf
[opensesamerun]: /usage/opensesamerun-no-gui/