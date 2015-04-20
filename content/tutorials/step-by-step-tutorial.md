---
layout: osdoc
title: Step-by-step tutorial (beginner)
group: Tutorials
permalink: /step-by-step-tutorial/
parser: academicmarkdown
author: Sebastiaan Mathôt, Elke Godefroid, Floor de Groot, Lotje van der Linden, and Eduard Ort
---

In this tutorial you will learn how to create a simple but complete psychological experiment using OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012)][references]. You will use mainly the graphical user interface of OpenSesame (i.e., no Python inline coding), although you will make small modifications to the OpenSesame script.

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: "The gaze-cuing paradigm [(Friesen and Kingstone, 1998)][references] that you will implement in this tutorial. This example depicts a trial in the incongruent condition, because the smiley looks at the distractor ('X') and not at the target ('F')."
--%

This document provides a detailed click-by-click walk-through. Screenshots are provided, as well as downloadable snapshots of the experiment as it should be after each step of the tutorial. This tutorial will take approximately one hour to complete.

## Overview

%--
toc:
 mindepth: 2
 maxdepth: 2
 exclude: [Overview]
--%

## About OpenSesame

OpenSesame is a cross-platform graphical experiment builder. It provides a very simple way to create psychological experiments using a point-and-click interface. For complex experiments, you can use [Python inline scripting] (not covered in this tutorial).

OpenSesame is freely available under the [General Public License v3][gpl].

## Resources

- __Download__ -- This tutorial assumes that you are running OpenSesame version 2.9.0 or later. To check which version you are running, see the bottom right of the 'Get started' tab (see %FigGetStarted). You can download the most recent version of OpenSesame from:
	- [/getting-opensesame/download](/getting-opensesame/download)
- __Documentation__ -- A dedicated documentation website can be found at:
	- <http://osdoc.cogsci.nl/>
- __Forum__ -- A support forum can be found at:
	- <http://forum.cogsci.nl/>

## The experiment

The experiment that you will create is a gaze-cuing paradigm, as introduced by [Friesen and Kingstone (1998)][references]. A face is presented in the center of the screen (%FigGazeCuing). This face looks either to the right or to the left. A target letter (an 'F' or an 'H') is presented to the left or right of the face. A distractor stimulus (the letter 'X') is presented on the other side of the face. The task is to indicate as quickly as possible whether the target letter is an 'F' or an 'H'. In the congruent condition, the face looks at the target. In the incongruent condition, the face looks at the distractor. As you may have guessed, the typical finding is that you are faster in the congruent condition, compared to to the incongruent condition, even though the direction of gaze is not predictive of the target location. This shows that our attention is automatically guided by other people's gaze, even in situations where this doesn't serve any purpose. (And even when the face is just a smiley!) Of course, following other people's gaze is generally not useless at all, so this is actually a good strategy.

The experiment will consist of a practice and an experimental phase. We will present visual feedback after every block of trials and play a sound after every incorrect response.

## Step 1: Create the main sequence

The 'Get started' tab is the first thing that you see when you start OpenSesame (%FigGetStarted). The box labeled 'New' contains a list of available templates, which provide convenient starting points for new experiments. After you saved your experiment the first time, you will see another box labeled 'Recent' that shows a list of recently opened experiments.

%--
figure:
 id: FigGetStarted
 source: get-started.png
 caption: "The 'Get started' dialog on OpenSesame start-up. The box labeled 'Recent' is empty if you start OpenSesame for the first time."
--%

Double-click on 'Default template', to start with a minimal experimental template. Save the experiment right away as `gaze_cuing.opensesame`.

By default there is a main `sequence`, which is simply called *experiment*. Click on *experiment* in the overview area (by default on the left side, see %FigInterface) to open its controls in the tab area. The *experiment* `sequence` consists of two items: a `notepad` called *getting started* and a `sketchpad` called *welcome*.

We don't need these two items. Remove *getting_started* by right-clicking on it in the overview area and selecting 'Move to unused items' (shortcut: `Del`). Remove *welcome* in the same way. The *experiment* `sequence` is now empty.

%--
figure:
 id: FigInterface
 source: interface.png
 caption: "The default layout of the OpenSesame interface."
--%

<div class='info-box' markdown='1'>

### Background box

__Names vs types__ -- Items in OpenSesame have a name and a type. The name and type can be the same, but they are usually not. For example, a `sketchpad` item can have the name *my_target_sketchpad*. To make this distinction clear, we will use `monospace` to indicate item types, and *italics* to indicate names.

__Tip__ -- The 'Extended template' is a good starting point for many experiments. It already contains the basic structure of a trial-based experiment.

__Tip__ -- You can click on the Help icons in the top right of an item's tab to get context-sensitive help.

__Tip__ -- Save (shortcut: `Ctrl+S`) your experiment often! In the unfortunate (and unlikely) event of data loss, you will often be able to recover your work from the back-ups that are created automatically, by default, every 10 minutes (Menu → Tools → Open backup folder).

__Tip__ -- Unless you have used 'Permanently delete' (shortcut: `Shift+Del`), deleted items are still available in the 'Unused items' bin, until you select 'Permanently delete unused items' in the 'Unused items' tab. You can re-add deleted items to a `sequence` by dragging them out of the 'Unused items' bin to somewhere in your experiment.

