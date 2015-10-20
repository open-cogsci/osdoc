---
layout: osdoc
title: Keyboard shortcuts
group: usage
permalink: /shortcuts/
---

The keyboard shortcuts listed below are default values, and can be changed as described under [Changing shortcuts].

## Overview

%--
toc:
 mindepth: 2
 excude: [overview]
--%

## General shortcuts

The following keyboard shortcuts are available everywhere:

- Quick switcher: `Meta+O`
- New experiment: `Ctrl+N`
- Open experiment: `Ctrl+O`
- Save experiment: `Ctrl+S`
- Save experiment as: `Ctrl+Shift+S`
- Undo: `Ctrl+Alt+Z`
- Redo: `Ctrl+Alt+Shift+Z`
- Run experiment fullscreen: `Ctrl+R`
- Run experiment in window: `Ctrl+W`
- Quick-run experiment: `Ctrl+Shift+W`
- Show/ hide overview area: `Ctrl+\`
- Show/ hide debug window: `Ctrl+D`
- Show/ hide file pool: `Ctrl+P`
- Show/ hide variable inspector: `Ctrl+I`
- Focus overview area: `Ctrl+1`
- Focus tab area: `Ctrl+2`
- Focus debug window: `Ctrl+3`
- Focus file pool: `Ctrl+4`
- Focus variable inspector: `Ctrl+5`

## Editor shortcuts

The following keyboard shortcuts are available in editor components, such as the `inline_script`:

- Run selected code in debug window (if applicable): `Alt+R`
- Run all code in debug window (if applicable): `Shift+Alt+R`
- Comment selected line(s): `Ctrl+M`
- Uncomment selected line(s): `Ctrl+Shift+M`
- Show find/ replace dialog: `Ctrl+F`
- Hide find/ replace dialog: `Escape`
- Show/ hide preferences: `Ctrl+Shift+P`
- Next tab (if applicable): `Alt+Left`
- Previous tab (if applicable): `Alt+Right`
- Undo: `Ctrl+Z`
- Redo: `Ctrl+Shift+Z`
- Copy: `Ctrl+C`
- Cut: `Ctrl+X`
- Paste: `Ctrl+V`

## Tab-area shortcuts

The following keyboard shortcuts are available in the tab area:

- Next tab: `Ctrl+Tab`
- Previous tab: `Ctrl+Shift+Tab`
- Close other tabs: `Ctrl+T`
- Close all tabs: `Ctrl+Shift+T`
- Close current tab: `Alt+T`

## Overview-area and sequence shortcuts

The following keyboard shortcuts are available in the overview area and the `sequence` item:

- Context menu: `+`
- Copy item: `Ctrl+C`
- Paste item: `Ctrl+V`
- Delete item: `Del`
- Permanently delete item: `Shift+Del`
- Create linked copy: `Ctrl+Shift+L`
- Create unlinked copy: `Ctrl+Shift+U`
- Rename: `F2`
- Change run-if statement (if applicable): `F3`

## Changing shortcuts

Currently, you can change most keyboard shortcuts only through the `cfg` object in the debug window. First, get a list of configuration options by typing:

~~~ .python
print(cfg)
~~~

Locate the name of the shortcut that you want change, such as `qProgEditRunSelectedShortcut`. Next, change it by typing:

~~~ .python
cfg.qProgEditRunSelectedShortcut = `Ctrl+Shift+E' # My new shortcut
~~~

Finally, restart OpenSesame for the new shortcuts to take effect.
