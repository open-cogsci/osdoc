# Stop signal task with coroutines

[TOC]

## About this tutorial

This tutorial shows how to create a stop-signal task in OpenSesame using the `coroutines` plugin. The experiment is based on the simple reaction-time version of Logan, Cowan, and Davis (1984). The goal of this tutorial is not only to build the task, but also to understand how coroutines allow several events to be placed on a single trial timeline.

This tutorial assumes that you are working with OpenSesame 4.1 or later and that you are running the experiment on the desktop. The `coroutines` plugin is used to present visual stimuli, collect responses, and schedule the stop signal within one shared timeline.

%--
figure:
 id: Fig_overview
 source: experiment_sequence.png
 caption: An overview of the stop-signal task that you will build in this tutorial.
--%

## The experiment

In this experiment, participants respond as quickly as possible to letters that appear on the screen. On most trials, they should press the spacebar when a letter appears. On some trials, a tone is played shortly after the letter appears, and participants should try to withhold their response.

The experiment uses four letters: `E`, `F`, `H`, and `L`. The response is always the same, regardless of which letter is shown. This makes the task a simple reaction-time version of the stop-signal paradigm.

Each trial has the following structure:

- A fixation dot is shown for 500 ms.
- A letter is shown 500 ms after trial onset.
- A response window opens when the letter appears.
- On stop trials, a 900-Hz tone is played after a short delay.
- A mask follows the letter.
- The total trial duration is fixed at 3500 ms.

The stop-signal delay is varied across stop trials. In this implementation, the delay can be 50, 100, 150, or 200 ms.

## What the task measures

The stop-signal task is commonly interpreted using the independent race model. According to this model, a go process and a stop process race against each other.

- If the go process finishes first, the participant responds.
- If the stop process finishes first, the participant successfully inhibits the response.

This task is often used to estimate stop-signal reaction time (SSRT), which is an index of inhibitory control.

Experiments like this generally show two typical findings:

- Participants are less likely to inhibit their response when the stop-signal delay is long than when it is short.
- Responses on go trials are often faster and less variable in the simple reaction-time version than in choice versions of the task.

In addition, participants may sometimes strategically slow down if they expect a stop signal. For this reason, the instructions should emphasize that they should respond quickly and should not wait for the tone.

## Experimental design

This design:

- is within-subject, because all participants complete all trial types
- contains two main trial types:
  - go trials
  - stop trials
- includes four stop-signal delays on stop trials:
  - 50 ms
  - 100 ms
  - 150 ms
  - 200 ms
- includes four letters:
  - `E`
  - `F`
  - `H`
  - `L`

In the implementation used here, the trial table contains 80 rows:

- 64 go trials
- 16 stop trials

The 16 stop trials are distributed equally across the four delays and four letters. The 64 go trials are also distributed equally across the four letters. The loop is repeated four times, which results in four blocks of 80 trials.

%--
figure:
 id: Fig_loop
 source: table_loop.png
 caption: The composition of one block: 64 go trials and 16 stop trials, with stop trials distributed across four stop-signal delays.
--%

## Step 1: Create the basic structure of the experiment

Start OpenSesame and create a new experiment. In this tutorial, the experiment consists of a short sequence of items:

- a consent form
- an instruction screen
- a loop that contains the trials

In the example experiment, the main sequence is called `experiment`, and it runs the following items:

- `new_form_consent`
- `instructions`
- `simple_rt`

The `simple_rt` item is a loop that contains one coroutine item. This coroutine defines the timeline of each trial.

## Step 2: Add a consent form and instruction screen

The example experiment begins with a consent form. This is optional from a technical point of view, but in many real experiments it is useful or necessary to ask participants for informed consent before the task begins.

After the consent form, participants see instructions. In this experiment, the instructions explain three important points:

- participants should press the spacebar whenever a letter appears
- on some trials they will hear a tone
- if they hear the tone, they should try to stop themselves from responding

The instructions also emphasize that participants should not wait for the tone before responding.

## Step 3: Create the trial loop

The trial structure is defined in the loop called `simple_rt`. This loop contains 80 rows and is repeated four times. The order of trials is randomized within each repetition.

Each row defines at least the following variables:

- `letters`
- `is_stop`
- `delay`
- `correct_response`

These variables determine what happens on a given trial.

For go trials:

- `is_stop` is `no`
- `delay` is `0`
- `correct_response` is `space`

For stop trials:

- `is_stop` is `yes`
- `delay` is one of `50`, `100`, `150`, or `200`
- `correct_response` is `None`

This is an elegant way to use the built-in scoring of the `keyboard_response` item. On go trials, pressing space is correct. On stop trials, withholding the response is correct because the correct response is defined as `None`.

## Step 4: Create the trial items

The coroutine uses several items that should be created separately first.

Before creating the individual items, it is important to understand how duration works in a coroutine. Normally, an item such as a sketchpad or keyboard response has its own duration or timeout setting. In a standard sequence, that setting helps determine when the experiment moves on to the next item. In a coroutine, however, the overall timing is controlled by the coroutine itself.

