---
layout: osdoc
title: Visual-search tutorial
group: Visual-search tutorial
permalink: /visual-search-tutorial/
level: 0
sortkey: 099.001
show: True
---

*Lotje van der Linden, Aix-Marseille Université, CNRS, Laboratoire de Psychologie Cognitive*

## Introduction

The purpose of the current tutorial is to design three visual search tasks, of increasing complexity, by using Python inline coding. To experience the difference between using only the graphical user interface (GUI) versus using some Python inline coding, we will start by designing the simplest visual search task by using the GUI only (as we did in the step-by-step gaze-cueint tutorial). Next, we'll design the *same* experiment by using some Python inline coding. You'll immediately experience the freedom and efficiency this method provides you with. Next, we'll design two more complex visual search tasks by using Python inline scripting. The most complex task of the three would be ipossible to design in the GUI-only way. But you'll see that doing some programming pays off in the sense that this design looks the most sophistcated and natural, and is the least predictable for the participant. Thus, I think this paradigm taps most into the processes under investigation (i.e. serial versus parallel search, but not other things like predictability).

Experience with the step-by-step tutorial will be assumed. Explanation of Python code will be incidental (if you want do some systematic self study, see REF)

## Background information about visual search

Looking for a yellow bicycle (i.e. a search target) amongst a number of dark-coloured bicycles (distractors) is easier than looking for a black bicycle amongst the same distractors. Also, looking for a black bicycle is easier if it's parked at a place where not much other bicycles are parked, whereas for a yellow bicycle the environment doesn't matter too much: its yellow color will 'pop out' regardless of how many other bicycles are around.

PLAATJE ZOEKEN FIETSEN

![](/img/fig/fig99.1.1.png)

This phonomenon can be translated to the laboratory by presenting a number of simple shapes on a display (see Figure 1), and asking participants to indicate whether a unique shape (the target) is present or absent (Treisman & Gelade, 1980). Typically, search time is shorter if the target differs from the distractors on only a single feature (e.g. the yellow color, in the bicycle example). Also, because participants only have to pay attention to one feature (e.g. color or shape), search can appear in a parallel fashion. As a consequence, the target 'pops out' regardless of the number of simutalenously-presented distractors (see Figure 2)

If, on the other hand, the target only differs from the distractors on a *combination* of features (i.e. color *and* shape), searching for the target is much more difficult, resulting in more errors and longer search times. The idea is that in this 'conjunction-search' condition search occurs in a serial manner: Participants have to attend to the objects one-by-one to look for the unique combination of features. As a consequence, in this condition search time *does* depend on the number of simutalenously-presented distractors (see Figure 2).

![](/img/fig/fig99.1.2.png)


## Implementing this paradigm ourselves:
	
### Simple visual search task
Our first visual search task will only contain four-object displays. You may find that we might as well builtd such a task by using only the GUI (cf. the step-by-step gaze-cuing tutorial). Still, this is not true, because we want to be able to do the following:
	
1. In case of target presence trials, randomise target
2. In case of feature search, randomise whether *all* distractors differ in shape or in color. 3. In case of conjunction search, we want to randomly determine *per* distractor whether it will differ from the target in shape or in color, and where on the display this distractor will occur.

So let's get started.

#### Step 1:
Build the structure of your experiment according to the following information about our paradigm:

- The experiment starts with an instruction display. Participants are instructed to look for a red circle (the target). If the target is present on a given display, they have to press the 'z' key. If not, they have to press the '/'. After reading the instructions, the experiment can be started by pressing any key.
- The experiment contains an experimental loop that repeatedly calls a block sequence.
- The block sequence, in turn, contains a block loop. The block loop repeatedly calls a trial sequence.
- A single trial consists of the following elements:
	- Firstly, a fixation_dot item (1000 ms) indicates the beginning of the trial 
	- Next, the stimuli are presented on the display. We will do this by using an inline_script item! Don't worry about the content of this one yet, simply append it to your trial sequence.
	- Then the participant's response is collected with a keyboard_response item. The allowed responses are 'z' and '/'.
	- And finally all trial info is written to an output file with a logger item