__Tip__ -- %FigExperimentStructure schematically shows the structure of the experiment that you will create. If you get confused during the tutorial, you can refer to %FigExperimentStructure to see where you are.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: "A schematic representation of the structure of the 'Gaze cuing' experiment. The item types are in bold face, item names in regular face."
--%

</div>

### Append a form_text_display item for the instruction display

As the name suggests, a `form_text_display` is a form that displays text. We are going to use a `form_text_display` to give instructions to the participant at the beginning of the experiment.

Click on *experiment* in the overview area to open its controls in the tab area. You will see an empty `sequence`. Drag a `form_text_display` from the item toolbar (under 'Form', see %FigInterface) onto the *experiment* `sequence` in the tab area. When you let go, a new `form_text_display` item will be inserted into the `sequence`. (We will get back to this in Step 12.)

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- You can drag items into the overview area and into `sequence` tabs.

__Tip__ -- If a drop action is ambiguous, a pop-up menu will ask you what you want to do.

__Tip__ -- A `form_text_display` only shows text. If you require images etc., you can use a `sketchpad` item. We will meet the `sketchpad` in Step 5.

</div>

### Append a loop item, containing a new sequence item, for the practice phase

We need to append a `loop` item to the *experiment* `sequence`. We will use this `loop` for the practice phase of the experiment. Click on the *experiment* `sequence` to open its controls in the tab area.

Drag the `loop` item from the item toolbar into the `sequence` just the way you added the `form_text_display`. New items are inserted below the item that they are dropped on, so if you drop the new `loop` onto the previously created `form_text_display`, it will appear where you want it: after the `form_text_display`. But don't worry if you drop a new item in the wrong place, because you can always re-order things later.

A `loop` does not do anything by itself.  A `loop` always needs another item to run. Therefore you have to fill the new `loop` item with another item (You will also see a warning written in red telling you that 'no item to run specified' in the tab area, if you select this `loop` item). Drag a `sequence` item from the item toolbar onto the `loop` item. A pop-up menu will appear, asking you whether you want to insert the `sequence` after the `loop` item, or use the `sequence` as the `loop`'s item to run. Select 'Set as item to run for loop'. (We will get back to this in Step 2.)

<div class='info-box' markdown='1'>

### Background box

__What is a `loop` item?__ -- A `loop` is an item that adds structure to your experiment. It repeatedly runs another item, typically a `sequence`. A `loop` is also the place where you will usually define your independent variables, the things that you manipulate in your experiment.

__What is a `sequence` item?__ -- A `sequence` item also adds structure to your experiment. As the name suggests, a `sequence` runs multiple other items in sequence.

__The `loop`-`sequence` structure__ -- You often want to repeat a sequence of events. To do this, you will need a `loop` item that contains a `sequence` item. By itself, a `sequence` does not repeat. It simply starts with the first item and ends with the last item. By 'wrapping' a `loop` item around the `sequence`, you can repeat the `sequence` multiple times. For example, a single trial will usually correspond to a single `sequence` called *trial_sequence*. A `loop` (often called *block_loop*) around this *trial_sequence* would then constitute a single block of trials. Similarly, but at another level of the experiment, a `sequence` (often called *block_sequence*) may contain a single block of trials, followed by a `feedback` display. A *practice_phase* `loop` around this 'block' `sequence` would then constitute the practice phase of the experiment. This may seem a bit abstract right now, but as you follow this tutorial, you will become familiar with the use of `loop`s and `sequence`s.

__Tip__ -- For more information about `sequence`s and `loop`s, see:

- [/usage/sequences-and-loops](/usage/sequences-and-loops)

</div>

### Append a new form_text_display item for the end-of-practice message

After the practice phase, we want to inform the participant that the real experiment will begin. For this we need another `form_text_display`. Go back to the *experiment* `sequence`, and drag a `form_text_display` from the item toolbar onto the `loop` item. The same pop-up menu will appear as before. This time, select 'Insert after loop'. (We will get back to this in Step 12.)

<div class='info-box' markdown='1'>

__Tip__ -- Don't worry if you have accidentally changed a `loop`'s item to run. You can undo this easily by dragging the `loop`'s original item to run back to the `loop`, or by selecting the correct item to run from the drop-down box in the `loop` tab.

</div>

### Append a new loop item, containing the previously created sequence, for the experimental phase

We need a `loop` item for the experimental phase, just like for the practice phase. Therefore, drag a `loop` from the item toolbar menu onto *_form_text_display*.

The newly created `loop` (called *_loop*) is empty, and should be filled with a `sequence`, just like before. However, because the trials of the practice and experimental phase are identical, they can use the same `sequence`. Therefore, instead of dragging a new `sequence` from the item toolbar, you can re-use the *existing* one (i.e. create a linked copy). To do this, drag the previously created `sequence` from the overview area onto *_loop* while holding the `Ctrl` key pressed. In the pop-up menu that appears, select 'Set as item to run for _loop'.

<div class='info-box' markdown='1'>

### Background box

