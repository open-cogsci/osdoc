---
layout: osdoc
title: About back-ends
group: Back-ends
permalink: /about-back-ends/
level: 1
sortkey: 008.002
---

Overview
--------

- [About back-ends](#about)
- [Differences](#differences)
- [Selecting a back-end](#select)
- [Back-end specific information](#specific)

About back-ends {#about}
---------------

The OpenSesame "back-end" is the layer that deals with input (waiting for key presses, etc.) and display output at the lowest level. There are many Python libraries that offer this type of functionality and OpenSesame could, in principle, use any one of them. For this reason, OpenSesame is back-end independent, in the sense that you can choose which back-end should be used. Currently there are four different back-ends: `legacy`, `opengl`, `psycho`, `droid`, and `xpyriment`.

Differences {#differences}
-----------

Generally, you won't really notice which back-end is being used. The difference is under the hood and OpenSesame shields you from the differences between back-ends when you use the graphical user interface or if you use the `openexp` modules when writing Python inline code. So, you can easily write Python code that works for all the back-ends by using `openexp`, as described [here][inline-script]. However, there are a number of reasons for why you might prefer one back-end over another.

- Not all back-ends are supported on all platforms.
- Not all back-end are equally accurate when it comes to timing (benchmarks are available in a technical paper).
- Not all back-ends are equally fast when it comes to generating stimuli.
- Users can exploit back-end specific functionality when writing Python inline code. This is mostly useful for advanced users, or users who have prior experience with one of the back-ends.

Selecting a back-end {#select}
--------------------

The recommended (and easiest) way to select a back-end is using the pulldown menu in the "General tab" of the experiment.

If you view the general script (select "Show script editor"), you will see that there are actually 5 distinct back-ends, for the canvas, keyboard, mouse, sampler and synth. The combobox-method automatically selects an appropriate, pre-defined combination of back-ends, but you could, in theory, mix and match.

For example, if you select the `psycho` back-end, the following code will be generated:

	set mouse_backend "psycho"
	set sampler_backend "legacy"
	set keyboard_backend "psycho"
	set canvas_backend "psycho"
	set synth_backend "legacy"

Back-end specific information {#specific}
-----------------------------

- [xpyriment][] (uses Expyriment)
- [psycho][] (uses PsychoPy)
- [legacy][] (uses PyGame without OpenGL)
- [opengl][] (uses PyGame with OpenGL)
- [droid][] (uses PyGame subset for Android)

[inline-script]: /python-inline-code/about-python-inline-code
[legacy]: /back-ends/legacy
[opengl]: /back-ends/opengl
[xpyriment]: /back-ends/xpyriment
[psycho]: /back-ends/psycho
[droid]: /back-ends/droid