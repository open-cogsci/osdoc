title: Variables
complete: false

Variables are a crucial part of any psychological experiment. Two classes of variables are distinguished: independent variables, which are manipulated by the researcher (and are independent of the participant's response), and dependent variables, which depend on the participant's response. The aim of the prototypical psychological experiment is to see if manipulating one or more independent variables has an effect on one or more dependent variables. For example, you may manipulate a participant's mood by presenting emotional pictures of different valences, and see if this affects response times. In this case, you manipulate the independent variable `emotion` and measure the effect on the dependent variable `response time`.

But you probably know all this. What you may not know is how to apply this knowledge to OpenSesame.

[TOC]

## The variable inspector

The variable inspector provides an overview of available variables (%FigVariableInspector). You can activate the variable inspector by pressing Control + I or through the menu (Menu → View → Show variable inspector). When the experiment is not running, this overview is based on a best guess of which variables will become available during the experiment. However, when the experiment is running, the variable inspector shows a live overview of variables and their values. This is very useful for debugging your experiment.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: The variable inspector provides an overview of all variables that OpenSesame knows about.
--%

## Defining variables

The simplest way to define variables is through a `loop` item. For example, in %FigLoop you can see that a variable named `target` has been defined. The *trial_sequence* item is called once while `target` is set to 'left' and once while 'target' is set to 'right'.

%--
figure:
 id: FigLoop
 source: defining-variables-in-a-loop.png
 caption: The most common way to define independent variables is using the `loop` table.
--%

## Built-in variables

The following variables are always available:

### Experiment variables

|`title`				|The title of the experiment|
|`description`			|The description of the experiment|
|`foreground`			|The default foreground color. E.g., 'white' or '#FFFFFF'.|
|`background`			|The default background color. E.g., 'black' or '#000000'.|
|`height`				|The height-part of the display resolution. E.g., '768'|
|`width`				|The width-part of the display resolution. E.g., '1024'|
|`subject_nr`			|The subject number, which is asked when the experiment is started.|
|`subject_parity`		|Is 'odd' if `subject_nr` is odd and 'even' if `subject_nr` is even. Useful for counterbalancing.|
|`experiment_path`		|Contains the folder of the current experiment, without the experiment filename itself. If the experiment is unsaved, it has the value 'None'.|
|`pool_folder`			|Contains the folder where the contents of the file pool have been extracted to. This is generally a temporary folder.|

### Item variables

There are also a number of variables that keep track of all the items in the experiment. For example, every item creates a `count_[item name]` variable, which reflects how often the item has been called. This means that you can use the `count_trial_sequence` variable to keep track of how often the *trial_sequence* has been called.

|`time_[item_name]`		|Contains a timestamp of when the item was last executed. For `sketchpad` items, this can be used to verify the timing of display presentation.|
|`count_[item_name]`	|Is equal the number of times minus one (starting at 0, in other words) that an item has been called. This can, for example, be used as a trial or block counter.|

### Response variables

When you use the standard response items, such as the `keyboard_response` and `mouse_response`, a number of variables are set based on the participant's response.

|`response`						|Contains the last response that has been given.|
|`response_[item_name]`			|Contains the last response for a specific response item. This is useful in case there are multiple response items.|
|`response_time`				|Contains the interval in milliseconds between the start of the response interval and the last response.|
|`response_time_[item_name]`	|Contains the response time for a specific response item.|
|`correct`						|Is set to '1' if the last `response` matches the variable `correct_response`, '0' if not, and 'undefined' if the variable `correct_response` has not been set.|
|`correct_[item_name]`			|As `correct` but for a specifc response item.|

### Feedback variables

Feedback variables maintain a running average of accuracy and response times.

|`average_response_time`		|The average response time. This is variable is useful for presenting feedback to the participant.|
|`avg_rt`						|Synonym for `average_response_time`|
|`accuracy`						|The average percentage of correct responses. This is variable is useful for presenting feedback to the participant.|
|`acc`							|Synonym for `accuracy`|

For more information, see:

- [usage/feedback](/usage/feedback)

## Using variables

Simply put, wherever you see a value in the OpenSesame GUI, you can replace that value by a variable using the '[variable name]' notation. For example, if you have defined a variable `soa` in a `loop` item, you can use this variable for the duration of a sketchpad as shown in %FigSketchpad.

%--
figure:
 id: FigSketchpad
 source: variable-duration.png
 caption: The duration '[soa]' indicates that the duration of the `sketchpad` depends on the variable `soa`.
--%

This works throughout the OpenSesame GUI. For example, if you have the defined a variable `my_freq`, you can use this variable as the frequency in a `synth` item, as shown in %FigSynth.

%--
figure:
 id: FigSynth
 source: variable-frequency.png
 caption: The frequency '[my_freq]' indicates that the frequency of the `synth` depends on the variable `my_freq`.
--%

Sometimes, the GUI doesn't let you type in arbitrary text. For example, the length field the `synth` only accepts numbers, so you cannot enter something like '[len]'. However, you can still use a variable length in the following way. Click on the 'Edit script' button at the top right of the tab. Now replace the following line ...

	set length "100"

... by ...

	set length [len]

... and press 'apply'.

## Getting and setting variables in inline_script items

`Inline_script` items allow you to use Python inline code in OpenSesame. This is useful for complex tasks, which are difficult or impossible to do through the GUI. In an `inline_script`, you can get experimental variables using the `var` object. The following, will print the value of the variable 'example_variable' to the debug window:

~~~ .python
print(var.example_variable)
~~~

You can set the experimental variable `example_variable` to the value 'some value' as follows:

~~~ .python
var.example_variable = 'some value'
~~~

For more information, see:

- [/python/var](/python/var)

## Using conditional ("if") statements

Conditional statements, or 'if statements', provide a way to indicate that something should happen only under specific circumstances, such when a certain variable has a specific value. In OpenSesame you can use conditional statements in `sequence`, `sketchpad`, and `feedback` items.

If you open a `sequence` item, you will see that every item from the sequence has a 'Run if...' option. The default value is 'always', in which case the item is always called, but you can also enter a condition here. For example, if you want to show a green fixation dot after a correct response, and a red fixation dot after an incorrect response, you can create a sequence like the following (this makes use of the fact that a `keyboard_response` item automatically sets the `correct` variable, as discussed above) as shown in %FigRunIf.

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: |
  'Run if' statements can be used to indicate that certain items from a `sequence` should only be executed under specific circumstances.
--%

You can use more complex conditions as well. Let's take a look at a few examples:

	[correct] = 1 and [response_time] > 2000
	[correct] != 1 or [response_time] > [max_response_time] or [response_time] < [min_response_time]

Variables are not typed and putting quotes around a value is only necessary if a value contains spaces (but always permitted).

Alternatively, you can use Python code in your conditional statements. To indicate that you are using Python code instead of the OpenSesame syntax (as above), simply prepend an `=` character to your conditional statement, like so:

~~~ .python
=var.correct == 0
~~~

You cannot use the square-bracket syntax when using Python code. Instead, you use the `var` object to retrieve a variable, like you would in an `inline_script`.

The same principle applies to 'Show if' fields in `sketchpad` items. For example, if you want to draw a leftwards arrow only if the variable `cue` has been set to 'right', simply type the proper condition in the 'Show if ...' field and draw the arrow, as in %FigShowIf. Make sure that you draw the arrow after you have set the condition.

%--
figure:
 id: FigShowIf
 source: show-if.png
 caption: "'Show if' statements can be used to indicate that certain elements from a `sketchpad` or `feedback` item should only be shown under specific circumstances."
--%

Note that the moment at which a conditional statement is evaluated may affect how your experiment works. This is related to the prepare-run strategy employed by OpenSesame, which is explained here:

- [usage/prepare-run](/usage/prepare-run)

## Smart variable typing (and some pitfalls)

Unlike in most programming languages, in OpenSesame you don't need to indicate whether the type of your variable is a string, integer, or floating point. Instead, OpenSesame selects a variable type automatically, according to the following logic:

- If a value is *numeric and integer*, it is treated as an integer. An example is the value *10*.
- If a value is *numeric, but not integer*, it is treated as a float. An example is the value *0.1*.
- If a value is *anything else*, it is treated as text. An example is the value *this is text*.

In general, this is convenient, because it allows you to compare numeric variables in conditional statements. However, it can also have unexpected side effects when OpenSesame interprets a value differently from how you intended it. This may happen as a result from smart variable typing and as a result of how Python deals with certain notations.

Let's take a look at various things that can go 'wrong', at least in the sense that the outcome is different from what you might expect. (Warning: Some knowledge of computer science will come in handy!)

~~~ .python
test_values = 10, 010, 0x10, 0b10, '10', '010', '0x10', '0b10', ' 10'
for input_value in test_values:
	var.my_var = input_value
	output_value = var.my_var
	print('Input = "%s" %s' % (input_value, type(input_value)))
	print('-> Output = "%s" %s\n' % (output_value, type(output_value)))
~~~

Let's walk through the output of this script one by one. (Here we focus on the things that go wrong, but don't be too concerned: In the overwhelming majority of cases smart variable works exactly how you would expect it to.)

	# In: 10
	Input = "10" <type 'int'>
	-> Output = "10" <type 'int'>

