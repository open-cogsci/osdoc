---
layout: osdoc
title: NeuroSpin 2015
group: General
parser: academicmarkdown
menuclass: external
permalink: /neurospin2015/
ext_url: /neurospin2015
author: Sebastiaan Mathôt
---

This tutorial is part of an OpenSesame workshop that will take place at the Cognitive Neuroimaging Unit in the NeuroSpin center on January 13 2015, 9:30.

%--
figure:
 id: FigNeurospin
 source: FigNeuroSpin.png
 caption: |
  The NeuroSpin institute in the south of Paris.
--%

## Overview

%--
toc:
 mindepth: 2
 maxdepth: 2
 exclude: [Overview]
--%

## Requirements

### Expertise

This is a medium-level tutorial that assumes a basic knowledge of experimental design, programming, and OpenSesame. If you're not familiar with OpenSesame, it will be helpful (but not strictly required) to follow the introductory [step-by-step tutorial] first.

### Software and equipment

- This tutorial assumes OpenSesame 2.9.0 or higher.
- If you bring your own laptop, please install OpenSesame before the workshop.
- OpenSesame is available for Windows XP/ 7/ 8, Linux, and Mac OS. If you are running Mac OS, you are advised to verify beforehand that OpenSesame runs properly on your system, because Mac OS support is still experimental.

### Materials

- The primary resource for the workshop is this page, which can be downloaded in `.pdf` format from [here][pdf]. Print-outs will be available for attendees.

## Introduction

You can download the introduction slides from [here][slides].

## About

In this tutorial, we will implement an attentional-blink paradigm, as introduced by [Raymond, Shapiro, and Arnell (1992)](#references). We will re-create experiment 2 from Raymond et al. almost exactly, with only a few minor modifications. In this experiment, the participant sees a stream of letters, typically called an RSVP stream (for Rapid Serial Visual Presentation). There are two conditions. In the *experimental* condition, the participant's task is twofold:

- Report the identity of the white letter (all other letters were black).
- Indicate whether an 'X' was present.

In the control condition, the participant's task is only to ...

- Indicate whether an 'X' was present.

The white letter is called the *T1* (or 'target'). The 'X' is called the *T2* (or 'probe'). The typical finding is that the T2 is often missed when it is presented 200 - 500 ms after T1, but only when T1 needs to be reported. This phenomenon is called the *attentional blink*, because it is as though your mind's eye briefly blinks after seeing T1. But surprisingly, T2 is usually not missed when it follows T1 immediately. This is called *lag-1 sparing*. The results of Raymond et al. (1992) looked like this:

%--
figure:
 id: FigResults
 source: FigResults.svg
 caption: |
  T2 accuracy as a function of the serial position of T2 relative to T1 ('lag'). A lag of 0 means that T1 and T2 where identical (i.e. a white 'X'). Adapted from Raymond et al. (1992).
--%

## Step 1: Download and start OpenSesame

OpenSesame is available for Windows, Linux, Mac OS (experimental), and Android (runtime only). This tutorial is written for OpenSesame 2.9.0 or later. You can download OpenSesame from here:

- <http://osdoc.cogsci.nl/>

When you start OpenSesame, you will be given a choice of template experiments, and a list of recently opened experiments (%FigStartup).

%--
figure:
 id: FigStartup
 source: FigStartup.png
 caption: |
  The OpenSesame window on start-up.
--%

## Step 2: Choose template, font, and colors

The 'Extended template' provides the basic structure of a typical trial-based experiment with a practice and experimental phase. Because our experiment fits this template very well, we're going to use it. Therefore, double-click on 'Extended template' to open it.

In the 'General tab' that now appears, you can specify the general properties of your experiment. For this experiment, we want to use black letters on a gray background. Also, the default font size of 18 is a bit small, so change that to 32. Finally, it's good practice to give your experiment an informative name and description. Your 'General tab' now looks as in %FigGeneralTab.

%--
figure:
 id: FigGeneralTab
 source: FigGeneralTab.png
 caption: |
  The General tab is where you define the general properties of your experiment.
--%

## Step 3: Implement counterbalancing

In Raymond et al. (1992), the experimental and control conditions were mixed between blocks: Participants first did a full block in one condition, and then a full block in the other condition. Condition order was counterbalanced, so that half the participants started with the experimental condition, and the other half started with the control condition.

Let's start with the counterbalancing part, and use the participant number to decide which condition is tested first. We need to do this as the very first thing of the experiment, and we need to use some Python scripting to do it.

Therefore, drag an `inline_script` from the item toolbar onto the very top of the experiment. Change the name of the new item to *counterbalance*. In the *Prepare* phase of the *counterbalance* item, enter the following script:

~~~ .python
if self.get('subject_parity') == 'even':
    exp.set('condition1', 'experimental')
    exp.set('condition2', 'control')
else:
    exp.set('condition1', 'control')
    exp.set('condition2', 'experimental')
~~~

Ok, let's take a moment to understand what's going on here.

The first thing to know is that `self.get()` retrieves experimental variables. These include variables that you have defined yourself, for example in a `loop` item, as well as built-in variables. One such built-in experimental variable is `subject_parity`, which is automatically set to 'even' when the experiment is launched with an even subject number (0, 2, 4, etc.), and to 'odd' when the subject number is odd (1, 3, 5, etc.).

The second thing to know is that `exp.set()` sets experimental variables. That is, it makes variables available elsewhere in OpenSesame, outside of `inline_script` items. So this line:

~~~ .python
exp.set('condition1', 'experimental')
~~~

... creates an experimental variable with the name `condition1`, and gives it the value 'experimental'. In step 4, we will use this variable to determine which condition is tested first.

In other words, this script says the following:

- All even-numbered subjects start with the experimental condition.
- All odd-subjects start with the control condition.

<div class='info-box' markdown='1'>

### Links

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)
- [/miscellaneous/counterbalancing/](/miscellaneous/counterbalancing/)