__Tip__ — There is an important distinction between *linked* and *unlinked* copies. If you create a linked copy of an item, you create another occurrence of the same item. Therefore, if you modify the original item, the linked copy will change as well. In contrast, if you create an unlinked copy of an item, the copy will be initially look identical (except for its name), but you can edit the original without affecting the unlinked copy, and vice versa. Important: If you create an unlinked copy of a `sequence` or `loop`, you do not automatically create unlinked copies of all child items. In this sense, an unlinked copy in OpenSesame is different from what computer scientists call a *deep* copy.

__Tip__ — You can create *linked* and *unlinked* copies as follows:

- To create a linked copy, hold `Ctrl` while dragging and dropping an item, or right-click on an item and select 'Create linked copy'.
- To create an unlinked copy, hold `Ctrl+Shift` while dragging and dropping an item, or right-click on an item and select 'Create unlinked copy'.

</div>

### Append a new form_text_display item, for the goodbye message

When the experiment is finished, we should inform the participant. For this we need another `form_text_display` item. Go back to the *experiment* `sequence`, and drag `form_text_display` from the item toolbar onto *_loop*. In the pop-up menu that appears, select 'Insert after _loop'. (We will get back to this in Step 12.)

### Give the new items sensible names

By default, new items have names like *sequence* and *_form_text_display*. It is good practice to give items sensible names. This makes it much easier to understand the structure of the experiment. If you want, you can also add a description to each item. Renaming items is very easy. Item names must consist of alphanumeric characters and/or underscores.

- Select *form_text_display* in the overview area, click on its label in the top of the tab area and rename the item to *instructions*. (Overview-area shortcut: `F2`)
- Select *loop* in the overview area and rename it to *practice_loop*.
- Select *sequence* (under *practice_loop*) in the overview area and rename it to *block_sequence*. Because you have re-used this item in the *experimental_loop*, the name automatically changes there as well. This illustrates why it is efficient to create linked copies whenever this is possible.
- Rename *_form_text_display* to *end_of_practice*.
- Rename *_loop* to *experimental_loop*.
- Rename *__form_text_display* to *end_of_experiment*.

### Give the whole experiment a sensible name.

The experiment in its entirety also has a name (a title, in this context) and a description. Click on 'New experiment' in the overview area. You can rename the experiment in the same way as you renamed its items. The title currently is 'New experiment'. Rename the experiment to 'Tutorial: Gaze cuing'. Note that, unlike item names, the experiment title may contain spaces etc.

The overview area of your experiment now looks like %FigStep1. This would be a good time to save your experiment (shortcut: `Ctrl+S`). You can download the experiment up to this point here:

- [tutorial_step1.opensesame][step1]

%--
figure:
 id: FigStep1
 source: step1.png
 caption: "The overview area at the end of the step 1."
--%

<div class='info-box' markdown='1'>

### Background box

__Tip__ — If you don't like having many tabs open, you can close all tabs except the currently opened one by clicking on the 'Close other tabs' button in the main toolbar (shortcut: `Ctrl+T`).

__Tip__ — You can enable 'one tab mode' (Menu -> View -> One tab mode) to prevent multiple tabs from opening simultaneously.

</div>

## Step 2: Create the block sequence

Click on *block_sequence* in the overview. At the moment this `sequence` is empty. We want *block sequence* to consist of a block of trials, followed by a  `feedback` display. For this we need to do the following:

### Append a reset_feedback item to reset the feedback variables

We don't want our feedback to be confounded by key presses that participants have made during the instruction phase (or during previous blocks of trials). Therefore, we start each block of trials by resetting the feedback variables. To do this we need a `reset_feedback` item. Grab `reset_feedback` from the item toolbar (under 'Response collection') and drag it onto *block_sequence*.

### Append a new loop, containing a new sequence, for a block of trials

For a single trial we need a `sequence`. For a block of trials, we need to repeat this `sequence` multiple times. Therefore, for a block of trials we need to wrap a `loop` around a `sequence`. Drag a `loop` from the item toolbar onto *reset_feedback*. Next, drag a `sequence` from the item toolbar onto the newly created `loop`, and select 'Set as item to run for loop' in the pop-up menu that appears. (We will get back to this in Step 3.)

### Append a feedback item

After every block of trials we want to give feedback to the participant, so that the participant knows how well he/ she is doing. For this we need a `feedback` item. Drag a `feedback` from the item toolbar onto *loop*, and select 'Insert after loop' in the pop-up menu that appears. (We will get back to this in Step 10.)

### Give the new items sensible names

