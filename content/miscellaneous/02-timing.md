---
layout: osdoc
title: Timing
group: Miscellaneous
permalink: /timing/
level: 1
sortkey: 010.002
---

Overview
--------

- [Benchmarks](#benchmarks)
- [Expyriment test suite](#test-suite)
- [Other scripts to test your system](#other-scripts)
- [Timing in loops and sequences](#loops-sequences)

Benchmarks {#benchmarks}
----------

A frequently asked question is whether OpenSesame is able to provide timing with millisecond accuracy. The short answer is *yes*. The long answer is that the question is more complicated than it seems. In the *Behavior Research Methods* paper we describe the results of a benchmark experiment. Please refer to [this paper][brm] for more details.

There are also some useful benchmarks available on the Expyriment wiki: <http://code.google.com/p/expyriment/wiki/Timing>. This information is not specific to OpenSesame, but should generalize to the hardware accelerated back-ends, which use the same underlying technology as Expyriment.

Expyriment test suite {#test-suite}
---------------------

Expyriment includes a very useful test suite. You can launch this test suite by running the `test_suite.opensesame` example experiment, or by adding a simple inline_script to your experiment with the following lines of code:
	
{% highlight python %}
import expyriment
expyriment.control.run_test_suite()
{% endhighlight %}

For more information, please visit:
	
- <http://docs.expyriment.org/Tools.html#expyriment-test-suite>

Other scripts to test your system {#other-scripts}
---------------------------------

It should be noted that it is always wise to test your own system, and not simply rely on benchmarks that others (we) have performed on other systems. There are three simple scripts to check the timing for the various back-ends. In order to download the files, follow these links, right-click on "raw" and select "save as".

- Download `xpyriment_timing_check.opensesame` from here: <https://gist.github.com/4176878>
- Download `psycho_timing_check.opensesame` from here: <https://gist.github.com/1675762>
- Download `legacy_timing_check.opensesame` from here: <https://gist.github.com/1767560>

You can open the tests scripts in OpenSesame and run them. To get the optimal results, you should run the experiments in fullscreen. Also, desktop-effect layers, such as *Aero* on Windows and *Compiz* on Linux, may adversely affect timing. If the test gives funky results, please disable the effect layer and try again.

After a brief test, these scripts will show a mean and a standard deviation. The mean should be the next value higher than 50 ms that is compatible with your display refresh rate. So, for example, if your refresh is 60Hz, the mean should be 50ms + 16.67ms = approx. 67ms. The standard deviation should be small, preferably below 1ms.

Please note that the legacy back-end may report a mean that is inconsistent with your display's refresh rate. That's fine, or at least it's normal: It will still correctly synchronize to the vertical refresh on most systems. This has to do with the fact that the legacy back-end doesn't wait for a display to be shown when returning a timestamp. For this reason, as you can also read in the paper, the legacy back-end provides slightly less accurate timestamps than the psycho and opengl back-ends.

Timing in loops and sequences {#loops-sequences}
-----------------------------

OpenSesame uses a prepare-run strategy, which is important to be aware of when you implement time-critical parts of your experiment using the GUI. See [this page][prepare-run] for more information.

[prepare-run]: /usage/prepare-run/#loop
[brm]: http://www.springerlink.com/content/n264513n66704v33/