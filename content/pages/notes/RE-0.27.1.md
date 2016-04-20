---
layout: osdoc
title: Release notes for 0.27.1
group: notes
permalink: /0.27.1/
show: false
---

OpenSesame 0.27.1 is the first maintenance release in the 0.27 'Frisky Freud' series. If you are upgrading from 0.26, please read the [0.27 release notes][].

Bugs fixed:

- Fix numeric values in form checkboxes
- Do not show start-up tab when opening a file directly
- Catch errors due to missing closing quotations when editing a sketchpad element
- Fix `super()` error in form plug-ins
- Fix variable background color in sketchpad item
- Catch recursion errors in general script
- More comprehensive HTML and font implementation in psycho and legacy back-ends
- Do not interpret special character sequences in script
- Fix joystick plug-in
- Fix `exp.get_file()` in opensesamerun
- Fix option splitting by return in form_multiple_choice plug-in
- Fix a bug where timeouts where always counted as incorrect

Windows packaging:

- Include joystick plug-in

Ubuntu/ Debian packaging:

- Include joystick plug-in
- Include repeat_cycle plug-in

[0.27 release notes]: /notes/0.27
