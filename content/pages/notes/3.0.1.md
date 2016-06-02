---
layout: osdoc
title: Release notes for 3.0.1
group: notes
permalink: /3.0.1/
---

OpenSesame 3.0.1 is the first maintenance release in the 3.0 series. If you are upgrading from OpenSesame 2.9.7 or earlier, please see the list of important changes in OpenSesame 3.0:

- [Important changes in 3.0](/miscellaneous/important-changes-3/)

## Credits

Thanks to Jarik den Hartog ([@JdenHartog](https://github.com/JdenHartog)) for his code contributions.

## Changes

### Improvements

- Give more informative error messages when using invalid variable names
- Update auto_example plugin
- Ignore 'undefined name' warnings when validating Python code (requires QProgEdit >= 3.1.0)
- Update srbox plugin and add require_state_change_option
- Add explanation how to suppress bug_report messages

### Bugs fixed

- Fix crash on fallback_console reset
- Catch syntax warnings in inline_script items
- Fix deleting items from pool

### Windows packaging

~~~
OpenSesame 3.0.1
Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
OpenCV is not available
OpenCV2 3.0.0
QProgedit 3.1.0
Expyriment  (Python 2.7.10)
IPython 3.2.0
NumPy 1.9.2
PIL is available (version is unknown)
PsychoPy 1.82.01
PyAudio 0.2.8
PyGame 1.9.1release
PyGaze 0.6.0a3
Pyglet 1.2.3
PyOpenGL 3.1.0
PyQt 4.11.4
PySerial 2.7
python-bidi 0.3.4
python-markdown 2.6.2
SciPy 0.15.1
~~~
