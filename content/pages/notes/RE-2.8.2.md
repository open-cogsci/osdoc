---
layout: osdoc
title: Release notes for 2.8.2
group: notes
permalink: /2.8.2/
parser: academicmarkdown
---

OpenSesame 2.8.2 is the second maintenance release in the 2.8 series. If you are upgrading from 0.27.4 or earlier, please also read the [2.8.0 release notes].

## Credits

Thanks to Daniel Schreij ([@dschreij](https://github.com/dschreij/)) for his code contributions (as always!).

## Changelog

### Improvements

- Improve support for psycho back-end on OSX
- Improve support for multiprocessing on OSX
- Open experiments by dropping on the overview area
- Add fallback pool folder to facilitate versioning
- Allow margins, spacing, and theme to be specified in `form_multiple_choice` plug-in (#255)
- Safely convert messages to unicode in `item.log()`
- Fall back to temporary folder when the default logfile is not writable in quickrun mode

### Bugs fixed

- Fix autosave folder dialog on OSX (#250)
- Fix sampler crashing on filenames with special characters (#244)
- All items set `time_[item name]` variables (#243)
- Do not crash on purely numeric text when using bi-direction language support (#253)
- Correctly evaluate conditional statements with special characters
- Fixed confusion in tab manager when saving while having an open and modified item script
- Fix translation bug for non-ASCII str objects
- Fix a unicode bug where exceptions with images with special-character paths where obscured

### Windows packaging

- Update included libraries. See `modules()` output below.
- Includes a slightly patched version of PsychoPy 1.80.05 that addresses an important issue with keypress timestamps.

~~~
OpenSesame 2.8.2
Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)]
OpenCV is not available
OpenCV2 2.4.9
QProgedit 1.3.2
Expyriment 0.7.0 (Revision 7a6b73d; Python 2.7.6)
NumPy 1.8.1
PIL is available (version is unknown)
PsychoPy 1.80.05-opensesame-1
PyAudio 0.2.7
PyGame 1.9.1release
Pyglet 1.1.4
PyOpenGL 3.0.2
PyQt 4.10.4
PySerial 2.7
python-bidi 0.3.4
python-markdown 2.4
SciPy 0.13.3
~~~

[2.8.0 release notes]: /notes/2.8.0