Done? Your overview area should look something like Figure 3 (INSERT FIG), and you should be able to run your experiment without any error messages (although for the moment we'll only see a fixation dot being shown).

![](/img/fig/fig99.1.3.png)


You can download the experiment up to this point here:

#### Step 2: Create the block loop

Our independent variables are:
	
- The search condition (feature or conjunction)
- The presence of the target (present or absent)

This results in a 2x2 factorial design, which you can easily create in your block loop. The result should look like this (INSERT FIG):
	
![](/img/fig/fig99.1.4.png)
	

You can download the experiment up to this point here:

#### Step 3: Declare general variables

Some of the variables of our experiment have values that will not change during our experiment. For example, the color of our target will always be 'red', and its shape will always be 'circle'. Another example is the center of our display. Once calculated, we can use this value throughout our whole experiment. The same holds for the radius of the circles in our experiment. 

It's good practice to declare all those 'constant' variables in an inline_script item at the beginning of your experiment, and then make them global such that they remain available in all subsequent inline_script items.
It's so much more convenient to make a 'myRadius' variable at the beginning of our experiment than to indicate that the radius is, say, 32 for every circle that we'll draw separately. Actually, the latter is even detrimental, for two important reasons: (1) it's very error prone (you can easily accidently type '23' or '332' once in a while), and (2) if you decide to enlarge all your circles to 42 instead of 32, you don't have to change this for every circle separately.

So let's start doing this by using our first inline_script item:
	
- Append an inline_script to the very beginning of our experiment (INSERT FIG)
- And open its *Run phase* tab

Variables are *identifiers*. Identifiers are names given to identify something. Declaring variables is done via the following principle:
	
- You start by the identifier's name. You can name your variables whatever you want, as long as they start with an alphabetical letter or an underscore ('_'). However, it's very good practice to keep your variable names informative (e.g. 'xCen' instead of 'my_variable3' for the variable indicating the coordinate of the vertical meridian).
- The identifier's name is followed by the assignment operator (=). This connects the variable to its value.
- Finally, give the variable it's value (either a number or a string).

Finally, before we start, note that you can add comments (notes for yourself or any other reader of your program) to your inline script by using the '#' sign. Everything to the right of this sign is considered as a comment, and will not be interpreted by Python. It's good practice to make use of comments!
	
ALSO: comments useful to test code....
	
So let's declare some 'constant' variables (see comments for more information):

~~~ .python
# Declare the target properties:
target_col = "red"
target_shape = "rect"

# Declare the sizes of the circles and rectangles:
# Note how you can assign the same value to two 
# different variables:
width = height = 40
radius = 20
~~~

	
We want to present our four objects such that all have an equal distance to the center and the boundaries of the display (see Fig). If we know the resolution of our computer screen, we can calculate four object positions meeting those criteria ourselves. However, it's a much better idea to let OpenSesame determine the screen resolution and let Python do the calculation. This is because this is much faster, less error prone, and has the advantage that we don't have to redo all the caclulations as soon as we switch to a different monitor.

![](/img/fig/fig99.1.5.png)


Use the Python script below to determine the central coordinates as well as the coordinates of the four quadrants:

~~~ .python
# Use the built-in OpenSesame variables 'width' and 'height' 
# to determine the central coordinates. 
# More info about the self.get() function will follow!
x_cen = self.get("width")/2
y_cen = self.get("height")/2

# Define coordinates for the four quadrants:
x_left = x_cen - self.get("width")/4 
x_right = x_cen + self.get("width")/4
y_up = y_cen - self.get("height")/4
y_low = y_cen + self.get("height")/4
~~~

We want to combine the x and y coordinates such that together they reflect a position in one of the four quadrants. We can do this by putting the appropriate x and y coordinates togeter in small lists. The sequential items in a list are put in between square brackets, and are separated by a comma. So (by convention we always start with the x coordinate): 


For more info about lists, see e.g.:
	http://docs.python.org/2/tutorial/datastructures.html#more-on-lists

~~~ .python

# Declare position list
~~~
Finally, we'll have to make all our variables global, such that they will remain available throughout our whole experiment. We'll do this with the following syntax.
MEER UITLEG!

~~~ .python
# Make all variables global:
global target_col, target_shape, width, height, radius, x_cen, y_cen, x_left, x_right, y_up, y_low, upleft, upright, lowleft, lowright
~~~

You can download the experiment up to this point here:

#### Step 4: Use if statements to determine the correct response.
As we wrote in our instructions, participants have to press 'z' if they see a red circle, and '/' if they don't. One easy way to 'tell' OpenSesame about this response rule (such that the response variables 'correct' and 'acc' will be determined correctly) is by simply adding a variable called 'correct_response' to the block loop and determine its value depending on whether the target is present (INSERT Fig). 

But let's do it slightly differently here, just to familiarise ourselves with Python inline coding. Append an inline_script item to the beginning of your trial sequence and call it 'determine_correct_response'. Open its Prepare phase tab.


##### Setting and getting variables:
In an inline_script, we can retrieve (called *get*, from now on) an in-the-GUI-defined variable as follows:

~~~ .python
self.get("target_presence")
~~~

Inversely, we can *set* an in-an-inline-script-defined variable as follows:

~~~ .python
exp.set("correct_response", "z")
~~~

After setting a variable, it becomes available in the GUI and works in the regular way (and, notably, it will be logged by the logger item).

For more info, see also:
	http://osdoc.cogsci.nl/usage/variables-and-conditional-qifq-statements/

##### If statements
Often we want our Python to do different things depending on different situations. For example, we want OpenSesame to mark the response 'z' as correct in a target present trial, but not in a target absent trial. In other words, we don't want Python to always fully execute a series of statements in the same order. Rather, we want to change the flow of our commands depending on the properties of our current trial. This is achieved by using the *if statement*. The if statement evaluates whether a certain condition is true, and, if so, runs a block of statements (called the if-block). Else another block of statements is ran (called the else-block). The latter is optional.

For more info on if statements:
	http://docs.python.org/2/tutorial/controlflow.html#if-statements

Translated to our current situation, we get the following script:
	
~~~ .python
# Determine correct response depending
# on presence of the target:

# 'Get' the presence of the target on the current trial
# by using the built-in 'self.get()' function:
target_pres = self.get('target_presence')

EXPLAIN == 

# If the target is present:
if target_pres == "present":
	correct_resp = "z"
# Else (i.e., if the target is absent):
else:
	correct_resp = "/"
	
# 'Set' the correct response for future use in the GUI.
# Note that we HAVE TO name this variable 'correct_response',
# because OpenSesame will look for this identifier name
# to determine the correctness of a given response, 
# the accuracy score across a number of trials, etc.:
exp.set("correct_response", correct_resp)
~~~

##### Debugging:
Printing stuff to the debug window (which can be opened by clicking the ladybird icon) can be very covenient. For example,

~~~ .python
print target_pres
print correct_resp
~~~

will immediately inform us about whether our if statements worked properly (INSERT FIG). Add the print statements to your code, run the experiment (abort it after a few trials) and check the output in your debug window. 

Did it work? If so, congratulations! 
Imagine how much this small piece of code may already enormously help you in future experiments. For example when your block loop contains many many rows and you don't feel like adding the correct response by hand (which, again, might also be prone to errors).

You can download the experiment up to this point here.

#### Step 5: The stimulus display.

##### The prepare-run strategy.
Until now, we've only used the Prepare phase tab of our inline_script items. But what is the difference with the Run phase tab, and when do you use which?

In general, it is good practice to adhere to the principle of putting time-consuming preparatory stuff (e.g., 'drawing' our objects on a canvas) in the Prepare phase tab, and putting a minimum amount of code in the Run phase tab (e.g., just showing our previously-prepared canvas).

For canvases, this means that we can draw all kinds of objects on a canvas without the objects being visible on the display. Only when we specifically tell OpenSesame to `show()` this canvas, the end result of our 'drawing' will occur on screen (INSERT Fig)

###### Preparing our canvas:
Let's first initialise an empty canvas object by typing the following code in our Prepare phase tab:
	
~~~ .python
# We start by initialising a canvas:
from openexp.canvas import canvas
my_canvas = canvas(exp)
~~~

Let's first make a list containing all four possible object positions. We do this by storing the four (x,y) combintations we determined in our 'general_variables' script into an 'umbrella' list (which will actually be a list of lists, since the (x,y) combinations are small lists in itself):
	
~~~ .python
# Make a list containing the four possible (x,y) combinations:
pos_list = [upleft, upright, lowleft, lowright]
~~~


Now we want to randomise the order of the items in this list. We can do this by using `shuffle()` from the Python library 'random`. Before we can use this function, we'll have to import the module. So:
	
~~~ .python
# Import the module random.shuffle
from random import shuffle
# And shuffle the copied list:
shuffle(pos_list)
~~~


Remember that we should only show a target on the target-present trials. Therefore, the statements that draw a red circle to a given position on the canvas, should occur as an if-block, following an if statement evaluating whether the target is present. So:

~~~ .python
if self.get("target_presence") == "present":
	# something
~~~ 

So let's create the if block. Note that, just as in our 'determine_correct_response' script, all lines being part of the if block should be indented!

We determine the (random) target location by 'popping' one item from our position list. This means that we draw an item without replacing it afterwards. This is good, because we don't want to draw any objects on top of each other (so, a given location should not be used more than once within a given trial):
	
~~~ .python
target_pos = pos_list.pop()
~~~

Remember that target_pos is a small list containing only two items: the x coordinate and the y coordinate. To 'unpack' those values:
	
~~~ .python
x_target, y_target = target_pos
~~~

Now we have all the information we need to draw the target: We know its shape (a circle), its color (red), its radius (radius, as defined in our 'general variables' script) and its location (x_target, y_target).

So let's draw the circle to our canvas. We'll do this by using the built-in canvas.circle() function. This function takes at least three parameters:
	x → The center X coordinate. 
	y → The center Y coordinate. 
	r → The radius. 
Two other parameters are optional (meaning that if you don't provide them, their default values will be used):
	fill → Set to True or False, indicating whether the circle is outlined (False) or filled (True). (Default=False)
	color → A custom human-readable foreground color (e.g. "red" or "#ef2929")

So:
	
~~~ .python
my_canvas.circle(x_target, y_target, radius, fill = True, color = "red")
~~~

Up to this point, the content of the Prepare phase tab of the 'display' item should look like this:
	
~~~ .python
# We start by initialising a canvas:
from openexp.canvas import canvas
my_canvas = canvas(exp)

# Make a list containing the four possible (x,y) combinations:
pos_list = [upleft, upright, lowleft, lowright]

dist_type_list = ["shape", "color"]

# Import the module random
import random
# And shuffle the copied list:
random.shuffle(pos_list)

if self.get('target_presence') == 'present':
	
	# The commands for drawing the target should only be 
	# executed on target-present trials, and therefore form 
	# the if-block of the if statement. All those lines are
	# indented with one tab:

	# Pop one item from the list:
	target_pos = pos_list.pop()
	x_target, y_target = target_pos
	
	# Draw the circle:
	my_canvas.circle(x_target, y_target, radius, fill = True, color = "red")
~~~

###### Debugging:
It's good practice to display your stimuli from time to time, even though your canvas is not entirely prepared yet. A quick-and-dirty way to do this is by TEMPORARILY put the following to lines at the end of your code (don't forget to remove them afterwards!)

~~~ .python
# Show the canvas to the display:
my_canvas.show()
# And pause the experiment for 1 sec:
self.sleep(1000)
~~~

Do you see your target? Don't forget that it's normal that nothing is presented (yet) on half of the trials; the target-absent trials.

# Draw the distractors:
Now it's time to fill all the remaining positions (i.e. three in case of target-present trials, and four in target absence trials). 

Let's first only consider the feature-search condition. In this condition the target differs from the distractors on one feature (and not on a combination of featuers. This means that either all distractors are green circles or all distractors are red squares (see FIG). For the current paradigm, we're not so interested in the way the distractors differ from the target (i.e. we're not going to do such analyses), so we can randomly choose the distractor change per trial. 

To do so, let's first make a list of the two types of possible distractors: distractors differing in shape or distractors differing in color. 

Because we're not in the if-block anymore (meaning that the following script should always be executed, regardless of whether the target is present or not), we restart at indentation level zero (i.e. no indentation)


~~~ .python
dist_change = ["shape", "color"]
~~~

Next, we randomly choose one of the possible distractors by using the random.choice() function. (Note that because we already imported the module `random` in the current inline_script, we don't have to do this again.)

##### The for ... in statement:
We know where to present the distractors: on the remaining (3 or 4) positions in our pos_list. So we can simply walk through those positions and, one by one, use their corresponding (x,y) coordinates. We'll do this by using a for ... in statement. The for in statement iterates over a sequence of objects, that it, it goes through each item in a sequence (i.e. a list, in our case). This is exactly what we need. Just as was the case for the if statement, the block of statements that should be executed for every item in our list is indented:

For more info on for ... in statements, see:
	http://docs.python.org/2/tutorial/controlflow.html#for-statements

~~~ .python
for dist_pos in pos_list:
	# Do something...
~~~

So what does this 'Do something...' constist of? Firstly, we determine the (x,y) coordinates of the current position (note that the following code is indented by one tab):
~~~ .python
	# Again, we can 'unpack' the coordinates as follows:
	x_dist, y_dist = dist_pos
~~~

Next, depending on the distractor type we're going to draw either a red rectangle or a green circle. As you may have guessed, we're going to this with another pair of if ... else statements:

~~~ .python
	if dist_type == "shape":
		# Draw red rectangles...
	else:
		# Draw green circles...
~~~

Let's first consider the "Draw red rectangles..." part, because we haven't practiced with drawing a rectangle yet. We'll do this by using the built-in canvas.rect() function, which takes at least four arguments: 
	x → The left X coordinate. 
	y → The top Y coordinate. 
	w → The width. 
	h → The height. 
The optional arguments (fill and color) work the same as in canvas.circle().

So if the distractor differs from the target in shape:
~~~ .python	
	
	if dist_type == "shape":
	
	# The distractor has a different shape, but the same color:
		dist_col = target_col
		my_canvas.rect(x_dist, y_dist, width, height, fill = True, color = dist_col)
~~~

Are you still using the correct indentation? The if statement is already indented itself (because it's part of our for ... in statement), so the subsequent if block should be indented with *two* tabs.

The "Draw green circles..." part is really similar to what we did before to draw the target (the only difference is the color). Can you figure this one out yourself? Check your progress by temporarily displaying your canvas.

Eventually, your script should look something like this:
	
~~~ .python
# We start by initialising a canvas:
from openexp.canvas import canvas
my_canvas = canvas(exp)

# Make a list containing the four possible (x,y) combinations:
pos_list = [upleft, upright, lowleft, lowright]

# Import the module random:
import random

# And shuffle the copied list:
random.shuffle(pos_list)

if self.get('target_presence') == 'present':

	# Pop one item from the list:
	target_pos = pos_list.pop()
	
	# 'Unpack' the small list containing the (x,y) position:
	x_target, y_target = target_pos
	
	# Draw the circle:
	my_canvas.circle(x_target, y_target, radius, fill = True, color = "red")

# Make a list containing the two possible distractor types:
dist_type_list = ["shape", "color"]

# and randomly pick one:
dist_type = random.choice(dist_type_list)
	
for dist_pos in pos_list:
	
	if dist_type == "shape":
		
		# The distractor has a different shape, but the same color:
		dist_col = target_col
		my_canvas.rect(x_dist, y_dist, width, height, fill = True, color = dist_col)
		
	else:
	
		# The distractor has a different color, but the same shape:
		dist_col = "green"
		my_canvas.circle(x_dist, y_dist, radius, fill = True, color = dist_col)
~~~

##### What about the conjunction-search condition?
So far we applied the same value of our 'dist_type' variable to *all* distractors in a given trial. However, in the conjunction-search condition we need to redefine 'dist_type' for all distractors separately, even *within* a given trial. Implementing this is easier than it sounds. We can simply add a final if statement at the end of our 'for dist_pos' block to verify whether the search condition of the current trial is 'conjunction'. If this is the case, we redefine the dist_type for the subsequent iteration (i.e., we overwrite the previous randomly-chosen dist_type and randomly pick a new one). If the search condition is *not* conjunction, nothing happens (the dist_type will not be overwritten and therefore remains constant across distractors within a given trial).

So:
	
