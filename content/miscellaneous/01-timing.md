---
layout: osdoc
title: Timing
group: Miscellaneous
permalink: /timing/
level: 1
sortkey: 010.002
---

A frequently asked question is whether OpenSesame is able to provide timing with millisecond accuracy. The short answer is *yes*. The long answer is that the question is more complicated than it seems. In the *Behavior Research Methods* paper we describe the results of a benchmark experiment. Please refer to [this paper][brm] for more details.

There are also some useful benchmarks available on the Expyriment wiki: <http://code.google.com/p/expyriment/wiki/Timing>. This information is not specific to OpenSesame, but should generalize to the hardware accelerated back-ends, which use the same underlying technology as Expyriment.

Scripts to test your system
---------------------------

It should be noted that it is always wise to test your own system, and not simply rely on benchmarks that others (we) have performed on other systems. There are three simple scripts to check the timing for the various back-ends. In order to download the files, follow these links, right-click on "raw" and select "save as".

- Download `xpyriment_timing_check.opensesame` from here: <https://gist.github.com/4176878>
- Download `psycho_timing_check.opensesame` from here: <https://gist.github.com/1675762>
- Download `legacy_timing_check.opensesame` from here: <https://gist.github.com/1767560>

You can open the tests scripts in OpenSesame and run them. To get the optimal results, you should run the experiments in fullscreen. Also, desktop-effect layers, such as *Aero* on Windows and *Compiz* on Linux, may adversely effect timing. If the test gives funky results, please disable the effect layer and try again.

After a brief test, these scripts will show a mean and a standard deviation. The mean should be the next value higher than 50 ms that is compatible with your display refresh rate. So, for example, if your refresh is 60Hz, the mean should be 50ms + 16.67ms = approx. 67ms. The standard deviation should be small, preferably below 1ms.

Please note that the legacy back-end may report a mean that is inconsistent with your display's refresh rate. That's fine, or at least it's normal: It will still correctly synchronize to the vertical refresh on most systems. This has to do with the fact that the legacy back-end doesn't wait for a display to be shown when returning a timestamp. For this reason, as you can also read in the paper, the legacy back-end provides slightly less accurate timestamps than the psycho and opengl back-ends.

A note regarding timing in loops and sequences
----------------------------------------------

OpenSesame uses a prepare-run strategy, which is important to be aware of when you care about timing. Specifically, a sequence is prepared in advance. This means that at the start of the sequence, all sketchpads, synths, etc. are constructed, so they can be used with minimal delay during the execution of the sequence. This preparation takes time, which can be a source of inaccurate timing.

So, therefore, if you want my_sketchpad to be presented for a fixed interval (say 60ms rounded up to the nearest possible value consistent with the display refresh), the following structure is fine, in the sense that my_sketchpad will be presented for the intended amount of time:

- sequence
	- my_sketchpad (60ms)
	- another_sketchpad (0ms)

However, the following structure will lead to unpredictable timing, in the sense that my_sketchpad may be presented for longer than intended.

- loop
	- sequence
	- my_sketchpad (60ms)

In this case, the interval between successive presentations of my_sketchpad is unpredictable and perhaps also variable. This is because successive presentations are not part of the same run of the sequence. Before the execution of the sequence, my_sketchpad (and also other items if they are part of the sequence) will be prepared and this takes an small, but unspecified amount of time. Therefore, you will get jitter in your timing.

The bottom line is: If you want timing to be perfectly controlled, make sure your items are executed as part of the same sequence! Or you can write an inline_script, of course, in which case you have full control.

[brm]: http://www.springerlink.com/content/n264513n66704v33/