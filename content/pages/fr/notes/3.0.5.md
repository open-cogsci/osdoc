---
layout: osdoc
title: Release notes for 3.0.5
group: notes
permalink: /3.0.5/
---

OpenSesame 3.0.5 is the fifth maintenance release in the 3.0 series. It contains bug fixes and minor improvements, and should be a pleasant and safe upgrade for everyone who is using the 3.0 series.

One notable feature of this release is the experimental Python-3.4-based package. Python 2.7 will remain the default for now (and probably for a while), because several key libraries that OpenSesame uses are not yet compatible with Python 3 (notably PsychoPy and Expyriment).

If you are upgrading from OpenSesame 2.9.7 or earlier, please see the list of important changes in OpenSesame 3.0:

- [Important changes in 3.0](/miscellaneous/important-changes-3/)

### Bugs fixed

- Fix catching of unexpected errors in multiprocess runner (#382)
- Don't crash when entering numeric break-if statement in loop
- Register 'self' when executing conditional statements (for backwards compatibility)
- Fix missing py3compat import in joystick
- Fix keyboard timestamps for older versions of PsychoPy (#381)
- Show .osexp files while browsing with opensesamerun GUI (#385)
- Fix rectangular envelope in noise patches
- Fix too-many-files-open error with gabor and noise elements in sketchpad
- Remove Python-3-incompatible relative imports from plugin_manager

### Improvements

- Add unit test for required py3compat import and encoding declaration
- Show version info in opensesamerun GUI
- Improve Python 3 compatibility

### Windows packaging

Python 2.7 release (recommended):

~~~
OpenSesame 3.0.5
Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
OpenCV is not available
OpenCV2 3.0.0
QProgedit 3.2.2
Expyriment  (Python 2.7.10)
IPython 3.2.0
NumPy 1.9.2
PIL is available (version is unknown)
PsychoPy 1.82.01
PyAudio 0.2.8
PyGame 1.9.1release
PyGaze 0.6.0a8
Pyglet 1.2.3
PyOpenGL 3.1.0
PyQt 4.11.4
PySerial 2.7
python-bidi 0.3.4
python-markdown 2.6.2
SciPy 0.15.1
~~~

Python 3.4 release (experimental):

~~~
OpenSesame 3.0.5
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
OpenCV is not available
OpenCV 2 is not available
QProgedit 3.2.2
Expyriment is not available (or version is unknown)
IPython 4.0.0
NumPy 1.9.3
PIL is available (version is unknown)
PsychoPy not available (or version is unknown)
PyAudio 0.2.9
PyGame 1.9.2a0
PyGaze is not available
Pyglet not available (or version is unknown)
PyOpenGL 3.1.1b1
PyQt 4.11.4
PySerial 2.7
python-bidi 0.4.0
python-markdown 2.6.2
SciPy 0.16.1
~~~
