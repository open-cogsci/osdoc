---
layout: osdoc
title: Release notes for 2.8.1
group: notes
permalink: /2.8.1/
parser: academicmarkdown
---

2.8.1 is in pre-release.
{.page-notification}

OpenSesame 2.8.1 is the first maintenance release in the 2.8 series. If you are upgrading from 0.27.4 or earlier, please also read the [2.8.0 release notes].

## Credits

With thanks to Daniel Schreij and Ronald Sprouse for their code contributions.

## Changelog

### Bugs fixed

- Do not choke on translations in font-selection dialog
- Fix buffer-flush issue in srbox plug-in (#234)
- Correctly parse non-Unix line separators in text_display plug-in (#237)
- Saner focus and event-handling in script view.
- Initial jitter_mode value in advanced_delay plug-in (#238)
- Fix crash on special characters in experiment title with legacy back-end

### Improvements

- Validate form geometry (#222)
- Improvements to joystick plug-in
- Flush keyboard during sound playback to catch 'Escape' presses (#227)
- Sort comboboxes alphabetically (#233)
- Sort items alphabetically in OpenSesame script (#236)
- Improved validation of conditional statements (#235)
- Debug window respects QProgEdit theme
- Store filename-only logfiles relative to experiment folder (#161)
- Use one-tab mode by default

### Windows packaging

- Update included libraries. See `modules()` output below.

~~~
TODO
~~~

[2.8.0 release notes]: /notes/2.8.0
