---
layout: osdoc
title: Release notes for 2.9.0
group: notes
permalink: /2.9.0/
---

OpenSesame 2.9.0 is the first release in the 2.9 series. It offers major usability improvements over the 2.8 series. If you are upgrading from 2.8.3 or earlier, please also read the [2.8.3 release notes].

## Credits

- Thanks to [Nicky Anderson](https://github.com/nccanderson) for her code contributions.
- Thanks to [Eduard Ort](https://github.com/eort) for his contributions to the documentation.
- Thanks to [Edwin Dalmaijer](https://github.com/esdalmaijer/) for his work on [PyGaze](/devices/pygaze).

## Changelog

__Bugs fixed__

- The radius keyword to circle sketchpad elements now specifies radius, instead of diameter
- Allow non-latin text input (#280)
- Clean up temporary files on Windows (#282)
- Fix incorrect line numbers in inline_script tracebacks (#281)
- Fix detection of uppercase keys in psycho back-end (#271)
- Fix speciying synth frequency by key (#269)

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
TODO
~~~

[2.8.3 release notes]: /notes/2.8.3