This is as you would expect, the `int` 10 stays the `int` 10.

	# In: 010
	Input = "8" <type 'int'>
	-> Output = "8" <type 'int'>

This is odd. We specify 010, but according to the script we have specified the `int` 8. This is because Python interprets numbers with a leading zero as an octal numbers. And octal 10 equals decimal 8.

	# In: 0x10
	Input = "16" <type 'int'>
	-> Output = "16" <type 'int'>

Again, we specify 0x10 but the script tells us that we have specified the `int` 16. This is because Python interprets numbers with a leading `0x` as hexadecimal. And hexadecimal 10 equals decimal 16.

	# In: 0b10
	Input = "2" <type 'int'>
	-> Output = "2" <type 'int'>

Same thing: The leading `0b` indicates that we are dealing with a binary number. And binary 10 equals decimal 2.

	# In: '10'
	Input = "10" <type 'str'>
	-> Output = "10" <type 'int'>

Here we have smart variable typing at work. The `str` '10' has been converted to the `int` 10.

	# In: '010'
	Input = "010" <type 'str'>
	-> Output = "10" <type 'int'>

Here again we have smart variable typing at work. The `str` '010' has been converted to the `int` 10. Note the difference between the interpretation of the `int` 010, which is interpreted as an octal number, and the `str` '010' which is not. This is a (confusing) property of Python.

	# In: '0x10'
	Input = "0x10" <type 'str'>
	-> Output = "0x10" <type 'unicode'>

