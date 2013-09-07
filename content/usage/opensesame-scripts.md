---
layout: osdoc
title: OpenSesame script syntax
group: Usage
permalink: /opensesame-scripts/
---

Overview
--------

- [About OpenSesame script](#about)
- General remarks
	- [Keywords](#keywords)
	- [Comments](#comments)
	- [Quotation](#quotation)
	- [Types](#types)
	- [Item-specific syntax](#item-specific-syntax)
	- [Resolving path names](#path-names)
- Statements
	- [define](#define)
	- [draw](#draw)
	- [log](#log)
	- [run](#run)
	- [set](#set)
	- [setcycle](#setcycle)
	- [widget](#widget)

About OpenSesame script {#about}
-----------------------

OpenSesame script is a simple definitional language that defines an experiment. It is not a full fledged programming language, and does not include features such a `for` loops. The OpenSesame script is interpreted by an OpenSesame runtime environment.

OpenSesame script is different from the Python scripts that are used in inline_script items. Python is a real programming language with all the flexibility and complexities that this entails. In contrast, OpenSesame script is used to define experiments in a simple, human-readable way.

General remarks
---------------

### Keywords {#keywords}

Some items, such as form_base and sketchpad accept keywords. Keywords are of the form `keyword=value`. Keywords are optional and should fall back to a default value.

### Comments {#comments}

Strings preceded by a hash should be interpreted as comments.

#### Example

	# This is a comment

### Quotation {#quotation}

Quotation is not necessary, except around strings that contain spaces or other forms of punctuation. So the following lines should be interpreted as identical:

	set my_var 'my_value'
	set my_var "my_value"
	set my_var my_value

However, the following lines are not. In fact, the first line is not valid, because it has an unexpected third parameter.

	set my_var my value
	set my_var "my value"

### Types {#types}

There are no types. No distinction is made between strings, integers, etc.

### Item-specific syntax {#item-specific-syntax}

Some items have a specific syntax. This is indicated in the “Applies to” section for each of the keywords discussed below.

### Resolving path names {#path-names}

TODO

*define* statement {#define}
------------------

Starts the definition of an item. After a define statement, all lines are indented by a single tab. The end of the item definition is the first string that is no longer indented. Nested define statements are not allowed.

*Applies to*

All items

*Format*

	define [item name] [item type]
		[item definition]

*Parameters*

|`item name`	|the name of the item	|
|`item type`	|the type of the item	|

*Example*

	define get_key keyboard_response
		set allowed_responses "a;x"
		set description "Collects keyboard responses"
		set timeout "infinite"
		set flush "yes"

*draw* statement {#draw}
----------------

Defines a visual element of a sketchpad or feedback item.

*Applies to*

sketchpad, feedback

*Format*

The format depends on the element.

	draw ellipse [left] [top] [width] [height] [keywords]
	draw circle [x] [y] [radius] [keywords]
	draw line [left] [right] [top] [bottom] [keywords]
	draw arrow [left] [right] [top] [bottom] [keywords]
	draw textline [x] [y] [text]
	draw image [x] [y] [path]
	draw gabor [x] [y]
	draw noise [x] [y]
	draw fixdot [x] [y]

*Parameters*

|`left` 		|the left-most x-coordinate		|
|`right`		|the right-most x-coordinate	|
|`top`			|the top y-coordinate			|
|`bottom`		|the bottom y-coordinate		|
|`x` 			|the x-coordinate				|
|`y`			|the y-coordinate				|
|`text` 		|text string					|
|`path` 		|the path to an image file		|

*Keywords*

TODO

*Example*

	draw fixdot 0 0

*log* statement {#log}
---------------

Indicates that a variable should be written to the log-file.

*Applies to*

logger

*Format*

	log [variable name]

*Parameters*

|`variable name`		|the name of a variable	|

*Example*

	log response_time

*run* statement {#run}
---------------

Indicates that an item should be run. In the case of the sequence, the order of the run statements determines the order in which items are called. In the case of the parallel plug-in all items are called at the same item.

*Applies to*

sequence

*Format*

	run [item name] [optional: condition]

*Parameters*

|`item name`			|the name of the item to run	|
|`condition` (optional)	|the conditional statement, which determines the item is actually called. If no condition is provided, the item is always called.|

*Example*

	run correct_feedback '[correct] = 1'

*set* statement {#set}
---------------

Defines single-line variables.

*Applies to*

All items

*Format*

	set [variable name] [value]

*Parameters*

|`variable name`	|the variable name	|
|`value`			|the variable value	|

*Example*

	set timeout 1000

*Notes*

Multi-line variables are defined using the `__[variable name]__` notation. This is mostly useful for items that require large blocks of text. Within an item definition, each line is preceded by a single tab, which should not be interpreted as part of the text. `__end__` indicates the end of the variable.

*For example:*

	__my_variable__
	This is the first line.
	This is the second line.
	__end__

*setcycle* statement {#setcycle}
--------------------

Similar to the regular “set” statement, but sets a variable only during a specific cycle of a loop. This is the script equivalent of the loop table.

*Applies to*

Loop

*Format*

	Setcycle [cycle #] [variable name] [variable value]

*Parameters*

|`Cycle #`			|the number of the cycle, where 0 is the first	|
|`variable name` 	|the variable name								|
|`value`			|the variable value								|

*Example*

	setcycle 0 cue valid

*widget* statement {#widget}
------------------

Adds a widget (buttons, labels, etc.) to a form. Valid keywords depend on the type of widget. The widget statement is not strictly part of the core OpenSesame syntax, but is used by the form_base plug-in.

*Applies to*

form_base (plug-in)

*Format*

	widget [column] [row] [column span] [row span] [widget type] [keywords]

*Parameters*

|`column`		|the widget's column position in the form, where 0 is left-most								|
|`row`			|the widget's row position in the form, where 0 is top										|
|`column span`	|the number of columns that the widget occupies												|
|`row span`		|the number of rows that the widget occupies												|
|`widget type`	|'button', 'checkbox', 'image', 'image_button', 'label', 'rating_scale', or 'text_input'	|

*Keywords*

TODO

*Example*

	widget 0 0 1 1 label text='This is a label'