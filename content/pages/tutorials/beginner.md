title: Beginner tutorial: gaze cuing

[TOC]

## About OpenSesame

OpenSesame is a program for easy of development of behavioral experiments for psychology, neuroscience, and experimental economy. For beginners, OpenSesame has a comprehensive graphical, point-and-click interface. For advanced users, OpenSesame supports Python scripting (not covered in this tutorial).

OpenSesame is freely available under the [General Public License v3][gpl].

## About this tutorial

This tutorial shows how to create a simple but complete psychological experiment using OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012)][references]. You will use mainly the graphical user interface of OpenSesame (i.e., no Python inline coding), although you will make small modifications to the OpenSesame script. This tutorial takes approximately one hour.

## Tutorial screencast

This tutorial is also available as a screencast:

%--
video:
 source: youtube
 id: BeginnerTutorial
 videoid: FCXcnAv9aMA
 width: 640
 height: 360
 caption: |
  A screencast of the beginner tutorial.
--%


## Resources

- __Download__ -- This tutorial assumes that you are running OpenSesame version 3.1.0 or later. To check which version you are running, see the bottom right of the 'Get started' tab (see %FigGetStarted). You can download the most recent version of OpenSesame from:
	- %link:download%
- __Documentation__ -- A dedicated documentation website can be found at:
	- <http://osdoc.cogsci.nl/>
- __Forum__ -- A support forum can be found at:
	- <http://forum.cogsci.nl/>

## The experiment

In this tutorial, you will create a gaze-cuing experiment, as introduced by [Friesen and Kingstone (1998)][references]. In this experiment, a face is presented in the center of the screen (%FigGazeCuing). This face looks either to the right or to the left. A target letter (an 'F' or an 'H') is presented to the left or right of the face. A distractor stimulus (the letter 'X') is presented on the other side of the face. The task is to indicate as quickly as possible whether the target letter is an 'F' or an 'H'. In the congruent condition, the face looks at the target. In the incongruent condition, the face looks at the distractor. As you may have guessed, the typical finding is that participant respond faster in the congruent condition, compared to to the incongruent condition, even though the direction of gaze is not predictive of the target location. This shows that our attention is automatically guided by other people's gaze, even in situations where this doesn't serve any purpose. (And even when the face is just a smiley!)

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  The gaze-cuing paradigm [(Friesen and Kingstone, 1998)][references] that you will implement in this tutorial. This example depicts a trial in the incongruent condition, because the smiley looks at the distractor ('X') and not at the target ('F').
--%

The experiment consists of a practice and an experimental phase. Visual feedback will be presented after every block of trials, and a sound will be played after every incorrect response.

## Experimental design

This design:

- is *within-subject*, because all participants do all conditions
- is *fully-crossed* (or full factorial), because all combinations of conditions occur
- has three conditions (or factors):
    - *gaze side* with three levels (left, right, neutral), or G<sub>3</sub>
    - *target side* with two levels (left, right), or T<sub>2</sub>
    - *target letter* with two levels (F, H), or L<sub>2</sub>
- has N subjects, or <u>S</u><sub>N</sub>

You can write this design as <u>S</u><sub>N</sub>×G<sub>3</sub>×T<sub>2</sub>×L<sub>2</sub>

For more information about this notation for experimental design, see:

- %link:experimentaldesign%

## Step 1: Create the main sequence

When you start OpenSesame, you see the 'Get started!' tab (%FigGetStarted). (If this is the very first time that you have started OpenSesame, you will see a tab that points you towards this tutorial. If so, you can close this tab.) A list of templates is shown below 'Start a new experiment'. These templates provide convenient starting points for new experiments. After you saved an experiment the first time, recently opened experiments are shown under 'Continue with a recent experiment'.

%--
figure:
 id: FigGetStarted
 source: get-started.png
 caption: |
  The 'Get started' dialog on OpenSesame start-up.
--%

Click on 'Default template' to start with a minimal experimental template.

By default there is a main SEQUENCE, which is simply called *experiment*. Click on *experiment* in the overview area (by default on the left side, see %FigInterface) to open its controls in the tab area. The *experiment* SEQUENCE consists of two items: a `notepad` called *getting started* and a SKETCHPAD called *welcome*.

We don't need these two items. Remove *getting_started* by right-clicking on it in the overview area and selecting 'Delete' (shortcut: `Del`). Remove *welcome* in the same way. The *experiment* SEQUENCE is now empty.

%--
figure:
 id: FigInterface
 source: interface.png
 caption: "The default layout of the OpenSesame interface."
--%

<div class='info-box' markdown='1'>

__Background box__