</div>

## Step 4: Define experimental variables that are varied between blocks

As mentioned above, conditions are varied between blocks. To understand how this works in OpenSesame, it's best to start at the bottom (see %FigStructure), with ...

- the *trial_sequence*, which corresponds (as you might expect) to a single trial. One level above ...
- the *block_loop* corresponds to a single block of trials. Therefore, this is where you would define experimental variables that are varied within a block. One level above ...
- the *block_sequence* corresponds to a single block of trials plus the events that happen before and after every block, such as post-block feedback on accuracy, and pre-block instructions. One level above ...
- the *practice_loop* and *experimental_loop* correspond to multiple blocks of trials during respectively the practice and non-practice (experimental) phase. Therefore, this is where you would define experimental variables that are varied between blocks.

In other words, we need to define our between-block manipulations near the top of the experimental hierarchy, in the *practice_loop* and *experimental_loop*.

%--
figure:
 id: FigStructure
 source: FigStructure.png
 caption: |
  A fragment of the experimental structure as shown in the overview area.
--%

Click on *practice_loop* to open the item. Right now, there is only one variable, `practice`, which has the value 'yes' during one cycle (i.e. one block).

Let's get to work! Add a variable called `condition`, change the number of cycles to 2, and change the order to 'sequential'.
Now use the previously created variables `condition1` and `condition2` to determine which condition is executed first, and which second (see %FigPracticeLoop). To indicate that something is the name of a variable, and not a literal value, put square brackets around the variable name: '[my_variable]'

%--
figure:
 id: FigPracticeLoop
 source: FigPracticeLoop.png
 caption: |
  The *practice_loop* item after Step 4.
--%

Do the same thing for *experimental_loop*, except that the variable `practice` has the value 'no'. (The `practice` variable doesn't have a real function. It only allows you to easily filter out all practice trials during data analysis.)

<div class='info-box' markdown='1'>

### Links

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)
- [/miscellaneous/counterbalancing/](/miscellaneous/counterbalancing/)

