title: Intermediate tutorial (JavaScript): visual search
uptodate: false

[TOC]

## About OpenSesame

OpenSesame is a user-friendly program for the development of behavioral experiments for psychology, neuroscience, and experimental economy. For beginners, OpenSesame has a comprehensive graphical, point-and-click interface. For advanced users, OpenSesame supports Python (desktop only) and JavaScript (desktop and browser).

OpenSesame is freely available under the [General Public License v3][gpl].

## About this tutorial

This tutorial shows how to create a basic visual-search experiment using OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012)][references]. We will use both the graphical interface and JavaScript. Some experience with OpenSesame and JavaScript is recommended. This tutorial takes approximately one hour.

A Python-based version of this tutorial is also available. If you don't need to run your experiments online, then the Python tutorial is likely what you need:

- %link:tutorials/intermediate%


## Resources

- __Download__ — This tutorial assumes that you are running OpenSesame version 3.3.10 or later and OSWeb 1.4 or later. You can download the most recent version of OpenSesame from:
	- %link:download%
- __Documentation__ — A dedicated documentation website can be found at:
	- <http://osdoc.cogsci.nl/>
- __Forum__ — A support forum can be found at:
	- <http://forum.cogsci.nl/>


## The experiment

In this tutorial, you will create a basic visual-search experiment. The experiment resembles the classic visual-search studies of [Treisman and Gelade (1980)][references], but it is not identical.

Before starting to *build* the experiment for yourself, you can already *participate* in it. This will give you a good idea of what you're working towards in this tutorial.

<a role="button" class="btn btn-success btn-align-left" href="https://jatos.mindprobe.eu/publix/1938/start?batchId=2191&generalMultiple">Participate in the experiment!</a>

In this experiment, participants search for a target object, which can be a yellow square, a yellow circle, a blue square, or a blue circle; the identity of the target is varied between blocks of trials. Participants indicate whether the target is present or not by pressing the right (present) or left (absent) arrow key.

In addition to the target, zero or more distractor objects are shown. There are three conditions, and the condition determines what kind of distractors there are:

- In the *Conjunction* condition, distractors can have any shape and color, with the only restriction that distractors cannot be identical to the target. So, for example, if the target is a yellow square, then distractors are yellow circles, blue circles, and blue squares.
- In the *Shape Feature* condition, distractors have a different shape from the target, but can have any color. So, for example, if the target is a yellow square, then distractors are yellow circles and blue circles.
- In the *Color Feature* condition, distractors can have any shape, but have a different color from the target. So, for example, if the target is a yellow square, then distractors are blue squares and blue circles.

Immediate feedback is shown after each trial: a green dot after a correct response, and a red dot after an incorrect response. Detailed feedback on average response times and accuracy is shown after each block of trials.

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg
 caption: |
  The visual-search experiment that you will implement in this tutorial.
--%

Experiments like this show two typical findings:

- It takes more time to find the target in the Conjunction condition than in the two Feature conditions.
- In the Conjunction condition, response times increase as the number of distractors increases. This suggests that people search for the target one item at a time; this is called *serial search*.
- In the Feature conditions (both shape and color), response times do not, or hardly, increase as the the number of distractors increases. This suggests that people process the entire display at once; this is called *parallel search*.

According to Treisman and Gelade's feature-integration theory, these results reflect that the Conjunction condition requires that you combine, or *bind*, the color and shape of each object. This binding requires attention, and you therefore need to shift your attention from one object to the next; this is slow, and explains why response times depend on how many objects there are. In contrast, in the Feature conditions, color and shape do not need to be bound, and therefore the whole display can be processed in a single sweep without attention being directed at each and every object.

## Experimental design

This design:

- Is *within-subject*, because all participants do all conditions
- Is *fully-crossed* (or full factorial), because all combinations of conditions occur
- Has three conditions (or factors):
	- Varied within blocks:
		- `set_size` with three levels (1, 5, 15), or SS<sub>3</sub>
		- `condition` with three levels (conjunction, feature_shape, feature_color), or CN<sub>3</sub>
		- `target_present` with two levels (present, absent), or TP<sub>2</sub>
	- Varied between blocks:
		- `target_shape` with two levels (square, circle), or TS<sub>2</sub>
		- `target_color` with two levels (yellow, blue), or TC<sub>2</sub>
- Has N subjects, or <u>S</u><sub>N</sub>

You can write this design as <u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub>

For more information about this notation for experimental design, see:

- %link:experimentaldesign%

## Step 1: Create the basic structure of the experiment

Start OpenSesame and, in the 'Get started!' tab, select the Extended template. This template provides the basic structure that is common to many cognitive-psychology experiments, such as the one that we will create here.

The Extended template contains a few items that we don't need. Delete the following items:

- *about_this_template*
- *practice_loop*
- *end_of_practice*

When you have deleted these items, they are still visible in the 'Unused items' bin. To permanently delete these items, click on the 'Unused items' bin, and then click on the 'Permanently delete unused items' button.

Finally, give the experiment a good title, such as 'Visual search'. To do this, open the general-properties tab (by clicking on 'Extended template' in the overview area) and click on the experiment name to edit it.

The overview area should now look like %FigStep1:

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area at the end of step 1.
--%

## Step 2: Define experimental variables that are varied between blocks

As described above, two variables are varied between blocks in our experiment: `target_shape` and `target_color`. We therefore need to define these variables in the *experimental_loop*. To understand why, consider the structure shown in %FigStep1, starting from the bottom (i.e. the most indented level).

- *trial_sequence* corresponds to a single trial
- *block_loop* corresponds to a block of a trials
	- Therefore, variables defined here vary for each run of *trial_sequence*; in other words, variables defined in *block_loop* are varied __within blocks__.
- *block_sequence* corresponds to a block of trials, preceded by resetting of the feedback variables, and followed by participant feedback
- *experimental_loop* corresponds to multiple blocks of trials
	- Therefore, variables defined here vary for each run of *block_sequence*; in other words, variables defined in *experimental_loop* are varied __between blocks__.
- *experiment* corresponds to the entire experimental, which is an instruction screen, followed by multiple blocks of trials, followed by an end-of-experiment screen

Click on experimental loop, and define:

- `target_shape`, which can be 'square' or 'circle'; and
- `target_color`, which can be 'yellow' or 'blue'.

We have a full-factorial design, which means that all 2 × 2 = 4 combinations must occur. The table of *experimental_loop* should now look like %FigStep2:

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The table of *experimental_loop* at the end of step 2.
--%

## Step 3: Give instructions at the start of each block

Right now, the experiment starts with a single *instructions* screen. In our case, we want to give instructions before each block of trials, to tell the participant what target to look for (because the identity of the target varies between blocks).

__Move the instructions into block_sequence__

Therefore, pick up the *instructions* item and drag it onto *block_sequence*. A pop-up will appear, asking you if you want to:

- Insert the item into *block_sequence*, in which case *instructions* would become the first item of *block_sequence*; or
- Insert the item after *block_sequence*, in which case *instructions* would move to a position after *block_sequence*.

Select the first option ('Insert into'). Now *block_sequence* starts with an instructions screen, which is what we want.

__Add instructional text__

Click on *instructions* to open it, and add a good instructional text, such as:

```text
INSTRUCTIONS

Search for the [target_color] [target_shape]

Press the right-arrow key if you find it
Press the left-arrow key if you don't

Press any key to begin
```

The square brackets around '[target_color]' and '[target_shape]' indicate that these are not literal text, but refer to the variables that we have defined in *experimental_loop*. When the experiment runs, the values of these variables will appear here, and the participant will see (for example), 'Search for the yellow circle'.

__Give a visual preview of the target__

It also good to show the participant the actual stimulus that she needs to find. To do this:

- Draw a filled circle at the center of the display (make sure it doesn't overlap with the text);
- Change the color of the circle to '[target_color]'. This means that the color of the circle depends on the value of the variable `target_color`; and
- Change the show-if statement to '[target_shape] = circle'.

In other words, we have drawn a circle of which the color is determined by `target_color`; furthermore, this circle is only shown when the variable `target_shape` has the value 'circle'. For more information about variables and show-if statements, see:

- %link:manual/variables%

We use the same trick to draw a square:

- Draw a filled square at the center of the display;
- Change the color of the square to '[target_color]'; and
- Change the show-if statement to '[target_shape] = square'

The *instructions*  screen should now look like %FigStep3:

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  The *instructions* screen at the end of step 3.
--%

## Step 4: Define experimental variables that are varied within blocks

Three variables are varied within blocks in our experiment: `condition`, `set_size`, and `target_present`. As described under Step 2, we need to define these variables in the *block_loop* so that they vary for each run of *trial_sequence*.

The three variables make a total of 3 × 3 × 2 = 18 different combinations. We can type these into the table manually, but, because we have full-factorial design, we can also use the full-factorial-design wizard. To do this, first open *block_loop* and click on the 'Full-factorial design' button.

In the table that appears, put the variable names on the first row, and the values on the rows below, as shown in %FigFullFactorial.

%--
figure:
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  The *instructions* screen at the end of step 3.
--%

Now click on 'Ok' to generate the full design. The table of *block_loop* should now look like %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  The table of *block_loop* at the end of step 4.
--%

## Step 5: Create the trial sequence

We want our trial sequence to look as follows:

- A fixation dot, for which we will use a SKETCHPAD.
- A search display, which we will create in JavaScript with a custom INLINE_JAVASCRIPT.
- Response collection, for which we will use a KEYBOARD_RESPONSE.
- Data logging, for which we will use a LOGGER.
- (We also want immediate feedback after each trial, but we will get back to this later.)

So the only thing that is missing is an INLINE_JAVASCRIPT.

- Insert a new INLINE_JAVASCRIPT after *sketchpad* and rename it to *search_display_script*.
- Rename *sketchpad* to *fixation_dot*, so that its function is clear; and
- Change the duration of *fixation_dot* to 500, so that the fixation dot is shown for 500 ms. (There should already be a fixation dot drawn; if not, draw one in the center of *fixation_dot*.)

The overview area should now look like %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  The overview area at the end of step 5.
--%

## Step 6: Generate the search display

__Top-down and defensive programming__

Now things will get interesting: We will start programming in JavaScript. We will use two guiding principles: *top-down* and *defensive* programming.

- *Top-down programming* means that we start with the most abstract logic, without bothering with how this logic is implemented. Once the most abstract logic is in place, we will move down to a slightly less abstract logic, and so on, until we arrive at the details of the implementation. This technique helps to keep the code structured.
- *Defensive programming* means that we assume that we make mistakes. Therefore, to protect us from ourselves, we build sanity checks into the code.

*Note:* The explanation below assumes that you're somewhat familiar with JavaScript. If concepts like `Array`, `for` loop, and functions don't mean anything to you, then it's best to first walk through an introductory JavaScript tutorial. You can find links to JavaScript tutorials here:

- %link:manual/javascript/about%

The logic of the code is shown in %FigHierarchy. The numbers indicate the order in which we will implement the functionality, starting at the abstract level.

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  The logic of the code to draw a visual-search display.
--%

__The Prepare and Run phases__

Open *search_display_script* and switch to the Prepare tab. OpenSesame distinguishes two phases of execution:

- During the Prepare phase, each item is given the opportunity to prepare itself; what this means depends on the item: For a SKETCHPAD, it means drawing a canvas (but not showing it); for a SAMPLER, it means loading a sound file (but not playing it); etc.
- During the Run phase, each item is actually executed; again, what this means depends on the item: For a SKETCHPAD, it means showing the previously prepared canvas; for a SAMPLER, it means playing a previously loaded sound file.

For an INLINE_JAVASCRIPT, you have to decide yourself what to put in the Prepare phase, and what to put in the Run phase. The distinction is usually quite clear: In our case, we put the code for drawing the canvas in the Prepare phase, and the code for showing the canvas (which is small) in the Run phase.

See also:

- %link:prepare-run%


__Choosing your version of JavaScript: ECMA 5.1 or 6__

The formal name of JavaScript is ECMASCRIPT, which exists in different versions. The latest version, ECMA 6 (or: ECMA 2015), has a number of useful features. ECMA 6 is supported by most modern browsers, which means that you can use these features when running an experiment in a browser. However, due to a limitation of the `js2py` library, which is used by OpenSesame to run JavaScript on the desktop, you can only use ECMA 5.1 when running the experiment on the desktop.

In many cases, you don't really care about being able to run your online experiment also on the desktop, in which case it makes sense to make use of ECMA 6. This is also the approach that we will take for this tutorial.

In other words: we will use ECMA 6 syntax, and therefore we will only be able to run the experiment in a browser, and not on the desktop.


__Implement the abstract level__

We start at the most abstract level: defining a function that draws a visual-search display. We don't specify *how* this is done; we simply assume that there is a function that does this, and we will worry about the details later—that's top-down programming.

In the Prepare tab, enter the following code:

```js
persistent.c = draw_canvas()
```

What happens here? We …

- Call `draw_canvas()`, which returns a `Canvas` object that we store as `c`; in other words, `c` is a `Canvas` object that corresponds the search display. This assumes that there is a function `draw_canvas()`, even though we haven't defined it yet.

A `Canvas` object is a single display; it is, in a sense, the JavaScript counterpart of a SKETCHPAD. See also:

- %link:manual/javascript/canvas%

We assign `c` as a property of the `persistent` object. This ensures that we are able to access `c` in the *Run* phase as well. This is necessary, because (unlike for Python INLINE_SCRIPT items) variables are not automatically shared between different INLINE_JAVASCRIPT items, nor between the Run and Prepare phase of the same INLINE_JAVASCRIPT item. See also:

We now go one step down by defining `draw_canvas()` (above the rest of the script so far):

```js
/**
 * Draws the search canvas.
 * @return A Canvas
 **/
function draw_canvas() {
    let c = Canvas()
    let xy_list = xy_random(vars.set_size, 500, 500, 75)
    if (vars.target_present === 'present') {
        let [x, y] = xy_list.pop()
        draw_target(c, x, y)
    } else if (vars.target_present !== 'absent') {
        throw 'Invalid value for target_present ' + vars.target_present
    }
    for (let [x, y] of xy_list) {
        draw_distractor(c, x, y)
    }
    return c
}
```


What happens here? We …

- Create an empty canvas, `c`, using the factory function `Canvas()`.
- Generate an array of random `x, y` coordinates, called `xy_list`, using another common function, `xy_random()`. This array determines where the stimuli are shown. Locations are sampled from a 500 × 500 px area with a minimum spacing of 75 px.
- Check if the experimental variable `target_present` has the value 'present'; if so, `pop()` one `x, y` tuple from `xy_list`, and draw the target at this location. This assumes that there is a function `draw_target()`, even though we haven't defined it yet.
- If `target_present` is neither 'present' nor 'absent', we `throw` an error; this is defensive programming, and protects us from typos (e.g. if we had accidentally entered 'presenr' instead of 'present').
- Loop through all remaining `x, y` values and draw a distractor at each position. This assumes that there is a function `draw_distractor()`, even though we haven't defined it yet.
- Return `c`, which now has the search display drawn onto it.

There are several common functions, such as `Canvas()` and `xy_random()`, which are always available in an INLINE_JAVASCRIPT item. See:

- %link:manual/javascript/common%

In JavaScript, experimental variables are stored as properties of the `vars` object. That's why you write `vars.set_size` and not directly `set_size`.

__Implement the intermediate level__

We now go one more step down by defining `draw_target` (above the rest of the script so far):

```js
/**
 * Draws the target.
 * @param c A Canvas
 * @param x An x coordinate
 * @param y A y coordinate
 **/
function draw_target(c, x, y) {
    draw_shape(c, x, y, vars.target_color, vars.target_shape)
}
```

What happens here? We …

- Call another function, `draw_shape()`, and specify the color and shape that needs to be drawn. This assumes that there is a function `draw_shape()`, even though we haven't defined it yet.

We also define `draw_distractor` (above the rest of the script so far):

```js
/**
 * Draws a single distractor.
 * @param c A Canvas
 * @param x An x coordinate
 * @param y A y coordinate
 **/
function draw_distractor(c, x, y) {
    if (vars.condition === 'conjunction') {
        draw_conjunction_distractor(c, x, y)
    } else if (vars.condition === 'feature_shape') {
        draw_feature_shape_distractor(c, x, y)
    } else if (vars.condition === 'feature_color') {
        draw_feature_color_distractor(c, x, y)
    } else {
        throw 'Invalid condition: ' + vars.condition
    }
}
```

What happens here? We …

- Call another function to draw a more specific distractor depending on the Condition.
- Check whether `vars.condition` has any of the expected values. If not, we `throw` an error. This is defensive programming! Without this check, if we made a typo somewhere, the distractor might simply not be shown without causing an error message.

Now we define the function that draws distractors in the Conjunction condition (above the rest of the script so far):

```js
/**
 * Draws a single distractor in the conjunction condition: an object that
 * can have any shape and color, but cannot be identical to the target.
 * @param c A Canvas.
 * @param x An x coordinate.
 * @param y A y coordinate.
 **/
function draw_conjunction_distractor(c, x, y) {
    let conjunctions = [
        ['yellow', 'circle'],
        ['blue', 'circle'],
        ['yellow', 'square'],
        ['blue', 'square'],
    ]
    let [color, shape] = random.pick(conjunctions)
    while (color === vars.target_color && shape === vars.target_shape) {
        [color, shape] = random.pick(conjunctions)
    }
    draw_shape(c, x, y, color, shape)
}
```

What happens here? We …

- Define a list, `conjunctions`, of all possible color and shape combinations.
- Randomly select one of the color and shape combinations from `conjunctions`.
- Check if the selected color and shape are both equal to the color and shape of the target. If so, keep selecting a new color and shape until this is no longer the case. After all, the distractor cannot be identical to the target!
- Call another function, `draw_shape()`, and specify the color and shape of the to-be-drawn distractor. This assumes that there is a function `draw_shape()`, even though we haven't defined it yet.

In addition, we …

- Use the `random` library, which is corresponds to the `random-ext` package. This library contains useful randomization functions (such as `random.pick()`) and is one of the non-standard JavaScript libraries that is included with OSWeb.

Now we define the function that draws distractors in the Shape Feature condition (above the rest of the script so far):

```js
/**
 * Draws a single distractor in the feature-shape condition: an object that
 * has a different shape from the target, but can have any color.
 * @param c A Canvas.
 * @param x An x coordinate.
 * @param y A y coordinate.
 **/
function draw_feature_shape_distractor(c, x, y) {
    let colors = ['yellow', 'blue']
    let color = random.pick(colors)
    let shape
    if (vars.target_shape === 'circle') {
        shape = 'square'
    } else if (vars.target_shape === 'square') {
        shape = 'circle'
    } else {
        throw 'Invalid target_shape: ' + vars.target_shape
    }
    draw_shape(c, x, y, color, shape)
}
```

What happens here? We …

- Randomly select a color.
- Choose a square shape if the target is a circle, and a circle shape if the target is square.
- If `target_shape` is neither 'circle' nor 'square', `throw` an error—more defensive programming!
- Call another function, `draw_shape()`, and specify the color and shape of the to-be-drawn distractor. This assumes that there is a function `draw_shape()`, even though we haven't defined it yet.

Now we define the function that draws distractors in the Color Feature condition (above the rest of the script so far):

```js
/**
 * Draws a single distractor in the feature-color condition: an object that
 * has a different color from the target, but can have any shape.
 * @param c A Canvas.
 * @param x An x coordinate.
 * @param y A y coordinate.
 **/
function draw_feature_color_distractor(c, x, y) {
    let shapes = ['circle', 'square']
    let shape = random.pick(shapes)
    let color
    if (vars.target_color === 'yellow') {
        color = 'blue'
    } else if (vars.target_color === 'blue') {
        color = 'yellow'
    } else {
        throw 'Invalid target_color: ' + vars.target_color
    }
    draw_shape(c, x, y, color, shape)
}
```

What happens here? We …

- Randomly select a shape.
- Choose a blue color if the target is yellow, and a yellow color if the target is blue.
- If `target_color` is neither 'yellow' nor 'blue', `throw` and error—more defensive programming!
- Call another function, `draw_shape()`, and specify the color and shape of the to-be-drawn distractor. This assumes that there is a function `draw_shape()`, even though we haven't defined it yet.

__Implement the detailed level__

Now we go all the way down to the details by defining the function that actually draws a shape to the canvas (above the rest of the script so far):

```js
/**
 * Draws a single shape.
 * @param c A Canvas.
 * @param x An x coordinate.
 * @param y A y coordinate.
 * @param color A color (yellow or blue)
 * @param shape A shape (square or circle)
 **/
function draw_shape(c, x, y, color, shape) {
    if (shape === 'square') {
        // Parameters are passed as an Object!
        c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
    } else if (shape === 'circle') {
        // Parameters are passed as an Object!
        c.circle({x:x, y:y, r:25, color:color, fill:true})
    } else {
        throw 'Invalid shape: ' + shape
    }
    if (color !== 'yellow' && color !== 'blue') {
        throw 'Invalid color: ' + color
    }
}
```

What happens here? We …

- Check which shape should be drawn. For squares, we add a `rect()` element to the canvas. For circles, we add a `circle()` element.
- Check if the the shape is either a square or a circle, and if not `throw` and error. This is another example of defensive programming! We're making sure that we haven't accidentally specified an invalid shape.
- Check if the the color is neither yellow nor blue, and if not `throw` and error.

Importantly, `Canvas` functions accept a single object (`{}`) that specifies all parameters by name, like so:

```js
// Correct: pass a single object that contains all parameters by name
c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
// Incorrect: do not pass parameters by order
// c.rect(x-25, y-25, 50, 50, color, true)
// Incorrect: named parameters are not supported in JavaScript
// c.rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=true)
```

__Implement the Run phase__

Because we have done all the hard work in the Prepare phase, the Run phase is just:

```js
persistent.c.show()
```

Note that we have assigned the canvas as a property of the `persistent` object in the Prepare phase, which is why we can refer to it also in the Run phase.

That's it! Now you have drawn a full visual-search display. And, importantly, you have done so in a way that is easy to understand, because of top-down programming, and safe, because of defensive programming.


## Step 7: Define the correct response

To know if the participant responds correctly, we need to know the correct response. You can define this explicitly in the *block_loop* (as done in the beginner tutorial); but here we're going to use some simple JavaScript that checks whether the target is present or not, and defines the correct response accordingly.

To do this, insert a new INLINE_JAVASCRIPT at the start of *trial_sequence*, and rename it to *correct_response_script*. In the Prepare phase, enter the following code:

```js
if (vars.target_present === 'present') {
    vars.correct_response = 'right'
} else if (vars.target_present === 'absent') {
    vars.correct_response = 'left'
} else {
    throw 'target_present should be absent or present, not ' + vars.target
}
```

What happens here? We …

- Check whether the target is present or not. If the target is present, the correct response is 'right' (the right arrow key); if the target is absent, the correct response is 'left' (the left arrow key). The experimental variable `correct_response` is automatically used by OpenSesame; therefore, we don't need to explicitly indicate that this variable contains the correct response.
- Check if the target is either present or absent, and if not `throw` an error—another example of defensive programming.

## Step 8: Give per-trial feedback

Feedback after every trial can motivate participants; however, per-trial feedback should not interfere with the flow of the experiment. A good way to give per-trial feedback is to briefly show a green fixation dot after a correct response, and a red fixation dot after an incorrect response.

To do this:

- Insert two new SKETCHPADs into *trial_sequence*, just after *keyboard_response*.
- Rename one SKETCHPAD to *green_dot*, draw a central green fixation dot onto it, and change its duration to 500.
- Rename the other SKETCHPAD to *red_dot*, draw a central red fixation dot onto it, and change its duration to 500.

Of course, only one of the two dots should be shown on each trial. To accomplish this, we will specify run-if statements in *trial_sequence*:

- Change the run-if statement for *green_dot* to '[correct] = 1', indicating that it should only be shown after a correct response.
- Change the run-if statement for *red_dot* to '[correct] = 0', indicating that it should only be shown after an incorrect response.

The variable `correct` is automatically created if the variable `correct_response` is available; that's why we defined `correct_response` in step 7. For more information about variables and run-if statements, see:

- %link:manual/variables%

The *trial_sequence* should now look like %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  The *trial_sequence* at the end of step 8.
--%


## Step 9: Checking compatibility

When you want to run an experiment in a browser, you cannot use all of OpenSesame's functionality. To check whether your experiment is able to run in a browser, you can use the OSWeb compatibility check by going to Menu → Tools → OSweb. If you've followed all the steps of this tutorial, the compatibility check will fail with the following warning (%FigCompatibilityCheck):

%--
figure:
 id: FigCompatibilityCheck
 source: compatibility-check.png
 caption: |
  The compatibility check may give warnings or errors.
--%

This is a warning that the *logger* has the option 'Log all variables' enabled. Enabling this option is recommended when running an experiment on the desktop, in which case it's no problem to collect a lot of unnecessary information. However, enabling this option is *not* recommend when running an experiment online, because doing so results in unnecessarily large data files and consumes an unnecessary amount of bandwidth.

Therefore, go the *logger*, disable the 'Log all variables' option, and select only those variables that you actually need. You can do that by opening the variable inspector and dragging variables into the *logger* table (%FigLogger).

%--
figure:
 id: FigLogger
 source: logger.png
 caption: |
  Logging only relevant variables is recommended when running an experiment online to save bandwidth.
--%


For a list of functionality that is supported by OSWeb, see:

- %link:manual/osweb/osweb%


## Finished!

Congratulations, the experiment is complete! You can give it a test run by pressing on the toolbar button that shows a green circle with a gray play button inside (shortcut: `Alt+Ctrl+W`).

If the experiment doesn't work on the first try: Don't worry, and calmly figure out where the mistake comes from. Crashes are part of the normal development process. But you can save yourself a lot of time and headache by working in a structured way, as we have done in this tutorial.

## References

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
