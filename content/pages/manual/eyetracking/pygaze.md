title: PyGaze (eye tracking)

[TOC]

## About

PyGaze is a Python library for eye tracking. A set of plugins allow you to use PyGaze from within OpenSesame. For more information on PyGaze, visit:

- <http://www.pygaze.org/>

Please cite PyGaze as:

Dalmaijer, E., Mathôt, S., & Van der Stigchel, S. (2014). PyGaze: An open-source, cross-platform toolbox for minimal-effort programming of eyetracking experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0422-2
{: .reference}

## Supported eye trackers

PyGaze supports the following eye trackers:

- [__EyeLink__](http://www.sr-research.com/) — For information on how to run OpenSesame with PyLink support, see [this page](%link:eyelink%).
- [__EyeTribe__](http://theeyetribe.com/) — Works out of the box.

For the following eye trackers, there is experimental support:

- [__SMI__](http://www.smivision.com/) — SMI support is experimental.
- [__Tobii__](http://www.tobii.com/en/eye-tracking-research/global/) — Tobii support is experimental.

PyGaze also includes two dummy eye trackers for testing purposes:

- __Simple dummy__ — Does nothing.
- __Advanced dummy__ — Mouse simulation of eye movements.

## Installing PyGaze

### Windows

If you use the official Windows package of OpenSesame, PyGaze is already installed.

### Ubuntu

If you use Ubuntu, you can get PyGaze from the Cogsci.nl PPA:

```
sudo add-apt-repository ppa:smathot/cogscinl
sudo apt-get update
sudo apt-get install python-pygaze
```

Or, if you are using Python 3, change the last comment to:

```
sudo apt-get install python3-pygaze
```

## pip install (all platforms)

You can install PyGaze with `pip`:

```
pip install python-pygaze
```

### Anaconda (all platforms)

```
conda install python-pygaze -c cogsci
```

## PyGaze OpenSesame plugins

The following PyGaze plugins are available:

- PYGAZE_INIT — Initializes PyGaze. This plugin is generally inserted at the start of the experiment.
- PYGAZE_DRIFT_CORRECT — Implements a drift correction procedure.
- PYGAZE_START_RECORDING — Puts PyGaze in recording mode.
- PYGAZE_STOP_RECORDING — Puts PyGaze out of recording mode.
- PYGAZE_WAIT — Pauses until an event occurs, such as a saccade start.
- PYGAZE_LOG — Logs experimental variables and arbitrary text.

## Example

For an example of how to use the PyGaze plugins, see the PyGaze template that is included with OpenSesame.

Below is an example of how to use PyGaze in a Python INLINE_SCRIPT:

~~~ .python
# Create a keyboard and a canvas object
my_keyboard = Keyboard(timeout=0)
my_canvas = Canvas()
my_canvas['dot'] = Circle(x=0, y=0, r=10, fill=True)
# Loop ...
while True:
	# ... until space is pressed
	key, timestamp = my_keyboard.get_key()
	if key == 'space':
		break
	# Get gaze position from pygaze ...
	x, y = eyetracker.sample()
	# ... and draw a gaze-contingent fixation dot!
	my_canvas['dot'].x = x + my_canvas.left
	my_canvas['dot'].y = y + my_canvas.top
	my_canvas.show()
~~~

## Function overview

To initialize PyGaze in OpenSesame, insert the PYGAZE_INIT plugin into your experiment. Once you have done this, an `eyetracker` object will be available, which offers the following functions:

%-- include: include/api/eyetracker.md --%
