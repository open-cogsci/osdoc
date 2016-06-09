---
layout: osdoc
title: About back-ends
group: Back-ends
permalink: /about/
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## About back-ends

The *back-end* is the software layer that deals with input (keyboard input, mouse input, etc.) and output (display presentation, sound playback, etc.). There are many Python libraries that offer this type of functionality and OpenSesame could, in principle, use any one of them. For this reason, OpenSesame is back-end independent, in the sense that you can choose which back-end should be used. Currently there are five different back-ends: `legacy`, `psycho`, `droid`, `xpyriment`, and `opengl` (deprecated).

## Differences and some tips

Usually, you won't notice which back-end is used. The differences between back-ends are largely technical, and, as long as you use the graphical user interface or the `openexp` Python modules, all back-ends work the same way. However, there are a number of reasons to prefer one back-end over another in a particular situation.

- Not all back-end are equally accurate when it comes to [timing].
	- Tip: If you care about millisecond precision timing, use `xpyriment` or `psycho`.
- Not all back-ends are equally fast when it comes to generating stimuli.
	- Tip: If [forms] are slow, use `legacy`.
	- Tip: If the intertrial interval is long (due to stimulus preparation), use `legacy`.
- You can make use of back-end specific functionality when writing Python inline code.
	- Tip: If you want to use PsychoPy functionality, use `psycho`.
	- Tip: If you want to use Expyriment functionality, use `xpyriment`.
	- Tip: If you want to use PyGame functionality, use `legacy`.
- Not all back-ends are supported on all platforms.

## Selecting a back-end

The easiest way to select a back-end is using the combobox in the "General tab" of the experiment (%FigSelect).

%--
figure:
 id: FigSelect
 source: fig-select.png
 caption: "The back-end selection combobox."
--%

If you view the general script (select "Show script editor"), you will see that there are actually five distinct back-ends, for the canvas, keyboard, mouse, sampler and synth. The combobox-method automatically selects an appropriate, pre-defined combination of back-ends, but you could, in theory, mix and match.

For example, if you select the `psycho` back-end, the following code will be generated:

	set mouse_backend "psycho"
	set sampler_backend "legacy"
	set keyboard_backend "psycho"
	set canvas_backend "psycho"
	set synth_backend "legacy"

## Back-end specific information

- [xpyriment][] (uses Expyriment)
- [psycho][] (uses PsychoPy)
- [legacy][] (uses PyGame without OpenGL)
- [droid][] (uses PyGame subset for Android)

[inline-script]: /python/about
[legacy]: /back-ends/legacy
[xpyriment]: /back-ends/xpyriment
[psycho]: /back-ends/psycho
[droid]: /back-ends/droid
[timing]: /miscellaneous/timing
[forms]: /forms/about
