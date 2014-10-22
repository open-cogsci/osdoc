---
layout: osdoc
title: Release notes for 2.9.0
group: notes
permalink: /2.9.0/
parser: academicmarkdown
---

OpenSesame 2.9.0 is the first release in the 2.9 series. It offers major usability improvements over the 2.8 series. If you are upgrading from 2.8.3 or earlier, please also read the [2.8.3 release notes].

## Credits

Thanks to [Nicky Anderson](https://github.com/nccanderson) for her code contributions.

## Changelog

__Bugs fixed__

- The radius keyword to circle sketchpad elements now specifies radius, instead of diameter
- Allow non-latin text input
- Clean up temporary files on Windows

__Improvements__

- Redesigned sketchpad GUI
- Added quick-open-item feature
- Added toggle-item-maximization feature
- Drag-and-drop improvements
- Script and controls now simultaneously editable
- Realtime inline_script syntax checking
- Introduce GUI extension framework

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

[2.8.3 release notes]: /notes/2.8.3