Rename *loop* to *block_loop* and *sequence* to *trial_sequence*. (See Step 1 if you don't remember how to do this.) The names *reset_feedback* and *feedback* are fine as they are.

The overview of your experiment now looks like %FigStep2. Remember to save your experiment regularly. You can download the experiment up to this point here:

- [tutorial_step2.opensesame][step2]

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%

## Step 3: Fill the block loop with independent variables

As the name suggests, *block_loop* corresponds to a single block of trials. In the previous step we created the *block_loop*, but we still need to 'fill' it with independent variables, which will be varied within the block. Our experiment has three independent variables:

- __gaze_cue__ can be 'left' or 'right'.
- __target_pos__ (the position of the target) can be '-300' or '300'. These values reflect the X-coordinate of the target in pixels (0 = center). Using the coordinates directly, rather than 'left' and 'right', will be convenient when we create the target displays (see Step 5).
- __target_letter__ (the target letter) can be 'F' or 'H'.

Therefore, our experiment has 2 x 2 x 2 = 8 levels. Although 8 levels is not that many (most experiments will have more), we don't need to type in all the possible combinations of variables by hand. Click on *block_loop* in the overview to open its tab. Now click on the 'Variable wizard' button. In the variable wizard, you simply define all variables by typing the name in the first row and the levels in the rows below the name (see %FigVariableWizard). If you select 'Ok', you will see that __block_loop__ has been filled with all 8 possible combinations. That's convenient!

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: "The loop variable wizard in Step 3."
--%

However, we are not done yet. There are two more variables that we need to add: the location of the distractor and the correct response.

- __dist_pos__ -- Click on 'Add variable' and type 'dist_pos 300' in the dialog that appears. This will create a variable called 'dist_pos', with the value '300'. Change the value of 'dist_pos' to '-300' in every row where 'target_pos' is '300'. By doing this, we make sure that the distractor is always presented opposite from the target.
- __correct_response__ -- Click on 'Add variable' and type 'correct_response' in the dialog that appears. Change 'correct_response' to 'm'  where 'target_letter' is 'H'. This means that the participant should press the 'z' key if he/ she sees an 'F' and the 'm' key if he/ she sees an 'H'.

Add one more variable which indicates if the face was looking at the target letter or at the distractor.

- __congruency__ -- Click on 'Add variable' and type 'congruency' in the dialog that appears. Change 'congruency' to 'congruent' where 'target_pos' is '-300' and 'gaze_cue' is 'left', and where 'target_pos' is '300' and 'gaze_cue' is 'right' (these are the values with which the face will look at the targer letter). Change the value of 'congruency' to 'incronguent' of the rows in which the face will look at the distractor. Thus, where 'target_pos' is '-300' and 'gaze_cue' is 'right', and where 'target_pos' is '300' and 'gaze_cue' is 'left'.

This variable is useful if you want to analyze your data later on. If you don't add this variable here, you will have still have to manually specify later whether the cue was valid or not.

There is one last thing to be done. 'Repeat' is currently set to '1.00'. This means that each cycle will be executed once. So the block now consists of 8 trials, which is a bit short. A reasonable length for a block of trials is 24, so set 'Repeat' to 3.00 (3 repeats x 8 cycles = 24 trials). You don't need to change 'Order', because 'random' is exactly what we want.

The *block_loop* now looks like %FigStep3. Remember to save your experiment regularly. You can download the experiment up to this point here:

- [tutorial_step3.opensesame][step3]

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- You can prepare your variable list in your favorite spreadsheet program and copy-paste it into the `loop` variable table. In this case, you first need to set 'Cycles' to the correct number of trials.

__Tip__ -- 'Cycles' refers to the number of distinct trials. 'Repeat' refers to the number of times that every trial occurs. Therefore, a block consists of 'Cycles' x 'Repeat' trials.

__Tip__ -- You can set 'Repeat' to a non-integer number. For example, by setting 'Repeat' to '0.5', only half the trials (randomly selected) are executed.

</div>

## Step 4: Add images and sound files to the file pool

We will not actually draw the stimuli in this experiment, but use images from file. In addition, we will play a sound if the participant makes an error. For this we need a sound file.

You can download the required files here (in most webbrowsers you can right-click the links and choose 'Save Link As' or a similar option):

- [gaze_neutral.png](/attachments/gaze-cuing/gaze_neutral.png)
- [gaze_left.png](/attachments/gaze-cuing/gaze_left.png)
- [gaze_right.png](/attachments/gaze-cuing/gaze_right.png)
- [incorrect.ogg](/attachments/gaze-cuing/incorrect.ogg)

After you have downloaded these files (to your desktop, for example), you can add them to the file pool. If the file pool is not already visible (by default on the right side of the window),  click on the 'Show file pool' button in the main toolbar (shortcut: `Ctrl+P`). The easiest way to add the four files to the file pool is to drag them from the desktop (or wherever you have downloaded the files to) into the file pool. Alternatively, you can click on the '+' button in the file pool and add files using the file select dialog that appears. The file pool will be automatically saved with your experiment if you save your experiment in the `.opensesame.tar.gz` format (which is the default format).

Your file pool now looks like %FigStep4. Remember to save your experiment regularly. You can download the experiment up to this point here:

- [tutorial_step4.opensesame.tar.gz][step4]

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%

<div class='info-box' markdown='1'>

### Background box

__Tip__ — So far you may have saved your experiment in `.opensesame` format. If so, from now you should save your experiment in `.opensesame.tar.gz` format. Otherwise the files in the file pool will not be saved along with your experiment.

</div>

## Step 5: Fill the trial sequence with items

A trial in our experiment is fairly straightforward:

1. __Fixation dot__ -- 750 ms, `sketchpad` item
2. __Neutral gaze__ -- 750 ms, `sketchpad` item
3. __Gaze cue__ -- 500 ms, `sketchpad` item
4. __Target__  -- 0 ms, `sketchpad` item
5. __Response collection__ 	-- `keyboard_response` item
6. __Play a sound if response was incorrect__ --  `sampler` item
7. __Log response to file__ -- `logger` item

Click on *trial_sequence* in the overview to open the *trial_sequence* tab. Select `sketchpad` in the item toolbar and drag it into the 'trial_sequence' four times. Next, select and append a `keyboard_response` item, a `sampler` item, and a `logger` item.

Again, we will rename the new items, to make sure that the *trial_sequence* is easy to understand. Rename *sketchpad* to *fixation_dot*, *_sketchpad* to *neutral_gaze*, *\_\_sketchpad* to *gaze_cue*, *\_\_\_sketchpad* to *target*, and *sampler* to *incorrect_sound*. (See Step 1 if you don't remember how to do this.)

The *incorrect_sound* item should only be executed if an error was made. To do this, we need to change the conditional statement (in the 'Run if …' field) to `[correct] = 0` in the *trial_sequence* tab. This works, because the *keyboard_response* item automatically creates a `correct` variable, which is set to `1` (correct), `0` (incorrect) or `undefined` (this relies on the `correct_response` variable that was defined in Step 3). The square brackets indicate that `correct` should be interpreted as the name of a variable and not as text. To change a run-if statement for an item in a `sequence`, simply double click on it (shortcut: `F3`).

The *trial_sequence* now looks like %FigStep5. You can download the experiment up to this point here:

- [tutorial_step5.opensesame.tar.gz][step5]

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%

<div class='info-box' markdown='1'>

### Background box

__What is a `sketchpad` item?__ -- As the name suggests, a `sketchpad` is used to present visual stimuli. This includes text, geometric shapes, fixation dots, Gabor patches, etc. You can draw on the `sketchpad` using the built-in drawing tools.

__What is a `keyboard_response` item?__ -- As the name suggests, a `keyboard_response` item collects a participant's response from the keyboard.

__What is a `sampler` item?__ -- A `sampler` item plays a sound from a sound file.

__What is a `logger` item?__ -- A `logger` item writes data to the log file. This is very important, because if you forget to include a `logger` item, no data will be logged during the experiment!

__Tip__ -- Variables and conditional "if" statements are very powerful! To learn more about them, see:

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)

</div>

## Step 6: Draw the sketchpad items

The `sketchpad` items that we have created in Step 5 are still blank. It's time to do some drawing!

### Set the background color to white

Click on *fixation_dot* in the overview area to open its tab. You can see that the `sketchpad` is black, while the images that we have downloaded have a white background. Oops, we forgot to set the background color of the experiment to white (it is black by default)! Click on 'Tutorial: Gaze cuing' in the overview area to open the 'General properties' tab. Change 'Foreground color' to 'black' and 'Background color' to 'white'.

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- For more fine-grained control over colors, you can also use the hexadecimal RGB notation (e.g., `#FF000` for red) or use the color-picker tool.

</div>

### Draw the fixation dot

Go back to the *fixation_dot* by clicking on *fixation_dot* in the overview. You can draw on the `sketchpad` right away, but (unless your screen is really large) it looks a bit cramped. Therefore, click on 'Toggle pop-out' in the top right corner to open the `sketchpad` editor in a separate window. Now select the fixation-dot tool by clicking on the button with the small black dot. If you move your cursor over the sketchpad, you can see the screen coordinates in the top-right. Set the (foreground) color to 'black'. Click on the center of the screen (0, 0) to draw a central fixation dot. Click again on 'toggle pop-out' to get back to the default OpenSesame interface.

Finally, change the 'Duration' field from 'keypress' to '745', because we want the fixation dot to be presented for 750 ms. Wait ... *why didn't we just specify a duration of 750 ms?* The reason for this is that the actual display-presentation duration is always rounded up to a value that is compatible with your monitor's refresh rate. This may sound complicated, but for most purposes the following rules of thumb are sufficient:

1. Choose a duration that is possible given your monitor's refresh rate. For example, if your monitor's refresh rate is 60 Hz, it means that every frame lasts 16.7 ms (= 1000 ms/60 Hz). Therefore, on a 60 Hz monitor, you should always select a duration that is a multiple of 16.7 ms, such as 16.7, 33.3, 50, 100, etc.
2. In the duration field of the `sketchpad` specify a duration that is a few milliseconds shorter than what you're aiming for. So if you want to present a `sketchpad` for 50 ms, choose a duration of 45. If you want to present a `sketchpad` for 1000 ms, choose a duration of 995. Etcetera.

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- For a detailed discussion of experimental timing, see:

- [/miscellaneous/timing](/miscellaneous/timing)

__Tip__ -- The duration of a `sketchpad` can be a value in milliseconds, but you can also enter 'keypress' or 'mouseclick' to collect a keyboard press or mouse click respectively. In this case a `sketchpad` will work much the same as a `keyboard_response` item (but with fewer options).

__Tip__ -- Make sure that the (foreground) color is set to black. Otherwise you will draw white on white and won't see anything!

</div>

### Draw the neutral gaze

Open the *neutral_gaze* `sketchpad`. Now select the image tool by clicking on the button with the moon-mountain-landscape-like icon. Click on the center of the screen (0, 0). The 'Select file from pool' dialog will appear. Select the file `gaze_neutral.png` and click on the 'Select' button. The neutral gaze image will now stare at you from the center of the screen! Finally, like before, change the 'Duration' field from 'keypress' to '745'. (And note again that this means a duration of 750 ms on most monitors!)

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- OpenSesame can handle a wide variety of image formats. However, some (non-standard) `.bmp` formats are known to cause trouble. If you find that a `.bmp` image is not shown, you may want to consider using a different format, such as `.png`. You can convert images easily with free tools such as [GIMP].
</div>

### Draw the gaze cue

Open the *gaze_cue* `sketchpad`, and select again the image tool. Click on the center of the screen (0, 0) and select the file `gaze_left.png`.

Obviously, we are not done yet, because the gaze cue should not always be 'left', but should depend on the variable `gaze_cue`, which we have defined in Step 3. However, by drawing the `gaze_left.png` image to the `sketchpad`, we have generated a script that needs only a tiny modification to make sure that the proper image is shown. Click on the 'Select view' button at the top-right of the *gaze_cue* tab and select 'View script'. You will now see the script that corresponds to the sketchpad that we have just created:

~~~ .python
set duration "keypress"
draw image 0 0 "gaze_left.png" scale=1 center=1 z_index=0 show_if="always"
~~~

The only thing that we have to do is replace `gaze_left.png` with `gaze_[gaze_cue].png`. This means that OpenSesame uses the variable `gaze_cue` (which has the values `left` and `right`) to determine which image should be shown.

While we are at it, we might as well change the duration to '495' (rounded up to 500!). The script now looks like this:

~~~ .python
set duration "495"
draw image 0 0 "gaze_[gaze_cue].png" scale=1 center=1 z_index=0 show_if="always"
~~~

Click the 'Apply and close' button at the top right to apply your changes to the script and return to the regular item controls. You will see a message saying that the image is unknown or variably defined, and is therefore not shown. Don't worry, it will be shown during the experiment!

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- If you use a variable in OpenSesame script, you need to know the exact name of the variable. If you don't remember the exact name of a certain variable (e.g. if you don't remember whether you used a capital or not), you can click the 'Variable inspector' button in the main toolbar (shortcut: `Ctrl+I`). The Variable inspector provides a list of all variables used in your experiment (see %FigVariableInspector).

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "The variable inspector is a convenient way to get an overview of the variables that exist in your experiment."
--%