</div>

## Step 5: Create instructions

Because the task differs between blocks, we need to show an instruction screen before each block. The *block_sequence* is the place to do this, because, as explained above, it corresponds to a single block of trials plus the events that occur before and after every block.

There are various items that we could use for an instruction screen, but we will use the `sketchpad`. Insert two new `sketchpad`s at the top of *block_sequence* by dragging them from the item toolbar. Rename the `sketchpad`s to *instructions_experimental* and *instructions_control*. Click on both items to add some instructional text, such as shown in %FigInstructions.

%--
figure:
 id: FigInstructions
 source: FigInstructions.png
 caption: |
  An example of instructional text in the *instructions_experimental* item.
--%

Right now both instruction screens are shown before every block, which is not what we want. Instead, we want to show only the *instructions_experimental* item in the experimental condition, and only the *instructions_control* item in the control condition. We can do this with conditional ('run if') statements.

Click on *block_sequence* to open it. You will see a list of item names, just as in the overview area, except that each item has the text 'always' next to it. These are run-if statements, and they determine the conditions under which an item is executed. Double click on the run-if statement next to *instructions_experimental* and add the following text:

~~~
[condition] = experimental
~~~

This means that *instructions_experimental* will only be executed when the variable `condition` has the value 'experimental.' Analogously, change the run-if statement for *instructions_control* to:

~~~
[condition] = control
~~~

Your *block_sequence* should now look as in %FigBlockSequence.

%--
figure:
 id: FigBlockSequence
 source: FigBlockSequence.png
 caption: |
  The *block_sequence* item at the end of Step 5.
--%

<div class='info-box' markdown='1'>

### Links

- [/usage/sequences-and-loops/](/usage/sequences-and-loops/)
- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)
- [/usage/text/](/usage/text/)

</div>

## Step 6: Modify feedback

Open *feedback*. By default, in the Extended Template, the participant receives feedback on speed (`avg_rt`) and accuracy (`acc`) after each experimental block. However, our experiment doesn't require speeded responses, and we should therefore only provide feedback on accuracy. Modify the *feedback* item to look something like %FigFeedback.

%--
figure:
 id: FigFeedback
 source: FigFeedback.png
 caption: |
  The *block_sequence* item at the end of Step 6.
--%

<div class='info-box' markdown='1'>

### Links

- [/usage/feedback/](/usage/feedback/)
- [/usage/text/](/usage/text/)

</div>

## Step 7: Define experimental variables that are varied within a block

Raymond et al. (1992) the position of T2 relative to T1 from 0 to 8, where 0 means that one letter is both T1 and T2 (i.e. a white 'X'). They also have trials in which there is no T2. This is all varied within a block. There are various ways to code this, but the easiest way is to use two variables:

- `lag` indicates the position of T2 relative to T1. It has a value of 0 - 8, or no value if there is no T2.
- `T2_present` is 'y' for trials on which there is a T2 and 'n' for trials on which there is no T2. Of course, this is redundant, because `T2_present` is 'y' on all trials on which `lag` has a value. But it's convenient to define `T2_present`, because we can use it later on to specify the correct T2 response.

Click on *block_loop* and create a variable table as shown in %FigBlockLoop.

%--
figure:
 id: FigBlockLoop
 source: FigBlockLoop.png
 caption: |
  The *block_loop* item after Step 7.
--%

<div class='info-box' markdown='1'>

### Links

- [/usage/sequences-and-loops/](/usage/sequences-and-loops/)
- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)

</div>

## Step 8: Define trial sequence

We will use an `inline_script` item to do most of the heavy lifting, and therefore our *trial_sequence* is quite simple. It consists of:

