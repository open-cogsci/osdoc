title: Cats, dogs, and capybaras

%--
figure:
 id: FigMeowingCapybara
 source: meowing-capybara.png
 caption: |
  Don't be fooled by meowing capybaras! ([Source][capybara_photo])
--%

[TOC]

## About

We will create a simple animal-filled multisensory integration task, in which participants see a picture of a dog, cat, or capybara. A meow or a bark is played while the picture is shown. To make things more fun, we will design the experiment so that you can run it on an Android device, using the [OpenSesame runtime for Android](%url:android%). You will see that this requires hardly any additional effort.

The participant reports whether a dog or a cat is shown, by tapping (or clicking) on the left (dog) or right (cat) side of the screen. No response should be given when a capybara is shown: those are catch trials.

We make two simple predictions:

- Participants should be faster to identify dogs when a barking sound is played, and faster to identify cats when a meowing sound is played. In other words, we expect a multisensory congruency effect.
- When participants see a capybara, they are more likely to report seeing a dog when they hear a bark, and more likely to report seeing a cat when they hear a meow. In other words, false alarms are biased by the sound.

## Step 1: Download and start OpenSesame

OpenSesame is available for Windows, Linux, Mac OS (experimental), and Android (runtime only). This tutorial is written for OpenSesame 3.1.X, and you can use either the version based on Python 2.7 (default) or Python 3.5. You can download OpenSesame from here:

- %link:download%

