---
layout: osdoc
title: Rovereto workshop
group: General
parser: academicmarkdown
menuclass: external
permalink: /rovereto2014/
ext_url: /rovereto2014
---

This tutorial is part of an OpenSesame workshop that will be held at the Center for Mind/ Brain Sciences at the University of Trento at May 7th, 9:00.
{: .page-notification}

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## Requirements

### Expertise

- A basic knowledge of experimental design is assumed.

### Laptop

- A laptop is *recommended (but not required)* so that you can walk through the steps of the tutorial yourself. If you bring a laptop, please install OpenSesame before the workshop.
- OpenSesame is available for Windows XP/ 7/ 8, Linux, and Mac OS. If you are running Mac OS, you are advised to verify beforehand that OpenSesame runs properly on your system, as Mac OS support is still experimental.
- If you have an Android tablet or phone, you can bring it along to run your experiment on a tablet! If you do this, please install the [OpenSesame runtime for Android] before the workshop.

### Materials

- The primary resource for the workshop is this page, which can be downloaded in `.pdf` format from [here][pdf]. Print-outs will be available for participants.

## Introduction

You can download the introduction slides from [here][slides].

## About

We will create a simple animal-filled multisensory integration task, in which participants see a picture of a dog, cat, or capybara. In addition, a meowing or barking sound is played. To make things more fun, we will design the experiment so that you can run it on an Android device, using the [OpenSesame runtime for Android]. You will see that this requires hardly any additional effort.

The task is to report whether a dog or a cat is shown, by tapping on the left (dog) or right (cat) side of the screen. No response should be given when a capybara is shown (i.e. those are 'catch trials'). The prediction is simple: When participants should be faster to identify dogs when a barking sound is played, and faster to identify cats when a meowing sound is played. In other words, we expect a multisensory congruency effect. A secondary prediction is that when participants see a capybara, they are more likely to report seeing a dog when they hear a bark, and more likely to report seeing a cat when they hear a meow.

%--
figure:
 id: FiMeowingCapybara
 source: meowing-capybara.png
 caption: |
  Don't be fooled by meowing capybaras!
--%

## Step 1: Download and start OpenSesame

OpenSesame is available for Windows, Linux, Mac OS (experimental), and Android (runtime only). This tutorial is written for OpenSesame 2.8.1 or later. You can download OpenSesame from here:

- <http://osdoc.cogsci.nl/>

When you start OpenSesame, you will be given a choice of template experiments, and a list of recently opened experiments (if any).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  The OpenSesame window on start-up.
--%

The 'Droid template' provides a good starting point for creating an Android-based experiment. However, for this tutorial, we will create the entire experiment from the ground up. Therefore, we will continue with the 'default template', which is loaded by default when OpenSesame is launched.

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  The structure of the 'Default template' as seen in the overview area.
--%

<div class='info-box' markdown='1'>

### Background box 1

Let's introduce the basics: OpenSesame experiments are collections of *items*. An item is a small chunk of functionality that, for example, can be used to present visual stimuli (the `sketchpad` item) or record key presses (the `keyboard_response` item). Items have a type and a name. For example, you might have two `keyboard_response` items, which are called *t1_response* and *t2_response*. To make the distinction between the type and the name of an item clear, we will use `code_style` for types, and *italic_style* for names.

To give structure to your experiment, two types of items are especially important: the `loop` and the `sequence`. Understanding how you can combine `loop`s and `sequence`s to build experiments is perhaps the trickiest part of working with OpenSesame, so let's get that out of the way first.

A `loop` is where, in most cases, you define your independent variables. In a `loop` you can create a table, where each column corresponds to a variable, and each row corresponds to a single run of the 'item to run'. To make this more concrete, let's consider the following *block_loop*:

%--
figure:
 id: FigLoopTable
 source: loop-table.png
 caption: |
  An example of variables defined in a loop table. (This example is not related to the experiment created in this tutorial.)
--%

This *block_loop* will execute *trial_sequence* four times. Once while `soa` is 100 and `target` is 'F', once while `soa` is 100 and `target` is 'H', etc. The order in which the rows are walked through is random, but can also be set to sequential in the top-right of the tab.

A `sequence` consists of a series of items that are executed one after another. A prototypical `sequence` is the *trial_sequence*, which corresponds to a single trial. For example, a basic *trial_sequence* might consist of a `sketchpad`, to present a stimulus, a `keyboard_response`, to collect a response, and a `logger`, to write the trial information to the log file.

