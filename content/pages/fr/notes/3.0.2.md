---
layout: osdoc
title: Release notes for 3.0.2
group: notes
permalink: /3.0.2/
---

OpenSesame 3.0.2 is the second maintenance release in the 3.0 series. If you are upgrading from OpenSesame 2.9.7 or earlier, please see the list of important changes in OpenSesame 3.0:

- [Important changes in 3.0](/miscellaneous/important-changes-3/)

## Credits

Thanks to Jarik den Hartog ([@JdenHartog](https://github.com/JdenHartog)) and Daniel Schreij ([@dschreij](https://github.com/dschreij)) for their code contributions.

## Changes

### Improvements

- Improved validation of variable names in loop item
- Improved validation of OpenSesame-script syntax
- Improved exception handling (including run-status emoticons)

### Bugs fixed

- Don't crash on non-ascii values in variable inspector
- Fix crash on invalid OpenSesame script
- Improved validation and quote handling in conditional statements (#356)
- Fix typo in bug_report success notification
- Fix incorrect URL in Windows installer
- Fix canvas.copy() (#355)
- Fix variable inspection (don't crash on empty values)
- Fix a crash when renaming a variable to itself
- Fix a crash when creating a linked copy of a non-existing item
- [Mac OS] Fix a crash when restoring config (#360)
- Safely decode input in syntax (fixes non-ascii text in Python forms)

### Windows packaging

~~~
OpenSesame 3.0.2
Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
OpenCV is not available
OpenCV2 3.0.0
QProgedit 3.2.0
Expyriment  (Python 2.7.10)
IPython 3.2.0
NumPy 1.9.2
PIL is available (version is unknown)
PsychoPy 1.82.01
PyAudio 0.2.8
PyGame 1.9.1release
PyGaze 0.6.0a4
Pyglet 1.2.3
PyOpenGL 3.1.0
PyQt 4.11.4
PySerial 2.7
python-bidi 0.3.4
python-markdown 2.6.2
SciPy 0.15.1
~~~
