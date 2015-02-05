---
layout: osdoc
title: Giving feedback to participants
group: Usage
permalink: /feedback/
---

You will often want to provide participants with feedback, to let them know how well they are doing. As a courtesy towards the participants, because most people find it unpleasant to perform a task without getting feedback. And also to improve the participants' motivation. In OpenSesame there are lots of ways to provide feedback.

%--
toc:
 mindepth: 2
--%

## The difference between `feedback` and `sketchpad` items

To give provide you will generally use the `feedback` item, instead of the `sketchpad` item. These two items are quite similar, but are different in *when* stimulus preparation occurs. See also:

- [usage/prepare-run]

## Relevant variables

OpenSesame automatically keeps track of a number of feedback variables, which are described here:

- [usage/variables-and-conditional-statements#feedback-variables]

## Feedback after a block of trials

It is common to provide feedback after every block of trials. This way you don't overwhelm the participant with feedback on every trial, which may disrupt the flow of the experiment (although it may be useful in some cases). To do this, construct a `sequence` that contains a single block of trials (typically a `loop` item), followed by a `feedback` item. It is also convenient to add a `reset_feedback` item just before the *block_loop*. This prevents carry-over effects, for example, from responses that have been collected during the instructions.

%--
figure:
 id: FigFeedback
 source: FigFeedback.png
 caption: |
  Providing feedback after a block of trials using a `feedback` item.
--%

In the `feedback` item, you can add some text. You can use the variables described above using the `[variable name]` notation.

%--
figure:
 id: FigFeedbackVariables
 source: FigFeedbackVariables.png
 caption: |
  You can use a number of standard feedback variables, such as `avg_rt` and `acc`.
--%

You can also use an `inline_script` item, inserted immediately before the `feedback` item, to provide custom types of feedback. For example, if you want to provide a warning when accuracy drops below 75% you could insert the following inline_script before the feedback item.

%--
code:
 id: LstFeedback
 source: custom-feedback.py
 syntax: python
 caption: |
  Using an `inline_script` item to provide custom feedback.
--%

## Feedback after a single trial

Sometimes you want to give the participant feedback after every trial. It's probably wise to use subtle feedback in this case, so you don't disrupt the flow of the experiment. What I often do is briefly (500 ms, say) present a green or red fixation dot, depending on whether the participant responded correctly. The easiest way to do this is by adding both a red and a green fixation dot to the *trial_sequence*, and execute only one of them, depending on the value of the `correct` variable.

%--
figure:
 id: FigRunIf
 source: FigRunIf.png
 caption: |
  Providing feedback after each trial using `Run if` statements.
--%

In this case, you can use a `sketchpad` item, because you don't change the contents of the canvas depending on the participant's response. You only change which of the two `sketchpad`s, both of which have been constructed in advance, will be shown: *green_fixation* or *red_fixation*.

You can also present full feedback after every trial, using a `feedback` item inserted after the response item (such as a `keyboard_response`), as shown in [Figure 1].

## Resetting and manipulating feedback variables

Feedback variables, such as `average_response_time` and `accuracy` are reset when a `feedback` item is called (assuming that the *Reset feedback variables* box is checked) and wherever you insert a `reset_feedback` plug-in. However, you can also manipulate the feedback variables using an `inline_script`.

For example, the following script resets the feedback variables:

%--
code:
 id: LstReset
 source: reset-feedback.py
 syntax: python
 caption: |
  Resetting feedback with an `inline_script` item.
--%

And the following script updates the feedback variables based on a response:

%--
code:
 id: LstUpdate
 source: update-feedback.py
 syntax: python
 caption: Updating feedback with an `inline_script` item.
--%

[usage/prepare-run]: /usage/prepare-run
[usage/variables-and-conditional-statements#feedback-variables]: /usage/variables-and-conditional-statements#feedback-variables