</div>

### Draw the target

We want three objects to be part of the target display: the target letter, the distractor letter, and the gaze cue (see %FigGazeCuing). Like before, we will start by creating a static display using the `sketchpad` editor. After this, we will only need to make minor changes to the script so that the exact display depends on the variables.

Click on *target* in the overview to open the target tab and like before, draw the `gaze_left.png` image at the center of the screen. Now select the draw text tool by clicking on the button with the 'A' icon. The default font size is 18pt, which is a bit small for our purpose, so change the font size to 32pt. Now click on (-320, 0) in the `sketchpad` (the X-coordinate does not need to be exactly 320, since we will change this to a variable anyway). Enter "[target_letter]" in the dialog that appears, to draw the target letter (when drawing text, you can use variables directly). Similarly, click on (320, 0) and draw an 'X' (the distractor is always an 'X').

Now open the script editor by clicking on the 'Select view' button at the top-right of the tab and selecting 'View script'. The script looks like this:

~~~ .python
set duration "keypress"
draw image 0 0 "gaze_left.png" scale=1 center=1 z_index=0 show_if="always"
draw textline -320 0 "[target_letter]" center=1 color="black" font_family="mono" font_size=32 font_bold="no" font_italic="no" html="yes" z_index=0 show_if="always"
draw textline 320 0 "X" center=1 color="black" font_family="mono" font_size=32 font_bold="no" font_italic="no" html="yes" z_index=0 show_if="always"
~~~

