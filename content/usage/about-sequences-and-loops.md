---
layout: osdoc
title: About sequences and loops
group: Usage
permalink: /about-sequences-and-loops/
level: 1
sortkey: 004.003
---

The *loop* and *sequence* items are two special items that add structure to your experiment. Understanding how loops and sequences work is one of the trickier aspects of working with OpenSesame.

Overview
--------

- [Sequences](#sequences)
- [Loops](#loops)
- [Combining loops and sequences](#combining)

Sequences <a id='sequences'></a>
---------

A sequence is a list of items that is executed in sequence. For every item in a sequence there is also a “Run if” condition, which specifies the conditions under which an item should be executed (by default this is “always”). A sequence does not repeat automatically: For this, you will need to combine it with a loop.

A typical place where a sequence is used is in a trial: A single trial will often correspond to a single sequence. This illustrated in the screenshot below.

![](/img/fig/fig4.3.1.png)

In this example trial, there is a trial_sequence, which consists of a fixation dot (a sketchpad item), a target display (another sketchpad), a response collection item (a keyboard_response), a green fixation dot (another sketchpad), a red fixation dot (another sketchpad), and a data logging item (a logger).

Most items are called “always”. However, the green and red fixation dots have specific “Run if” conditions. The green fixation dot is only called when the variable “correct” has the value “1”. The red fixation dot is only called when the variable “correct” has the value “0”. Effectively, this means that the color of the fixation dot provides the participant with immediate feedback on every trial: Green means correct, red means incorrect.

The variable “correct” is set automatically by the keyboard_response item. For more information about variables and conditional statements, see here.

Loops <a id='loops'></a>
-----

Loops repeatedly call a single other item, the “item to run”. Loops are also used to control independent variables, so that every time that the item to run is called, the independent variables have different values. A loop does not call multiple items, for this you will need to combine it with a sequence.

A typical place where a loop is used is to form a block of trials. In that case, the item to run is a trial sequence, which is called multiple times. This is illustrated in the screenshot below.

![](/img/fig/fig4.3.2.png)

In this example loop, 3 independent variables have been defined: “object”, “orientation”, and “correct_response”. There are 8 different “cycles”, or combinations (“knife, left, z”, “knife, right, z”, etc.). Because “repeat” is set to 3, every combination is called 3 times. Therefore, “trial_sequence” is called 8 x 3 = 24 times. The “order” is set to random, which means that a random cycle is selected (without replacement) for every call of “trial_sequence”.

Combining loops and sequences <a id='combining'></a>
-----------------------------

Loops and sequences are often combined to create a structure in which multiple items are repeated. As we've seen, a typical example of a loop-sequence structure is a single block of trials. Here a single trial is a sequence, which is called repeatedly by a loop to form a block of trials, as shown in the screenshots below.

![](/img/fig/fig4.3.3.png)

One level up in the hierarchy of the experiment, there is another loop-sequence structure, which corresponds to multiple blocks of trials (almost a complete experiment, in other words). Here, a sequence (called “block_sequence” in the figure) calls a single block of trials (“block_loop”), followed by a feedback item. This sequence is repeated by a loop (called “experimental_loop” in the figure), so that there are multiple blocks of trials, each followed by feedback.

![](/img/fig/fig4.3.4.png)

The structure displayed in the screenshot above might look a bit confusing at first sight, but it becomes clearer when you think about it as a two loop-sequence structures. The first one (“block_loop” - “trial_sequence”) corresponds to a single block of trials. The second one (“experimental_loop” - “block_sequence”) corresponds to multiple blocks of trials, each followed by feedback to the participant. Many experiments will contain a structure of this kind.

[timing]: TODO