This means that when you create items for use inside a coroutine, you should think of their own duration settings as secondary. The most important timing information will later be defined by the `start` and `end` values inside the coroutine item.

For example:

- a sketchpad may still have a duration field in its own editor, but inside a coroutine the moment at which it appears is determined by the coroutine
- a keyboard response item may still have a timeout field, but inside a coroutine the effective response window is mainly determined by when the item starts and ends on the coroutine timeline
- a synth item may have its own sound properties, such as tone length, but the moment at which the sound is triggered is determined by the coroutine

Therefore, when creating the items below, it is fine to give them simple default duration settings, but you should not think of those settings as the main source of timing control. The coroutine will provide the actual trial timing.

### 4.1 Fixation

Create a sketchpad called `fixation` and draw a central fixation dot on it.

Because this sketchpad will be shown inside a coroutine, its own duration setting is not what determines when fixation appears on the trial timeline. What matters is that the sketchpad exists and can be called by the coroutine at the appropriate moment.

### 4.2 Letter display

Create a sketchpad called `letter`. Add a text element that shows the value of the variable `letters`, so that the displayed letter changes from trial to trial.

Again, the important point is not the duration field inside the sketchpad editor, but the fact that the coroutine will schedule this item to appear 500 ms after trial onset.

### 4.3 Mask

Create a sketchpad called `mask`. In the current experiment this sketchpad is empty, so it functions mainly as a placeholder that occupies part of the timeline after the letter. You can later replace it with an actual mask if you want.

As with the other sketchpads, the mask is positioned in time by the coroutine, not by its own duration field.

### 4.4 Response item

Create a keyboard response item called `resp_simple_rt`. Set the allowed response to `space`.

In a standard sequence, a keyboard response item would use its own timeout setting to determine how long it waits for a response. In a coroutine, however, the response item becomes active when the coroutine starts it, and its effective timing is governed primarily by the coroutine timeline.

In the example experiment, this item starts when the letter appears and remains active during the response window. On go trials, `space` is the correct response. On stop trials, the correct response is `None`, which means that withholding the response is scored as correct.

### 4.5 Stop signal

Create a synth item called `stop_signal`. Set:

- waveform to `sine`
- frequency to `900`
- length to `500`
- duration to `0`

The tone will be used only on stop trials.

Here it is especially useful to distinguish between two kinds of duration. The `length` of the synth determines how long the sound itself lasts. The `duration` setting determines whether OpenSesame waits for the sound item before continuing. By setting `duration` to `0`, the coroutine can continue immediately after triggering the tone, while the 500-ms sound keeps playing.

### 4.6 Logger

Create a logger item called `logger`. In the example experiment, automatic logging is turned off and the following variables are logged manually:

- `acc`
- `avg_rt`
- `correct`
- `correct_response`
- `delay`
- `is_stop`
- `letters`
- `response`
- `response_time`

Because stop-signal delay is critical for later analysis, it is important to include `delay` in the log.

## Step 5: Add the coroutine item

Now create a `coroutines` item called `coroutines`. This is the core of the experiment.

Set the total coroutine duration to `3500`. Then add the trial items to the coroutine so that each item is placed at the correct moment in the shared timeline.

In the example experiment, the coroutine runs:

- `fixation`
- `letter`
- `mask`
- `stop_signal`
- `resp_simple_rt`
- `logger`

At this stage, it is useful to keep in mind that coroutines do not support every OpenSesame item. Only some items can be placed inside a coroutine. Supported items include at least:

- `feedback`
- `inline_script`
- `keyboard_response`
- `logger`
- `mouse_response`
- `sampler`
- `synth`
- `sketchpad`

If an item does not support coroutines, it cannot be placed on the shared coroutine timeline.

It is also important to keep in mind that, once an item is placed inside a coroutine, the timing is primarily controlled by the coroutine itself. In other words, the `start` and `end` values inside the coroutine are what determine when the item is active on the trial timeline.

## Step 6: Configure the coroutines item

The core of this experiment is the `coroutines` item. Coroutines allow multiple items to run on a shared trial timeline, so that events can overlap in time instead of being presented strictly one after another. This is useful for the stop-signal task, because the participant can respond to the letter while the stop signal is scheduled independently at a variable delay.

In this experiment, the coroutine has a total duration of 3500 ms. Within this time window, several items are started at different moments.

### 6.1 Why coroutines are useful here

In a stop-signal task, the visual stimulus, the response window, and the stop tone are closely related in time, but they do not all start and end together. The fixation dot appears first, the letter appears later, the response window opens when the letter appears, and the stop tone is presented only on some trials and only after a variable delay.

A sequence item is not well suited for this kind of temporal overlap, because it presents items one after another. A coroutine is more appropriate, because it allows you to define a single trial timeline and place each event at the right moment on that timeline.

### 6.2 Which items run in parallel

The `coroutines` item in this experiment runs the following items:

- `fixation`
- `letter`
- `mask`
- `stop_signal`
- `resp_simple_rt`
- `logger`

