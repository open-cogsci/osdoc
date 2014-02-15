---
layout: osdoc
title: Release notes for 2.8.0
group: notes
permalink: /2.8.0/
parser: academicmarkdown
---

If you are upgrading from 0.27.4, please read the [0.27.4 release notes][].

## Changelog 

### New functionality and improvements

- Add runner functionality
- Improved exception handling
- Migrate to QProgEdit editor component
- Updated offline help pages
- Improve support for non-Latin alphabets (#211)
- Add correct-response option to touch_response plug-in (#214)
- Add style argument to canvas.fixdot()
- Add item.set_response() convenience method
- Add gamma and suppress-warnings options to psycho back-end

### Bugs fixed

- Line wrapping causes double spaces (#203)
- Keywords to `decode()` break compatibility with Python < 2.7 (#201)
- Respect `focus=no` in `form_base` (#208)
- Fix ugly exception on Escape press in joystick plug-in (#162)
- Correctly parse non-Unix line separators in HTML parser
- Do not give ugly warning on close (#124)
- Set subject_parity in Android runtime (#221)

###  Debian packaging

- Remove large template files

### Windows packaging

- Update included libraries

[0.27.4 release notes]: /notes/0.27
