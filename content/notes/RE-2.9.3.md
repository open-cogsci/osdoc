---
layout: osdoc
title: Release notes for 2.9.3
group: notes
permalink: /2.9.3/
---

OpenSesame 2.9.3 is the fourth maintenance release in the 2.9 series. If you are upgrading from 2.8.3 or earlier, please also read the [2.9.0 release notes].

## Changelog

### Bugs fixed

- Font size was specified in points instead of pixels in GUI
- Legacy back-end crashed when specifying system font in general properties
- Show arrow-size field in sketchpad
- Fix a bug where description changes weren't applied

### Improvements

- Allow descriptions to wrap over multiple lines for better screen use
- Massively improved performance for large experiments (#305)

### Windows packaging

~~~
OpenSesame 2.9.2
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