1. A `sketchpad` (called *fixation*) to show a fixation dot.
2. An `inline_script` (called *RSVP*) item that implements the RSVP stream.
3. A `sketchpad` (called *ask_T1*) that asks the participant to report T1.
4. A `keyboard_response` (called *response_T1*) that collects the T1 report.
5. A `sketchpad` (called *ask_T2*) that asks the participant to report T2.
6. A `keyboard_response` (called *response_T2*) that collects the T2 report.
7. A `logger` (called *logger*) that writes all the data to a log file.

Drag all the required items from the item toolbar into *trial_sequence*, re-order them if necessary, and give them informative names. Also, use run-if statements to collect a T1 response only in the experimental condition. Your trial sequence should now look like %FigTrialSequence.

%--
figure:
 id: FigTrialSequence
 source: FigTrialSequence.png
 caption: |
  The *trial_sequence* item after Step 6.
--%

<div class='info-box' markdown='1'>

### Links

- [/usage/sequences-and-loops/](/usage/sequences-and-loops/)
- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)

</div>

## Step 9: Create RSVP stream (prepare phase)

Now we're getting to the fun-but-tricky part: implementing the RSVP stream. Click on *RSVP* to open the item. You see two tabs: *Prepare* and *Run*. The golden rule is to add all code related to stimulus preparation to the *Prepare* tab, and all code related to stimulus presentation to the *Run* tab. Let's start with the preparatory stuff, so switch to the *Prepare* tab.

First, we need to import all Python modules that we plan to use:

~~~ .python
import random
import string
from openexp.canvas import canvas
~~~

Here, `random` and `string` are part of the Python standard library. `openexp.canvas.canvas` is part of OpenSesame: It's a class for presenting visual stimuli.

Next, we need to define several variables that determine the details of the RSVP stream: (Note that, like before, we use `self.get()` to retrieve experimental variables that have been defined in a `loop`.)

~~~ .python
# Is T2 present?
T2_present = self.get('T2_present')
# The position of T2 relative to T1
lag = self.get('lag')
# The color of T1
T1_color = 'white'
# The presentation time of each stimulus
# (rounded up to nearest value compatible with refresh rate)
letter_dur = 10
# The inter-stimulus interval
# (rounded up to nearest value compatible with refresh rate)
isi = 70
~~~

Next, we are going to create the letter stream. Raymond et al. have a few rules:

- The number of letters that precede T1 is randomly selected between 7 and 15.
- The number of letters that follow T1 is always 8.
- Letters are randomly sampled without replacement from all uppercase letters except 'X' (which is used for T2).

Let's translate these rules to Python:

~~~ .python
# The position of T1 is random between 7 and 15. Note that the first position is
# 0, so the position indicates the number of preceding stimuli.
T1_pos = random.randint(7, 15)
# The maximum lag, i.e. the number of letters that follow T1.
max_lag = 8
# The length of the stream is the position of T1 + the maximum lag + 1. We need
# to add 1, because we count starting at 0, so the length of a list is always
# 1 larger than its maximum index.
stream_len = T1_pos + max_lag + 1
# We take all uppercase letters, which have been predefined in the `string`
# module. Converting to a `list` creates a list of characters.
letters = list(string.ascii_uppercase)
# We remove 'X' from this list.
letters.remove('X')
# Randomly sample a `stream_len` number of letters
stim_list = random.sample(letters, stream_len)
~~~

Ok, `stim_list` now contains all letters that make up our RSVP stream on a given trial, except for the T2 (if present). Therefore, on T2-present trials, we need to replace the letter at the T2 position by an 'X'.

~~~ .python
if T2_present == 'y':
    T2_pos = T1_pos + lag
    stim_list[T2_pos] = 'X'
~~~

We now have a variable called `stim_list` that specifies the letters in our RSVP stream. This is a `list` that might contain something like: `['M', 'F', 'O', 'P', 'S', 'R', 'Y', 'C', 'U', 'Z', 'G', 'A', 'T', 'E', 'H', 'J', 'V', 'N', 'B', 'K', 'X', 'Q']`

