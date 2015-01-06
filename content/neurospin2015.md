---
layout: osdoc
title: NeuroSpin 2015
group: General
parser: academicmarkdown
menuclass: external
permalink: /neurospin2015/
ext_url: /neurospin2015
---

This tutorial is part of an OpenSesame workshop that will take place at the Cognitive Neuroimaging Unit in the NeuroSpin center on 13 Jan 2015, 9:30.

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

- A basic knowledge of OpenSesame is assumed. If you are not familiar with OpenSesame, it is recommended to follow the [step-by-step tutorial].
- A basic knowledge of experimental design is assumed.
- A basic knowledge of programming (not necessarily in Python) is assumed.

### Software and equipment

- This tutorial assumes OpenSesame 2.9.0 or higher.
- If you bring your own laptop, please install OpenSesame before the workshop.
- OpenSesame is available for Windows XP/ 7/ 8, Linux, and Mac OS. If you are running Mac OS, you are advised to verify beforehand that OpenSesame runs properly on your system, because Mac OS support is still experimental.

### Materials

- The primary resource for the workshop is this page, which can be downloaded in `.pdf` format from [here][pdf]. Print-outs will be available for attendees.

## Introduction

You can download the introduction slides from [here][slides].

## About

In this tutorial, we will implement an attentional-blink paradigm, as introduced by Raymond, Shapiro, and Arnell (1992). We will re-create experiment 2 from Raymond et al. almost exactly, with only a few minor modifications. In this experiment, the participant sees a stream of letters, which is typically called an RSVP stream (for Rapid Serial Visual Presentation).

There were two conditions. In the *experimental* condition, the participant's task was twofold:

- Report the identity of the white letter (all other letters were black).
- Indicate whether they saw an 'X'.

In the control condition, the participant's task was only to ...

- Indicate whether they saw an 'X'.

The white letter is called the *T1* (or 'target' in Raymond et al., 1992). The 'X' is called the *T2* (or 'probe' in Raymond et al., 1992). The typical finding is that the T2 is often missed when it is presented 200 - 500 ms after T1, but only when T1 needs to be reported. This phenomenon is called the *attentional blink*, because it is as though your mind's eye briefly blinks after seeing T1. Surprisingly, however, T2 is usually not missed when it follows T1 immediately, a phenomenon called *lag-1 sparing*. In Raymond et al., the results looked like this:

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

When you start OpenSesame, you will be given a choice of template experiments, and a list of recently opened experiments (if any, see %FigStartup).

%--
figure:
 id: FigStartup
 source: FigStartup.png
 caption: |
  The OpenSesame window on start-up.
--%

## Step 2: Choose template, font, and colors

The 'Extended template' already provides the basic structure of a typical trial-based experiment with a practice and an experimental phase. Because our experiment fits this template very well, we're going to use it. Therefore, double-click on 'Extended template' to open it.

In the 'General tab' that now appears, you can specify the general properties of your experiment. For this experiment, we want to use black letters on a gray background. Also, the default font size of 18 is a bit small, so change that to 32. Finally, it's good practice to give your experiment an informative name and description. Your 'General tab' now looks as %FigGeneralTab.

%--
figure:
 id: FigGeneralTab
 source: FigGeneralTab.png
 caption: |
  The General tab is where you define the general properties of your experiment.
--%

## Step 3: Implement counterbalancing

In Raymond et al., the experimental and control conditions were mixed between blocks: Participants first did a full block in one condition, and then a full block in the other condition. Condition order was counterbalanced, so that half the participants started with the experimental condition, and the other half started with the control condition.

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

The first thing to know is that `self.get()` retrieves experimental variables. These include variables that you have defined yourself, for example in a `loop` item, as well as built-in variables, which are available. One such built-in experimental is `subject_parity`, which is automatically set to 'even' when the experiment is launched with an even subject number, and to 'odd' when the subject number is odd.

The second thing to know is that `exp.set()` sets experimental variables. That is, it makes variables available elsewhere in OpenSesame, outside of `inline_script` items. So the line ...

~~~ .python
exp.set('condition1', 'experimental')
~~~

... creates an experimental variable with the name `condition1`, and gives it the value 'experimental'. Later on, in Step 3, we will use `condition1` to determine which condition is tested first. In other words, this script says the following:

- All even-numbered subjects start with the experimental condition.
- All odd-subjects start with the control condition.

<div class='info-box' markdown='1'>

## Links

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)
- [/miscellaneous/counterbalancing/](/miscellaneous/counterbalancing/)

</div>

## Step 4: Define experimental variables that are varied between blocks

As mentioned above, conditions are varied between blocks. To understand how this works in OpenSesame, it's best to start at the bottom (see %FigStructure), with ...

