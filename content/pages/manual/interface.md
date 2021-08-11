title: Using the interface

OpenSesame has a powerful graphical interface that consists of several components (%FigInterface).

%--
figure:
 id: FigInterface
 source: interface.png
 caption: The OpenSesame user interface.
--%


[TOC]

## Toolbars and menubar

### The menubar

The menubar (%FigMenubar) is shown at the top of the window, or, on some operating systems, is integrated into the border around the window. The menubar contains general functionality, such as saving and opening experiments, running experiments, etc.

%--
figure:
 id: FigMenubar
 source: menubar.png
 caption: The menubar.
--%

### The main toolbar

The main toolbar (%FigMainToolbar) is (by default) shown at the top of the window, just below the menubar. The main toolbar contains a selection of the most relevant functionality from the menubar.

%--
figure:
 id: FigMainToolbar
 source: main-toolbar.png
 caption: The main toolbar.
--%

### The item toolbar

The item toolbar (%FigItemToolbar) is (by default) shown at the left of the window. The item toolbar contains all items, that is, all building blocks of an experiment. You can add items to your experiment by dragging them from the item toolbar into the overview area.

%--
figure:
 id: FigItemToolbar
 source: item-toolbar.png
 caption: The item toolbar.
--%

## The tab area

The tab area is the central part of the window (%FigTabArea). The tab area is where item controls, documentation, important messages, etc. are shown. The tab area can contain multiple tabs, and functions much like a tabbed web browser.

%--
figure:
 id: FigTabArea
 source: tab-area.png
 caption: The tab area.
--%

## The overview area

The overview area (%FigOverviewArea) is (by default) shown at the left of the window, to the right of the item toolbar. The overview area shows the structure of your experiment as a tree. You can re-order the items in your experiment by dragging them from one position to another in the overview area.

- Shortcut to hide/ show: `Ctrl+\`

%--
figure:
 id: FigOverviewArea
 source: overview-area.png
 caption: The overview area.
--%

## The file pool

The file pool (%FigFilePool) is (by default) shown at the right of the window. It provides an overview of all files that are bundled with the experiment.

- Shortcut to hide/ show: `Ctrl+P`

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: The file pool.
--%

## The debug window

The debug window (%FigDebugWindow) is (by default) shown at the bottom of the window. It provides an [IPython interpreter](https://ipython.org/), and is used as the standard output while an experiment is running. That is, if you use the Python `print()` function, the result will be printed to the debug window.

- Shortcut to hide/ show: `Ctrl+D`

%--
figure:
 id: FigDebugWindow
 source: debug-window.png
 caption: The debug window.
--%

## The variable inspector

The variable inspector (%FigVariableInspector) is (by default) shown at the right of the window. It provides a list of all variables that are detected in your experiment. When you are running an experiment, the variable inspector also provides a real-time overview of variables and their values.

- Shortcut to hide/ show: `Ctrl+I`

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: The variable inspector.
--%

## Keyboard shortcuts

The keyboard shortcuts listed below are default values. Many of them can be changed through *Menu → Tools → Preferences*.

### General shortcuts

The following keyboard shortcuts are available everywhere:

- Quick switcher: `Ctrl+Space`
- Command palette: `Ctrl+Shift+P`
- New experiment: `Ctrl+N`
- Open experiment: `Ctrl+O`
- Save experiment: `Ctrl+S`
- Save experiment as: `Ctrl+Shift+S`
- Undo: `Ctrl+Alt+Z`
- Redo: `Ctrl+Alt+Shift+Z`
- Run experiment fullscreen: `Ctrl+R`
- Run experiment in window: `Ctrl+W`
- Quick-run experiment: `Ctrl+Shift+W`
- Test experiment in browser: `Alt+Ctrl+W`
- Show/ hide overview area: `Ctrl+\`
- Show/ hide debug window: `Ctrl+D`
- Show/ hide file pool: `Ctrl+P`
- Show/ hide variable inspector: `Ctrl+I`
- Focus overview area: `Ctrl+1`
- Focus tab area: `Ctrl+2`
- Focus debug window: `Ctrl+3`
- Focus file pool: `Ctrl+4`
- Focus variable inspector: `Ctrl+5`

### Editor shortcuts

The following keyboard shortcuts are available in editor components, such as the INLINE_SCRIPT:

- (Un)comment selected line(s): `Ctrl+/`
- Find text: `Ctrl+F`
- Replace text: `Ctrl+H`
- Hide find/ replace dialog: `Escape`
- Duplicate line: `Ctrl+Shift+D`
- Undo: `Ctrl+Z`
- Redo: `Ctrl+Shift+Z`
- Copy: `Ctrl+C`
- Cut: `Ctrl+X`
- Paste: `Ctrl+V`

### Tab-area shortcuts

The following keyboard shortcuts are available in the tab area:

- Next tab: `Ctrl+Tab`
- Previous tab: `Ctrl+Shift+Tab`
- Close other tabs: `Ctrl+T`
- Close all tabs: `Ctrl+Alt+T`
- Close current tab: `Alt+T`

### Overview-area and sequence shortcuts

The following keyboard shortcuts are available in the overview area and the SEQUENCE item:

- Context menu: `+`
- Copy item (unlinked): `Ctrl+C`
- Copy item (linked): `Ctrl+Shift+C`
- Paste item: `Ctrl+V`
- Delete item: `Del`
- Permanently delete item: `Shift+Del`
- Rename: `F2`
- Change run-if statement (if applicable): `F3`