The next step is to create a `list` of `canvas` objects, each of which contains a single letter from `stim_list`. A `canvas` object corresponds to a static visual stimulus display, i.e. to one frame in our RSVP stream.

~~~ .python
# Create an empty list for the canvas objects.
letter_canvas_list = []
# Loop through all letters in `stim_list`. `enumerate()` is a convenient
# function that automatically returns (index, item) tuples. In our case, the
# index (`i`) reflects the position in the RSVP stream. This Python trick, in
# which you assign a single value to two variables, is called tuple unpacking.
for i, stim in enumerate(stim_list):
    # Create a `canvas` object.
    letter_canvas = canvas(exp)
    # If we are at the position of T1, we change the foreground color, because
    # T1 is white, while the default color (specified in the General tab) is
    # black.
    if i == T1_pos:
        letter_canvas.set_fgcolor(T1_color)
    # Draw the letter!
    letter_canvas.text(stim)
    # And add the canvas to the list.
    letter_canvas_list.append(letter_canvas)
~~~

We also need to create a blank `canvas` to show during the inter-stimulus interval:

~~~ .python
blank_canvas = canvas(exp)
~~~

Finally, we use `exp.set()` to set the position and identity of T1 as experimental variables, because they have been randomly determined in the scriipt. By setting these variables we can use them elsewhere in OpenSesame, such as for logging or to specify the correct T1 response.

~~~ .python
exp.set('T1_pos', T1_pos)
# Extract T1 from the list
T1 = stim_list[T1_pos]
exp.set('T1', T1)
~~~

Preparation done!

<div class='info-box' markdown='1'>

### Links

- [/python/about/](/python/about/)
- [/python/canvas/](/python/canvas/)
- <https://docs.python.org/2/library/random.html>
- <https://docs.python.org/2/library/string.html>
- <https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences>

</div>

## Step 10: Execute RSVP stream (run phase)

Now, let's switch to the *Run* tab of the `RSVP` item. Here we add the code that is necessary to show all the `canvas` objects that we have created during the *Prepare* phase. And that's not so hard! All we need to do is:

- For each letter canvas in the letter-canvas list
    - Show the letter canvas
    - Wait for `letter_dur` milliseconds
    - Show the blank canvas
    - Wait for `isi` milliseconds

This translates almost directly into Python:

~~~ .python
for letter_canvas in letter_canvas_list:
    letter_canvas.show()
    self.sleep(letter_dur)
    blank_canvas.show()
    self.sleep(isi)
~~~

Done!

<div class='info-box' markdown='1'>

### Links

- [/python/about/](/python/about/)
- [/python/canvas/](/python/canvas/)

</div>

## Step 11: Create fixation point

After all this coding, it's time to get back to something simpler: Defining the fixation point. Click on *fixation* in to open the item. Change the duration to 995. This value will be rounded up to the nearest value compatible with your monitors refresh rate, which is 1000 ms for most common refresh rates. Draw a fixation dot in the center, using the fixation-dot tool (the dot with the little hole in it).

%--
figure:
 id: FigFixation
 source: FigFixation.png
 caption: |
  The *fixation* `sketchpad` after Step 11.
--%

## Step 12: Define response collection

We will collect responses as follows:

- Ask for T1
- Collect a response, which is a single key press that corresponds to T1. So if T1 was 'A', the participant should press the 'a' key.
- Ask for T2
- Collect a response, which is 'y' when T2 was present and 'n' when T1 was absent.

We will use the *ask_T1* `sketchpad` to ask the participant for T1. Click on *ask_T1* to open the item, and add a line of text, such as 'Please type the white letter'. Change the duration to 0. This 0 ms duration does not mean that the text is only shown for 0 ms, but that the experiment moves immediately to the next item, which is *response_T1*.

Open *response_T1*. The only thing that we have to do is define the correct response. To do this, we can use the `T1` experimental variable that we have set while preparing the RSVP stream. Therefore, enter '[T1]' in the 'Correct response' field.