- the *trial_sequence*, which corresponds (as you might expect) to a single trial. One level above ...
- the *block_loop* corresponds to a single block of trials. Therefore, this is where you would define experimental variables that are varied within a block, which we'll get to later. One level above ...
- the *block_sequence* corresponds to a single block of trials plus the events that happen before and after every block, such as per-block feedback on accuracy, and pre-block instructions. One level above ...
- the *practice_loop* and *experimental_loop* correspond to multiple blocks of trials during respectively the practice and non-practice (experimental) phase. Therefore, this is where you would define experimental variables that are varied between blocks.

So we need to define our between-block manipulations near the top of the experimental hierarchy, in the *practice_loop* and *experimental_loop*.

%--
figure:
 id: FigStructure
 source: FigStructure.png
 caption: |
  A fragment of the experimental structure as shown in the overview area.
--%

Click on *practice_loop* to open the item. Right now, there is only one variable, `practice`, which has the value 'yes' during one cycle, which corresponds to one block here.

Let's get to work! Add a variable called `condition`, change the number of cycles to 2, and change the order to 'sequential'.
Now use the previously created variables `condition1` and `condition2` to determine which condition is executed first, and which second (see %FigPracticeLoop). To indicate that something is the name of a variable, and not a literal value, put square brackets around the variable name: '[my_variable]'

%--
figure:
 id: FigPracticeLoop
 source: FigPracticeLoop.png
 caption: |
  The *practice_loop* item after Step 4.
--%

Do the same thing for *experimental_loop*, except that the variable `practice` has the value 'no'. (The only function of the `practice` variable is so that you can easily filter out all practice trials during data analysis.)

<div class='info-box' markdown='1'>

## Links

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)
- [/miscellaneous/counterbalancing/](/miscellaneous/counterbalancing/)

</div>

## Step 5: Create instructions

Because the task differs between blocks, we need to show an instruction screen before each block. The *block_sequence* is the place to do this, because, as explained above, it corresponds to a single block of trials plus the events that occur before and after every block.

There are various items that we could use for an instruction screen, but we will use the good old `sketchpad`. Insert two new `sketchpad`s at the top of *block_sequence* by dragging them from the item toolbar. Rename the `sketchpad`s to *instructions_experimental* and *instructions_control*. Click on both items to add some instructional text, such as shown in %FigInstructions.

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

## Links

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

## Links

- [/usage/feedback/](/usage/feedback/)
- [/usage/text/](/usage/text/)

</div>

## Step 7: Define experimental variables that are varied within a block

Raymond et al. manipulate the position of T2 relative to T1 from 0 to 8, where 0 means that one letter is both T1 and T2 (i.e. a white 'X'). They also have trials in which there is no T2. This is all varied within a block. There are various ways to code this, but the easiest way is to use two variables:

- `lag` indicates the position of T2 relative to T1 and has a value of 0 - 8, or no value if there is no T2.
- `T2_present` is 'y' for trials on which there is a T2 and 'n' for trials on which there is no T2. Of course, this is redundant, because `T2_present` is 'y' on all trials on which `lag` has a value. But it's convenient to define `T2_present`, because we can use it later on to define the correct T2 response.

Click on *block_loop* and create a variable table as shown in %FigBlockLoop.

%--
figure:
 id: FigBlockLoop
 source: FigBlockLoop.png
 caption: |
  The *block_loop* item after Step 7.
--%

<div class='info-box' markdown='1'>

## Links

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

## Links

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

Next, we need to define a number of variables that determine the details of the RSVP stream: (Note that, like before, we use `self.get()` to retrieve experimental variables that have been defined in a `loop`.)

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
- Letters are randomly sampled without replacement from all uppercase letters, except for the 'X' (which is used for the T2).

So, let's translate these rules to Python:

~~~ .python
# The position of T1 is random between 7 and 15.
# Note that the first position is 0.
T1_pos = random.randint(7, 15)
# The maximum lag, i.e. the number of letters that follow T1.
max_lag = 8
# The length of the stream is the position of T1 + the maximum lag + 1. We need
# to add one, because we count starting at 0, so the length of a list is always
# 1 larger than its maximum index.
stream_len = T1_pos + max_lag + 1
# We take all uppercase letters, which have been predefined in the `string`
# module. Converting to a `list` creates a list of separate characters.
letters = list(string.ascii_uppercase)
# We remove the 'X' from this list.
letters.remove('X')
# Randomly sample `stream_len` items from `letters`!
stim_list = random.sample(letters, stream_len)
~~~

`stim_list` now contains all letters that make up our RSVP stream on a given trial, except for the T2. We still need to add an 'X' somewhere, but only on T2-present trials:

~~~ .python
if T2_present == 'y':
    T2_pos = T1_pos + lag
    stim_list[T2_pos] = 'X'
~~~