__Names vs types__ -- Items in OpenSesame have a name and a type. The name and type can be the same, but they are usually not. For example, a SKETCHPAD item can have the name *my_target_sketchpad*. To make this distinction clear, we will use `monospace` to indicate item types, and *italics* to indicate names.

__Tip__ -- The 'Extended template' is a good starting point for many experiments. It already contains the basic structure of a trial-based experiment.

__Tip__ -- You can click on the Help icons in the top right of an item's tab to get context-sensitive help.

__Tip__ -- Save (shortcut: `Ctrl+S`) your experiment often! In the unfortunate (and unlikely) event of data loss, you will often be able to recover your work from the back-ups that are created automatically, by default, every 10 minutes (Menu → Tools → Open backup folder).

__Tip__ -- Unless you have used 'Permanently delete' (shortcut: `Shift+Del`), deleted items are still available in the 'Unused items' bin, until you select 'Permanently delete unused items' in the 'Unused items' tab. You can re-add deleted items to a SEQUENCE by dragging them out of the 'Unused items' bin to somewhere in your experiment.

__Tip__ -- %FigExperimentStructure schematically shows the structure of the experiment that you will create. If you get confused during the tutorial, you can refer to %FigExperimentStructure to see where you are.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  A schematic representation of the structure of the 'Gaze cuing' experiment. The item types are in bold face, item names in regular face.
--%

</div>

__Append a form_text_display item for the instruction display__

As the name suggests, a `form_text_display` is a form that displays text. We are going to use a `form_text_display` to give instructions to the participant at the beginning of the experiment.

Click on *experiment* in the overview area to open its controls in the tab area. You will see an empty SEQUENCE. Drag a `form_text_display` from the item toolbar (under 'Form', see %FigInterface) onto the *experiment* SEQUENCE in the tab area. When you let go, a new `form_text_display` item will be inserted into the SEQUENCE. (We will get back to this in Step 12.)

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- You can drag items into the overview area and into SEQUENCE tabs.

__Tip__ -- If a drop action is ambiguous, a pop-up menu will ask you what you want to do.

__Tip__ -- A `form_text_display` only shows text. If you require images etc., you can use a SKETCHPAD item. We will meet the SKETCHPAD in Step 5.

</div>

__Append a loop item, containing a new sequence item, for the practice phase__

We need to append a LOOP item to the *experiment* SEQUENCE. We will use this LOOP for the practice phase of the experiment. Click on the *experiment* SEQUENCE to open its controls in the tab area.

Drag the LOOP item from the item toolbar into the SEQUENCE just the way you added the `form_text_display`. New items are inserted below the item that they are dropped on, so if you drop the new LOOP onto the previously created `form_text_display`, it will appear where you want it: after the `form_text_display`. But don't worry if you drop a new item in the wrong place, because you can always re-order things later.

By itself, a LOOP does not do anything. A LOOP always needs another item to run. Therefore, you have to fill the new LOOP item with another item. (If you view the loop item, you will also see a warning: 'No item specified'.) Drag a SEQUENCE item from the item toolbar onto the LOOP item. A pop-up menu will appear, asking you whether you want to insert the SEQUENCE after or into the LOOP item. Select 'Insert into new_loop'. (We will get back to this in Step 2.)

<div class='info-box' markdown='1'>

__Background box__

__What is a LOOP item?__ -- A LOOP is an item that adds structure to your experiment. It repeatedly runs another item, typically a SEQUENCE. A LOOP is also the place where you will usually define your independent variables, that is, those variables you manipulate in your experiment.

__What is a SEQUENCE item?__ -- A SEQUENCE item also adds structure to your experiment. As the name suggests, a SEQUENCE runs multiple other items in sequence.

__The LOOP-SEQUENCE structure__ -- You often want to repeat a sequence of events. To do this, you will need a LOOP item that contains a SEQUENCE item. By itself, a SEQUENCE does not repeat. It simply starts with the first item and ends with the last item. By 'wrapping' a LOOP item around the SEQUENCE, you can repeat the SEQUENCE multiple times. For example, a single trial usually corresponds to a single SEQUENCE called *trial_sequence*. A LOOP (often called *block_loop*) around this *trial_sequence* would then constitute a single block of trials. Similarly, but at another level of the experiment, a SEQUENCE (often called *block_sequence*) may contain a single block of trials, followed by a FEEDBACK display. A *practice_phase* LOOP around this 'block' SEQUENCE would then constitute the practice phase of the experiment. This may seem a bit abstract right now, but as you follow this tutorial, you will become familiar with the use of LOOPs and SEQUENCEs.

