---
layout: osdoc
title: Release notes for 0.27
group: notes
permalink: /0.27/
level: 1
sortkey: 999.999
show: false
---

OpenSesame 0.27 is almost completely backwards compatible with previous versions, expect for the following differences:

- `canvas.keyboard.get_key()` now returns a key as `unicode`, rather than as an `int` corresponding to an ASCII value. This change has been made to improve support for non-QWERTY keyboard layouts.
- Response timeouts are now registered as `None`, rather than the string 'timeout'.
- In the Windows release, the media_player plug-in has been replaced in favour of the media_player_vlc plug-in. This was necessary, because the libraries used by the old media_player are not compatible with Python 2.7.

Notable changes:

- Added Expyriment backend
- Added form functionality
- Improved Unicode support
- Improved internationalization
- Added quick run button
- Add ecological alternative to S&V template
- Numerous bug-fixes
- Improved compatibility with Nexus 7 tablet