Like before, change `gaze_left.png` to `gaze_[gaze_cue].png`. We also need to make the position of the target and the distractor depend on the variables `target_pos` and `dist_pos` respectively. To do this, simply change `-320` to `[target_pos]` and `320` to `[dist_pos]`. Make sure that you leave the `0`, which is the Y-coordinate. The script now looks like this:

~~~ .python
set duration "keypress"
draw image 0 0 "gaze_[gaze_cue].png" scale=1 center=1 z_index=0 show_if="always"
draw textline "[target_pos]" 0 "[target_letter]" center=1 color="black" font_family="mono" font_size=32 font_bold="no" font_italic="no" html="yes" z_index=0 show_if="always"
draw textline "[dist_pos]" 0 "X" center=1 color="black" font_family="mono" font_size=32 font_bold="no" font_italic="no" html="yes" z_index=0 show_if="always"
~~~

Click on the “Apply” button to apply the script and go back to the regular item controls.

Finally, set the 'Duration' field to '0'. This does not mean that the target is presented for only 0 ms, but that the experiment will advance to the next item (the *keyboard_response*) right away. Since the *keyboard_response* waits for a response, but doesn't change what's on the screen, the target will remain visible until a response has been given.

Remember to save your experiment regularly. You can download the experiment up to this point here:

- [tutorial_step6.opensesame.tar.gz][step6]

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- Each element of a `sketchpad` has a 'show if' option, which specifies when the element should be shown. You can use this to hide/ show elements from a `sketchpad` depending on certain variables.

__Tip__ -- Make sure that the (foreground) color is set to black. Otherwise you will draw white on white and won't see anything!

</div>

## Step 7: Configure the keyboard response item

Click on *keyboard_response* in the overview to open its tab. You will see three options: Correct response, Allowed responses, and Timeout.

We have already set the `correct_response` variable in Step 3, so we don't need to set it here. If we do, we will simply override the previously set correct response, which is definitely not what we want.

We do need to set the allowed responses. Enter 'z;m' in the allowed-responses field. The semicolon is used to separate responses. The `keyboard_response` now only accepts 'z' and 'm' keys. All other key presses are ignored, with the exception of 'escape', which aborts the experiment.

We also want to set a timeout, which is the maximum interval that the `keyboard_response` waits before deciding that the response was incorrect and setting the 'response' variable to 'timeout'. '2000' (ms) is a good value.

The `keyboard_response` now looks like %FigStep7. You can download the experiment up to this point here:

- [tutorial_step7.opensesame.tar.gz][step7]

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "The `keyboard_response` at the end of Step 7."
--%

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- By default, the `keyboard_response` will use the `correct_response` variable to determine whether a response was correct. But you can use a different variable as well. To do this, enter a variable name between square brackets (`[my_variable]`) in the correct response field.

__Tip__ -- If 'flush pending key presses' is enabled (it is by default), all pending key presses are discarded when the `keyboard_response` item is called. This prevents carry-over effects, which might otherwise occur if the participant accidentally presses a key during a non-response part of the trial.

__Tip__ -- To use special keys, such as '/' or the up-arrow key, you can use key names (e.g., 'up' and 'space') or associated characters (e.g., '/' and ']'). The 'List available keys' button provides an overview of all valid key names.

</div>

## Step 8: Configure the incorrect (sampler) item

The *incorrect_sound* item doesn't need much work. Essentially we only need to select the sound that should be played. Click on *incorrect_sound* in the overview to open its tab. Click on the 'Browse' button and select `incorrect.ogg` from the file pool.

The sampler now looks like %FigStep8. You can download the experiment up to this point here:

- [tutorial_step8.opensesame.tar.gz][step8]

%--
figure:
 id: FigStep8
 source: step8.png
 caption: "The *incorrect_sound* item at the end of Step 8."
--%

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- You can use variables to specify which sound should be played by using a variable name between square brackets as (part of) the file name. For example, `[a_word].ogg`.

__Tip__ -- The `sampler` handles files in `.ogg` and `.wav` format. If you have sound files in a different format, [Audacity] is a great free tool to convert sound files (and much more).

</div>

## Step 9: Configure the variable logger

Actually, we don't need to configure the variable `logger`, but let's take a look at it anyway. Click on *logger* in the overview to open its tab. You will see that the option 'Automatically detect and log all variables' is selected. This means that OpenSesame logs everything, which is fine.

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- If you like your log-files clean, you can disable the auto-detect option and manually select variables to log or use the 'Smart select' button. 'Smart select' will select 1) all variables that are defined in the `loop`s, 2) all variables offered by the response items, and  3) the `count_[item name]` variables of all `sequence` items, which keep track of how often a particular `sequence` has been executed (essentially these are trial and block counters).

__The one tip to rule them all__ -- Always triple-check whether all the necessary variables are logged in your experiment! The best way to check this is to run the experiment and investigate the resulting log files.

</div>

## Step 10: Draw the feedback item

After every block of trials, we want to present feedback to the participant to let him/ her know how well he/ she is doing. Therefore, in Step 2, we added a `feedback` item, simply named *feedback* to the end of *block_sequence*.

Click on *feedback* in the overview to open its tab and select the draw text tool and click at (0, -128). Enter "Your average response time was [avg_rt]ms". Similarly, draw "Your accuracy was [acc]%" at (0, -64) and "Press any key to continue ..." at (0, 64). Because we want the feedback item to remain visible as long as the participant wants (i.e. until he/ she presses a key), we leave 'Duration' field set to 'keypress'.

The feedback item now looks like %FigStep_10 You can download the experiment up to this point here:

- [tutorial_step10.opensesame.tar.gz][step10]

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: "The feedback item at the end of Step 10."
--%

<div class='info-box' markdown='1'>

### Background box

__What is a feedback item?__ -- A `feedback` item is almost the same as a `sketchpad` item. The only difference is that a `feedback` item is not prepared in advance. This means that you can use it to present feedback, which requires up-to-date information about a participant's response. You should not use `feedback` items to present time critical displays, since the fact that it is prepared 'at runtime' means that its timing properties are not as good as that of the `sketchpad` item.

__Feedback and variables__ -- Response items automatically keep track of the accuracy and average response time of the participant in the variables 'acc' (synonym: 'accuracy') and 'avg_rt' (synonym: 'average_response_time') respectively. See also:

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)