__Tip__ -- For more information about SEQUENCEs and LOOPs, see:

- %link:loop%
- %link:sequence%

</div>

__Append a new form_text_display item for the end-of-practice message__

After the practice phase, we want to inform the participant that the real experiment will begin. For this we need another `form_text_display`. Go back to the *experiment* SEQUENCE, and drag a `form_text_display` from the item toolbar onto the LOOP item. The same pop-up menu will appear as before. This time, select 'Insert after new_loop'. (We will get back to this in Step 12.)

<div class='info-box' markdown='1'>

__Tip__ -- Don't worry if you have accidentally changed a LOOP's item to run. You can undo this easily by clicking the 'Undo' button in the toolbar (`Ctrl+Shift+Z`).

</div>

__Append a new loop item, containing the previously created sequence, for the experimental phase__

We need a LOOP item for the experimental phase, just like for the practice phase. Therefore, drag a LOOP from the item toolbar menu onto *_form_text_display*.

The newly created LOOP (called *new_loop_1*) is empty, and should be filled with a SEQUENCE, just like the LOOP we created before. However, because the trials of the practice and experimental phase are identical, they can use the same SEQUENCE. Therefore, instead of dragging a new SEQUENCE from the item toolbar, you can re-use the *existing* one (i.e. create a linked copy).

To do this, right-click on the previously created *new_sequence*, and select 'Create copy (linked)'. Now, right-click on *new_loop_1* and select 'Paste'. In the pop-up menu that appears, select 'Insert into new_loop 1'.

<div class='info-box' markdown='1'>

__Background box__

__Tip__ — There is an important distinction between *linked* and *unlinked* copies. If you create a linked copy of an item, you create another occurrence of the same item. Therefore, if you modify the original item, the linked copy will change as well. In contrast, if you create an unlinked copy of an item, the copy will be initially look identical (except for its name), but you can edit the original without affecting the unlinked copy, and vice versa.

</div>

__Append a new form_text_display item, for the goodbye message__

When the experiment is finished, we should say goodbye to the participant. For this we need another `form_text_display` item. Go back to the *experiment* SEQUENCE, and drag a `form_text_display` from the item toolbar onto *new_loop_1*. In the pop-up menu that appears, select 'Insert after new_loop_1'. (We will get back to this in Step 12.)

__Give the new items sensible names__

By default, new items have names like *new_sequence* and *new_form_text_display_2*. It is good practice to give items sensible names. This makes it much easier to understand the structure of the experiment. If you want, you can also add a description to each item. Item names must consist of alphanumeric characters and/or underscores.

- Select *new_form_text_display* in the overview area, click on its label in the top of the tab area and rename the item to *instructions*. (Overview-area shortcut: `F2`)
- Rename *new_loop* to *practice_loop*.
- Rename *new_sequence* to *block_sequence*. Because you have re-used this item in *new_loop_1*, the name automatically changes there as well. (This illustrates why it is efficient to create linked copies whenever this is possible.)
- Rename *new_form_text_display_1* to *end_of_practice*.
- Rename *new_loop_1* to *experimental_loop*.
- Rename *new_form_text_display_2* to *end_of_experiment*.

__Give the whole experiment a sensible name__

The experiment in its entirety also has a title and a description. Click on 'New experiment' in the overview area. You can rename the experiment in the same way as you renamed its items. The title currently is 'New experiment'. Rename the experiment to 'Tutorial: Gaze cuing'. Unlike item names, the experiment title may contain spaces etc.

The overview area of your experiment now looks like %FigStep1. This would be a good time to save your experiment (shortcut: `Ctrl+S`).

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area at the end of the step 1.
--%

<div class='info-box' markdown='1'>

__Background box__

__Tip__ — If you don't like having many tabs open, you can close all tabs except the currently opened one by clicking on the 'Close other tabs' button in the main toolbar (shortcut: `Ctrl+T`).

__Tip__ — You can enable 'one tab mode' (Menu -> View -> One tab mode) to prevent multiple tabs from opening simultaneously.

</div>

## Step 2: Create the block sequence

Click on *block_sequence* in the overview. At the moment this SEQUENCE is empty. We want *block sequence* to consist of a block of trials, followed by a  FEEDBACK display. For this we need to do the following:

__Append a reset_feedback item to reset the feedback variables__

We don't want our feedback to be confounded by key presses that participants have made during the instruction phase (or during previous blocks of trials). Therefore, we start each block of trials by resetting the feedback variables. To do this we need a `reset_feedback` item. Grab `reset_feedback` from the item toolbar (under 'Response collection') and drag it onto *block_sequence*.

__Append a new loop, containing a new sequence, for a block of trials__