Similar to above, the `str` '0x10' is not interpreted as a hexadecimal number, although the `int` 0x10 is. This is a property of Python. Also, you see that the `str` comes out as `unicode`. This is because OpenSesame works internally with `unicode` objects, which is a special kind of string that is interchangeable with `str` objects for most purposes.

	# In: '0b10'
	Input = "0b10" <type 'str'>
	-> Output = "0b10" <type 'unicode'>

Similar to the case of '0x10' above.

	# In: ' 10'
	Input = " 10" <type 'str'>
	-> Output = "10" <type 'int'>

Finally, you see that the leading space is removed from the `str` ' 10', and that the value is converted to the `int` 10.

## Resolving recursion errors

Sometimes, you may encounter a runtime error of the following type (%FigRecursion):

	Recursion detected! Is variable 'freq' defined
	in terms of itself (e.g., 'var = [var]')

%--
figure:
 id: FigRecursion
 source: recursion-error.png
 caption: If you see an error message of this type, you have probably used a variable name that was already in use by OpenSesame, resulting in a recursion error.
--%

This error maybe confusing at first, but is easy to prevent once you understand it. The problem is that the `synth` item (in this example) uses an item-level variable that is called `freq`. Therefore, if you try to use a global variable called `freq` to specify the item's internal variable called `freq`, OpenSesame will get into an infinite recursion!

The solution, of course, is to use a different name for your own variable. For example, `my_freq` will do just fine.

[tutorial]: /usage/step-by-step-tutorial/
[feedback]: /usage/giving-feedback-to-participants/
[prepare-run]: /usage/prepare-run#conditional-statements
