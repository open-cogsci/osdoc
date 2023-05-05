---
layout: osdoc
title: Release notes for 2.9.4
group: notes
permalink: /2.9.4/
---

OpenSesame 2.9.4 is the fourth maintenance release in the 2.9 series. If you are upgrading from 2.8.3 or earlier, please also read the [2.9.0 release notes]. This release mainly addresses a critical regression that was introduced in 2.9.3.

## Changelog

### Bugs fixed

- Prevent indirect recursion errors in overview area.
- Don't crash on empty loop items.

### Windows packaging

~~~
OpenSesame 2.9.4
Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)]
OpenCV is not available
OpenCV2 2.4.10
QProgedit 2.1.0
Expyriment  (Revision ; Python 2.7.8)
NumPy 1.9.1
PIL is available (version is unknown)
PsychoPy 1.80.05-opensesame-1
PyAudio 0.2.8
PyGame 1.9.1release
PyGaze 0.5.0~opensesame3
Pyglet 1.1.4
PyOpenGL 3.1.0
PyQt 4.11.3
PySerial 2.7
python-bidi 0.3.4
python-markdown 2.5.2
SciPy 0.14.0
~~~

[2.9.0 release notes]: /notes/2.9.0/