%--
figure:
 id: FigExampleSequence
 source: example-sequence.png
 caption: |
  An example of a `sequence` item used as a trial sequence. (This example is not related to the experiment created in this tutorial.)
--%

You can combine `loop`s and `sequence`s in a hierarchical way, to create trial blocks, and practice and experimental phases. For example, the *trial_sequence* is called by the *block_loop*. Together, these correspond to a single block of trials. One level up, the *block_sequence* is called by the *practice_loop*. Together, these correspond to the practice phase of the experiment.

</div>

## Step 2: Select the droid back-end

Click on 'New experiment' in the overview area to open the tab with some general options for the experiment. To have our experiment work on an Android device, we need to select the *droid* back-end in the 'back-end' pull-down menu.

Change the resolution to 1280 x 800 px. You don't have to worry about the actual resolution of the phone/ tablet that you will run the experiment on, because the display will be scaled automatically. But 1280 x 800 px is the resolution that you will assume during the development of your experiment.

And that's it: Your have now made the necessary changes to run your experiment on Android!

<div class='info-box' markdown='1'>

### Background box 2

The back-end is the layer of software that controls the display, input devices, sound, etc. Most experiments will work with all back-ends, but there are reasons to prefer one back-end over the other, mostly related to timing. For more information about back-ends, see:

- [/back-ends/about](/back-ends/about)

</div>

## Step 3: Add a block loop and trial sequence

By default, the experiment contains three items: A `notepad` called *getting_started*, a `sketchpad` called *welcome*, and a `sequence` called *experiment*. We don't need *getting_started* and *welcome*, so let's remove them right away. To do so, simply right-click on these items and select 'Delete'. Don't remove *experiment*: That's the 'top-level' `sequence`, i.e. the `sequence` that is executed when the experiment is started.

The structure of our experiment is very simple. At the top of the hierarchy is a loop, which we will call *block_loop*. The *block_loop* is the place where you define your independent variables (see also [Background box 1]). To add a `loop` to your experiment, simply drag the `loop` icon from the item toolbar onto the *experiment* item in the overview area.

A `loop` item always needs another item to run, and therefore you will see a dialog asking you whether you want to create a new item for the `loop` or whether you want to select an existing item. We want to create a new `sequence` for our loop, so select `sequence` in the pull-down menu labeled 'Create new item to use' and click on the 'Create' button.

By default, items have names such as *sequence*, *loop*, *_sequence*, etc. These names are not very informative, and it is good practice to rename them. Item names must consist of alphanumeric characters and/ or underscores. To rename an item, simply right-click on the item in the overview area and select 'Rename'. Rename *sequence* to *trial_sequence* to indicate that it will correspond to a single trial. Rename *loop* to *block_loop* to indicate that will correspond to a block of trials.

The overview area of our experiment now looks as in %FigStep3.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  The overview area at the end of Step 3.
--%

<div class='info-box' markdown='1'>

### Background box 3

__Tip__ -- Deleted items are still available in the 'Unused items' bin, until you select 'Permanently delete unused items' in the 'Unused items' tab. You can re-add deleted items to a `sequence` using the 'Append existing item' button (%FigAppendExisting).

</div>

## Step 4: Import images and sound files

For this experiment, we will use images of cats, dogs, and capybaras. We will also use sound samples of meows and barks. You can download all the required files from here:

- [/attachments/cats-dogs-capybaras/stimuli.zip](/attachments/cats-dogs-capybaras/stimuli.zip)

Download `stimuli.zip` and extract it somewhere (to your desktop, for example). Now, in OpenSesame, click on the 'Show file pool' button in the main toolbar (or: Menu →View → Show file pool). This will show the file pool, by default on the right side of the window. The easiest way to add the stimuli to the file pool is by dragging them from the desktop (or wherever you have extracted the files to) into the file pool. Alternatively, you can click on the '+' button in the file pool and add files using the file select dialog that appears. The file pool will be automatically saved with your experiment if you save your experiment in the `.opensesame.tar.gz` format (which is the default format).

After you have added all the stimuli, your file pool looks as in %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  The file pool at the end of Step 4.
--%

## Step 5: Define the experimental variables in the block loop

