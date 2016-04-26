title: Counterbalancing

Counterbalancing is a way to remove confounding factors from an experiment by having slightly different tasks for different groups of participants. This sounds abstract, so let's consider two examples.

[TOC]

### Example 1: Counterbalancing response rule

Consider a lexical-decision experiment in which participants classify words as verbs by pressing 'z' with their left hand, or as nouns by pressing 'm' with their right hand. This design has a problem: If you find that participants respond faster to nouns than to verbs, this could be because nouns are processed faster than verbs, or because participants respond faster with their right than their left hand. You can fix this problem through counterbalancing the response rule.

For even participant numbers:

- verb -> z
- noun -> m

For uneven participant numbers:

- verb -> m
- noun -> z

### Example 2: Rotating stimulus conditions

Consider a masked-priming experiment in which participants read aloud target words. On each trial, the target word is preceded by one of three types of priming words:

- An unrelated prime, e.g. priming with 'berry' for target 'house'.
- An ortoghraphically related prime, e.g. priming with 'mouse' for target 'house'
- A semantically related prime, e.g. priming with 'garden' for target 'house'

To avoid repetition effects, you only want to show target words only once per participant. Therefore, you create three different sets of target words, one for each prime type. This is a between-word design, which has less statistical power than a within-word design, in which each target word occurs in each condition. (For the same reason that between-subject designs are less powerful than within-subject designs.)

You can use counterbalancing to change this experiment into a within-word design by 'rotating' the condition in which each word occurs between participants. We have three conditions, and we therefore have three groups of participants:

- Participants 1, 4, 7, etc.
    - Word A in condition 1
    - Word B in condition 2
    - Word C in condition 3
- Participants 2, 5, 8, etc.
    - Word A in condition 2
    - Word B in condition 3
    - Word C in condition 1
- Participants 3, 6, 9, etc.
    - Word A in condition 3
    - Word B in condition 1
    - Word C in condition 2

## Implementing counterbalancing

When you run an experiment in OpenSesame, you are asked for a subject number. This subject number is available as the experimental variable `subject_nr`. In  addition, the experimental variable `subject_parity` has the value 'odd' or 'even', depending on whether the subject number is odd or even. Now say that you want to counterbalance the response rule as in Example 1, you could add the following `inline_script` to the start of the experiment.

~~~ .python
if var.subject_parity == 'odd':
	var.verb_response = 'z'
	var.noun_response = 'm'
else:
	var.verb_response = 'm'
	var.noun_response = 'z'
~~~

Now, in your *block_loop*, instead of setting `correct_response` to a fixed value, you set it to a variable: `[verb_response]` or `[noun_response]`. You can take a look at the *lexical-decision task* example to see how this works (Menu -> Tools -> Example experiments).

## Counterbalancing Video tutorial

The video below illustrates both a simple counterbalancing example, for two block orders or conditions, and a more complex example, for three or more block orders or conditions.

%--
video:
 source: youtube
 id: VidScreencast
 videoid: zP8ucRtWU5g
 width: 640
 height: 360
 caption: |
  Video by <a href="http://www.chrislongmore.co.uk/">Chris Longmore</a>.
--%