When you start OpenSesame, you will be given a choice of template experiments, and (if any) a list of recently opened experiments (see %FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  The OpenSesame window on start-up.
--%

The 'Droid template' provides a good starting point for creating Android-based experiments. However, in this tutorial we will create the entire experiment from scratch. Therefore, we will continue with the 'default template', which is already loaded when OpenSesame is launched (%FigDefaultTemplate). Therefore, simply close the 'Get started!' and (if shown) 'Welcome!' tabs.

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  The structure of the 'Default template' as seen in the overview area.
--%

<div class='info-box' markdown='1'>

**Background box 1: Basics**

OpenSesame experiments are collections of *items*. An item is a small chunk of functionality that, for example, can be used to present visual stimuli (the SKETCHPAD item) or record key presses (the KEYBOARD_RESPONSE item). Items have a type and a name. For example, you might have two KEYBOARD_RESPONSE items, which are called *t1_response* and *t2_response*. To make the distinction between the type and the name of an item clear, we will use THIS_STYLE for types, and *this style* for names.

To give structure to your experiment, two types of items are especially important: the LOOP and the SEQUENCE. Understanding how you can combine LOOPs and SEQUENCEs to build experiments is perhaps the trickiest part of working with OpenSesame, so let's get that out of the way first.

A LOOP is where, in most cases, you define your independent variables. In a LOOP you can create a table in which each column corresponds to a variable, and each row corresponds to a single run of the 'item to run'. To make this more concrete, let's consider the following *block_loop* (unrelated to this tutorial):

%--
figure:
 id: FigLoopTable
 source: loop-table.png
 caption: |
  An example of variables defined in a loop table. (This example is not related to the experiment created in this tutorial.)
--%

This *block_loop* will execute *trial_sequence* four times. Once while `soa` is 100 and `target` is 'F', once while `soa` is 100 and `target` is 'H', etc. The order in which the rows are walked through is random by default, but can also be set to sequential in the top-right of the tab.

A SEQUENCE consists of a series of items that are executed one after another. A prototypical SEQUENCE is the *trial_sequence*, which corresponds to a single trial. For example, a basic *trial_sequence* might consist of a SKETCHPAD, to present a stimulus, a KEYBOARD_RESPONSE, to collect a response, and a LOGGER, to write the trial information to the log file.

%--
figure:
 id: FigExampleSequence
 source: example-sequence.png
 caption: |
  An example of a SEQUENCE item used as a trial sequence. (This example is not related to the experiment created in this tutorial.)
--%

You can combine LOOPs and SEQUENCEs in a hierarchical way, to create trial blocks, and practice and experimental phases. For example, the *trial_sequence* is called by the *block_loop*. Together, these correspond to a single block of trials. One level up, the *block_sequence* is called by the *practice_loop*. Together, these correspond to the practice phase of the experiment.

</div>

## Step 2: Making your experiment Android-ready

Click on 'New experiment' in the overview area to open the General Properties tab, which contains general options for the experiment. To make your experiment work on Android devices, you need to select the *droid* backend in the 'backend' pull-down menu.

Change the resolution to 1280 × 800 px—the droid backend requires this. You don't have to worry about the actual resolution of the phone/ tablet that you will run the experiment on, because the display will be scaled automatically. But 1280 × 800 px is the resolution that you will develop with.

That's it. You have now made the necessary changes to run your experiment on Android!

<div class='info-box' markdown='1'>

**Background box 2: Backends**

The *backend* is the layer of software that controls the display, input devices, sound, etc. Many experiments will work with all backends, but there are reasons to prefer one backend over the other, mostly related to timing and crossplatform support.

For more information, see:

- %link:backends%

</div>

## Step 3: Add a block_loop and trial_sequence

The default template starts with three items: A `notepad` called *getting_started*, a SKETCHPAD called *welcome*, and a SEQUENCE called *experiment*. We don't need *getting_started* and *welcome*, so let's remove these right away. To do so, right-click on these items and select 'Delete'. Don't remove *experiment*, because it is the entry for the experiment (i.e. the first item that is called when the experiment is started).

Our experiment will have a very simple structure. At the top of the hierarchy is a LOOP, which we will call *block_loop*. The *block_loop* is the place where we will define our independent variables (see also Background box 1). To add a LOOP to your experiment, drag the LOOP icon from the item toolbar onto the *experiment* item in the overview area.

A LOOP item needs another item to run; usually, and in this case as well, this is a SEQUENCE. Drag the SEQUENCE item from the item toolbar onto the *new_loop* item in the overview area. OpenSesame will ask whether you want to insert the SEQUENCE into or after the LOOP. Select 'Insert into new_loop'.

By default, items have names such as *new_sequence*, *new_loop*, *new_sequence_2*, etc. These names are not very informative, and it is good practice to rename them. Item names must consist of alphanumeric characters and/ or underscores. To rename an item, right-click on the item in the overview area and select 'Rename'. Rename *new_sequence* to *trial_sequence* to indicate that it will correspond to a single trial. Rename *new_loop* to *block_loop* to indicate that will correspond to a block of trials.

The overview area of our experiment now looks as in %FigStep3.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  The overview area at the end of Step 3.
--%

<div class='info-box' markdown='1'>

**Background box 3: Unused items**

__Tip__ -- Deleted items are still available in the Unused Items bin, until you select 'Permanently delete unused items' in the Unused Items tab. You can re-add deleted items to your experiment by dragging them out of the Unused Items bin into a SEQUENCE or LOOP.

</div>

## Step 4: Import images and sound files

For this experiment, we will use images of cats, dogs, and capybaras. We will also use sound samples of meows and barks. You can download all the required files from here:

- %static:attachments/cats-dogs-capybaras/stimuli.zip%

Download `stimuli.zip` and extract it somewhere (to your desktop, for example). Next, in OpenSesame, click on the 'Show file pool' button in the main toolbar (or: Menu →View → Show file pool). This will show the file pool, by default on the right side of the window. The easiest way to add the stimuli to the file pool is by dragging them from the desktop (or wherever you have extracted the files to) into the file pool. Alternatively, you can click on the '+' button in the file pool and add files using the file-selection dialog that appears. The file pool will automatically be saved with your experiment if you save your experiment in the `.opensesame.tar.gz` format (which is the default format).

After you have added all stimuli, your file pool looks as in %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  The file pool at the end of Step 4.
--%

## Step 5: Define the experimental variables in the block_loop

Conceptually, our experiment has a fully crossed 3×2 design: We have three types of visual stimuli (cats, dogs, and capybaras) which occur in combination with two types of auditory stimuli (meows and barks). However, we have five exemplars for each stimulus type: five meow sounds, five capybara pictures, etc. From a technical point of view, it therefore makes sense to treat our experiment as a 5×5×3×2 design, in which picture number and sound number are factors with five levels.

OpenSesame is very good at generating full-factorial designs. First, open *block_loop* by clicking on it in the overview area. Next, click on the Full-Factorial Design button. This will open a wizard for generating full-factorial designs, which works in a straightforward way: Every column corresponds to an experimental variable (i.e. a factor). The first row is the name of the variable, the rows below contain all possible values (i.e. levels). In our case, we can specify our 5×5×3×2 design as shown in %FigLoopWizard.

%--
figure:
 id: FigLoopWizard
 source: loop-wizard.png
 caption: |
  The loop wizard generates full-factorial designs.
--%

After clicking 'Ok', you will see that there is now a LOOP table with four rows, one for each experimental variable. There are 150 cycles (=5×5×3×2), which means that we have 150 unique trials. Your LOOP table now looks as in %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  The LOOP table at the end of Step 5.
--%

## Step 6: Add items to the trial sequence

Open *trial_sequence*, which is still empty. It's time to add some items! Our basic *trial_sequence* is:

1. A SKETCHPAD to display a central fixation dot for 500 ms
2. A SAMPLER to play an animal sound
3. A SKETCHPAD to display an animal picture
4. A TOUCH_RESPONSE to collect a response
5. A LOGGER to write the data to file

To add these items, simply drag them one by one from the item toolbar into the *trial_sequence*. If you accidentally drop items in the wrong place, you can simply re-order them by dragging and dropping. Once all items are in the correct order, give each of them a sensible name. The overview area now looks as in %FigStep6.

%--
figure:
 id: FigStep6
 source: step6.png
 caption: |
  The overview area at the end of Step 6.
--%

## Step 7: Define the central fixation dot

Click on *fixation_dot* in the overview area. This opens a basic drawing board that you can use to design your visual stimuli. To draw a central fixation dot, first click on the crosshair icon, and then click on the center of the display, i.e. at position (0, 0).

We also need to specify for how long the fixation dot is visible. To do so, change the duration from 'keypress' to 495 ms, in order to specify a 500 ms duration. (See Background box 4 for an explanation.)

The *fixation_dot* item now looks as in %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: |
  The *fixation_dot* item at the end of Step 7.
--%

<div class='info-box' markdown='1'>

**Background box 4: Selecting the correct duration**

Why specify a duration of 495 if we want a duration of 500 ms? The reason for this is that the actual display-presentation duration is always rounded up to a value that is compatible with your monitor's refresh rate. This may sound complicated, but for most purposes the following rules of thumb are sufficient:

1. Choose a duration that is possible given your monitor's refresh rate. For example, if your monitor's refresh rate is 60 Hz, this means that every frame lasts 16.7 ms (=1000 ms/60 Hz). Therefore, on a 60 Hz monitor, you should always select a duration that is a multiple of 16.7 ms, such as 16.7, 33.3, 50, 100, etc.
2. In the duration field of the SKETCHPAD specify a duration that is a few milliseconds shorter than what you're aiming for. So if you want to present a SKETCHPAD for 50 ms, choose a duration of 45. If you want to present a SKETCHPAD for 1000 ms, choose a duration of 995. Etcetera.

For a detailed discussion of experimental timing, see:

- %link:timing%

</div>

## Step 8: Define the animal sound

Open *animal_sound*. The SAMPLER item provides a number of options, the most important being the sound file that should be played. Click on the browse button to open the file-pool selection dialog, and select one of the sound files, such as `bark1.ogg`.

Of course, we don't want to play the same sound over-and-over again! Instead, we want to select a sound based on the variables `sound` and `sound_nr` that we have defined in the *block_loop* (Step 5). To do this, simply replace the part of the string that you want to have depend on a variable by the name of that variable between square brackets. More specifically, 'bark1.ogg' becomes '[sound][sound_nr].ogg', because we want to replace 'bark' by the value of the variable `sound` and '1' by the value of `sound_nr`.

We also need to change the duration of the SAMPLER. By default, the duration is 'sound', which means that the experiment will pause while the sound is playing. Change the duration to 0. This does not mean that the sound will be played for only 0 ms, but that the experiment will advance right away to the next item, while the sound continues to play in the background. The item *animal_sound* now looks as shown in %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  The item *animal_sound* at the end of Step 8.
--%

<div class='info-box' markdown='1'>

**Background box 5: Variables**

For more information about using variables, see:

- %link:manual/variables%

</div>

## Step 9: Define the animal picture

Open *animal_picture*. Select the image tool by clicking on the button with the landscape-like icon. Click on the center (0, 0) of the display. In the File Pool dialog that appears, select `capybara1.png`. The capybara's sideways glance will now lazily stare at you from the center of the display. But of course, we don't always want to show the same capybara. Instead, we want to have the image depend on the variables `animal` and `pic_nr` that we have defined in the *block_loop* (Step 5).

We can use essentially the same trick as we did for *animal_sound*, although things work slightly differently for images. First, right-click on the capybara and select 'Edit script'. This allows you to edit the following line of OpenSesame script that corresponds to the capybara picture:

	draw image center=1 file="capybara1.png" scale=1 show_if=always x=0 y=0 z_index=0

Now change the name of image file from 'capybara.png' to '[animal][pic_nr].png':

	draw image center=1 file="[animal][pic_nr].png" scale=1 show_if=always x=0 y=0 z_index=0

Click on 'Ok' to apply the change. The capybara is now gone, replaced by a placeholder image, and OpenSesame tells you that one object is not shown, because it is defined using variables. Don't worry, it will be shown during the experiment!

To remind the participant of the task, also add two response circles, one marked 'dog' on the left side of the screen, and one marked 'cat' on the right side. I'm sure you will able to figure out how to do this with the SKETCHPAD drawing tools. My rendition is shown in %FigStep9. Note that these response circles are purely visual, and we still need to explicitly define the response criteria (see Step 10).

Finally, set 'Duration' field to '0'. This does not mean that the picture is presented for only 0 ms, but that the experiment will advance to the next item (*touch_response*) right away. Since *touch_response* waits for a response, but doesn't change what's on the screen, the target will remain visible until a response has been given.

%--
figure:
 id: FigStep9
 source: step9.png
 caption: |
  The *animal_picture* SKETCHPAD at the end of Step 9.
--%

<div class='info-box' markdown='1'>

**Background box 6: Image formats**

__Tip__ -- OpenSesame can handle a wide variety of image formats. However, some (non-standard) `.bmp` formats are known to cause trouble. If you find that a `.bmp` image is not shown, you may want to consider using a different format, such as `.png`. You can convert images easily with free tools such as [GIMP].

</div>

## Step 10: Define the touch response

Open the *touch_response* item. The *touch_response* collects a tap (for devices with a touch screen) or a mouse click (for devices with a mouse) and automatically recodes the response coordinates into discrete response values based on a grid. This may sound a bit abstract, but it simply means the following. The display is divided into a grid and each cell in the grid gets a number. The value of the response is the number of the cell that is tapped/ clicked. For example, if you divide the display into four columns and three rows and the participant taps the cell labeled '7', then the `response` variable will have the value '7' (see %FigTouchResponse).

%--
figure:
 id: FigTouchResponse
 source: touch_response.png
 caption: |
  The `touch_response` item records display taps and mouse clicks and assigns a response value based on a grid.
--%

In our case, we simply divide the screen into a left and a right side, which means that we have to set the number of columns to 2 and the number of rows to 1 (it already is by default). Following the logic shown in %FigTouchResponse, the left side of the display now corresponds to a 1 response, and the right side corresponds to a 2 response. (Note that we are therefore much more liberal than the visual response circles of %FigStep9 suggest, because we accept taps/ clicks anywhere on the screen.)

Finally, we have to make it possible for participants *not* to respond, because the response should be withheld on capybara trials. To do so, change the 'Timeout' field from 'infinite' to '2000'. This means that the response automatically times out after 2000 ms. When this happens, the response is set to 'None' and the experiment continues.

The *touch_response* now looks as in %FigStep10.

%--
figure:
 id: FigStep10
 source: step10.png
 caption: |
  The *touch_response* at the end of Step 10.
--%

## Step 11: Define the correct response

So far, we haven't defined what the correct response is for each stimulus. Typically, this is done by defining a `correct_response` variable in the LOOP table. Response items, such as the *touch_response* automatically use this variable to decide whether a response was correct or not, unless a different correct response is explicitly provided in the item.

Open the *block_loop*. In the top row of the first empty column, enter the name of the variable that you want to create: 'correct_response'. On rows where `animal` is 'dog', set `correct_response` to 1 (i.e. left-side tap). Where `animal` is 'cat', set `correct_response` to 2 (i.e. right-side tap). Where `animal` is 'capybara' set `correct_response` to 'None' (i.e. a timeout). I recommend using some clever copy-pasting to save some time!

## Step 12: Define the logger

We don't need to configure the LOGGER, because its default settings are fine; but let's take a look at it anyway. Click on *logger* in the overview area to open it. You see that the option 'Log all variables (recommended)' is selected. This means that OpenSesame logs everything, which is fine.

<div class='info-box' markdown='1'>

**Background box 8: Always check your data!**

__The one tip to rule them all__ -- Always triple-check whether all the necessary variables are logged in your experiment! The best way to check this is to run the experiment and investigate the resulting log files.

</div>

## Step 13: Add per-trial feedback

It is good practice to inform the participant of whether the response was correct or not. To avoid disrupting the flow of the experiment, this type of immediate feedback should be as unobtrusive as possible. Here, we will do this by briefly showing a green fixation dot after a correct response, and a red fixation dot after an incorrect response.

First, add two new SKETCHPADs to the end of the *trial_sequence*. Rename the first one to *feedback_correct* and the second one to *feedback_incorrect*. Of course, we want to run only one of these items on any given trial, depending on whether or not the response was correct. To do this, we can make use of the built-in variable `correct`, which has the value 0 after an incorrect response, and 1 after a correct response. (Provided that we have defined `correct_response`, which we did in Step 11.) To tell the *trial_sequence* that the *feedback_correct* item should be called only when the response is correct, we use the following run-if statement:

	[correct] = 1

The square brackets around `correct` indicate that this is the name of a variable, and not simply the string 'correct'. Analogously, we use the following run-if statement for the *feedback_incorrect* item:

	[correct] = 0

We still need to give content to the *feedback_correct* and *feedback_incorrect* items. To do this, simply open the items and draw a green or red fixation dot in the center. Also, don't forget to change the durations from 'keypress' to some brief interval, such as 195.

The *trial_sequence* now looks as shown in %FigStep13.

%--
figure:
 id: FigStep13
 source: step13.png
 caption: |
  The *trial_sequence* at the end of Step 13.
--%

<div class='info-box' markdown='1'>

**Background box 9: Conditional statements**

For more information about conditional 'if' statements, see:

- %link:manual/variables%

</div>

## Step 14: Add instructions and goodbye screens

A good experiment always start with an instruction screen, and ends by thanking the participant for his or her time. The easiest way to do this in OpenSesame is with `form_text_display` items.

Drag two `form_text_display`s into the main *experiment* SEQUENCE. One should be at the very start, and renamed to *form_instructions*. The other should be at the very end, and renamed to *form_finished*. Now simply add some appropriate text to these forms, for example as shown in %FigStep14.

%--
figure:
 id: FigStep14
 source: step14.png
 caption: |
  The *form_instructions* item at the end of Step 15.
--%

<div class='info-box' markdown='1'>

**Background box 10: Text**

__Tip__ -- Forms, and text more generally, support a subset of HTML tags to allow for text formatting (i.e. colors, boldface, etc.). This is described here:

- %link:visual%

</div>

## Step 15: Finished!

Your experiment is now finished! Click on the 'Run fullscreen' (`Control+R`) button in the main toolbar to give it a test run. If you have an Android device, you can transfer the experiment file to the device (typically to the SD card), launch the [OpenSesame runtime for Android], and select the experiment file to launch it.

<div class='info-box' markdown='1'>

**Background box 11: Quick run**

__Tip__ -- A test run is executed even faster by clicking the orange 'Run in window' button, which doesn't ask you how to save the logfile (and should therefore only be used for testing purposes).

</div>

## Extra: A smarter way to define the correct response

In Step 11, we have defined `correct_response` variable manually. This works, but it takes time and is prone to mistakes. A smarter way is to use an INLINE_SCRIPT and a bit of deductive logic to determine the correct response for a given trial. First, open *block_loop* and remove the `correct_response` column, because we don't need it anymore. Next, drag an INLINE_SCRIPT from the item toolbar to the start of the *trial_sequence*. In the *prepare* tab of the INLINE_SCRIPT, add the following:

~~~ .python
if var.animal == 'dog':
	var.correct_response = 1
elif var.animal == 'cat':
	var.correct_response = 2
else:
	var.correct_response = None
~~~

So what's going on here? First things first: The reason for putting this code in the *prepare* tab is that every item in a SEQUENCE is called twice. The first phase is called the *prepare* phase, and is used to perform time consuming tasks before the time-critical run phase of the SEQUENCE. Determining the correct response is exactly the type of preparatory stuff that you would put in the *prepare* phase. During the *run* phase, the actual events happen. To give a concrete example, the contents of a SKETCHPAD are created during the *prepare* phase, and during the *run* phase they are merely 'flipped' to the display. For more information about the prepare-run strategy, see:

- %link:prepare-run%

The script itself is almost human-readable language, at least if you know the following: In an INLINE_SCRIPT, experimental variables are properties of the `var` object. So where you would write `[animal]` in OpenSesame script, you write `var.animal` in a Python INLINE_SCRIPT. For more information, see:

- %link:var%

We can summarize the script as follows: If the picture is a dog, the correct response is 1; if the picture is a cat, the correct response is 2; but if the picture is neither (and by exclusion must therefore be a capybara), the correct response is no response, or a timeout (indicated by None).

Finally, let's consider the following variation of the script above:

~~~ .python
if var.animal == 'dog':
	var.correct_response = 1
elif var.animal == 'cat':
	var.correct_response = 2
elif var.animal == 'capybara':
	var.correct_response = None
else:
	raise Exception('%s is not a valid animal!' % var.animal)
~~~

Here we allow for the possibility that an animal is neither a dog, nor a cat, nor a capybara. And if we encounter such an exotic creature, we abort the experiment with an error message, by raising an `Exception`. This may feel like a silly thing to do, because we have programmed the experiment ourselves, and we (think we) know with 100% certainty that it includes only cats, dogs, and capybaras. But it is nevertheless good practice to add these kinds of sanity checks to your experiment, to protect yourself from typos, logical errors, etc. This is called *defensive programming*. The more complex your experiment becomes, the more important defensive programming is. Never assume that your code is bug-free!

## Extra: Add breaks and per-block feedback

Right now, our experiment consists of a single, very long block of trials. In most experiments, you would keep your *block_loop* short (30 trials, say) and repeat it several times with a short break after each block.

However, this approach doesn't work here, because we have a lot of unique trials (150 to be exact), and there is no straightforward way to divide these trials into multiple blocks. (Although it is possible.) Therefore, we will use the following trick: We will add a FEEDBACK item to our *trial_sequence*, and use a run-if statement to call it only after every 50 trials. This is moderately advanced, but follow me!

First add a FEEDBACK item to the end of the *trial_sequence*. Next, assign the following run-if statement to it:

~~~ .python
=var.count_trial_sequence % 50 == 49
~~~

Note that this run-if statement starts with an `=` sign. This indicates that it is Python syntax, instead of the simplified OpenSesame script that you used before (e.g. `[correct] = 0` is OpenSesame script). The use of Python gives us a lot of extra flexibility. The `count_[item name]` variables are built-in variables that keep track of how often an item has been called, starting from 0. In other words, `count_trial_sequence` corresponds to the trial number. Finally, we take the modulo 50 of the trial number and check whether it equals 49. [Modulo] is a mathematical operator that returns the remainder of an integer division. For example, 13 % 5 equals 3, because 5 goes twice into 12 and leaves 3.

Why does this work? If we start counting at 0, we want to insert a break after trials 49, 99, and 149. These trial numbers have in common that their modulo 50 is 49. This is why this run-if statement works.

We still need to add some content to the *feedback* item. OpenSesame automatically keeps track of certain feedback variables, which you can use to inform the participant of his or her performance. For example, the variable `avg_rt` contains the average response time, and `acc` contains the percentage of accurate response. An example of a good feedback display is shown in %FigBreak.

%--
figure:
 id: FigBreak
 source: break.png
 caption: |
  An example FEEDBACK display.
--%

For more information about feedback, see:

- %link:visual%

## References

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}

[OpenSesame runtime for Android]: /getting-opensesame/android
[slides]: /attachments/rovereto2014-workshop-slides.pdf
[modulo]: http://en.wikipedia.org/wiki/Modulo_operation
[pdf]: /rovereto2014/index.pdf
[gimp]: http://www.gimp.org/
[capybara_photo]: https://commons.wikimedia.org/wiki/File:Capybara_Hattiesburg_Zoo_(70909b-58)_2560x1600.jpg
