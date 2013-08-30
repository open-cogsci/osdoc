---
layout: osdoc
title: Release notes for 0.27.4
group: notes
permalink: /0.27.4/
level: 1
sortkey: 999.999
show: false
---

OpenSesame 0.27.4 is currently in pre-release.
{: .page-notification}

OpenSesame 0.27.4 is the fourth maintenance release in the 0.27 'Frisky Freud' series, and was released on July 9 2013. If you are upgrading from 0.26, please read the [0.27 release notes][].

New features and enhancements:

- Chinese translation (`zh_CN`), contributed by Zhongquan Li and Gabriel Chan
- HTML parsing is now optional in `sketchpad` items

Bugs fixed:

- Prevent key names like '[1]' to avoid variable errors
- Fix `color` keyword argument in `canvas.arrow()`
- Fix `advanced_delay` plug-in to work with Unicode
- Intercept `psychopy.core.quit()` to prevent PsychoPy from killing OpenSesame

Windows packaging:

- All dependencies have been updated to most recent version
- PyGame has been downgraded to 1.9.1 to prevent mouse issues

[0.27 release notes]: /notes/0.27