Conceptually, our experiment has a fully crossed 3x2 design: We have three types of visual stimuli (cats, dogs, and capybaras) which occur in combination with two types of auditory stimuli (meows and barks). However, we have five exemplars for each stimulus type: five meow sounds, five capybara pictures, etc. From a technical point of view, it therefore makes sense to treat our experiment as a 5x5x3x2 design, in which picture number and sound number are factors with five levels.

OpenSesame is very good at generating full-factorial designs. First, open the *block_loop* by clicking on it in the overview area. Next, click on the 'Variable wizard' button. The variable wizard is a tool that helps you to quickly generate a full-factorial design, such as the one that we want to create here. It works in a very straightforward way: Every column corresponds to an experimental variable (i.e. a factor). The first row is the name of the variable, the rows below contain all possible values (i.e. levels). In our case, we can specify our 5x5x3x2 design as shown in %FigLoopWizard.

%--
figure:
 id: FigLoopWizard
 source: loop-wizard.png
 caption: |
  The loop wizard is a convenient way to generate full-factorial designs.
--%

If you click on 'Ok', you will see that there is a `loop` table with four rows, one for each experimental variable. There are 150 loops (=5x5x3x2), which means that we have 150 unique trials. Your `loop` table now looks as in %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  The `loop` table at the end of Step 5.
--%

## Step 6: Add items to the trial sequence

Open *trial_sequence* by clicking on it in the overview area. You will see that the `sequence` is empty: It doesn't contain any items. It is time to add some!

Our basic *trial_sequence* looks as follows:

