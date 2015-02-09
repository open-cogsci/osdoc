---
layout: osdoc
title: Release notes for 2.9.1
group: notes
permalink: /2.9.1/
---

OpenSesame 2.9.1 is the second maintenance release in the 2.9 series. If you are upgrading from 2.8.3 or earlier, please also read the [2.9.0 release notes].

## Credits

Thanks to Timo Lüke for updating the German translation.

## Changelog

### Bugs fixed

- Fix resetting font size and family in sketchpad (#284)
- Fix rounding issue in canvas._gabor() (#283)
- Better detection of Exception messages (#285)
- Fix a race condition when dropping an item on a loop or sequence
- Fix broken context menu in sketchpad when running a translation (#287)
- Correctly parse variables in video_player plug-in (#288)
- Use new sketchpad-element icons also in 32x32 size
- Fixed a bug when reducing and canceling the number of cycles in a loop
- Fixed display of font style in sketchpad widget
- Include PyQt4 plugins in Windows build

### Improvements

- Application-wide keyboard shortcuts for tab switching
- Add close current tab action
- Improved focus behavior

### Translation updates

- Update German translation (de_DE)

### Windows packaging

- Update included libraries. See `modules()` output below.
- Includes a snapshot of PyGaze (0.5.0~opensesame-3)
- Includes a slightly patched version of PsychoPy 1.80.05 that addresses an important issue with keypress timestamps. (Unchanged from 2.8.2.)

~~~
OpenSesame 2.9.1
Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)]
OpenCV is not available
OpenCV2 2.4.9
QProgedit 2.0.5
Expyriment 0.7.0 (Revision 7a6b73d; Python 2.7.6)
NumPy 1.8.1
PIL is available (version is unknown)
PsychoPy 1.80.05-opensesame-1
PyAudio 0.2.8
PyGame 1.9.1release
PyGaze 0.5.0~opensesame3
Pyglet 1.1.4
PyOpenGL 3.1.0
PyQt 4.11.1
PySerial 2.7
python-bidi 0.3.4
python-markdown 2.4.1
SciPy 0.14.0
~~~

[2.9.0 release notes]: /notes/2.9.0/
