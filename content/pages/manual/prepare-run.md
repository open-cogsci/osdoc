title: The prepare-run strategy
reviewed: false

[TOC]

## About

Experiments typically consist of short intervals ('trials') during which a participant perceives stimuli and performs a task. Timing should be controlled during a trial, but some unpredictable variation in the duration of the interval between trials is acceptable. Therefore, the best strategy for experimental software is to perform time consuming tasks before a trial, and to keep the operations that need to be performed during a trial to a bare minimum.

OpenSesame implements this strategy by calling each element from a SEQUENCE item twice. This is the prepare-run strategy:

- During the prepare phase, items are given time to prepare, for example by generating a sound in the case of a SYNTH item, or by creating an 'offline canvas' in the case of a SKETCHPAD.
- During the run phase, items simply execute a very limited number of trivial functions, such as showing a previously constructed canvas.

This strategy substantially reduces the risk of timing glitches. The prepare-run strategy is implemented at the level of SEQUENCE items, which will typically contain the time-critical parts of an experiment. This means that, if a SEQUENCE is called multiple times by a LOOP, the LOOP as a whole is not prepared. Doing so would quickly lead to excessive memory usage and cause rather than prevent timing issues.

## Item-specific notes

### loop items

A LOOP item is not prepared in advance. It is important to take this into account when using a LOOP to implement time-critical parts. For example, it is possible (but generally a bad idea) to implement an RSVP stream using a LOOP item, with something like the following structure:

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

All items that are part of a SEQUENCE are prepared in advance. Therefore, the following construction ...

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

SKETCHPAD and FEEDBACK items differ in when they are prepared. For SKETCHPADs preparation occurs during the prepare phase; for FEEDBACK items, preparation occurs only during the run phase.

For more information, see:

- %link:manual/stimuli/visual%

### synth and sampler items

For SYNTH and SAMPLER items, the sound is generated and preloaded during the prepare phase.

### inline_script items

In an INLINE_SCRIPT item, you can choose how you want to implement the run and prepare strategy. In general, it is good practice to adhere to the following guidelines:

- Time-consuming, preparatory functionality goes in the prepare phase. For example, creating canvas objects, and generating sounds.
- A minimum amount of code is put in the run phase. For example, only showing a previously prepared canvas.

### Other items and plug-ins

In general, items should follow the principle of performing as much as possible time-consuming preparation during the prepare phase, and minimizing the run phase. However, every plug-in is implemented differently. If you are unsure about a specific case, please post a query on the forum.

## Conditional statements ('Run if' and 'Show if')

In SEQUENCE items, the 'Run if' condition is evaluated at the last moment, during the run phase. Therefore, you can use a condition like `[correct] = 0` which depends on the results of a KEYBOARD_RESPONSE item which has been called just before. It is important to take into account that the 'Run if' statement applies *only* to the run phase of an item--The prepare phase is *always* executed.

In SKETCHPAD items, the 'Show if' condition is evaluated during the prepare phase, when the SKETCHPAD is constructed. In FEEDBACK items, the 'Show if' condition is evaluated during the run phase.