1. A `sketchpad` to display a central fixation dot for 500 ms.
2. A `sampler to play back a sound. The sound will play in the background while the picture is shown and the response is collected.
3. A `sketchpad` to display the animal picture.
4. A `touch_response` to collect a response.
5. A `logger` to write the data to file.

To add these items, simply drag them one by one from the item toolbar into the *trial_sequence*. If the order of the *trial_sequence* is incorrect, you can open the *trial_sequence* and re-order the items by dragging them by their grab-handle (i.e. the four-square icon on the left). Once all items are in the correct order, give each of them a sensible name. The overview area now looks as shown in %FigStep6.

%--
figure:
 id: FigStep6
 source: step6.png
 caption: |
  The overview area at the end of Step 6.
--%

## Step 7: Define the central fixation dot

Click on *fixation_dot* in the overview area. This will open a basic drawing board that you can use to design your stimulus displays. To draw a central fixation dot, first click on the fixation-dot icon (with the small gray circle) and then click on the center of the display, i.e. at position `0, 0`.

We also need to specify for how long the fixation dot is visible. To do so, change the duration from 'keypress' to 495 ms, in order to specify a 500 ms duration. But wait ... *why didn't we just specify a duration of 500 ms?* The reason for this is that the actual display-presentation duration is always rounded up to a value that is compatible with your monitor's refresh rate. This may sound complicated, but for most purposes the following rules of thumb are sufficient:

1. Choose a duration that is possible given your monitor's refresh rate. For example, if your monitor's refresh rate is 60 Hz, it means that every frame lasts 16.7 ms (=1000 ms/60 Hz). Therefore, on a 60 Hz monitor, you should always select a duration that is a multiple of 16.7 ms, such as 16.7, 33.3, 50, 100, etc.
2. In the duration field of the `sketchpad` specify a duration that is a few milliseconds shorter than what you're aiming for. So if you want to present a `sketchpad` for 50 ms, choose a duration of 45. If you want to present a `sketchpad` for 1000 ms, choose a duration of 995. Etcetera.

<div class='info-box' markdown='1'>

### Background box 4

__Tip__ -- For a detailed discussion of experimental timing, see:

- [/miscellaneous/timing](/miscellaneous/timing)

__Tip__ -- The duration of a `sketchpad` can be a value in milliseconds, but you can also enter 'keypress' or 'mouseclick' to collect a keyboard press or mouse click respectively. In this case a `sketchpad` will work much the same as a `keyboard_response` item (but with fewer options).

</div>

## Step 8: Define the animal sound

Open *animal_sound*. You will see that the `sampler` item provides a number of options, the most important one of which is the sound file that is to be played. Click on the browse button to open the file-pool selection dialog, and select one of the sound files, such as `bark1.ogg`.

Of course, we don't want to play the same sound over-and-over again. Instead, we want to select a sound based on the variables `sound` and `sound_nr` that we have defined in the *block_loop* (Step 5). To do this, simply replace the part of the string that you want to depend on a variable by the name of that variable between square brackets. More specifically, 'bark1.ogg' becomes '[sound][sound_nr].ogg', because we want to replace 'bark' by the value of the variable `sound` and '1' by the value of `sound_nr`.

We also need to change the duration of the `sampler`. By default, the duration is 'sound', which means that the experiment will pause while the sound is playing. Change the duration to 0. This does not mean that the sound will be played for only 0 ms, but that the experiment will advance right away to the next item, while the sound continues playing in the background. The item *animal_sound* now looks as shown in %FigStep8.


%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  The item *animal_sound* at the end of Step 8.
--%

<div class='info-box' markdown='1'>

### Background box 5

For more information about using variables, see:

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)

</div>

## Step 9: Define the animal picture

Open *animal_picture*. This will again open a `sketchpad` drawing board. Now select the image tool by clicking on the button with the aquarium-like icon. Click on the center of the screen (0, 0). The 'Select file from pool' dialog will appear. Select the file `capybara1.png` and click on the 'Select' button. The capybara will now stare at you lazily from the center of the screen! But of course, as with the sound, we don't always want to present the same image. Instead, we want to have the image depend on the variables `animal` and `pic_nr` that we have defined in the *block_loop* (Step 5).

We can do this in a very similar way as we did for *animal_sound*, although it is slightly more complex. First, right-click on the capybara and select 'Edit'. This will allow you to edit the following line of script that corresponds to the capybara picture:

	draw image 0.0 0.0 "capybara1.png" scale=1.0 center=1 show_if="always"

Now change the name of image file from 'capybara.png' to '[animal][pic_nr].png' ...

	draw image 0 0 "[animal][pic_nr].png" scale=1 center=1 show_if="always"

... and click on 'Ok' to apply the change. The capybara is now gone, and you will see a message saying that one object is not shown, because it is defined using variables. Don't worry, it will be shown during the experiment!

To help the participant, we will also add two response circles, one marked 'dog' on the left side of the screen, and one marked 'cat' on the right side. I'm sure you will able to figure out how to do this with the `sketchpad` drawing tools. My version is shown in %FigStep9. Note that these response circles are purely visual, and we still need to explicitly define the response criteria (see Step 10).

Finally, set 'Duration' field to '0'. This does not mean that the picture is presented for only 0 ms, but that the experiment will advance to the next item (the *touch_response*) right away. Since the *touch_response* waits for a response, but doesn't change what's on the screen, the target will remain visible until a response has been given.

%--
figure:
 id: FigStep9
 source: step9.png
 caption: |
  The *animal_picture* `sketchpad` at the end of Step 9.
--%

<div class='info-box' markdown='1'>

### Background box 6

__Tip__ -- OpenSesame can handle a wide variety of image formats. However, some (non-standard) `.bmp` formats are known to cause trouble. If you find that a `.bmp` image is not shown, you may want to consider using a different format, such as `.png`. You can convert images easily with free tools such as [GIMP].

</div>

## Step 10: Define the touch response

Open the *touch_response* item. The *touch_response* collects a tap (for devices with a touch screen) or a mouse click (for devices with a mouse) and automatically recodes the response coordinates into discrete response values, based on a grid. This may sound a bit abstract, but it simply means the following. The display is divided into a grid and each cell in the grid gets a number. The value of the response is the number of the cell that is tapped/ clicked. For example, if you divide the display into four columns and three rows and the participant taps the cell labeled '7', then the `response` variable will have the value '7' (see %FigTouchResponse).

%--
figure:
 id: FigTouchResponse
 source: touch_response.png
 caption: |
  The *touch_response* item records display taps and mouse clicks and assigns a response value based on a grid.
--%

In our case, we simply divide the screen into a left and a right side, which means that we have to set the number of columns to 2 and the number of rows to 1 (it is by default). Following the logic shown in %FigTouchResponse, the left side of the display now corresponds to a 1 response, and the right side corresponds to a 2 response. (Note that we are therefore much more liberal than the visual response circles of %FigStep9 suggest.)

Finally, we have to make it possible for participants *not* to respond, because the response should be withheld on capybara trials. To do so, we change the 'Timeout' field from 'infinite' to '2000'. This means that the response will automatically time out after 2000 ms. When this happens, the response will be set to 'None' and the experiment will continue.

The *touch_response* now looks as in %FigStep10.

%--
figure:
 id: FigStep10
 source: step10.png
 caption: |
  The *touch_response* at the end of Step 10.
--%

## Step 11: Define the correct response

So far, we have not 'told' our experiment what the correct response is for each stimulus. The typical way to specify a correct response is to define a `correct_response` variable in the `loop` table. Response items, such as the *touch_response* will automatically use this variable to decide whether a response was correct or not,  unless a different correct response is explicitly provided in the item. (For a slightly more advanced solution, see [Background box 7].)

Open the *block_loop*. Click on 'Add variable' and add a variable named 'correct_response'. This will add a long empty column to the table. On rows where `animal` is 'dog', set `correct_response` to 1 (i.e. left-side tap). Where `animal` is 'cat', set `correct_response` to 2 (i.e. right-side tap). Where `animal` is 'capybara' set `correct_response` to 'None' (i.e. a timeout). I recommend using some clever copy-pasting to do save some time!

<div class='info-box' markdown='1'>

### Background box 7

Alternatively, we can use a little bit of deductive logic to determine the correct response for a given trial. To do so, we need some minor Python scripting. Drag an `inline_script` item from the item toolbar to the start of the *trial_sequence*. Open the *prepare* tab of the `inline_script` and add the following script:

{% highlight python %}
if self.get('animal') == 'dog':
	exp.set('correct_response', 1)
elif self.get('animal') == 'cat':
	exp.set('correct_response', 2)
else:
	exp.set('correct_response', None)
{% endhighlight %}

So what's going on here?

First things first: Why do we need to put this code in the *prepare* tab of the `inline_script`? The reason for this is that every item in a `sequence` is called twice. The first phase is called the *prepare* phase, and is used to perform time consuming tasks before the time-critical run phase of the `sequence`. During the *run* phase, the actual events happen. For example, a the contents of a `sketchpad` are created during the *prepare* phase, and during the *run* phase it is merely 'flipped' to the display. For more information about the prepare-run strategy, see:

- [/usage/prepare-run/](/usage/prepare-run/)

The script itself is almost human readable, at least if you know the following. Firstly, to retrieve an experimental variable in an `inline_script`, you need to use `self.get()`. So where you would write `[animal]` in OpenSesame script, you write `self.get('animal')` in a Python `inline_script`. Secondly, to define an experimental variable, you need to use `exp.set()`. So to set the variable `correct_response` to `2`, you call `exp.set('correct_response', 2). For more information, see:

- [/python/about/](/python/about/)

So we can summarize the script as follows: If the picture is a dog, the correct response is 1. But if the picture is a cat, the correct response is 2. If the picture is neither (and by exclusion must therefore be a capybara), the correct response is no response, or a timeout.

</div>

## Step 12: Define the logger

Actually, we don't need to configure the `logger`, but let's take a look at it anyway. Click on *logger* in the overview to open it. You will see that the option 'Automatically detect and log all variables' is selected. This means that OpenSesame logs everything, which is fine.

<div class='info-box' markdown='1'>

### Background box 8

__Tip__ -- If you like your log-files clean, you can disable the 'auto-select' option and manually select variables to log or use the 'Smart select' button. 'Smart select' will select 1) all variables that are defined in the `loop`s, 2) all variables offered by the response items, and  3) the `count_[item name]` variables of all `sequence` items, which keep track of how often a particular `sequence` has been executed (essentially these are trial and block counters).

__The one tip to rule them all__ -- Always triple-check whether all the necessary variables are logged in your experiment! The best way to check this is to run the experiment and investigate the resulting log files.

</div>

## Step 13: Add per-trial feedback

It is good practice to inform the participant on each trial of whether the response was correct or not. To avoid disrupting the flow of the experiment, this type of per-trial feedback should be as unobtrusive as possible. Here, we will do this by briefly showing a green fixation dot after a correct response, and a red fixation dot after an incorrect response.

First, add two new `sketchpad`s to the end of the *trial_sequence*. Rename the first one to *feedback_correct* and the second one to *feedback_incorrect*. Of course, we want to select one of these items on any given trial, depending on whether or not the response was correct. To do this, we can make use of the built-in variable `correct`, which has the value 0 after an incorrect response, and 1 after a correct response. (Provided that we have defined the `correct_response` variable, which we did in Step 11.) To tell the *trial_sequence* that the *feedback_correct* item should be called only when the response is correct, we use the following run-if statement:

	[correct] = 1

