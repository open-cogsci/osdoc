---
layout: osdoc
title: Sequences and loops
group: Usage
permalink: /sequences-and-loops/
---

The `loop` and `sequence` items are two special items that add structure to your experiment. Understanding how `loop`s and `sequence`s work is one of the trickier aspects of working with OpenSesame.

%--
toc:
 mindepth: 2
--%

## Sequence items

A `sequence` is a list of items that is executed sequentially. For every item in a `sequence` there is also a 'Run if' condition, which specifies the conditions under which an item should be executed (by default this is 'always'). A `sequence` does not repeat automatically: For this, you will need to combine it with a `loop`.

A typical situation where a `sequence` is used is as a trial: A single trial will often correspond to a single `sequence` item. This illustrated in the screenshot below.

%--
figure:
 id: FigTrial
 source: FigTrial.png
 caption: |
  A single trial often corresponds to a single `sequence` item.
--%

In this example trial, there is a *trial_sequence*, which consists of a fixation dot (a `sketchpad` item), a target display (another `sketchpad`), a response collection item (a `keyboard_response`), a green fixation dot (another `sketchpad`), a red fixation dot (another `sketchpad`), and a data logging item (a `logger`).

Most items are called 'always'. However, the green and red fixation dots have specific 'Run if' conditions. The green fixation dot is only called when the variable `correct` has the value 1. The red fixation dot is only called when the variable `correct` has the value 0. Effectively, this means that the color of the fixation dot provides the participant with immediate feedback on every trial: Green means correct, red means incorrect.

The variable “correct” is set automatically by the keyboard_response item. For more information about variables and conditional statements, see:

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)

## loop items

`Loop` items repeatedly call a single other item, the 'item to run'. `Loop`s are also used to control independent variables, so that every time that the item-to-run is called, the independent variables have different values. A `loop` only calls a single other item. To call multiple items, will need to combine a `loop` with a `sequence`.

A typical situation where a loop is `used` is to form a block of trials. In that case, the item-to-run is a trial sequence, which is called multiple times. This is illustrated in the screenshot below.

%--
figure:
 id: FigLoopTable
 source: FigLoopTable.png
 caption: |
  A `loop` item provides a table in which you can define your independent variables.
--%

In this example `loop`, three independent variables have been defined: `object`, `orientation`, and `correct_response`. There are eight different cycles, or combinations ('knife, left, z', 'knife, right, z', etc.). Because 'repeat' is set to 3, every combination is called three times. Therefore, the item *trial_sequence* is called 8 x 3 = 24 times. The 'order' is set to 'random', which means that a random cycle is selected (without replacement) for every call of the item *trial_sequence*.

## Combining loops and sequences

`Loop`s and `sequence`s are often combined to create a structure in which multiple items are repeated. As we've seen, a typical example of a `loop`-`sequence` structure is a single block of trials. Here a single trial is a `sequence`, which is called repeatedly by a `loop` to form a block of trials, as shown in the screenshots below.

%--
figure:
 id: FigBlock
 source: 3.png
 caption: |
  A block of trials often corresponds to a `loop` item, which in turn calls a `sequence` item that corresponds to a single trial.
--%

One level up in the hierarchy of the experiment, there is another `loop`-`sequence` structure, which corresponds to multiple blocks of trials. Here, a `sequence` (the *block_sequence* in the figure) calls a single block of trials (the *block_loop*), followed by a `feedback` item. This `sequence` is repeatedly called by a `loop` (the *experimental_loop*), so that there are multiple blocks of trials, each followed by feedback.

%--
figure:
 id: FigLoopSequence
 source: 4.png
 caption: |
  You can use nested `loop`-`sequence` structures to implement trials, blocks of trials, blocks of blocks, etc.
--%

The structure displayed in the screenshot above might look a bit confusing at first sight, but it becomes clearer when you think about it as a two nested `loop`-`sequence` structures. The first one (*block_loop* - *trial_sequence*) corresponds to a single block of trials. The second one (*experimental_loop* - *block_sequence*) corresponds to multiple blocks of trials, each followed by feedback to the participant. Many experiments will contain a structure of this kind.
