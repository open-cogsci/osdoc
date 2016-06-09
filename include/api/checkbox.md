<div class="ClassDoc YAMLDoc" id="checkbox" markdown="1">

# class __checkbox__

The checkbox widget is a checkable box accompanied by a string of text.

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 checkbox group="group" text="Option 1"
widget 0 1 1 1 checkbox group="group" text="Option 2"
~~~

__Example (Python):__

~~~ .python
from libopensesame import widgets
form = widgets.form(exp)
checkbox1 = widgets.checkbox(form, text='Option 1', group='group')
checkbox2 = widgets.checkbox(form, text='Option 2', group='group')
form.set_widget(checkbox1, (0,0))
form.set_widget(checkbox2, (0,1))
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="checkbox-__init__" markdown="1">

## function __checkbox\.\_\_init\_\___\(form, text=u'checkbox', frame=False, group=None, checked=False, click\_accepts=False, var=None\)

Constructor.

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

[checkbox.__init__]: #checkbox-__init__
[__init__]: #checkbox-__init__

<div class="FunctionDoc YAMLDoc" id="checkbox-draw_frame" markdown="1">

## function __checkbox\.draw\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

[checkbox.draw_frame]: #checkbox-draw_frame
[draw_frame]: #checkbox-draw_frame

<div class="FunctionDoc YAMLDoc" id="checkbox-draw_text" markdown="1">

## function __checkbox\.draw\_text__\(text, html=True\)

Draws text inside the widget.

__Arguments:__

- `text` -- The text to draw.
	- Type: str, unicode

__Keywords:__

- `html` -- Indicates whether HTML should be parsed.
	- Type: bool
	- Default: True

</div>

[checkbox.draw_text]: #checkbox-draw_text
[draw_text]: #checkbox-draw_text

<div class="FunctionDoc YAMLDoc" id="checkbox-on_mouse_click" markdown="1">

## function __checkbox\.on\_mouse\_click__\(pos\)

Is called whenever the user clicks on the widget. Toggles the state of the checkbox.

__Arguments:__

- `pos` -- An (x, y) coordinate tuple.
	- Type: tuple

</div>

[checkbox.on_mouse_click]: #checkbox-on_mouse_click
[on_mouse_click]: #checkbox-on_mouse_click

<div class="FunctionDoc YAMLDoc" id="checkbox-render" markdown="1">

## function __checkbox\.render__\(\)

Draws the widget.

</div>

[checkbox.render]: #checkbox-render
[render]: #checkbox-render

<div class="FunctionDoc YAMLDoc" id="checkbox-set_checked" markdown="1">

## function __checkbox\.set\_checked__\(checked=True\)

Sets the checked status of the checkbox.

__Keywords:__

- `checked` -- The checked status.
	- Type: bool
	- Default: True

</div>

[checkbox.set_checked]: #checkbox-set_checked
[set_checked]: #checkbox-set_checked

<div class="FunctionDoc YAMLDoc" id="checkbox-set_rect" markdown="1">

## function __checkbox\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

[checkbox.set_rect]: #checkbox-set_rect
[set_rect]: #checkbox-set_rect

<div class="FunctionDoc YAMLDoc" id="checkbox-set_var" markdown="1">

## function __checkbox\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.
	- Type: str, unicode

__Keywords:__

- `var` -- A variable name, or `None` to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

[checkbox.set_var]: #checkbox-set_var
[set_var]: #checkbox-set_var

</div>

[checkbox]: #checkbox