For a single trial we need a SEQUENCE. For a block of trials, we need to repeat this SEQUENCE multiple times. Therefore, for a block of trials we need to wrap a LOOP around a SEQUENCE. Drag a LOOP from the item toolbar onto *reset_feedback*. Next, drag a SEQUENCE from the item toolbar onto the newly created LOOP, and select 'Insert into new_loop' in the pop-up menu that appears. (We will get back to this in Step 3.)

__Append a feedback item__

After every block of trials we want to give feedback to the participant, so that the participant knows how well he/ she is doing. For this we need a FEEDBACK item. Drag a FEEDBACK from the item toolbar onto *new_loop*, and select 'Insert after loop' in the pop-up menu that appears. (We will get back to this in Step 10.)

__Give the new items sensible names__

Rename: (See Step 1 if you don't remember how to do this.)

- *new_loop* to *block_loop*
- *new_sequence* to *trial_sequence*
- *new_reset_feedback* to *reset_feedback*
- *new_feedback* to *feedback*

The overview of your experiment now looks like %FigStep2. Remember to save your experiment regularly.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%

## Step 3: Fill the block loop with independent variables

As the name suggests, *block_loop* corresponds to a single block of trials. In the previous step we created the *block_loop*, but we still need define the independent variables that will be varied within the block. Our experiment has three independent variables:

- __gaze_cue__ can be 'left' or 'right'.
- __target_pos__ (the position of the target) can be '-300' or '300'. These values reflect the X-coordinate of the target in pixels (0 = center). Using the coordinates directly, rather than 'left' and 'right', will be convenient when we create the target displays (see Step 5).
- __target_letter__ (the target letter) can be 'F' or 'H'.

Therefore, our experiment has 2 x 2 x 2 = 8 levels. Although 8 levels is not that many (most experiments will have more), we don't need to enter all possible combinations by hand. Click on *block_loop* in the overview to open its tab. Now click on the 'Full-factorial design' button. In the variable wizard, you simply define all variables by typing the name in the first row and the levels in the rows below the name (see %FigVariableWizard). If you select 'Ok', you will see that *block_loop* has been filled with all 8 possible combinations.

In the resulting loop table, each row corresponds to one run of *trial_sequence*. Because, in our case, one run of *trial_sequence* corresponds to one trial, each row in our loop table corresponds to one trial. Each column corresponds to one variable, which can have a different value on each trial.

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: |
  The loop variable wizard in Step 3.
--%

But we are not done yet. We need to add three more variables: the location of the distractor, the correct response, and the congruency.

- __dist_pos__ -- On the first row of the first empty column, enter 'dist_pos'. This automatically adds a new experimental variable named 'dist_pos'. In the rows below, enter '300' wherever 'target_pos' is -300, and '-300' wherever 'target_pos' is 300. In other words, the target and the distractor should be positioned opposite from each other.
- __correct_response__ -- Create another variable, in another empty column, with the name 'correct_response'. Set 'correct_response' to 'z' where 'target_letter' is 'F', and to 'm' where 'target_letter' is 'H'. This means that the participant should press the 'z' key if she sees an 'F' and the 'm' key if she sees an 'H'. (Feel free to choose different keys if 'z' and 'm' are awkward on your keyboard layout; for example, 'w' and 'n' are better on AZERTY keyboards.)
- __congruency__ -- Create another variable with the name 'congruency'. Set 'congruency' to 'congruent' where 'target_pos' is '-300' and 'gaze_cue' is 'left', and where 'target_pos' is '300' and 'gaze_cue' is 'right'. In other words, a trial is congruent if the face looks at the target. Set 'congruency' to 'incronguent' for the trials on which the face looks at the distractor. The 'congruency' variable is not necessary to run the experiment; however, it is useful for analyzing the data later on.

We need to do one last thing. 'Repeat' is currently set to '1.00'. This means that each cycle will be executed once. So the block now consists of 8 trials, which is a bit short. A reasonable length for a block of trials is 24, so set 'Repeat' to 3.00 (3 repeats x 8 cycles = 24 trials). You don't need to change 'Order', because 'random' is exactly what we want.

The *block_loop* now looks like %FigStep3. Remember to save your experiment regularly.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- You can prepare your loop table in your favorite spreadsheet program and copy-paste it into the LOOP variable table.

__Tip__ -- You can specify your loop table in a separate file (in `.xlsx` or `.csv`) format, and use this file directly. To do so, select 'file' under 'Source'.

__Tip__ -- You can set 'Repeat' to a non-integer number. For example, by setting 'Repeat' to '0.5', only half the trials (randomly selected) are executed.

</div>

## Step 4: Add images and sound files to the file pool

For our stimuli, we will use images from file. In addition, we will play a sound if the participant makes an error. For this we need a sound file.

You can download the required files here (in most webbrowsers you can right-click the links and choose 'Save Link As' or a similar option):

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

After you have downloaded these files (to your desktop, for example), you can add them to the file pool. If the file pool is not already visible (by default on the right side of the window), click on the 'Show file pool' button in the main toolbar (shortcut: `Ctrl+P`). The easiest way to add the four files to the file pool is to drag them from the desktop (or wherever you have downloaded the files to) into the file pool. Alternatively, you can click on the '+' button in the file pool and add files using the file select dialog that appears. The file pool will be automatically saved with your experiment.

Your file pool now looks like %FigStep4. Remember to save your experiment regularly.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%

## Step 5: Fill the trial sequence with items

A trial in our experiment looks as follows:

1. __Fixation dot__ -- 750 ms, SKETCHPAD item
2. __Neutral gaze__ -- 750 ms, SKETCHPAD item
3. __Gaze cue__ -- 500 ms, SKETCHPAD item
4. __Target__  -- 0 ms, SKETCHPAD item
5. __Response collection__ 	-- KEYBOARD_RESPONSE item
6. __Play a sound if response was incorrect__ --  SAMPLER item
7. __Log response to file__ -- LOGGER item

Click on *trial_sequence* in the overview to open the *trial_sequence* tab. Pick up a SKETCHPAD from the item toolbar and drag it into the *trial_sequence*. Repeat this three more time, so that *trial_sequence* contains four SKETCHPADs. Next, select and append a KEYBOARD_RESPONSE item, a SAMPLER item, and a LOGGER item.

Again, we will rename the new items, to make sure that the *trial_sequence* is easy to understand. Rename:

- *new_sketchpad* to *fixation_dot*
- *new_sketchpad_1* to *neutral_gaze*
- *new_sketchpad_2* to *gaze_cue*
- *new_sketchpad_3* to *target*
- *new_keyboard_response* to *keyboard_response*
- *new_sampler* to *incorrect_sound*
- *new_logger* to *logger*

The *incorrect_sound* item should only be executed if an error was made. To do this, we need to change the 'Run if …' statement to `[correct] = 0` in the *trial_sequence* tab. This works, because the *keyboard_response* item automatically creates a `correct` variable, which is set to `1` (correct), `0` (incorrect), or `undefined` (this relies on the `correct_response` variable that was defined in Step 3). The square brackets indicate that `correct` should be interpreted as the name of a variable and not as text. To change a run-if statement, double click on it (shortcut: `F3`).

The *trial_sequence* now looks like %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%

<div class='info-box' markdown='1'>

__Background box__

__What is a SKETCHPAD item?__ -- A SKETCHPAD is used to present visual stimuli: text, geometric shapes, fixation dots, Gabor patches, etc. You can draw on the SKETCHPAD using the built-in drawing tools.

__What is a KEYBOARD_RESPONSE item?__ -- A KEYBOARD_RESPONSE item collects a single participant's response from the keyboard.

__What is a SAMPLER item?__ -- A SAMPLER item plays a sound from a sound file.

__What is a LOGGER item?__ -- A LOGGER item writes data to the log file. This is very important: If you forget to include a LOGGER item, no data will be logged during the experiment!

__Tip__ -- Variables and conditional "if" statements are very powerful! To learn more about them, see:

- %link:manual/variables%

</div>

## Step 6: Draw the sketchpad items

The SKETCHPAD items that we have created in Step 5 are still blank. It's time to do some drawing!

__Set the background color to white__

Click on *fixation_dot* in the overview area to open its tab. The SKETCHPAD is still black, while the images that we have downloaded have a white background. Oops, we forgot to set the background color of the experiment to white (it is black by default)! Click on 'Tutorial: Gaze cuing' in the overview area to open the 'General properties' tab. Change 'Foreground color' to 'black' and 'Background color' to 'white'.

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- For more fine-grained control over colors, you can also use the hexadecimal RGB notation (e.g., `#FF000` for red) or use the color-picker tool. See also:

- %link:canvas%

</div>

__Draw the fixation dot__

Go back to the *fixation_dot* by clicking on *fixation_dot* in the overview. Now select the fixation-dot element by clicking on the button with the crosshair. If you move your cursor over the sketchpad, you can see the screen coordinates in the top-right. Set the (foreground) color to 'black'. Click on the center of the screen (0, 0) to draw a central fixation dot.

Finally, change the 'Duration' field from 'keypress' to '745', because we want the fixation dot to be presented for 750 ms. Wait ... *why didn't we just specify a duration of 750 ms?* The reason for this is that the actual display-presentation duration is always rounded up to a value that is compatible with your monitor's refresh rate. This may sound complicated, but for most purposes the following rules of thumb are sufficient:

1. Choose a duration that is possible given your monitor's refresh rate. For example, if your monitor's refresh rate is 60 Hz, it means that every frame lasts 16.7 ms (= 1000 ms/60 Hz). Therefore, on a 60 Hz monitor, you should always select a duration that is a multiple of 16.7 ms, such as 16.7, 33.3, 50, 100, etc.
2. In the duration field of the SKETCHPAD specify a duration that is a few milliseconds less than what you're aiming for. So if you want to present a SKETCHPAD for 50 ms, choose a duration of 45. If you want to present a SKETCHPAD for 1000 ms, choose a duration of 995. Etcetera.

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- For a detailed discussion of experimental timing, see:

- %link:timing%

__Tip__ -- The duration of a SKETCHPAD can be a value in milliseconds, but you can also enter 'keypress' or 'mouseclick' to collect a keyboard press or mouse click respectively. In this case a SKETCHPAD will work much the same as a KEYBOARD_RESPONSE item (but with fewer options).

__Tip__ -- Make sure that the (foreground) color is set to black. Otherwise you will draw white on white and won't see anything!

</div>

__Draw the neutral gaze__

Open the *neutral_gaze* SKETCHPAD. Now select the image tool by clicking on the button with the moon-mountain-landscape-like icon. Click on the center of the screen (0, 0). The 'Select file from pool' dialog will appear. Select the file `gaze_neutral.png` and click on the 'Select' button. The neutral gaze image will now stare at you from the center of the screen! Finally, like before, change the 'Duration' field from 'keypress' to '745'. (And note again that this means a duration of 750 ms on most monitors!)

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- OpenSesame can handle a wide variety of image formats. However, some (non-standard) `.bmp` formats are known to cause trouble. If you find that a `.bmp` image is not shown, you can convert it to a different format, such as `.png`. You can convert images easily with free tools such as [GIMP].
</div>

__Draw the gaze cue__

Open the *gaze_cue* SKETCHPAD, and again select the image tool. Click on the center of the screen (0, 0) and select the file `gaze_left.png`.

Obviously, we are not done yet, because the gaze cue should not always be 'left', but should depend on the variable `gaze_cue`, which we have defined in Step 3. However, by drawing the `gaze_left.png` image to the SKETCHPAD, we have generated a script that needs only a tiny modification to make sure that the proper image is shown. Click on the 'Select view' button at the top-right of the *gaze_cue* tab and select 'View script'. You will now see the script that corresponds to the sketchpad that we have just created:

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=always x=0 y=0 z_index=0
~~~

The only thing that we need to do is replace `gaze_left.png` with `gaze_[gaze_cue].png`. This means that OpenSesame uses the variable `gaze_cue` (which has the values `left` and `right`) to determine which image should be shown.

While we are at it, we might as well change the duration to '495' (rounded up to 500!). The script now looks like this:

~~~ .python
set duration 495
set description "Displays stimuli"
draw image center=1 file="gaze_[gaze_cue].png" scale=1 show_if=always x=0 y=0 z_index=0
~~~

Click the 'Apply and close' button at the top right to apply your changes to the script and return to the regular item controls. OpenSesame will warn you that the image cannot be shown, because it is defined using variables, and a placeholder image will be shown instead. Don't worry, the correct image will be shown during the experiment!

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- The variable inspector (shortcut: `Ctrl+I`) is a powerful way to find out which variables have been defined in your experiment, and which values they have (see %FigVariableInspector). When your experiment is not running, most variables don't have a value yet. But when you run your experiment in a window, while having the variable inspector visible, you can see variables changing in real time. This is very useful for debugging your experiment.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "The variable inspector is a convenient way to get an overview of the variables that exist in your experiment."
--%

</div>

__Draw the target__

We want three objects to be part of the target display: the target letter, the distractor letter, and the gaze cue (see %FigGazeCuing). As before, we will start by creating a static display using the SKETCHPAD editor. After this, we will only need to make minor changes to the script so that the exact display depends on the variables.

Click on *target* in the overview to open the target tab and like before, draw the `gaze_left.png` image at the center of the screen. Now select the draw text tool by clicking on the button with the 'A' icon. Change the foreground color to 'black' (if it isn't already). The default font size is 18 px, which is a bit small for our purpose, so change the font size to 32 px. Now click on (-320, 0) in the SKETCHPAD (the X-coordinate does not need to be exactly 320, since we will change this to a variable anyway). Enter "[target_letter]" in the dialog that appears, to draw the target letter (when drawing text, you can use variables directly). Similarly, click on (320, 0) and draw an 'X' (the distractor is always an 'X').

Now open the script editor by clicking on the 'Select view' button at the top-right of the tab and selecting 'View script'. The script looks like this:

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=always x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=always text="[target_letter]" x=-320 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=always text=X x=320 y=0 z_index=0
~~~

Like before, change `gaze_left.png` to `gaze_[gaze_cue].png`. We also need to make the position of the target and the distractor depend on the variables `target_pos` and `dist_pos` respectively. To do this, simply change `-320` to `[target_pos]` and `320` to `[dist_pos]`. Make sure that you leave the `0`, which is the Y-coordinate. The script now looks like this:

~~~ .python
set duration "keypress"
set description "Displays stimuli"
draw image center=1 file="gaze_[gaze_cue].png" scale=1 show_if=always x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=always text="[target_letter]" x=[target_pos] y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=always text=X x=[dist_pos] y=0 z_index=0
~~~

Click on the 'Apply and close' button to apply the script and go back to the regular item controls.

Finally, set the 'Duration' field to '0'. This does not mean that the target is presented for only 0 ms, but that the experiment will advance to the next item (the *keyboard_response*) right away. Since the *keyboard_response* waits for a response, but doesn't change what's on the screen, the target will remain visible until a response has been given.

Remember to save your experiment regularly.

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- Each element of a SKETCHPAD has a 'Show if' option, which specifies when the element should be shown. You can use this to hide/ show elements from a SKETCHPAD depending on certain variables, similar to run-if statements in a SEQUENCE.

__Tip__ -- Make sure that the (foreground) color is set to black. Otherwise you will draw white on white and won't see anything!

</div>

## Step 7: Configure the keyboard response item

Click on *keyboard_response* in the overview to open its tab. You see three options: Correct response, Allowed responses, and Timeout.

We have already set the `correct_response` variable in Step 3. Unless we explicitly specify a correct response, OpenSesame automatically uses the `correct_response` variable if it is available. Therefore, we don't need to change the 'Correct response' field here.

We do need to set the allowed responses. Enter 'z;m' in the allowed-responses field (or other keys if you have chosen different response keys). The semicolon is used to separate responses. The KEYBOARD_RESPONSE now only accepts 'z' and 'm' keys. All other key presses are ignored, with the exception of 'escape', which pauses the experiment.

We also want to set a timeout, which is the maximum interval that the KEYBOARD_RESPONSE waits before deciding that the response is incorrect and setting the 'response' variable to 'None'. '2000' (ms) is a good value.

The KEYBOARD_RESPONSE now looks like %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "The KEYBOARD_RESPONSE at the end of Step 7."
--%

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- By default, the KEYBOARD_RESPONSE will use the `correct_response` variable to determine whether a response was correct. But you can use a different variable as well. To do this, enter a variable name between square brackets (`[my_variable]`) in the correct response field.

__Tip__ -- If 'flush pending key presses' is enabled (it is by default), all pending key presses are discarded when the KEYBOARD_RESPONSE item is called. This prevents carry-over effects, which might otherwise occur if the participant accidentally presses a key during a non-response part of the trial.

__Tip__ -- To use special keys, such as '/' or the up-arrow key, you can use key names (e.g., 'up' and 'space') or associated characters (e.g., '/' and ']'). The 'List available keys' button provides an overview of all valid key names.

</div>

## Step 8: Configure the incorrect (sampler) item

The *incorrect_sound* item doesn't need much work: We only need to select the sound that should be played. Click on *incorrect_sound* in the overview to open its tab. Click on the 'Browse' button and select `incorrect.ogg` from the file pool.

The sampler now looks like %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: "The *incorrect_sound* item at the end of Step 8."
--%

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- You can use variables to specify which sound should be played by using a variable name between square brackets as (part of) the file name. For example: `[a_word].ogg`

__Tip__ -- The SAMPLER handles files in `.ogg` and `.wav` format. If you have sound files in a different format, [Audacity] is a great free tool to convert sound files (and much more).

</div>

## Step 9: Configure the variable logger

Actually, we don't need to configure the variable LOGGER, but let's take a look at it anyway. Click on *logger* in the overview to open its tab. You see that the option 'Log all variables (recommended)' is selected. This means that OpenSesame logs everything, which is fine.

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- If you like your log-files clean, you can disable the 'Log all variables' option and manually select variables, either by entering variable names manually ('Add custom variable'), or by dragging variables from the variable inspector into the LOGGER table.

__The one tip to rule them all__ -- Always triple-check whether all the necessary variables are logged in your experiment! The best way to check this is to run the experiment and investigate the resulting log files.

</div>

## Step 10: Draw the feedback item

After every block of trials, we want to present feedback to the participant to let him/ her know how well he/ she is doing. Therefore, in Step 2, we added a FEEDBACK item, simply named *feedback* to the end of *block_sequence*.

Click on *feedback* in the overview to open its tab, select the draw text tool, change the foreground color to 'black' (if it isn't already), and click at (0, 0). Now enter the following text:

    End of block

    Your average response time was [avg_rt] ms
    Your accuracy was [acc] %

    Press any key to continue

Because we want the feedback item to remain visible as long as the participant wants (i.e. until he/ she presses a key), we leave 'Duration' field set to 'keypress'.

The feedback item now looks like %FigStep_10.

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: "The feedback item at the end of Step 10."
--%

<div class='info-box' markdown='1'>

__Background box__

__What is a feedback item?__ -- A FEEDBACK item is almost identical to a SKETCHPAD item. The only difference is that a FEEDBACK item is not prepared in advance. This means that you can use it to present feedback, which requires up-to-date information about a participant's response. You should not use FEEDBACK items to present time critical displays, because the fact that it is not prepared in advance means that its timing properties are not as good as that of the SKETCHPAD item. See also:

- %link:visual%

__Feedback and variables__ -- Response items automatically keep track of the accuracy and average response time of the participant in the variables 'acc' (synonym: 'accuracy') and 'avg_rt' (synonym: 'average_response_time') respectively. See also:

- %link:manual/variables%

__Tip__ -- Make sure that the (foreground) color is set to black. Otherwise you will draw white on white and won't see anything!

</div>

## Step 11: Set the length of the practice phase and experimental phase

We have previously created the *practice_loop* and *experiment_loop* items, which both call *block_sequence* (i.e., a block of trials). However, right now they call *block_sequence* only once, which means that both the practice and the experimental phase consist of only a single block of trials.

Click on *practice_loop* to open its tab and set 'Repeat' to '2.00'. This means that the practice phase consists of two blocks.

Click on *experimental_loop* to open its tab and set 'Repeat' to '8.00'. This means that the experimental phase consists of eight blocks.

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- You can create a variable `practice` in both *practice_loop* and *experimental_loop* and set it to 'yes' and 'no' respectively. This is an easy way of keeping track of which trials were part of the practice phase.

</div>

## Step 12: Write the instruction, end_of_practice and end_of_experiment forms

I think you can handle this step your own! Simply open the appropriate items and add some text to present instructions, an end-of-practice message, and an end-of-experiment message.

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- You can use a subset of HTML tags to format your text. For example, *&lt;b&gt;this will be bold&lt;b&gt;* and *&lt;span color='red'&gt;this will be red&lt;span&gt;*. For more information, see:

- %link:text%

</div>

## Step 13: Run the experiment!

You're done! Click on the 'Run in window' (shortcut: `Ctrl+W`) or 'Run fullscreen' (shortcut: `Ctrl+R`) buttons in the toolbar to run your experiment.

<div class='info-box' markdown='1'>

__Background box__

__Tip__ -- A test run is executed even faster by clicking the orange 'Run in window' button (shortcut: `Ctrl+Shift+W`), which doesn't ask you how to save the logfile (and should therefore only be used for testing purposes).

</div>

## Finally: Some general considerations regarding timing and backend selection

In the 'General properties' tab of the experiment (the tab that you open by clicking on the experiment name), you can select a backend. The backend is the layer of software that controls the display, input devices, sound, etc. Most experiments work with all backends, but there are reasons to prefer one backend over the other, mostly related to timing. Currently there are four backends (depending on your system, not all three may be available):

- __legacy__ -- a 'safe' backend, based on PyGame. It provides reliable performance on most platforms, but, due to a lack of hardware acceleration, its timing properties are not as good as those of the other backends.
- __psycho__ -- a hardware accelerated backend, based on PsychoPy [(Peirce, 2007)][references].
- __xpyriment__ -- a hardware-accelerated backend, based on Expyriment [(Krause & Lindeman, 2013)][references]
- __droid__ -- a backend that allows you to run your experiment on an Android device with the [OpenSesame runtime for Android](/getting-opensesame/android/).

See also:

- %link:timing%
- %link:backends%

See also [Damian (2010)][references], [Brand and Bradley (2011)][references], and [Ulrich and Giray (1989)][references] for some general considerations about when to worry, and when not to worry about timing.

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

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about