Open *ask_T2*, and add a line of text, such as 'Did you see an X? (y/n)'. Again, set the duration to 0, so that the experiment moves immediately to the next item, which is *response_T2*.

Open *response_T2*. Again, we need to define the correct response, this time using the variable `T2_present`, which we had defined in the *block_loop*. Therefore, add '[T2_present]' to the 'Correct response' field. It's also useful to restrict the allowed responses to 'y' and 'n', so that participants don't accidentally press the wrong key. You can do this by entering a semicolon-separated list of keys in the 'Allowed responses' field (i.e. 'y;n').

So how will the responses be logged? Each response item sets `response`, `correct`, and `response_time` variables. In addition, to distinguish responses set by different items, each response item sets these same variables followed by `_[item name]`. In other words, in this experiment the response variables of interests would be `correct_T1_response` and `correct_T2_response`.

<div class='info-box' markdown='1'>

### Links

- [/usage/collecting-responses/](/usage/collecting-responses/)
- [/usage/text/](/usage/text/)

</div>

## Step 13: Specify number and length of blocks

You now have a fully working experiment, but one thing still needs to be done: Setting the length and number of blocks. We will use the following structure:

- 1 practice block of 9 trials in each conditon.
- 5 experimental blocks of 36 trials in each condition.

First, open *block_loop*. The 'Repeat' value is currently set to 1, which means that each trial is executed once, giving a block length of 18 trials. We want to specify the 'Repeat' value with a variable, so that we can have a different value for the practice and experimental blocks. To do this, we need to make a small modification to the script of *block_loop*. Click on the 'View' button in top-right of the tab (the middle of the three buttons), and select 'View script'. This will hide the graphical controls, and show the underlying OpenSesame script. Now change this line ...

~~~
set repeat "1"
~~~

... to ...

~~~
set repeat "[block_repeat]"
~~~

... and click 'Apply and close'. This means that the variable `repeat` is now defined in terms of another variable, `block_repeat`. OpenSesame will tell you that it doesn't know the length of the block anymore (see %FigVariableLoop), but that's ok: As long as the variable `block_repeat` is defined, things will work fine.

%--
figure:
 id: FigVariableLoop
 source: FigVariableLoop.png
 caption: |
  If the length of a `loop` is variably defined, OpenSesame notifies you of this.
--%

Now open *practice_loop*. Add a variable `block_repeat` and give it the value 0.5. This means that 0.5 x 18 = 9 cycles of *block_loop* will be executed, just as we want.

Now open *experimental_loop*. Again, add a variable `block_repeat` and give it the value 2. This means that each block has a length of 2 x 18 = 36 trials. Also, change the number of cycles to 10, and arrange the loop table so that you first have five blocks of `condition1`, followed by five blocks of `condition2` (see %FigExperimentalLoop).

%--
figure:
 id: FigExperimentalLoop
 source: FigExperimentalLoop.png
 caption: |
  If the length of a `loop` is variably defined, OpenSesame notifies you of this.
--%

<div class='info-box' markdown='1'>

### Links

- [/usage/opensesame-script/](/usage/opensesame-script/)

</div>

## Step 14: Run experiment!

That's it. You can now run the experiment!

%--
figure:
 id: FigDone
 source: FigDone.svg
 caption: Yes, you did!
--%

## Extra 1: Check timing (and learn some NumPy)

In time-critical experiments, you should always verify whether the timing is as intended. When using `canvas` objects, you can make use of the fact that the `canvas.show()` method returns the timestamp of the display onset. Therefore, as a first step, we maintain two lists: one to keep track of the letter-canvas onsets, and one to keep track of the blank-canvas onsets.

To do this, we need a small modification to the script in the *Run* tab of the *RSVP* item:

~~~ .python
l_letter_time = []
l_blank_time = []
for letter_canvas in letter_canvas_list:
    t1 = letter_canvas.show()
    l_letter_time.append(t1)
    self.sleep(letter_dur)
    t2 = blank_canvas.show()
    l_blank_time.append(t2)
    self.sleep(isi)
