---
layout: osdoc
title: Release notes for 2.9.7
group: notes
permalink: /2.9.7/
---

OpenSesame 2.9.7 is the seventh maintenance release in the 2.9 series. If you are upgrading from 2.8.3 or earlier, please also read the [2.9.0 release notes].

## Credits

Thanks to Jarik den Hartog ([@JdenHartog](https://github.com/JdenHartog)) for his code contributions.

## Changes

### Improvements

- Add append menu to overview and sequence
- Add permanently delete menu option to unused items

### Bugs fixed

- Use px (not pt) as units in font GUI
- Explicitly set window type in psycho backend (#331)
- Fix recursion errors in drag-and-drop
- Restore structure when a drag is canceled (#337)
- Fix inconsistent folding/unfolding behavior in overview area (#336)
- Fix missing debug output on Android (#346)
- Allow uppercase text input on Android (#341)
- Allow external links in notification dialog (#340)
- Fix drag-and-drop between different instances of OpenSesame (#338)
- Fix a crash when dropping an item onto an unused item (#343)
- Fix a crash on Android when there are filenames with special characters in the file pool (#345)

### Windows packaging

~~~
OpenSesame 2.9.7
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
