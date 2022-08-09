title: The prepare-run strategy

[TOC]

## About

Experiments typically consist of short intervals ('trials') during which participants perceive stimuli and perform a task. Timing should be controlled during a trial, but some unpredictable variation in the duration of the interval between trials is acceptable. Therefore, a good strategy is to perform time-consuming tasks before a trial, and to keep the operations that are performed during a trial to a minimum.

OpenSesame does this by calling each element from a SEQUENCE item twice. This is the *prepare-run strategy*:

- During the Prepare phase, items are given the opportunity to prepare. For example, a SYNTH generates a sound (but doesn't play it); and a SKETCHPAD draws a canvas (but doesn't show it).
- During the Run phase, items do as a little as possible. For example, a SYNTH plays back a previously prepared sound; and a SKETCHPAD shows a previously prepared canvas.

This reduces the risk of timing glitches. The prepare-run strategy is implemented at the level of SEQUENCE items, which typically contains the time-critical parts of an experiment. This means that before a SEQUENCE is started, there is some unpredictable temporal jitter.

## Item-specific notes

### loop items

A LOOP item is not prepared in advance. It is important to take this into account when using a LOOP to implement time-critical parts. For example, you may be tempted to implement an RSVP stream using a LOOP item as follows:

~~~text
rsvp_loop item (4 cycles)
- stimulus_item
~~~

In this construction, *stimulus_item* will be prepared and run four times in alternation, like so:

~~~text
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

All items that are part of a SEQUENCE are prepared in advance. Therefore, the following construction ...

~~~text
trial_sequence
- fixation_sketchpad
- target_sketchpad
- keyboard_response
- logger
~~~

... will be executed as follows ...

~~~text
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

SKETCHPAD and FEEDBACK items differ in when they are prepared. For SKETCHPADs preparation occurs during the Prepare phase; for FEEDBACK items, preparation occurs only during the Run phase.

For more information, see:

- %link:manual/stimuli/visual%

### synth and sampler items

For SYNTH and SAMPLER items, the sound is generated and preloaded during the Prepare phase.

### inline_script items

In an INLINE_SCRIPT item, you can choose how you want to implement the run and prepare strategy. In general, it is good practice to adhere to the following guidelines:

- Time-consuming, preparatory functionality goes in the Prepare phase. For example, creating canvas objects, and generating sounds.
- A minimum amount of code is put in the run phase. For example, only showing a previously prepared canvas.

### Other items and plugins

In general, items should follow the principle of performing as much as possible time-consuming preparation during the Prepare phase, and minimizing the Run phase. However, every plugin is implemented differently. If you are unsure about a specific case, please post a query on the forum.

## Conditional statements ('Run if' and 'Show if')

In SEQUENCE items, the 'Run if' condition is evaluated at the last moment, during the run phase. Therefore, you can use a condition like `[correct] = 0` which depends on the results of a KEYBOARD_RESPONSE item which has been called just before. It is important to take into account that the 'Run if' statement applies *only* to the run phase of an item—The prepare phase is *always* executed.

In COROUTINES items, the 'Run if' condition is evaluated during the Prepare phase. Therefore, the conditions cannot depend on events that occur during the execution of the COROUTINES.

In SKETCHPAD items, the 'Show if' condition is evaluated during the Prepare phase, when the canvas is constructed. In FEEDBACK items, the 'Show if' condition is evaluated during the Run phase (because the canvas is only constructed in the Run phase).
