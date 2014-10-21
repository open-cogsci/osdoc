---
layout: osdoc
title: PyGaze (eye tracking)
group: Devices
permalink: /pygaze/
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## About

PyGaze is a Python library for eye tracking. A set of plug-ins allow you to use PyGaze from within OpenSesame. As of OpenSesame 2.9.0, these plug-ins are included by default in the OpenSesame Windows packages.

For more information on PyGaze, visit:

- <http://www.pygaze.org/>

## Supported eye trackers

Currently, PyGaze supports the following eye trackers:

- [__EyeLink__](http://www.sr-research.com/) -- For information on how to run OpenSesame with PyLink support, see [/devices/eyelink](/devices/eyelink).
- [__EyeTribe__](http://theeyetribe.com/) -- Works out of the box.
- [__SMI__](http://www.smivision.com/) -- SMI support is experimental.
- [__Tobii__](http://www.tobii.com/en/eye-tracking-research/global/) -- Tobii support is experimental.

PyGaze also includes two dummy eye trackers for testing purposes:

- __Simple dummy__ -- Does nothing.
- __Advanced dummy__ -- Mouse simulation of eye movements.

## PyGaze OpenSesame plug-ins

The following PyGaze plug-ins are available:

- `pygaze_init` -- Initializes PyGaze. This plug-in is generally inserted at the start of the experiment.
- `pygaze_drift_correct` -- Implements a drift correction procedure.
- `pygaze_start_recording` -- Puts PyGaze in recording mode.
- `pygaze_stop_recording` -- Puts PyGaze out of recording mode.
- `pygaze_wait` -- Pauses until an event occurs, such a saccade start.
- `pygaze_log` -- Logs experimental variables and arbitrary text.

## Example

For an example of how to use the PyGaze plug-ins, see the PyGaze template that is included with OpenSesame.

Below is an example of how to use PyGaze in a Python `inline_script`. For a list of available functions, see [Function overview].

{% highlight python %}
from openexp.canvas import canvas
from openexp.keyboard import keyboard
# Create a keyboard and a canvas object
my_keyboard = keyboard(exp, timeout=0)
my_canvas = canvas(exp)
# Loop ...
while True:
	# ... until space is pressed
	key, timestamp = my_keyboard.get_key()
	if key == 'space':
		break
	# Get gaze position from pygaze ...
	x, y = exp.pygaze_eyetracker.sample()
	# ... and draw a gaze-contingent fixation dot!
	my_canvas.clear()
	my_canvas.fixdot(x, y)
	my_canvas.show()
{% endhighlight %}

## Function overview

To initialize PyGaze in OpenSesame, insert the `pygaze_init` plug-in into your experiment. Once you have done this, an `exp.pygaze_eyetracker` object will be available, which offers the following functions:

{% include doc/pygaze %}
