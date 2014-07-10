---
layout: osdoc
title: Release notes for 2.8.3
group: notes
permalink: /2.8.3/
parser: academicmarkdown
---

OpenSesame 2.8.3 is the third maintenance release in the 2.8 series. If you are upgrading from 0.27.4 or earlier, please also read the [2.8.0 release notes].

## Credits

Thanks to Timo Lüke for contributing a German translation, and Vladimir Kosonogov for contributing a Russian translation.

## Changelog

### Improvements

- Add German translation (de_DE)
- Add Russian translation (ru_RU)
- Remember experiment and logfile folders on Android (#259)
- Add show_virtual_keyboard() function to keyboard back-ends (#254)

### Bugs fixed

- Fix canvas.arrow() docstring
- canvas.text_size() respects line breaks and formatting (#262)
- Advanced loop settings are preserved in GUI (#263)

### Windows packaging

- Update included libraries. See `modules()` output below.
- Includes a slightly patched version of PsychoPy 1.80.05 that addresses an important issue with keypress timestamps. (Unchanged from 2.8.2.)

~~~
OpenSesame 2.8.3
Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)]
OpenCV is not available
OpenCV2 2.4.9
QProgedit 1.3.4
Expyriment 0.7.0 (Revision 7a6b73d; Python 2.7.6)
NumPy 1.8.1
PIL is available (version is unknown)
PsychoPy 1.80.05-opensesame-1
PyAudio 0.2.8
PyGame 1.9.1release
Pyglet 1.1.4
PyOpenGL 3.1.0
PyQt 4.11.1
PySerial 2.7
python-bidi 0.3.4
python-markdown 2.4.1
SciPy 0.14.0
~~~

[2.8.0 release notes]: /notes/2.8.0
