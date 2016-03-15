---
layout: osdoc
title: Release notes for 3.0.7
group: notes
permalink: /3.0.7/
---

OpenSesame 3.0.7 is the seventh maintenance release in the 3.0 series. It contains bug fixes and minor improvements, and should be a pleasant and safe upgrade for everyone who is using the 3.0 series.

If you are upgrading from OpenSesame 2.9.7 or earlier, please see the list of important changes in OpenSesame 3.0:

- [Important changes in 3.0](/miscellaneous/important-changes-3/)

### Bugs fixed

- Fix 'sound' duration in sampler and sketchpad (#401)
- Correctly escape slashes in OpenSesame syntax (#403)
- Don't crash on viewing remote urls ending in .md

### Improvements

- Preserve cursor position when switching to and from inline_script items (#390)
- Give better error message when missing end-of-block line for multiline variables

### Windows packaging

Python 2.7 release (recommended):

~~~
OpenSesame 3.0.7
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
PyGaze 0.6.0a9
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
OpenSesame 3.0.7
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
PyGaze 0.6.0a9
Pyglet 1.2.3
PyOpenGL 3.1.0
PyQt 4.11.4
PySerial 2.7
python-bidi 0.3.4
python-markdown 2.6.2
SciPy 0.15.1
~~~

### Mac OS packaging

~~~
TODO
~~~~