~~~

We now have two `list`s with timestamps: `l_letter_time` and `l_blank_time` From these, we want to determine the average presentation duration of a letter, the average duration of a blank, and the standard deviation for both averages. But because `list`s are not great for these kinds of numerical computations, we are going to convert them to another kind of object: a `numpy.array`.

~~~ .python
import numpy
a_letter_time = numpy.array(l_letter_time)
a_blank_time = numpy.array(l_blank_time)
~~~

Now we can easily create an array that contains the presentation duration for each letter:

~~~ .python
a_letter_dur = a_blank_time - a_letter_time
~~~

This creates a new array, `a_letter_dur`, in which each item is the result of subtracting the corresponding item in `a_letter_time` from the corresponding item in `a_blank_time`. Schematically:

    a_letter_dur    ->  [  1,  1,  1 ]
    =
    a_blank_time    ->  [ 11, 21, 31 ]
    -
    a_letter_time   ->  [ 10, 20, 30 ]

Similarly, but slightly more complicated, we can create a new array, `a_blank_dur`, in which each item is the result of subtracting item *i* in `a_blank_time` from item *i+1* in `a_letter_time`.

~~~ .python
a_blank_dur = a_letter_time[1:] - a_blank_time[:-1]
~~~

Schematically:

    a_blank_dur         ->  [  9,  9 ]
    =
    a_letter_time[1:]   ->  [ 20, 30 ] # The leading 10 is stripped off
    -
    a_blank_time[:-1]   ->  [ 11, 21 ] # The trailing 31 is stripped off

The next step is to use the `array.mean()` and `array.std()` methods to get the averages and standard deviations of the durations in one go:

~~~ .python
mean_letter_dur = a_letter_dur.mean()
std_letter_dur = a_letter_dur.std()
mean_blank_dur = a_blank_dur.mean()
std_blank_dur = a_blank_dur.std()
~~~

And finally set them as experimental variables, so that they are logged an available for offline inspection:

~~~ .python
exp.set('mean_letter_dur', mean_letter_dur)
exp.set('std_letter_dur', std_letter_dur)
exp.set('mean_blank_dur', mean_blank_dur)
exp.set('std_blank_dur', std_blank_dur)
~~~

Done!

<div class='info-box' markdown='1'>

### Links

- [/miscellaneous/timing/](/miscellaneous/timing/)
- <http://wiki.scipy.org/Tentative_NumPy_Tutorial>

</div>

## Extra 2: Add assertions to check your experiment

A Dutch proverb states that a mistake is in a small corner. (I suspect that according to the original proverb the mistake, rather than the corner, was small, but no matter.) Developing experiments, or any kind of software, without bugs is almost impossible. However, you can protect yourself from many bugs by building safeguards into your experiment.

For example, our experiment has two conditions, defined as 'experimental' and 'control'. But what if I accidentally misspelled 'experimental' as 'experimentel' in the *experimental_loop*? The experiment would still run, but it would no longer work as expected. Therefore, we want to make sure that `condition` is either 'experimental' or 'control', but nothing else. In computer-speak, we want to *assert* that this is the case. Let's take a look at how we can do this.

First, drag a new `inline_script` item to the start of the *trial_sequence* and rename it to *assertions*. Add the following line to the *Run* tab:

~~~ .python
assert(self.get('condition') in ['experimental', 'control'])
~~~

Let's dissect this line:

- `self.get('condition')` retrieves the `condition` variable.
- `in ['experimental', 'control']` checks whether this variable matches any of the items in the list, i.e. whether it is 'experimental' or 'control'.
- `assert()` states that there *has* to be a match. If not, the experiment will crash (an `AssertionError` will be raised).

In other words, whatever you pass to `assert()` has to be `True`, otherwise your experiment will crash. This useful for sanity checks.

Some more assertions:

