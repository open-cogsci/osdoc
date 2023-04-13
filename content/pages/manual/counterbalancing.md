title: Counterbalancing

Counterbalancing is a way to remove confounding factors from an experiment by having slightly different tasks for different groups of participants. This sounds abstract, so let's consider two examples.

[TOC]

### Example 1: Counterbalancing response rule

Consider a lexical-decision experiment in which participants classify words as verbs by pressing 'z' with their left hand, or as nouns by pressing 'm' with their right hand. This design has a problem: If you find that participants respond faster to nouns than to verbs, this could be because nouns are processed faster than verbs, or because participants respond faster with their right hand than with their left hand. You can fix this problem by counterbalancing the response rule.

For even participant numbers:

- verb → z
- noun → m

For uneven participant numbers:

- verb → m
- noun → z

### Example 2: Rotating stimulus conditions

Consider a masked-priming experiment in which participants read target words aloud. On each trial, the target word is preceded by one of three types of priming words:

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


### Using the subject number

When you run an experiment in OpenSesame on the desktop, you are asked for a subject number. When you run an experiment online, a subject number is randomly selected from the list of possible subject numbers that you have specified in the [OSWeb extension](%url:osweb). (This means that for online experiments you cannot ensure that the number of participants is exactly equal for the different conditions that you want to counterbalance, at least not if you rely on the subject number.)

This subject number is available as the experimental variable `subject_nr`. In  addition, the experimental variable `subject_parity` has the value 'odd' or 'even', depending on whether the subject number is odd or even. Now say that you want to counterbalance the response rule as in Example 1, you could add the following INLINE_SCRIPT to the start of the experiment.

```python
if subject_parity == 'odd':
    verb_response = 'z'
    noun_response = 'm'
else:
    verb_response = 'm'
    noun_response = 'z'
```

Or, when creating an OSWeb experiment, add the following INLINE_JAVASCRIPT to the start of the experiment:

```javascript
if (subject_parity === 'odd') {
    verb_response = 'z'
    noun_response = 'm'
} else {
    verb_response = 'm'
    noun_response = 'z'
}
```

Now, in your *block_loop*, instead of setting `correct_response` to a fixed value, you set it to a variable: `{verb_response}` or `{noun_response}`. You can take a look at the *lexical-decision task* example to see how this works (Menu -> Tools -> Example experiments).


### Using Batch Session Data (JATOS and OSWeb only)

When running an OSWeb experiment that is hosted on JATOS, you can make use of [Batch Session Data](https://www.jatos.org/jatos.js-Reference.html#functions-to-access-the-batch-session). This is data that is shared between all experimental sessions that are part of the same worker batch. Therefore, you can use this data to define a list of conditions that should be distributed across participants. At the start of each experimental session, one condition is removed from this list and used for the current session. This is the most sophisticated way to implement counterbalancing for OSWeb experiments that are hosted on JATOS.

You can download a template experiment here:

- %static:attachments/counterbalancing-osweb-jatos.osexp%

When running from JATOS, the experiment retrieves a single condition from the Batch Session Data (see below) and registers this as the experimental variable `condition`. When doing a test run, `condition` is set to a default value specified at the end of *init_condition*.

The experiment itself should be implemented in the *experiment* SEQUENCE, which in the template contains only the *show_condition* SKETCHPAD (see %FigCounterbalancingOSWebJATOS).

%--
figure:
    source: counterbalancing-osweb-jatos.png
    id: FigCounterbalancingOSWebJATOS
    caption: |
        The overview area of the template experiment for implementing counterbalancing with JATOS Batch Session Data.
--%

When importing the experiment into JATOS, all conditions should be specified in the Batch Session Data as the `pending` list (under Worker & Batch Manager; see %FigBatchSessionData). Each condition from `pending` corresponds to a single experimental session; therefore, if condition `a` should be used for two experimental sessions, then `a` needs to occur twice in the `pending` list. The conditions are used in the order in which they are defined.

%--
figure:
    source: batch-session-data.png
    id: FigBatchSessionData
    caption: |
        The conditions should be specified in the Batch Session Data in JATOS.
--%

At the start of an experimental session, a single condition is moved from `pending` to `started`. (When the `pending` list is empty, the participant is informed that he or she can no longer participate in the experiment.) At the end of the experimental session, the condition is appended to the `finished` list.

To make this more concrete, let's say that you've defined the Batch Session Data as shown in %FigBatchSessionData. Then, four experimental sessions are started, but the second experimental session, with condition `a`, never finishes, for example because the participant closes the browser halfway the experiment. The Batch Session Data will then look as in %FigBatchSessionAfter:

%--
figure:
    source: batch-session-data-after.png
    id: FigBatchSessionAfter
    caption: |
        The Batch Session Data after all conditions have been consumed. One session, with condition `a`, never finished.
--%

You can tell from the Batch Session Data that one experimental session started with condition `a` but never finished. To nevertheless collect an experimental session with this condition, you have to manually add a new `a` to the `pending` list and collect a new session.
