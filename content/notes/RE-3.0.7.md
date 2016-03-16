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
- Fix crashing help menu when off-line (#395)

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
PyGaze 0.6.0a10
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

### Mac OS packaging

~~~
OpenSesame 3.0.7
Python 2.7.11 |Continuum Analytics, Inc.| (default, Dec 6 2015, 18:57:58)
[GCC 4.2.1 (Apple Inc. build 5577)]
OpenCV is not available
OpenCV2 3.1.0
QProgedit 3.2.2
Expyriment 0.8.0-41-g147b7d7 (Python 2.7.11)
IPython 4.1.2
NumPy 1.10.4
PIL is available (version is unknown)
PsychoPy 1.82.01
PyAudio 0.2.7
PyGame 1.9.2a0
PyGaze is not available
Pyglet 1.2.4
PyOpenGL 3.1.1a1
PyQt 4.11.4
PySerial 3.0.1
python-bidi 0.4.0
python-markdown 2.6.5
SciPy 0.17.0
~~~~