~~~ .python
assert(self.get('T2_present') in ['y', 'n'])
assert(self.get('lag') in ['']+range(0,9))
~~~

And a final one that is a bit more complicated. Can you figure out what it does?

~~~ .python
assert((self.get('lag') == '') != (self.get('T2_present') == 'y'))
~~~

<div class='info-box' markdown='1'>

### Links

- <https://wiki.python.org/moin/UsingAssertionsEffectively>
- Advice on protective programming in Axelrod (2014, doi:10.3389/fpsyg.2014.01435)

</div>

## Extra 3: Use PsychoPy directly

OpenSesame is back-end independent. This means that different libraries can be used for controlling the display, sound, response collection, etc. You can select the back-end in the General tab (see %FigBackend).

%--
figure:
 id: FigBackend
 source: FigBackend.png
 caption: |
  You can select a back-end in the General tab of your experiment.
--%

So far, we have used OpenSesame's own `openexp` modules, wich automatically map all commands to the correct functions of the selected back-end. Therefore, you don't have to bother with or know about the details of each back-end. However, you can also directly use the functions offered by a specific back-end, such as PsychoPy. This is especially useful if you want to use functionality that is not available in the `openexp` modules.

First, to use PsychoPy, you need to switch to the *psycho* back-end (see %FigBackend). Now, when you start the experiment, OpenSesame will automatically initialize PsychoPy, and the `psychopy.visual.Window` object will be available as `win` in `inline_script`s.

Now let's see how we can implement our RSVP stream in PsychoPy. (The script below replaces the part in the *Prepare* phase of *RSVP* in which we created `letter_canvas_list`.)

~~~ .python
from psychopy import visual
textstim_list = []
for i, stim in enumerate(stim_list):
    if i == T1_pos:
        color = 'white'
    else:
        color = 'black'
    # All stimuli require an psychopy.visual.Window object to be passed as first
    # argument. In OpenSesame, this object is available as `win`.
    textstim = visual.TextStim(win, text=stim, color=color)
    textstim_list.append(textstim)
~~~

The main difference with our previous script is that we don't draw text on a `canvas` object. Instead, the text is an object by itself (a `TextStim`), and it has its own `draw()` method to draw it to the screen.

Of course, we also need to update the *Run* phase of the *RSVP* stream, which now looks like this:

~~~ .python
for textstim in textstim_list:
    textstim.draw()
    win.flip()
    self.sleep(letter_dur)
    win.flip()
    self.sleep(isi)
~~~

The main difference here is that we need to call several methods to show our stimuli, instead of only `canvas.show()`. First, we need to call the `draw()` method on all stimuli that we want to show: `textstim.draw()` Next, we need to call `win.flip()` to refresh the display so that the stimuli actually become visible. If we call `win.flip()` without any preceding calls to `draw()`, as we do before the inter-stimulus-interval, it has the effect of clearing the display.

That's it!

<div class='info-box' markdown='1'>

### Links

- [/back-ends/psycho/](/back-ends/psycho/)
- <http://www.psychopy.org/api/visual.html>

</div>

## References

Axelrod, V. (2014). Minimizing bugs in cognitive neuroscience programming. *Frontiers in Psychology: Perception Science*, *5*, 1435. doi:10.3389/fpsyg.2014.01435
{: .reference}

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8–13. doi:10.1016/j.jneumeth.2006.11.017
{: .reference}

Raymond, J. E., Shapiro, K. L., & Arnell, K. M. (1992). Temporary suppression of visual processing in an RSVP task: An attentional blink? *Journal of Experimental Psychology: Human Perception and Performance*, *18*(3), 849–860. doi:10.1037/0096-1523.18.3.849
{: .reference}

[OpenSesame runtime for Android]: /getting-opensesame/android
[slides]: /attachments/neurospin2015-workshop-slides.pdf
[pdf]: /neurospin2015/index.pdf
[step-by-step tutorial]: /tutorials/step-by-step-tutorial/
