---
layout: osdoc
title: Source-code architecture
group: contribute
permalink: /architecture/
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 maxdepth: 4
 exclude: [Overview]
--%

## About this page

This page is intended to provide (potential) developers with an idea of OpenSesame's source-code architecture. This is an informal and incomplete description of the most important characteristics of the architecture. If you have questions that are not answered here, please refer to the source code, or ask questions in the 'OpenSesame-dev' section of the [forum].

## General description of the architecture

The source-code architecture of OpenSesame is highly modular, and the various levels of abstraction are separated across three different Python packages, each of which contains several sub-packages (see %FigUML). At the highest level, `openexp` deals with input (keyboard responses, etc.) and output (display presentation, etc.). The `libopensesame` package implements the OpenSesame runtime, i.e. the functionality required to execute experiments. Finally, the `libqtopensesame` package implements the graphical user interface (GUI).

### UML class diagram

%--
figure:
 source: uml-class-diagram.png
 id: FigUML
 caption: A schematic depiction of the source-code architecture. This diagram is a sketch that conveys some general principles, and not a complete UML class diagram.
--%

### The `openexp` package

The `openexp` package (yellow in %FigUML) implements input and output in a way that is not tied to a specific mechanism. For example, whenever something needs to be shown on the display, an instance of `canvas` is created, as shown in %OpenexpExample:

%--
code:
 source: openexp-example.py
 id: OpenexpExample
 syntax: python
 caption: The `canvas` class is a factory that produces a back-end specific `canvas` object.
--%

The `canvas` class is a [factory] that produces a back-end-specific canvas object, based on the `canvas_backend` property of the `experiment` object. For example, if the `xpyriment` back-end is used, `my_canvas` (in the example above) will become an instance of `openexp._canvas.xpyriment.xpyriment`. All `openexp._canvas.[backend].[backend]` classes are [adapters] that implement the same interface and map this onto functions that are specific to the underlying library. The interface specified in `openexp._canvas.legacy.legacy` is the reference interface, which all other back-ends must implement.

The same principle is also used for the `keyboard`, `mouse`, `sampler`, and `synth` classes.

### The `libopensesame` package

The `libopensesame` package (blue in %FigUML) implements the runtime of OpenSesame. It provides all the functionality that is required to execute an experiment, but is not concerned with the GUI.

An experiment consists of several items, such as `sketchpad`s, `sequence`s, and `loop`s. Items may execute other items. For example, a `sequence` executes one or more other items in a sequential order. In this way, by hopping from item to item, the progression of the experiment is determined.

All items are derived from the `item` class, which provides the basic functionality that is common to all items. A special type of item is the `experiment` item. The `experiment` item embeds all other items in its `items` attribute (a `dict` where item names are keys and item objects are values), stores experimental variables, and implements functionality for pre-experiment initialization and post-experiment clean-up. All other items have an `experiment` attribute, which points towards the `experiment` item.

%--
code:
 source: libopensesame-example.py
 id: LibopensesameExample
 syntax: python
 caption: You can parse and execute an experiment with a few lines of code.
--%

The four most important `item` methods are:

- `prepare()` implements the item's prepare phase.
- `run()` implements the item's run phase.
- `from_string()` parses an OpenSesame script into an item.
- `to_string()` generates an OpenSesame script from an item.

### The `libqtopensesame` package

The `libqtopensesame` package (green in %FigUML) implements the OpenSesame GUI. It is the most complicated and largest part of OpenSesame. The main application window is implemented in `qtopensesame`.

#### Items

The `libqtopensesame.items` sub-package is the GUI counterpart of `libopensesame`. At the heart of this package is the `qtitem` class, which provides the basic GUI functionality that is common to all items. Every item class from `libopensesame` has a counterpart in `libqtopensesame.items`, in which the runtime functionality is extended with GUI functionality. Basically, what an item does is implemented in `libopensesame`, while its GUI controls are implemented in `libtopensesame.items`.

The four most important `qtitem` methods are:

- `apply_edit_changes()` updates the item based on changes in the GUI.
- `edit_widget()` updates the GUI based on the status of the item.
- `init_edit_widget()` constructs the item's GUI controls.

#### Runners

The `[runner name]_runner` classes, all of which are derived from `base_runner`, provide the functionality required for running an experiment. Essentially, an instance of `libopensesame.experiment.experiment` is created based on the active instance of `libqtopensesame.items.experiment.experiment` in the GUI. The experiment is executed and any exceptions that occur during execution are passed as `osexception`s back to the GUI.

#### UI classes

The `libqtopensesame.ui` sub-package contains various auto-generated modules that implement parts of the user interface. All modules are generated directly from the `.ui` files located in `/resources/ui`.

## Linked list of packages and modules

Click on the links below to view the relevant source-code files on GitHub.

{% include architecture %}

[factory]: http://en.wikipedia.org/wiki/Factory_method_pattern
[adapters]: http://en.wikipedia.org/wiki/Adapter_pattern
[back-ends]: /back-ends/
[forum]: http://forum.cogsci.nl
