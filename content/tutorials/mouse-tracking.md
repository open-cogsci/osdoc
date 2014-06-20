---
layout: osdoc
title: Mouse-tracking tutorial
group: Tutorials
permalink: /mouse-tracking/
parser: academicmarkdown
author: Eoin Travers
---

Reproduced from <http://eointravers.github.io/blog/2014/03/os-mousetracking/>.
{: .page-notification}

In my PhD, I'm looking at what process-tracing measures like mouse tracking can tell us about what goes on during high-level reasoning and decision making.  In particular, I'm interested in what this technique can tell us about category-based induction, and reasoning under uncertainty.

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## Mouse Tracking

The idea behind mouse tracking is simple: you records people's mouse movements as they respond to a question, and use them to figure out how drawn they were to each response over the course of the decision.
[Spivey et al (2005)](http://www.pnas.org/content/102/29/10393) introduced the method, showing that phonologically similar words have partially overlapping representations: told to 'Click the candle', participants move as if they're partially drawn towards clicking the 'candy' instead (but not if the alternative is 'pickle').  Since then, the paradigm has been applied to a whole range of questions, including [social categorisation](http://www.dartmouth.edu/~freemanlab/pubs.htm), [lies and deception](http://link.springer.com/article/10.3758/PBR.17.4.486), [lexical decision](http://www.plosone.org/article/info:doi/10.1371/journal.pone.0035932), [pragmatic inference](http://www.sciencedirect.com/science/article/pii/S0749596X13000132), and [learning](http://www.nature.com/srep/2013/130717/srep02210/full/srep02210.html).


### Doing it by hand

Originally, mouse tracking experiments were programmed using in-house software (mostly using PsyScope on OSX, I think), and so there was a barrier to curious researchers applying the method to their own field.  Happily, Jonathon Freeman packaged and released his code as [MouseTracker](http://www.dartmouth.edu/~freemanlab/mousetracker/), allowing researchers to quickly and easily program mouse-tracking experiments, and analyse the huge dataset (for cognitive psychology) the paradigm produces.

However, while immensely useful, MouseTracker is a little inflexible in what your experiment actually looks like, and so for more advanced or exotic experiments it can still be necessary to code them yourself, which is exactly what happened to me.

I got around this by programming my own mouse-tracking experiments in [OpenSesame](http://osdoc.cogsci.nl/), and it's this code that I'm going to share here.  I've also done some work on using HTML5 to run similar experiments in a web browser, which I'll be posting about later.

### OpenSesame

OpenSesame is an open source experiment builder, written in Python. If you're new to OpenSesame, I would recommend you take a look at [this introduction](http://osdoc.cogsci.nl/tutorials/).
Most of what you'll need for most experiments can be built in OpenSesame using just the GUI.
More complicated designs can be created by placing [Python](http://www.python.org/) code in the experiment ('inline code'), and that's what we'll do here.
Mouse-tracking in OpenSesame, you have two options: you can use the GUI to control stimuli, etc., and just use Python code to record the mouse data, or you can control the entire trial using Python code, which is what I'll do here.

<div class='info-box' markdown='1'>

### Mouse Tracking

I've provided the complete `.opensesame` file for this experiment at the bottom of the page, so you don't need to copy and paste from here, although it will help in understanding what's going on.

</div>

## The Experiment

%--
figure:
 id: fig_osmt_blank_experiment
 source: osmt_blank_experiment.png
 caption: |
  New experiment.
--%

Creating a new experiment in OpenSesame, you start with an almost blank template.
The first thing you'll need to do with this is set up some global parameters, by clicking on the experiment object (`New Experiment`) in the Overview panel.
Here, first set the back-end (the software used to interact with your monitor, mouse, and keyboard) to `legacy`, which is the most reliable option.
Your resolution should be the same as that of your computer monitor; larger won't work at all, and smaller leaves a blank border around your experiment.
I like to set a smaller resolution when developing (so that I can run it in a window), and then scale it up for testing.
I've included code in this experiment that compensates for different resolutions to allow this.

The rest here is largely aesthetic, but I've gone for white background, black foreground, and left the font as it is.

You'll need to delete the `getting_started` and the `welcome` items.

### Setting everything up

Before anything else happens, we'll need to define our keyboard, mouse, and canvas (the imaginary page on which your visual stimuli are 'drawn') in Python, so that we can use them later on.
We'll create an `inline_script` item at the very start of your experiment by selecting the `experiment` item in the Overview, and using the 'Append new item' menu.
Then, rename it `setup_script`, and fill it with the following code (in the `Run phase` tab):

{% highlight python %}
# Create our input and output routines
from openexp.mouse import mouse
from openexp.keyboard import keyboard
from openexp.canvas import canvas
my_mouse = mouse(exp, visible=True)
my_keyboard = keyboard(exp)
my_canvas = canvas(exp)
# Declare them as global, so we can use them later on.
global my_mouse, my_keyboard, my_canvas

# Make an empty list
# We'll use this to log our data in a more Python-friendly way
# More on this later
exp.data = []
{% endhighlight %}

Next, we'll set up our actual stimuli. For this silly example, we can imagine we're going to show participants sentences, and ask them to make a true or false judgment.
Place a `loop` after `setup_script` (in real life, you'll want some instructions before the loop too), and make it run a `sequence`. Call them `trial_loop` and `trial_sequence`, to make life easy for yourself. Now you can define your stimuli in `trial_loop` in the usual way (see the picture below).

%--
figure:
 id: fig_osmt_trial_loop
 source: osmt_trial_loop.png
 caption: |
  Defining stimuli.
--%

<div class='info-box' markdown='1'>

### A note on 'variables'

In OpenSesame, there's two distinct things that are referred to as 'variables'.  OpenSesame variables are properties of the experiment itself, and are what the software mostly deals with: they're generated by items in the experiment like `keyboard_response` or `text_input`, and are recorded to the logfile by `logger`.  On the other hand, python variables exist only in the context of an `inline_script` item, and are what we will be using for most of the mouse-tracking code. They can be created, edited, and manipulated within each script, but are not accessible to the rest of the experiment. OpenSesame variables can be imported into an `inline_script` using the function:

{% highlight python %}
variable_name = exp.get("variable_name")
{% endhighlight %}

and python variables can be exported to OpenSesame with:

{% highlight python %}
exp.set("variable_name", variable_name)
{% endhighlight %}

</div>

### The trial

In this example, we're going to place all of the code for a trial in a single `inline_script` at the start of the `trial_sequence`, and call it `question_script`.
In the `Prepare phase` tab of this, we have the following:

{% highlight python %}
# Constants
max_response_time = 3000
fixation_length = 1500
error_message_duration = 1000
max_init_time = 800
sample_rate = 30

# Images
start_button = exp.get_file('materials/start.png')
yes_button = exp.get_file('materials/yes.png')
no_button = exp.get_file('materials/no.png')

# Text
timeout_message = "Too slow!\n\
Try to respond more quickly.\n\
Press any key to continue."
slow_start_message = "\
Please try to move the mouse as soon\n\
as you see the target, even if you're not\n\
sure of your response yet\n\
Press any key to continue."
error_message = "<span color='red'>Wrong!</span>" # Text can use some HTML tags
# Turn our OpenSesame variables into plain Python ones
probe = exp.get('probe')
condition = exp.get('condition')

# Some dimensions
# Our start button is 80x80 pixels.
# Change these values if using a different sized image.
half_start_w = 40
half_start_h = 40
# Likewise for the response images
response_w = 256
response_h = 157
# Get the size of the screen
mx = my_canvas.xcenter()
my = my_canvas.ycenter()

# Some empty lists for recording mouse data
xList, yList, tList = [], [], []
{% endhighlight %}

We're doing a couple of things here: we're telling the experiment how long certain things in the trial should last, providing the images and text to use, turning the OpenSesame variables probe and condition into python variables, telling it how big our images are (so it can figure out when they're being clicked on), and making some empty python lists, which will later be filled with the mouse trajectory data.

Moving on to the `Run phase` tab, there's a lot of code, so I'm going to break it up into chunks here.
First, we have this:

{% highlight python %}
# Draw Start Button
my_canvas.clear()
my_canvas.image(start_button, True, mx, (2*my) - half_start_h)
my_canvas.image(yes_button, False, 0, 0)
my_canvas.image(no_button, False, 2*mx - response_w, 0)
my_canvas.show()

#Wait for click on start button
while 1:
	button, position, timestamp = my_mouse.get_click()
	x, y = position
	if x > mx-half_start_w and x < mx+half_start_w and y > (2*my) - 2*half_start_h:
		my_canvas.clear()
		break

# Hide the mouse
my_mouse.set_visible(visible=False)
# Fixation
tick = fixation_length / 3 # a 'tick' lasts 1/3 of the total fixation.
my_canvas.clear()
my_canvas.image(yes_button, False, 0, 0)
my_canvas.image(no_button, False, 2*mx - response_w, 0)
my_canvas.show()
exp.sleep(tick)
my_canvas.text('+')
my_canvas.image(yes_button, False, 0, 0)
my_canvas.image(no_button, False, 2*mx - response_w, 0)
my_canvas.show()
exp.sleep(tick)
my_canvas.clear()
my_canvas.image(yes_button, False, 0, 0)
my_canvas.image(no_button, False, 2*mx - response_w, 0)
my_canvas.show()
exp.sleep(tick)

# Show the stimuli
my_canvas.clear()
my_canvas.text(probe)
my_canvas.image(yes_button, False, 0, 0)
my_canvas.image(no_button, False, 2*mx - response_w, 0)
my_canvas.show()
# Show the mouse, and move it to the starting point
my_mouse.set_visible(visible=True)
my_mouse.set_pos(pos=(mx, (2*my)-half_start_h))
{% endhighlight %}

What we've done here is show a start button (along with the two responses), and wait for the participant to click the screen. If the click is on the button, it hides the mouse, goes on to the fixation (500 msec blank, 500 msec fixation cross, 500 msec blank), before actually showing the probe text in the middle of the screen, showing the mouse again, and moving it to a start point in the middle of the start button. All those references to 'mx' and 'my' allow this code to work regardless of the actual screen size, otherwise we would have to explicitly use the screen resolution.

Next:

{% highlight python %}
# The actual mouse tracking
t0 = start = exp.time()
t1 = t0 + sample_rate
resp = 0
timed_out = False
slow_start = False
while 1:
	position, timestamp = my_mouse.get_pos()
	if my_mouse.get_pressed()[0]: # A click
		if x < response_w and y < response_h:
			# Clicked response 1
			rt = timestamp - start
			resp = 1
			print 'response 1'
			break
		elif x > (2*mx) - response_w and y < response_h:
			# Clicked response 2
			rt = timestamp - start
			resp = 2
			print 'response 2'
			break
	if timestamp > t1:
		# It's time to record the mouse position
		t1 += sample_rate
		t = timestamp - start
		x, y = position
		xList.append(x)
		yList.append(y)
		tList.append(t)
		if t > max_response_time:
			# Out of time, record a null response.
			timed_out = True
			resp = -1
			rt = None
			print 'Timeout'
			break
{% endhighlight %}

This complicated looking loop does a few things:

* Check if the mouse is being clicked
	* If it is being clicked, check is it over a response, and if so end the loop.
* If a given period has passed since the last sample, record the x and y position of the mouse, and the time.
* If the maximum time allowed has elapsed, end the loop and set the response as -1.

Afterwards, we have this:

{% highlight python %}
# Let's figure out if the response was correct
if condition == 'truth':
	correct_response = 1
else:
	correct_response = 2
accuracy = int(resp == correct_response)

# Figure out if the mouse had left the start button by max_init_time
for i in range(len(yList)):
	y = yList[i]
	if y < ((2*my) - (2*half_start_h)):
		init_step = i # The sample where y left the button
		break
init_time = tList[init_step] # 	The time of that sample
slow_start = int(init_time > max_init_time)

# Show a message if wrong answer (optional)
if accuracy == 0 and not timed_out:
	my_canvas.clear()
	my_canvas.text(error_message)
	my_canvas.show()
	exp.sleep(error_message_duration)

# Show a message if the trial has timed out without a response
if timed_out:
	my_canvas.clear()
	my_canvas.text(timeout_message)
	my_canvas.show()
	timed_out = False
	my_keyboard.get_key()
# Show a message if participant took too long to start moving
if (slow_start and not timed_out):
	my_canvas.clear()
	my_canvas.text(slow_start_message)
	my_canvas.show()
	timed_out = False
	my_keyboard.get_key()
{% endhighlight %}

Most of this is explained in the comments: we figure out if the response was the right one for that condition, and display various messages as necessary.

Finally, we have this:

{% highlight python %}
# Standard Logging (the probe and code variables are taken care of automatically)
self.experiment.set("response", resp)
self.experiment.set("accuracy", accuracy)
self.experiment.set("rt", rt)
self.experiment.set("xTrajectory", str(xList))
self.experiment.set("yTrajectory", str(yList))
self.experiment.set("tTrajectory", str(tList))

# Saves data in as Python variables

# Make a dict to hold data from this trial
trial_data = {}
trial_data['height'] = exp.get('height')
trial_data['subject_nr'] = exp.get('subject_nr')
trial_data['width'] = exp.get('width')
trial_data['probe'] = probe
trial_data['condition'] = condition
trial_data['response'] = resp
trial_data['accuracy'] = accuracy
trial_data['rt'] =rt
trial_data['xTrajectory'] = xList
trial_data['yTrajectory'] = yList
trial_data['tTrajectory'] = tList
trial_data['count_trial_sequence'] = exp.get('count_trial_sequence')

# Add this dict to the list
exp.data.append(trial_data)
{% endhighlight %}

The first bit here turns our python variables (resp, accuracy, rt, xList, yList, tList) into OpenSesame variables, to be saved in the log file.  Note how we're saving the 3 list variables as strings: because OpenSesame saves data in a csv file, it can't save an actual python list (which looks like `[1, 2, 3]`, but instead has to save a string representation of one: `"[1, 2, 3]"`.

The second, which is more novel, makes a python dictionary (dict) item called `trial_data`. We store all the variables we want to log here, along with the appropriate labels, and add it to the list we made at the start. I'll explain what variables you should be including here shortly. Also note (but don't worry too much) that some of what we're logging here is just python variables (resp, accuracy, etc.), while some are OpenSesame variables, retrieved using the `exp.get()` command.

### Logger

After each `question_script`, you'll need to actually write the data to the logfile. The `logger` item in OpenSesame does this in a straightforward way, but it does require a little bit of care in picking the right variables (you could just long everything, but I find this just creates more work down the line).
In our case, it's actually easier to edit the `logger` script than to use the GUI, like so (click the icon shown in %fig_osmt_scripticon):

%--
figure:
 id: fig_osmt_scripticon
 source: osmt_scripticon.png
 caption: The 'Edit script' button.
--%

~~~
set ignore_missing "yes"
set description "Logs experimental data"
set auto_log "no"
set use_quotes "yes"
log "height"
log "subject_nr"
log "width"
log "probe"
log "condition"
log "response"
log "accuracy"
log "rt"
log "xTrajectory"
log "yTrajectory"
log "tTrajectory"
log "count_trial_sequence"
~~~

Most of this is pretty self explanatory; the variable `"count_trial_sequence"` is simply which where this trial is chronologically in the experiment. If your experiment is more complex (and it probably will be), log whatever else is necessary.

Obviously, these are the same variables that we logged in the python logging bit above.

Make sure you click 'Apply and close' when you're done here, or your changes won't be saved.
Afterwards, the logger GUI should have those variables selected.

### Finishing up

OpenSesame automatically saves the csv logfile, even if the experiment crashes, so you don't have to worry about that.
We need to add a few more lines of code to save the python variables though (hopefully, in the future, OpenSesame can do this automatically too).
At the very end of the experiment, create an `inline_script`, and call it `savedata_script`.
Fill it with this (in the `Run phase` tab):

{% highlight python %}
import os
subject_nr = exp.get('subject_nr')
# Save the file as 'subject_1.py', for example, in the same folder as the experiment.
path = os.path.join(exp.experiment_path, 'subject-%i.py' % subject_nr)
saveFile = open(path, "w")
out = "data = " + repr(exp.data)
saveFile.write(out)
saveFile.close()
{% endhighlight %}

This will save the data in a python file with the same name as your csv logfile. The format of the file will be `data = []`, only instead of a blank list, you'll have a list full of dict items for every trial in the experiment.

Note: There's a more robust way of doing this, which I now use instead. This post will be updated with the new method shortly.
{: .page-notification}

I'll be posting in the future about using python to analyse this kind of data, but you can consolidate all these files into a single data structure with something like this (using [Pandas](http://pandas.pydata.org/)):

{% highlight python %}
import pandas as pd
import os

data_dir = 'path/to/datafiles/'
all_data = []

# One big list of trial_dict items
for filename in os.listdir(data_dir): # For all the files in this directory
    if filename[:3] == '.py' # If it's a python file...
    filepath = os.path.join(data_dir, filename)
    exec(filepath) # This executes 'data = [...list...]'
    all_data.append(data)

# Turn it all into a Pandas DataFrame
results = pd.DataFrame(all_data)
results.to_csv('path/to/save/results.csv') # Save as a table
results.to_pickle('path/to/save/results.pkl') # Save as Python variables
{% endhighlight %}

And now we have a mouse-tracking experiment!
If you're interested, give this a go, and let us know how you got on in the comments section. If, in the fullness of time, you use the code in this article to collect data that's being published, please considering citing this page.

Finally, [click here to download the finished experiment](/attachments/mousetracking.zip).
You'll need to keep the folder 'Materials' in the same directory as the experiment for it to work.