Ok! We now have a variable called `stim_list` that specifies the letters in our RSVP stream. This is a `list` that might contain something like: `['M', 'F', 'O', 'P', 'S', 'R', 'Y', 'C', 'U', 'Z', 'G', 'A', 'T', 'E', 'H', 'J', 'V', 'N', 'B', 'K', 'X', 'Q']`

The next step is to create a `list` of `canvas` objects, each of which contains a single letter from `stim_list`:

~~~ .python
# Create an empty list for the canvas objects.
letter_canvas_list = []
# Loop through all letters in `stim_list`. `enumerate()` is a convenient
# function that automatically returns (index, item) tuples. In our case, the
# index (`i`) reflects the position in the RSVP stream. The Python trick in
# which you assign a single value to two variables is called 'tuple unpacking'.
for i, stim in enumerate(stim_list):
    # Create a `canvas` object.
    letter_canvas = canvas(exp)
    # If we are at the position of T1, we change the foreground color, because
    # T1 is white, and the default color is black.
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

Finally, we use `exp.set()` to set the position and identity of T1 as experimental variables. That way we can use them elsewhere in OpenSesame, such as for logging and to specify the correct T1 response.

~~~ .python
exp.set('T1_pos', T1_pos)
# Extract T1 from the list
T1 = stim_list[T1_pos]
exp.set('T1', T1)
~~~

Preparation done!

<div class='info-box' markdown='1'>

## Links

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
    - Wait for a time specified as `letter_dur`
    - Show the blank canvas
    - Wait for a time specified as `isi`

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

## Links

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
- Collect a response, which is 'y' when T2 was present as 'n' when T1 was absent.

We will use the *ask_T1* `sketchpad` to ask the participant for T1. Click on *ask_T1* to open the item, and add a line of text, such as 'Please type the white letter'. Change the duration to 0. This 0 ms duration does not mean that the text is only shown for 0 ms, but that the experiment moves immediately to the next item, which is *response_T1*.

Open *response_T1*. The only thing that we have to do is define the correct response. To do this, we can use the `T1` experimental variable that we have set while preparing the RSVP stream. Therefore, enter '[T1]' in the 'Correct response' field.

Open *ask_T2*, and add a line of text, such as 'Did you see an X? (y/n)'. Again, set the duration to 0, so that the experiment moves immediately to the next item, which is *response_T2*.

Open *response_T2*. Again, we need to define the correct response, this time using the variable `T2_present`, which we had defined in the *block_loop*. Therefore, add '[T2_present]' to the 'Correct response' field. It's also useful to restrict the allowed responses to 'y' and 'n', so that participants don't accidentally press the wrong key. You can do this by entering a semicolon-separated list of keys in the 'Allowed responses' field (i.e. 'y;n').

<div class='info-box' markdown='1'>

## Links

- [/usage/collecting-responses/](/usage/collecting-responses/)
- [/usage/text/](/usage/text/)

</div>

## Step 13: Specify number and length of blocks

You now have a fully working experiment, but one thing still needs to be done: Setting the length of and number of blocks. We will use the following structure:

- 1 practice block of 9 trials in each conditon.
- 5 experimental blocks of 36 trials in each condition.

First, open *block_loop*. The 'Repeat' value if currently set to 1, which means that each trial is executed once, giving a block length of 18 trials. We want to make the Repeat-value variable, so that we can have a different value for the practice and experimental blocks. To do this, we need to make a small modification to the script of *block_loop*. Click on the 'View' button in top-right of the tab (the middle of the three buttons), and select 'View script'. Now change this line ...

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

Now open *experimental_loop*. Again, add a variable `block_repeat` and give it the value 2. This means that each block has a length of 2 x 18 = 36 trials. Also, change the number of cycles to 10, and arrange the loop table so that you first have five blocks of `condition1`, followed by five blocks of `condition 2` (see %FigExperimentalLoop).

%--
figure:
 id: FigExperimentalLoop
 source: FigExperimentalLoop.png
 caption: |
  If the length of a `loop` is variably defined, OpenSesame notifies you of this.
--%

## Step 14: Run experiment!

That's it. You can now run the experiment!

%--
figure:
 id: FigDone
 source: FigDone.svg
--%

## Extra (easy): Check timing

TODO

## Extra (medium): Validate your experiment

TODO

## Extra (difficult): Use PsychoPy directly

TODO

## References

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}

Raymond, J. E., Shapiro, K. L., & Arnell, K. M. (1992). Temporary suppression of visual processing in an RSVP task: An attentional blink? *Journal of Experimental Psychology: Human Perception and Performance*, *18*(3), 849–860. doi:10.1037/0096-1523.18.3.849
{: .reference}

[OpenSesame runtime for Android]: /getting-opensesame/android
[slides]: /attachments/neurospin2015-workshop-slides.pdf
[pdf]: /neurospin2015/index.pdf
[step-by-step tutorial]: /tutorials/step-by-step-tutorial/
