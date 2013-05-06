---
layout: osdoc
title: Variables and conditional ("if") statements
group: Usage
permalink: /variables-and-conditional-qifq-statements/
level: 1
sortkey: 004.005
---

Variables are a crucial part of any psychological experiment. Two classes of variables are distinguished: independent variables, which are manipulated by the researcher (and are independent of the participant's response), and dependent variables, which depend on the participant's response. The aim of the prototypical psychological experiment is to see if manipulating one or more independent variables has an effect on one or more dependent variables. For example, you may manipulate a participant's mood by presenting emotional pictures of different valences, and see if this affects response times. In this case, you manipulate the independent variable 'emotion' and measure the effect on the dependent variable 'response time'.

But you probably know all this. What you may not know is how to apply this knowledge to OpenSesame.

Overview
--------

- [Smart variable typing](#smart-typing)
- [The variable inspector](#variable-inspector)
- [Defining variables](#defining-variables)
- [Built-in variables](#built-in-variables)
- [Using variables](#using-variables)
- [Resolving recursion errors](#recursion-errors)
- [Using conditional ("if") statements](#using-conditionals)
- [When are conditions evaluated?](#when-are-conditions-evaluated)
- [Getting and setting variables in inline_script items](#getting-and-setting)

Smart variable typing {#smart-typing}
---------------------

In OpenSesame, you do not need to indicate whether the type of your variable is a string, integer, or floating point. Instead, OpenSesame picks a variable type automatically, as follows:

- If a value is *numeric and integer*, it is treated as an integer. An example is the value *10*.
- If a value is *numeric, but not integer*, it is treated as a float. An example is the value *0.1*.
- If a value is *anything else*, it is treated as text. An example is the value *this is text*.

In general, this is convenient, because it allows you to compare numeric variables in conditional statements. However, it can also have unexpected side effects. For example, if you give a variable the value *0001*, and [print it to the screen with a sketchpad](#using-variables), you will see *1*. This is because *0001* is interpreted as an integer, and the leading zeros get lost in translation. Similarly, if you use `exp.set()` [in an inline_script](#getting-and-setting) to store an object, the object will be converted into some (unpredictable) string representation, which is generally not what you want.

The variable inspector {#variable-inspector}
----------------------

The variable inspector provides a convenient overview of the available variables. You can activate the variable inspector by pressing Control + I or through the menu (Menu → View → Show variable inspector).

![](/img/fig/fig4.5.1.png)

Defining variables {#defining-variables}
------------------

The simplest way to define variables is using loop items. For example, in the screenshot below you can see that a variable named 'target' has been defined. The 'trial_sequence' item is called once while 'target' is set to 'left' and once while 'target' is set to 'right'.

![](/img/fig/fig4.5.2.png)

Built-in variables {#built-in-variables}
------------------

A number of variables are built into OpenSesame. The following global variables are always available.

### Global variables

|`title`				|The title of the experiment|
|`description`			|The description of the experiment|
|`foreground`			|The default foreground color. E.g., 'white' or '#FFFFFF'.|
|`background`			|The default background color. E.g., 'black' or '#000000'.|
|`height`				|The height-part of the display resolution. E.g., '768'|
|`width`				|The width-part of the display resolution. E.g., '1024'|
|`subject_nr`			|The subject number, which is asked when the experiment is started.|
|`subject_parity`		|Is 'odd' if subject_nr is odd and 'even' if subject_nr is even. Useful for counterbalancing.|

### Item variables

There are also some of variables which are automatically set by all items. For example, every item creates a `count_[item name]` variable, which reflects how often the item has been called.

|`time_[item_name]`		|Contains a timestamp of the last call of the item. For sketchpad items, this can be used to verify the timing of display presentation.|
|`count_[item_name]`		| Is the number of times minus one (starting at 0, in other words) that an item has been called. This can, for example, be used as a trial or block counter.|

### Response variables

Response items, such as the keyboard_response and mouse_response items, also set variables based on the participant's response.

|`response`						|Contains the last response that has been given.|
|`response_[item_name]`			|Contains the last response for a specific response item.|
|`response_time`					|Contains the interval in milliseconds between the start of the response interval and the last response.|
|`response_time_[item_name]`		|Contains the response time for a specific response item.|
|`correct`						|Set to '1' if the last response matches the 'correct_response' variable, '0' if not, and 'undefined' if no 'correct_response' variable has been set.|
|`correct_[item_name]`			|As `correct` but for a specifc response item.|

### Feedback variables

Feedback variables maintain a running accuracy and average of response times. For more information, see [this article][feedback].

|`average_response_time`			|The average response time. This is variable is useful for presenting feedback to the participant.|
|`avg_rt`						|Synonym for 'average_response_time'|
|`accuracy`						|The average percentage of correct responses. This is variable is useful for presenting feedback to the participant.|
|`acc`							|Synonym for 'accuracy'|

Using variables {#using-variables}
---------------

Simply put, everywhere you see a value in the OpenSesame GUI, you can replace the value by a variable using the '[variable name]' notation. For example, if you have defined a variable 'soa' in a loop item, you can use this variable for the duration of a sketchpad as follows:

![](/img/fig/fig4.5.3.png)

This principle works throughout the OpenSesame GUI. For example, if you have the defined a variable `my_freq`, you can use this variable as the frequency in a synth item as follows:

![](/img/fig/fig4.5.4.png)

Sometimes, the GUI doesn't let you type arbitrary text. For example, the length field the synth only accepts numbers, so you cannot enter something like '[len]'. However, you can still use a variable length in the following way. Click on the 'Edit script' button at the top right of the tab. Now replace the following line

	set length "100"

by

	set length [len]

and press 'apply'.

You can find a much more detailed example of using variables in this way in the tutorial.

Resolving recursion errors {#recursion-errors}
--------------------------

Sometimes, you may encounter a runtime error of the following type:

	Recursion detected! Is variable 'freq' defined
	in terms of itself (e.g., 'var = [var]')

![](/img/fig/fig4.5.5.png)

This error maybe confusing at first, but is easy to prevent once you understand it. The problem is that the synth item (in this example) uses an internal item variable that is called `freq`. Hence, if you try to use a global variable called `freq` to specify the item's internal variable called `freq`, OpenSesame will get into an infinite recursion!

The solution, of course, is to use a different name for your own variable. For example, `my_freq` will do just fine.

Using conditional ("if") statements {#using-conditionals}
-----------------------------------

Conditional statements, more commonly referred to as "if statements", provide a way to specify that something should happen only under specific circumstances (i.e., when variables have specific values). In OpenSesame you can use conditions in sequence, sketchpad, and feedback items.

If you open a sequence item, you can see that every item from the sequence has a 'Run if...' option. The default value is 'always', in which case the item is always called, but you can replace this by a condition. For example, if you want to show a green fixation dot after a correct response, and a red fixation dot after an incorrect response, you can create a sequence like the following (this makes use of the fact that a keyboard_response item automatically sets the `correct` variable, as discussed above):

![](/img/fig/fig4.5.6.png)

You can use more complex conditions as well. Let's take a look at a few examples:

	[correct] = 1 and [response_time] > 2000
	[correct] != 1 or [response_time] > [max_response_time] or [response_time] < [min_response_time]

You can concatenate as many and's and or's as you want. 'and' takes precedence over 'or'. Brackets are not supported yet. Note that variables are not typed and putting quotes around a value is only necessary if a value contains spaces (but always permitted), as described here.

Alternatively, you can use Python code in your conditional statements. To indicate that you are using Python code instead of the OpenSesame syntax (as above), you prepend an `=` character your conditional statement, like so:

{% highlight python %}
=self.get('correct') == 0
{% endhighlight %}

Note that you cannot use the square-bracket syntax when using Python code, because that is not valid Python. Instead, you use `self.get()` to retrieve a variable, like you would in an inline_script.

The same principle applies to 'Show if' fields in sketchpad items. For example, if you want to draw a leftwards arrow only if the variable `cue` has been set to 'right', you simply type the proper condition in the 'Show if ...' field and draw the arrow, as in the screenshot below. Make sure that you draw the arrow after you have set the condition.

![](/img/fig/fig4.5.6.png)

When are conditions evaluated? {#when-are-conditions-evaluated}
------------------------------

See [this page][prepare-run].

Getting and setting variables in inline_script items {#getting-and-setting}
----------------------------------------------------

Inline_script items allow you to use Python inline code in OpenSesame. This is useful for complex tasks, which are difficult or impossible to do through the GUI. Fore more information about inline_script items, see this article.

In an inline_script, you can retrieve a variable as follows (this will print the value of the variable 'example_variable' to the debug window):

{% highlight python %}
print self.get("example_variable")
{% endhighlight %}

You can set a variable as follows:

{% highlight python %}
self.experiment.set("example_variable", "some_value")
exp.set("example_variable", "some_value")
{% endhighlight %}

`exp.set()` works, because `exp` is simply a shortcut to `self.experiment`. Variables which that set in an inline_script item can be used in other items in the regular way.

Note the asymmetry: You use `exp.set()`, rather than `self.set()`, even though you do use `self.get()`. This is because variables can exist on two levels. In the item (local) or in the experiment (global). `self.get()` looks first at the item level and then at the experiment level, which is fine. However, `self.set()` sets an item at the item level, which is usually not what you want, because this means that you can only access the variable from within the current inline_script item. Therefore, you should use `exp.set()`, which sets a variable at the experiment level.

[tutorial]: /usage/step-by-step-tutorial/
[feedback]: /usage/giving-feedback-to-participants/
[prepare-run]: /usage/prepare-run#conditional-statements