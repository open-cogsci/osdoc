---
layout: osdoc
title: The prepare-run strategy
group: Usage
permalink: /prepare-run/
---

:--
cmd: overview
--:

## About

Experiments typically consist of short intervals ('trials') during which a participant perceives stimuli and performs a task. Timing should be controlled during a trial, but some unpredictable variation in the duration of the interval between trials is acceptable. Therefore, the best strategy for experimental software is to perform time consuming tasks before a trial, and to keep the operations that need to be performed during a trial to a bare minimum.

OpenSesame implements this strategy by calling each element from a `sequence` item twice. During the prepare phase, items are given time to prepare, for example by generating a sound in the case of a `synth` item, or by creating an 'offline canvas' in the case of a `sketchpad`. During the run phase, items simply execute a very limited number of trivial functions, such as showing a previously constructed canvas. This strategy substantially reduces the risk of timing glitches. The prepare-run strategy is implemented at the level of `sequence` items, which will typically contain the time-critical parts of an experiment. If a `sequence` is called multiple times by a `loop`, the `loop` as a whole is not prepared. Doing so would quickly lead to excessive memory usage and potentially cause rather than prevent timing issues.

## Item-specific notes

### loop items

A `loop` item is not prepared in advance. It is important to take this into account when using a `loop` to implement time-critical parts. For example, it is possible to implement an RSVP stream using a `loop` item, with something like the following structure:
	
~~~
rsvp_loop item (4 cycles)
- stimulus_item 
~~~

In this construction, *stimulus_item* will be prepared and run four times in alternation, like so:

~~~
prepare stimulus_item
run stimulus_item
prepare stimulus_item
run stimulus_item
prepare stimulus_item
run stimulus_item
prepare stimulus_item
run stimulus_item
~~~

Therefore, you need to verify that the preparation of *stimulus_item* does not cause any timing glitches.

### sequence items
	
All items that are part of a `sequence` are prepared in advance. Therefore, the following construction ...

~~~
trial_sequence
- fixation_sketchpad
- target_sketchpad
- keyboard_response
- logger
~~~

... will be executed as follows ...

~~~
prepare fixation_sketchpad
prepare target_sketchpad
prepare keyboard_response
prepare logger
run fixation_sketchpad
run target_sketchpad
run keyboard_response
run logger
~~~

### sketchpad and feedback items

`sketchpad` and `feedback` items are very similar. They both provide a drawable canvas that can be used as a stimulus display during the experiment. The crucial difference lies in the phase during which the canvas is constructed

For a `sketchpad` item, the canvas is constructed during the prepare phase of the `sequence` of which it is part. This is done to reduce the possibility of timing glitches, because constructing a canvas can take a bit of time, especially when it contains many and/ or complex stimuli. Consequently, the contents of a `sketchpad` cannot depend on what happens during the `sequence` of which it is part. In contrast, for `feedback` items, the canvas is constructed at the moment that it is shown, during the run phase. Therefore, it may take some time for a `feedback` item to actually appear on the screen, and it should not be used for presenting time critical stimuli. But unlike a `sketchpad` item, the contents of a `feedback` item can depend on what happened during the `sequence` of which it is part, which makes it suitable for presenting feedback.

### synth and sampler items

For `synth` and `sampler` items, the sound is generated and preloaded during the prepare phase.

### inline_script items

In an `inline_script` item, you can choose how you want to implement the run and prepare strategy. In general, it is good practice to adhere to the principle of putting time-consuming preparatory stuff (e.g., creating canvas objects) in the prepare phase, and put a minimum amount of code in the run phase (e.g., just showing a canvas).

### Other items and plug-ins

In general, items should follow the principle of performing as much as possible time-consuming preparation during the prepare phase, and minimizing the run phase. However, every plug-in is implemented differently. If you are unsure about a specific case, please post a query on the forum.

## Conditional statements ('Run if' and 'Show if')

In `sequence` items, the 'Run if' condition is evaluated at the last moment, during the run phase. Therefore, you can use a condition like `[correct] = 0` which depends on the results of a `keyboard_response` item which has been called just before. It is important to take into account that the 'Run if' statement applies *only* to the run phase of an item--The prepare phase is *always* executed.

In `sketchpad` items, the 'Show if' condition is evaluated during the prepare phase, when the `sketchpad` is constructed. In `feedback` items, the 'Show if' condition is evaluated during the run phase.