__Tip__ -- Make sure that the (foreground) color is set to black. Otherwise you will draw white on white and won't see anything!

__Tip__ -- For more information about feedback, see:

- [/usage/feedback](/usage/feedback)

</div>

## Step 11: Set the length of the practice phase and experimental phase

We have previously created the *practice_loop* and *experiment_loop* items, which both call *block_sequence* (i.e., a block of trials). However, right now they call *block_sequence* only once, which means that both the practice and the experimental phase consist of only a single block of trials.

Click on *practice_loop* to open its tab and set 'Repeat' to '2.00'. This means that the practice phase consists of two blocks.

Click on *experimental_loop* to open its tab and set 'Repeat' to '8.00'. This means that the experimental phase consists of eight blocks.

You can download the experiment up to this point here:

- [tutorial_step11.opensesame.tar.gz][step11]

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- You can create a variable `practice` in both *practice_loop* and *experimental_loop* and set it respectively to 'yes' and 'no'. This is an easy way of keeping track of which trials were part of the practice phase.

</div>

## Step 12: Write the instruction, end_of_practice and end_of_experiment forms

I think you can handle this step your own! Simply open the appropriate tabs and add some text to present instructions, an end-of-practice message and an end-of-experiment message.

You can download the experiment up to this point here:

- [tutorial_step12.opensesame.tar.gz][step12]

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- You can use a subset of HTML tags to format your text. For example, *&lt;b&gt;this will be bold&lt;b&gt;* and *&lt;span color='red'&gt;this will be red&lt;span&gt;*. For more information, see:

- [/usage/text](/usage/text)

</div>

## Step 13: Run the experiment!

You're done! Click on the 'Run in window' (shortcut: `Ctrl+W`) or 'Run fullscreen' (shortcut: `Ctrl+R`) buttons in the toolbar to run your experiment.

You can download the finished experiment here:

- [tutorial.opensesame.tar.gz][finished-experiment]

<div class='info-box' markdown='1'>

### Background box

__Tip__ -- If you want to give your experiment a test run without having to press any keys, you can activate the auto response option (Menu → Run → Enable auto response). In this mode, OpenSesame will simulate the participant's responses.

__Tip__ -- A test run is executed even faster by clicking the orange 'Run in window' button (shortcut: `Ctrl+Shift+W`), which doesn't ask you how to save the logfile (and should therefore only be used for testing purposes).

</div>

## Finally: Some general considerations regarding timing and back-end selection

In the 'General properties' tab of the experiment, you can select a back-end. The back-end is the layer of software that controls the display, input devices, sound, etc. Most experiments will work with all back-ends, but there are reasons to prefer one back-end over the other, mostly related to timing. Currently there are three back-ends (depending on your system, not all three may be available):

- __legacy__ -- a 'safe' back-end, based on PyGame. It provides reliable performance on most platforms, but, due to a lack of hardware acceleration, its timing properties are not as good as those of the other back-ends.
- __psycho__ -- a hardware accelerated back-end, based on PsychoPy [(Peirce, 2007)][references].
- __xpyriment__ -- a hardware-accelerated back-end, based on Expyriment [(Krause & Lindeman, 2013)][references]
- __droid__ -- a back-end that allows you to run your experiment on an Android device with the [OpenSesame runtime for Android](/getting-opensesame/android/).

A detailed discussion of timing-related issues can be found here:

- [/miscellaneous/timing](/miscellaneous/timing)

See also [Damian (2010)][references], [Brand and Bradley (2011)][references], and [Ulrich and Giray (1989)][references] for some general considerations about when to worry, and when not to worry about timing.

<div class='info-box' markdown='1'>

### Background box

For more information about back-ends, see:

- [/back-ends/about](/back-ends/about)

</div>

## References

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. *Social Science Computer Review*. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? *Behavior Research Methods*, *42*, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Time resolution of clocks: Effects on reaction time measurement—Good news for bad clocks. *British Journal of Mathematical and Statistical Psychology*, *42*(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[gpl]: http://dummy.com
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[step1]: /attachments/gaze-cuing/tutorial_step1.opensesame
[step2]: /attachments/gaze-cuing/tutorial_step2.opensesame
[step3]: /attachments/gaze-cuing/tutorial_step3.opensesame
[step4]: /attachments/gaze-cuing/tutorial_step4.opensesame.tar.gz
[step5]: /attachments/gaze-cuing/tutorial_step5.opensesame.tar.gz
[step6]: /attachments/gaze-cuing/tutorial_step6.opensesame.tar.gz
[step7]: /attachments/gaze-cuing/tutorial_step7.opensesame.tar.gz
[step8]: /attachments/gaze-cuing/tutorial_step8.opensesame.tar.gz
[step10]: /attachments/gaze-cuing/tutorial_step10.opensesame.tar.gz
[step11]: /attachments/gaze-cuing/tutorial_step11.opensesame.tar.gz
[step12]: /attachments/gaze-cuing/tutorial_step12.opensesame.tar.gz
[finished-experiment]: /attachments/gaze-cuing/gaze-cuing.opensesame.tar.gz
[python inline scripting]: /python/about
