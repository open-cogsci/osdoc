---
layout: osdoc
title: Release notes for 3.0.3
group: notes
permalink: /3.0.3/
---

OpenSesame 3.0.3 is the third maintenance release in the 3.0 series. If you are upgrading from OpenSesame 2.9.7 or earlier, please see the list of important changes in OpenSesame 3.0:

- [Important changes in 3.0](/miscellaneous/important-changes-3/)

## Credits

Thanks to Eduard Ort ([@eort](https://github.com/eort)) and Igor Gnatenko ([@ignatenkobrain](https://github.com/ignatenkobrain)) for their code contributions.

## Changes

### Improvements

- Fix templates for Python 3
- Fix Exception handling for multiprocess_runner in Python 3
- Update German translation (de_DE)
- Update droid template to API 2 (avoids warning)

### Bugs fixed

- Fix Python-3 compatibility for script validator
- Restore overview area when drop fails (#361)
- Warn on missing `__end__` statements in OpenSesame script (#364)
- Don't be greedy when parsing YAML front matter (#369)
- Fix external_runner (#371)
- Improve handling of variably defined font and sketchpad element settings (#372)
- Don't crash when moving sketchpad elements with variably defined positions (#373)
- Don't crash when copy-pasting in loop table when no cells are selected (#374)
- Fall back to z_index=0 when an invalid z_index has been specified for sketchpad elements (#375)
- Don't crash on empty filename in image element in sketchpad (#377)
- Fix recursion error in overview area with multiple linked copies (#376)
- Don't try to copy and edit non copyable/editable treeitems
- Don't crash when failing to get size information for file pool
- Catch invalid variable names in logger script
- Don't allow editing run-if statement of top-level sequence in sequence-view
- Fix gabor and noise-patch elements

### Windows packaging

~~~
OpenSesame 3.0.3
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
PyGaze 0.6.0a7
Pyglet 1.2.3
PyOpenGL 3.1.0
PyQt 4.11.4
PySerial 2.7
python-bidi 0.3.4
python-markdown 2.6.2
SciPy 0.15.1
~~~