The square brackets around `correct` mean that this is the name of a variable, and not simply the string 'correct'. Analogously, we use the following run-if statement for the *feedback_incorrect* item:

	[correct] = 0

We still need to give content to the *feedback_correct* and *feedback_incorrect* items. To do, simply open them and draw a green or red fixation dot in the center. Also, don't forget to change the durations from 'keypress' to some brief interval, such as 195.

The *trial_sequence* now looks as shown in %FigStep13.

%--
figure:
 id: FigStep13
 source: step13.png
 caption: |
  The *trial_sequence* at the end of Step 13.
--%

<div class='info-box' markdown='1'>

### Background box 9

For more information about conditional 'if' statements, see:

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)

</div>

## Step 14: Add breaks and per-block feedback

Right now, our experiment consists of a single, very long block of trials.

Usually, we would keep our *block_loop* short (30 trials, say) and have it followed by a `feedback` item. Then you could repeat the *block_loop* - *feedback* sequence multiple times to create a multi-block experiment.

However, this typical approach doesn't work here, because we have a lot of unique trials (150 to be exact), and there is no straightforward way to divide these trials over multiple blocks. Therefore, we will use the following trick: We will add a `feedback` item to our *trial_sequence*, and use a run-if statement to call it only after every 50 trials. This is moderately advanced, but follow me!

First add a `feedback` item to the end of the *trial_sequence*. Next, assign the following run-if statement to it:

{% highlight python %}
=self.get('count_trial_sequence') % 50 == 49
{% endhighlight %}

The first thing to note is that this run-if statement starts with an `=` sign. This means that it is Python syntax, instead of the simplified OpenSesame script that you used before (e.g. `[correct] = 0` is OpenSesame script). Using Python gives us a lot of extra flexibility. Next, we retrieve the value of the experimental variable `count_trial_sequence`. The `count_[item name]` variables are built-in variables that keep track of how often an item has been called, starting from 0. In other words, `count_trial_sequence` corresponds to the trial number. Next, we take the modulo 50 of the trial number. [Modulo] is an mathematical operator that returns the remainder of an integer division. For example, `12 % 5` equals `2`, because 5 goes twice into 12 and leaves 2.

Now here's some modest mathematics: If we start counting at 0, we want to insert a break after trial 49, 99, 149, and 199. These trial numbers have in common that their modulo 50 is 49. This is why this run-if statement works. Get it?

Now, we still need to add some content to the *feedback* item. OpenSesame automatically keeps track of a number of feedback variables, which you can use to inform the participant of his or her performance. For example, the variable `avg_rt` contains the average response time, and `acc` contains the percentage of accurate response. An example of a good feedback display is shown in %FigStep14.

For more information about feedback, see:

- [/usage/feedback/](/usage/feedback/)

%--
figure:
 id: FigStep14
 source: step14.png
 caption: |
--%

<div class='info-box' markdown='1'>

### Background box 10

For more information about feedback, see:

- [/usage/feedback/](/usage/feedback/)

</div>

## Step 15: Add instructions and goodbye screens

A good experiment always start with an instruction screen, and ends by thanking the participant for his or her time. The easiest way to do this in OpenSesame is using `form_text_display` items.

Drag two `form_text_display`s into the main *experiment* `sequence`. Move one to the very start, one the very end, and give them sensible names (e.g. *form_instructions* and *form_finished*). Now simply add some appropriate text to these forms, for example as shown in %FigStep15.

%--
figure:
 id: Step15
 source: step15.png
 caption: |
  The *form_instructions* item at the end of Step 15.
--%

<div class='info-box' markdown='1'>

### Background box 11

Forms, and text more generally, support a subset of HTML tags to allow for text formatting (i.e. colors, boldface, etc.). This is described here:

- [/usage/text/](/usage/text/)

</div>

## Step 16: Finished!

Your experiment is now finished! Click on the 'Run fullscreen' (`Control+R`) button in the main toolbar to give it a test run.

<div class='info-box' markdown='1'>

### Background box 12

__Tip__ -- A test run is executed even faster by clicking the orange 'Run in window' button, which doesn't ask you how to save the logfile (and should therefore only be used for testing purposes).

</div>

[OpenSesame runtime for Android]: /getting-opensesame/android
[slides]: http://to.do/
[modulo]: http://en.wikipedia.org/wiki/Modulo_operation
[pdf]: http://todo.do/
