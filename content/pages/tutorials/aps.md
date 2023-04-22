title: APS tutorial
uptodate: false
translate: false

This OpenSesame workshop was presented at the 25th annual convention of the Association for Psychological Science (APS) on May 26, 2013. The workshop was co-sponsored by the Society of Multivariate Experimental Psychology ([SMEP][]). This page is a slightly modified version of the original workshop page, which can be found [here](/aps2013).

%--
toc:
 mindepth: 2
--%

## The goal

We will create a simple optimal-viewing-position (OVP) experiment with a lexical-decision response. Participants briefly see a five-letter string and decide whether the string is a word or a non-word by pressing a key. The position of the word relative to fixation is varied. The typical finding is that participants are faster to name or discriminate a string of letters when they fixate *just left* of the center [(O'Regan & Jacobs, 1992)](#references). Presumably, this left-wards bias reflects the fact that most western languages are read from left to right, and that the left cerebral hemisphere is specialized in language processing. (When we fixate to the left, most of the word falls in the right visual field and is thus initially processed by the left hemisphere.)

%--
figure:
 id: FigResults
 source: 1.png
 caption: |
  Lexical-decision times are lowest when participants fixate slightly to the left of the word center. In this example, using 7 (blue) and 5 (orange) letter words, the size of this effect is about 0.63 and 0.70 in letter units. [(Adapted from Brysbaert & Nazir, 2005)](#references).
--%

In our experiment, each trial will start with a fixation stimulus, after which a five-letter string will be presented. After 150 ms, the string is masked by five hash-tags. The participant's task is to indicate as quickly and accurately as possible whether the target was a word or a non-word.

%--
figure:
 id: FigTrialSequence
 source: 2.png
 caption: |
  Schematic example of the trial sequence.
--%

The lexical-decision part of the experiment shows how to collect response-time data. To illustrate how you can implement questionnaires, we will also include a consent form and a few questions.

## Step 1: Download and start OpenSesame

You can download OpenSesame from [here][download]. OpenSesame is available for Windows, Linux, Mac OS (experimental), and Android (runtime only). This tutorial is written for OpenSesame 0.27 or later. (Earlier versions of OpenSesame do not support the form functionality that is used for the questionnaires.)

When you start OpenSesame, you will be given a choice of template experiments, and a list of recently opened experiments (if any).

%--
figure:
 id: FigStartup
 source: 3.png
 caption: |
  The OpenSesame window on start-up.
--%

The 'Extended template' provides a good starting point for many experiments, because it already contains the basic structure of a typical block-trial-based experiment. To save time, we will use this template here. Double-click on the 'Extended template' in the 'Get started!' tab.

%--
figure:
 id: FigExtendedTemplate
 source: 4.png
 caption: |
  The structure of the 'Extended template' as seen in the overview area.
--%

<div class='info-box' markdown='1'>

### Background box 1

Let's introduce the basics: OpenSesame experiments are collections of *items*. An item is a small chunk of functionality that, for example, can be used to present visual stimuli (the SKETCHPAD item) or record key presses (the KEYBOARD_RESPONSE item). Items have a type and a name. For example, you might have two KEYBOARD_RESPONSE items, which are called *t1_response* and *t2_response*. To make the distinction between the type and the name of an item clear, we will use `code_style` for types, and *italic_style* for names.

To give structure to your experiment, two types of items are especially important: the LOOP and the SEQUENCE. Understanding how you can combine LOOPs and SEQUENCEs to build experiments is perhaps the trickiest part of working with OpenSesame, so let's get that out of the way first.

A LOOP is where, in most cases, you define your independent variables. In a LOOP you can create a table, where each column corresponds to a variable, and each row corresponds to a single run of the 'item to run'. To make this more concrete, let's consider the following *block_loop*:

%--
figure:
 id: FigLoopTable
 source: 5.png
 caption: |
  An example of variables defined in a loop table. (This example is not related to the experiment created in this tutorial.
--%

This *block_loop* will execute *trial_sequence* four times. Once while `soa` is 100 and `target` is 'F', once while `soa` is 100 and `target` is 'H', etc. The order in which the rows are walked through is random, but can also be set to sequential in the top-right of the tab.

A SEQUENCE consists of a series of items that are executed one after another. A prototypical SEQUENCE is the *trial_sequence*, which corresponds to a single trial. For example, a basic *trial_sequence* might consist of a SKETCHPAD, to present a stimulus, a KEYBOARD_RESPONSE, to collect a response, and a LOGGER, to write the trial information to the log file.

%--
figure:
 id: FigExampleSequence
 source: 6.png
 caption: |
  An example of a SEQUENCE item used as a trial sequence. (This example is not related to the experiment created in this tutorial.
--%

You can combine LOOPs and SEQUENCEs in a hierarchical way, to create trial blocks, and practice and experimental phases. For example, the *trial_sequence* is called by the *block_loop*. Together, these correspond to a single block of trials. One level up, the *block_sequence* is called by the *practice_loop*. Together, these correspond to the practice phase of the experiment.

</div>

## Step 2: Define the independent variables

We will limit ourselves to two independent variables: `word` and `displacement`. The variable `word` simply contains the word that the participant must identify on a given trial. The variable `displacement` is the horizontal displacement of the word in pixels, where 0 is the central position. Fortunately, we do not need to type in all combinations of `word` and `displacement`, but can use the LOOP's variable wizard to generate a factorial design for us. To do this, select the *block_loop* item and click on the 'Variable wizard' button.

Type the variable names on the first row of the variable wizard, an each level at the rows below. For `word`, just select some arbitrary five-letter words and non-words. (Or, if you're a psycholinguist, feel free to make an informed selection.) For `displacement`, we choose -60, -30, 0, 30, and 60. This corresponds to the horizontal displacement in pixels. Later, we will choose the font size such that 30 px corresponds to the width of a single letter. Click on the 'Ok' button to generate your design.

%--
figure:
 id: FigLoopWizard
 source: 7.png
 caption: |
  The loop wizard quickly generates full-factorial designs.
--%

It is often convenient to tell OpenSesame what the correct response is on a given trial, by setting the `correct_response` variable. If you do this, OpenSesame will automatically keep track of feedback variables (`correct`, `avg_rt`, and `acc`) as described [here][feedback].

Click on the 'Add variable' button in the *block_loop*, enter 'correct_response' and press `Enter`. You will now have an empty column for your newly created `correct_response` variable. In the rows with non-words, set `correct_response` to 'm'. In the rows with words, set `correct_response` to 'z'.

%--
figure:
 id: FigLoopTable2
 source: 8.png
 caption: |
  The loop table after you have manually added the `correct_response` variable.
--%

<div class='info-box' markdown='1'>

### Background box 2

You can prepare your variable list in your favorite spreadsheet and copy-paste it into OpenSesame. To do this, you need to make sure that the loop-table in OpenSesame has the proper dimensions (i.e. the correct number of variables and cycles).

</div>

## Step 3: Add items to your trial sequence

Right now, the *trial_sequence* contains only a single SKETCHPAD item, which is called *sketchpad*. We want to have three SKETCHPADs, one for a fixation stimulus, one for the target word, and one for the mask. From the item toolbar, drag a SKETCHPAD item onto the *trial_sequence* item in the overview area. This will add another SKETCHPAD. Do this again to add the third SKETCHPAD. Your *trial_sequence* now looks like this:

%--
figure:
 id: FigTrialSequence2
 source: 9.png
 caption: |
  Your *trial_sequence* after you have added two new sketchpads.
--%

By default, OpenSesame assigns names such as *__sketchpad* to newly created items. These names are not very informative, and it is good practice to change them. You can do this by right-clicking on the items in the overview area, and selecting 'rename'. Here we will rename the SKETCHPADs to *fixation*, *target*, and *mask*.

%--
figure:
 id: Fig10
 source: 10.png
 caption: |
  Your *trial_sequence* after you have give the new sketchpads more informative names.
--%

Often, you want to provide feedback to the participant after every trial. You can do this in various ways, but here we will use a FEEDBACK item. Drag a FEEDBACK item from item toolbar onto the *logger* in the *trial_sequence*. This will cause a new FEEDBACK item to be inserted before the *logger*. Rename the newly created item to *trial_feedback*.

## Step 4: Design the *fixation*, *target*, and *mask* SKETCHPADs

SKETCHPADs are one of the really powerful features of OpenSesame. They allow you to draw your stimulus displays using the built-in drawing tools. You can also use SKETCHPADs to create variably defined displays (i.e. displays that depend on variables), by first creating a prototype display, and then making certain aspects of this display variable. This may sound a bit abstract, but it's actually very easy.

First, click on the *fixation* item. This will open a tab with drawing tools. If you're working on a small screen, this may not fit well on your screen, in which case you can click on 'Open editor in new window' to open a new window with only the drawing tools.

%--
figure:
 id: Fig11
 source: 11.png
 caption: |
  A blank SKETCHPAD item.
--%

A fixation dot is available as a drawing primitive, so you can just click on the fixation-dot icon and then click on the middle of the display to draw a central fixation dot (the coordinates are shown in the top-right, where 0,0 is the center).

However, in OVP studies it is also common to draw two vertical fixation bars, above and below the center, instead of a central fixation dot. I personally find this a bit weird, as it requires participants to fixate in blank space (which I doubt they will do), although I suppose it has the benefit of reduced forward masking. To draw the first fixation bar, click on the line icon to select the line tool and then indicate the beginning and the end of the line by a mouse click. Do the same for the second bar. (Draw whatever fixation stimulus you find most appropriate.)

Right now the duration is set to 'keypress', which means that the *fixation* SKETCHPAD will be shown until the participant presses a key. Change this value to a sensible duration, such as '1000' (ms).

%--
figure:
 id: Fig12
 source: 12.png
 caption: |
  A SKETCHPAD item with fixation bars and a 1000 ms duration.
--%

Next, close the SKETCHPAD window (only if you have opened a new window before) and open the *target* item by clicking on it in the overview area.

The *target* SKETCHPAD should contain only a single word, which we have defined as the variable `word` in the *block_loop*. We want to present this word approximately in the center of the screen, but shifted a bit to the left or the right, depending on the value of the variable `displacement`.

First, click on the 'Ab' icon to select the text tool. When the text tool is selected, a number of controls will appear that let you customize the font etc. In this case, a monospace font (`mono`) of 38 pt will do just fine.

%--
figure:
 id: Fig13
 source: 13.png
 caption: |
  The text drawing-tool of the SKETCHPAD item.
--%

Click on the center of the screen. This will pop up a dialog asking you to specify a text. Enter `[word]` and click on 'Ok'. OpenSesame will automatically interpret the square brackets as indicating that we're dealing with a variable, as described [here][variables].

%--
figure:
 id: Fig14
 source: 14.png
 caption: |
  Text in a SKETCHPAD item. The square brackets indicate that 'word' should be interpreted as a variable name.
--%

Of course, we don't want the word to always be presented in the center. To make the position of the word variable, we need to make a small adjustment to the OpenSesame script. Click on the 'Edit script' button in the top-right of the tab. This will open a script editor that contains the auto-generated script:

	set duration "keypress"
	set description "Displays stimuli"
	draw textline 0.0 0.0 "[word]" center=1 color=white font_family="mono" font_size=38 font_italic=no font_bold=no show_if="always"

To change the horizontal position of the word, you can use the `displacement` variable to indicate the X-coordinate of the stimulus, again using the square-bracket notation, like so :

	draw textline [displacement] 0.0 "[word]" center=1 color=white font_family="mono" font_size=38 font_italic=no font_bold=no show_if="always"

Also, while we're at it, change the duration to 150:

	set duration 150

To apply the changes, click on the 'Apply and close' button at the bottom-right of the tab. You will notice that the word is now no longer visible. Instead, OpenSesame says that one object is not shown, because it is defined using variables. Don't worry, it will be shown during the experiment!

Now it's time to create the mask, which has its own SKETCHPAD item. Click on the *mask* item in the overview area. You will probably find that there is a fixation dot in the center, which is part of the 'Extended template' that you started with. Right-click on the fixation dot and select 'Delete'. Now, draw the mask in the same way that you drew the word, except that you use the text `#####`, instead of `[word]`. Don't forget to set the font size to 38 and to make the X-coordinate of the mask variable!

%--
figure:
 id: Fig15
 source: 15.png
 caption: |
  A string of five hash-tags is used for the mask.
--%

The duration of the *mask* item should be set to 0 (it probably is already, again as a result of the `Extended template`). This might be slightly counter-intuitive, because it suggests that the *mask* will not be shown at all. But what this actually means is that OpenSesame will advance immediately to the next item, which is the *keyboard_response*. Because a *keyboard_response* item will not change what's on the display, the mask will remain visible until the participant presses a key.

## Step 5: Fine-tune the *keyboard_response*

The *keyboard_response* item already works, but it doesn't have a timeout and it reacts to all keys. To improve this, click on *keyboard_response* in the overview area to open its tab.

You don't need to add anything to the 'Correct response' field: If you leave it empty, the variable `correct_response` will be used by default (if your enter, say, '[cresp]', the variable `cresp` would be used instead). In the 'Allowed responses' field, enter 'z;m' to indicate that all keys except `z` and `m` should be ignored. In the 'Timeout' field, add an appropriate timeout value, such as '5000' (ms).

%--
figure:
 id: Fig16
 source: 16.png
 caption: |
  The KEYBOARD_RESPONSE item.
--%

<div class='info-box' markdown='1'>

### Background box 3

The participant's response will be stored as the variable `response`, and the response time as `response_time`. The variable `correct` is either 0 (incorrect) or 1 (correct). If a timeout occurs, `response` will have the value 'None' and `correct` will be 0. For more info, see [here][responses].

</div>

## Step 6: Give content to the *trial_feedback* item

Click on the *trial_feedback* item in the overview area to open its tab. We will add two stimuli and make use of the 'Show if' statement to determine which of these stimuli will actually be shown.

<div class='info-box' markdown='1'>

### Background box 4

FEEDBACK items are virtually identical to SKETCHPAD items, except for the moment at which they are prepared. A SKETCHPAD is prepared before the SEQUENCE that it is part of. This means that, during the SEQUENCE, there will be no lag due to the preparation of the SKETCHPAD. The downside of this approach is that the contents of the sketchpad cannot depend on what happens during the SEQUENCE. Therefore, to give feedback during the trial, we use a FEEDBACK item, which is prepared just as when it is shown. For more information, see [here][prepare-run].

</div>

*Tip: If you are not online, and don't have any image files to use for feedback, you can use red and green fixation dots instead.*

Here are two good stimuli for feedback: A smiley face for correct responses, and a frowney face for incorrect responses.

![](/img/emotes/smiley.png)

![](/img/emotes/frowney.png)

Right-click on the smiley and frowney faces and save them to your computer. Now select the image tool in the FEEDBACK item by clicking on the aquarium-like icon. We will first draw the smiley face, so enter `[correct] = 1` in the 'Show if' field (i.e. show only after a correct response). Next, click in the center of the canvas. This will pop up a file pool dialog, asking you to select an image. Currently, the file pool does not contain any items, so we first need to import the smiley and frowney faces. The easiest way to do this is to drag them into the file-pool selection dialog, from your Downloads folder or wherever the images are located.

%--
figure:
 id: Fig17
 source: 17.png
 caption: |
  The file-pool selection dialog.
--%

Select `smiley.png` and click on the 'Select' button.

Now change the 'Show if' field to `[correct] = 0` and add `frowney.png` to the canvas in the same way. The canvas now contains both images, but only one will be shown during the experiment, depending on whether the participant responds correctly.

Also, change the duration of the *trial_feedback* item to an appropriate value, such as '500' (ms).

<div class='info-box' markdown='1'>

### Background box 5

If you save your experiment in `.opensesame.tar.gz` format, your file pool will be saved along with your experiment. This will make your experiment easily portable between computers!

</div>

## Step 7: Test your experiment so far!

Congratulations, you now have a fully working experiment! Press the 'Run fullscreen' (`Control+R`) button in the main toolbar to run your experiment. To abort your experiment, press `escape`.

<div class='info-box' markdown='1'>

### Background box 6

To quickly test your experiment in a window, you can click on the 'Quick run' button in the main toolbar, or press `Control+Shift+W`.

</div>

## Step 8: Add consent form and questionnaire

So far, the experiment is about collecting single key-press responses to visual stimuli. But, of course, you may often want to collect more complicated, questionnaire-like responses. This can be done using [forms][].

<div class='info-box' markdown='1'>

### Background box 7

If you find that forms are really slow on your system, see [this article][forms-performance].

</div>

Forms are very flexible. A number of commonly-used forms are available as plugins, but almost any kind of form can be easily implemented using [OpenSesame script][forms-opensesame] or, for more advanced users, [Python script][forms-python]. We will start simple, with the `form_consent` plugin. Drag a new `form_consent` from the item toolbar onto the *experiment* SEQUENCE in the overview area. This will add a digital consent form to the start of your experiment.

%--
figure:
 id: Fig18
 source: 18.png
 caption: |
  The `form_consent` plugin.
--%

We will also record the gender, age and handedness of each participant. We could to this by inserting two `form_multiple_choice` items (for gender and handedness) and a `form_text_input` (for age) item into the experiment. That would the easiest way, but it's nicer to combine these questions in a single form. To do this, you need to define your own form with the `form_base` plugin. So drag a new `form_base` item into your experiment, just below *form_consent*.

You will notice that *form_base* does not have any controls. Instead, it just says 'Edit the script to modify the form'. Click on the 'Edit script' button in the top-right of the tab to open the script. Right now, the script is completely empty: The form hasn't been defined yet.

[This article][forms-opensesame] describes in detail how you define custom forms using OpenSesame script. For now, you can just paste the script below into the script editor and press 'Apply'. You can read the comments to get an understanding of how the form syntax works.

	# Four columns, five rows, all of equal size
	set cols 1;1;1;1
	set rows 1;1;1;1;1

	# A bold (using the HTML-like <b></b> tag) title for the form. The title spans
	# all four columns.
	widget 0 0 4 1 label text='<b>Some questions</b>'

	# For the gender, a label in the first column, and checkboxes in the second
	# and third columns. By using the 'group' keyword, selecting one checkbox
	# will deselect other checkboxes in same group. The 'var' keyword specifies
	# in which variable the response (which is the text on the checkbox) should
	# be saved.
	widget 0 1 1 1 label text='Gender' center='no'
	widget 1 1 1 1 checkbox text='Male' group='gender' var='gender'
	widget 2 1 1 1 checkbox text='Female' group='gender' var='gender'

	# For handedness, a label in the first column, and checkboxes in the second,
	# third, and fourth columns.
	widget 0 2 1 1 label text='Handedness' center='no'
	widget 1 2 1 1 checkbox text='Right' group='handedness' var='handedness'
	widget 2 2 1 1 checkbox text='Left' group='handedness' var='handedness'
	widget 3 2 1 1 checkbox text='Bimanual' group='handedness' var='handedness'

	# For age, a label in the first column and a text_input that spans columns
	# two through four.
	widget 0 3 1 1 label text='Age' center='no'
	widget 1 3 3 1 text_input var='age'

	# A button on the last row. Clicking the button will exit the form.
	widget 0 4 4 1 button text='Ok'

The resulting form looks like this (colors and fonts may differ, depending on the settings of your experiment):

%--
figure:
 id: Fig19
 source: 19.png
 caption: |
  A form in action!
--%

<div class='info-box' markdown='1'>

### Background box 8

Forms, and text more generally, support a subset of HTML tags to allow for text formatting (i.e. colors, boldface, etc.). This is described [here][html-subset].

</div>

## Step 9: Specify the number of blocks and trials

Currently, your experiment just consists of a single practice block and a single experimental block, and each block consists of a small number of trials (depending on how many words you entered). You can make your experiment longer by adjusting the 'repeat' setting in the *block_loop*, *practice_loop*, and *experimental_loop* items.

## Step 10: Finished!

%--
figure:
 id: Fig20
 source: 20.png
 caption: |
  Finished!
--%

Your experiment is now finished! Click on the 'Run fullscreen' (`Control+R`) button in the main toolbar to give it a test run.

## References

Brysbaert, M., & Nazir, T. (2005). Visual constraints in written word recognition: evidence from the optimal viewing-position effect. *Journal of Research in Reading*, *28*(3), 216-228. doi:10.1111/j.1467-9817.2005.00266.x
{: .reference}

O'Regan, K. J., & Jacobs, A. M. (1992). Optimal viewing position effect in word recognition: A challenge to current theory. *Journal of Experimental Psychology: Human Perception and Performance*, *18*(1), 185-197. doi:10.1037/0096-1523.18.1.185
{: .reference}

Mathôt, S. (2013, May). *An Introduction to Experiment Building with OpenSesame*. Workshop presented at the APS 25th Annual Convention, Washington, DC, United States. doi:10.6084/m9.figshare.791576
{: .reference}

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social science. *Behavior Research Methods*, *44*(2), 313-324. doi:10.3758/s13428-011-0168-7
{: .reference}

[download]: /getting-opensesame/download/
[feedback]: /usage/feedback/
[forms]: /forms/about/
[forms-opensesame]: /forms/custom-forms/#opensesame-script
[forms-performance]: /forms/performance-issues-and-troubleshooting/
[forms-python]: /forms/custom-forms/#python
[slides]: /attachments/aps2013-workshop-slides.pdf
[variables]: /usage/variables-and-conditional-statements/#using-variables
[responses]: /usage/collecting-responses/
[tutorial]: /usage/step-by-step-tutorial/
[html-subset]: /usage/text-formatting/
[aps-page]: http://aps.psychologicalscience.org/convention/program_2013/search/viewProgram.cfm?Abstract_ID=26153
[smep]: http://www.smep.org/
[pdf]: /aps2013/index.pdf
[prepare-run]: /usage/prepare-run/#sketchpad-feedback
