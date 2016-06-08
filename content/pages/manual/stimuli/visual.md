title: Visual stimuli

The most common way to present visual stimuli is using the SKETCHPAD item, or, for non-time-critical stimuli, the FEEDBACK item.

[TOC]

## Using the sketchpad and feedback items

The SKETCHPAD and FEEDBACK item offer basic what-you-see-is-what-you get drawing tools (%FigSketchpad).

%--
figure:
 id: FigSketchpad
 source: sketchpad.png
 caption: The SKETCHPAD provides built-in drawing tools.
--%

## The difference between sketchpad and feedback items

The SKETCHPAD and FEEDBACK items are identical in most ways, except for two important differences.

### Sketchpad items are prepared in advance, feedback items are not

The contents of a SKETCHPAD are prepared during the prepare phase of the SEQUENCE that it is part of. This is necessary to ensure accurate timing: It allows the SKETCHPAD to be shown right away during the run phase, without any delays due to stimulus preparation. However, the downside of this is that the contents of a SKETCHPAD cannot depend on what happens during the SEQUENCE that it is part of. For example, you cannot use a SKETCHPAD to provide immediate feedback on the response time collected by a KEYBOARD_RESPONSE item (assuming that the SKETCHPAD and KEYBOARD_RESPONSE are part of the same sequence.)

In contrast, the contents of a FEEDBACK item are only prepared when they are actually shown, that is, during the run phase of the SEQUENCE that it is part of. This makes it possible to provide feedback on things that just happened--hence the name. However, the FEEDBACK item should not be used to present time-critical stimuli, because it suffers from delays due to stimulus preparation.

For more information about the prepare-run strategy, see:

- %link:prepare-run%

### Feedback variables are (by default) reset by feedback items

The FEEDBACK item has an option 'Reset feedback variables'. When this option is enabled (it is by default), feedback variables are reset when the FEEDBACK item is shown.

For more information about feedback variables, see:

- %link:variables%

## Presenting visual stimuli in Python

You can use the `canvas` object to present visual stimuli in Python:

- %link:canvas%
