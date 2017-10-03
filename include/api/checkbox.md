<div class="ClassDoc YAMLDoc" id="Checkbox" markdown="1">

# class __Checkbox__

The `Checkbox` widget is a checkable box accompanied by a string of
text.

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 checkbox group="group" text="Option 1"
widget 0 1 1 1 checkbox group="group" text="Option 2"
~~~

__Example (Python):__

~~~ .python
form = Form()
checkbox1 = Checkbox(text='Option 1', group='group')
checkbox2 = Checkbox(text='Option 2', group='group')
form.set_widget(checkbox1, (0,0))
form.set_widget(checkbox2, (0,1))
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="Checkbox-__init__" markdown="1">

## function __Checkbox\.\_\_init\_\___\(form, text=u'checkbox', frame=False, group=None, checked=False, click\_accepts=False, var=None\)

Constructor to create a new `Checkbox` object. You do not generally
call this constructor directly, but use the `Checkbox()` factory
function, which is described here: [/python/common/]().

__Arguments:__

- `form` -- The parent form.
	- Type: form

__Keywords:__

- `text` -- Checkbox text.
	- Type: str, unicode
	- Default: 'checkbox'
- `frame` -- Indicates whether a frame should be drawn around the widget.
	- Type: bool
	- Default: False
- `group` -- If a group is specified, checking one checkbox from the group will uncheck all other checkboxes in that group. Checkboxes that are part of a group cannot be unchecked, except by clicking on another checkbox in the group. The `group` keyword also affects how variables are stored (see the `var` keyword).
	- Type: str, unicode, NoneType
	- Default: None
- `checked` -- The initial checked state of the checkbox.
	- Type: bool
	- Default: False
- `click_accepts` -- Indicates whether a click press should accept and close the form.
	- Type: bool
	- Default: False
- `var` -- The name of the experimental variable that should be used to log the widget status. This variable will contain a semi-colon separated list of the text of all checked checkboxes in the same group, or 'no' if no checkbox in the group is checked. For the purpose of the variable, all checkboxes that are not part of a group are placed in the same group. For more information about the use of response variables in forms, see the form documentation page.
	- Type: str, unicode, NoneType
	- Default: None

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-_init_canvas_elements" markdown="1">

## function __Checkbox\.\_init\_canvas\_elements__\(\)

Initializes all canvas elements.

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-_update" markdown="1">

## function __Checkbox\.\_update__\(\)

Draws the widget.

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-_update_frame" markdown="1">

## function __Checkbox\.\_update\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-_update_text" markdown="1">

## function __Checkbox\.\_update\_text__\(text\)

Draws text inside the widget.

__Arguments:__

- `text` -- The text to draw.
	- Type: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-coroutine" markdown="1">

## function __Checkbox\.coroutine__\(\)

Implements the interaction. This can be overridden to implement more complicated keyboard/ mouse interactions.

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-on_key_press" markdown="1">

## function __Checkbox\.on\_key\_press__\(key\)

Is called whenever the widget is focused and the users enters a key.

__Arguments:__

- `key` -- A key
	- Type: str

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-on_mouse_click" markdown="1">

## function __Checkbox\.on\_mouse\_click__\(pos\)

Is called whenever the user clicks on the widget. Toggles the state of the checkbox.

__Arguments:__

- `pos` -- An (x, y) coordinate tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-set_checked" markdown="1">

## function __Checkbox\.set\_checked__\(checked=True\)

Sets the checked status of the checkbox.

__Keywords:__

- `checked` -- The checked status.
	- Type: bool
	- Default: True

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-set_rect" markdown="1">

## function __Checkbox\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="Checkbox-set_var" markdown="1">

## function __Checkbox\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.
	- Type: str, unicode

__Keywords:__

- `var` -- A variable name, or `None` to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

</div>