These items do not all begin together. Instead, each item has its own start and end point within the 3500-ms coroutine. Because the items are coordinated by the same coroutine, they can overlap in time and together define a single trial.

### 6.3 How `start`, `end`, and `runif` work

Each line in the coroutine specifies when an item should run.

- `start` indicates when the item begins, in milliseconds after the start of the coroutine.
- `end` indicates when the item is stopped.
- `runif` indicates whether the item should run at all.

For example, the line for the letter item starts it at 500 ms. This means that the letter appears 500 ms after the beginning of the trial. The response item also starts at 500 ms, so response collection begins when the letter appears.

The stop signal includes a `runif` expression:

`is_stop == "yes"`

This means that the stop tone is only presented on stop trials. On go trials, the stop signal item is skipped.

### 6.4 Which items use an end time

Not every item in a coroutine has a meaningful end time. Some items are one-shot items. A sketchpad, for example, shows a display and then terminates immediately. For such items, the start time determines when the item is shown, but the end time does not play the same role as it does for items that remain active over an interval.

By contrast, response items and sound items can remain active over part of the coroutine timeline. For such items, the start and end settings determine during which part of the coroutine they are active.

### 6.5 How item duration relates to coroutine timing

When an item is placed inside a coroutine, the timing is controlled by the coroutine itself. This means that the start and end times defined in the coroutine generally take precedence over the duration or timeout settings inside the item.

For example, a `keyboard_response` item may have its own timeout or duration setting in the item editor, but when it is used inside a coroutine, the effective response window is determined by the coroutine timeline.

Similarly, the `stop_signal` synth has its own sound settings, but the moment at which it starts is defined by the coroutine.

For this reason, when working with coroutines, it is better to think of the coroutine as the structure that controls when items are active.

### 6.6 How the stop signal is scheduled

The stop signal is defined like this:

`start="{delay + 500}"`

The value of `delay` comes from the loop table and can be 50, 100, 150, or 200 on stop trials. Because the letter appears at 500 ms, the stop signal is scheduled relative to letter onset, not relative to the beginning of the whole trial.

This means that:

- if `delay = 50`, the tone starts 50 ms after the letter appears
- if `delay = 100`, the tone starts 100 ms after the letter appears
- if `delay = 150`, the tone starts 150 ms after the letter appears
- if `delay = 200`, the tone starts 200 ms after the letter appears

This is the critical timing manipulation in the stop-signal task.

### 6.7 Why the synth uses `duration = 0`

The `stop_signal` item is a `synth` with a tone length of 500 ms and a `duration` of `0`. This is important.

A `duration` of `0` means that OpenSesame starts the sound and then immediately continues with the coroutine timeline, instead of waiting for the synth item to finish. As a result, the tone can continue to play in the background while other parts of the coroutine are still active.

This is exactly what is needed here. The stop signal should begin at a precise moment after letter onset, but it should not pause the rest of the trial. The participant must still be able to respond, and the trial should continue until the overall coroutine duration has elapsed.

### 6.8 The resulting trial timeline

The trial timeline is therefore as follows:

- `fixation` starts at 0 ms
- `letter` starts at 500 ms
- `resp_simple_rt` starts at 500 ms
- `mask` starts at 1000 ms
- `stop_signal` starts at `delay + 500` ms on stop trials only
- `logger` runs at the end of the trial
- the coroutine ends at 3500 ms

This arrangement makes the coroutine item the temporal backbone of the task.

%--
figure:
 id: Fig_coroutines
 source: coroutines.png
 caption: A schematic overview of the trial timeline inside the coroutine.
--%

## Step 7: Test the experiment

When the structure is in place, give the experiment a test run. During testing, check the following points carefully:

- the fixation dot appears first
- the letter appears 500 ms after trial onset
- the response window opens with letter onset
- the stop tone is only played on stop trials
- the stop tone starts at the correct delay after letter onset
- the trial always lasts 3500 ms

It is also useful to inspect the log file to verify that the variables `letters`, `is_stop`, `delay`, `response`, `response_time`, and `correct` are stored correctly.

## Finished

Congratulations, the experiment is complete. You can now give it a test run by pressing the blue double-arrow button (shortcut: `Ctrl+W`).

A finished block should show the following features:

- the consent form appears before the task starts
- the instructions explain both go and stop trials
- each trial begins with fixation
- the letter appears after 500 ms
- the stop tone is presented only on stop trials
- the timing of the stop tone depends on the value of `delay`
- the log file contains the critical variables for later analysis

Below is a demonstration of the working experiment. For the purpose of this recording, a shorter demonstration version of the trial loop was used so that the full behavior of the task could be shown in a compact video.

%--
video:
 source: STOP_tutorial.mp4
 caption: Demonstration of a completed stop-signal task block.
--%

## References

Logan, G. D., Cowan, W. B., & Davis, K. A. (1984). On the ability to inhibit simple and choice reaction time responses: A model and a method. *Journal of Experimental Psychology: Human Perception and Performance*, *10*(2), 276–291.

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324.