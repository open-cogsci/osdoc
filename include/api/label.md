<div class="ClassDoc YAMLDoc" id="label" markdown="1">

# class __label__

The label widget is a non-interactive string of text.

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 label text='My text'
~~~

__Example (Python):__

~~~ .python
from libopensesame import widgets
form = widgets.form(exp)
label = widgets.label(form, text='My text')
form.set_widget(label, (0,0))
form._exec()
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="label-__init__" markdown="1">

## function __label\.\_\_init\_\___\(form, text=u'label', frame=False, center=True\)

Constructor.

__Arguments:__

- `form` -- The parent form.
	- Type: form

__Keywords:__

- `text` -- The label text.
	- Type: str, unicode
	- Default: 'label'
- `frame` -- Indicates whether a frame should be drawn around the widget.
	- Type: bool
	- Default: False
- `center` -- Indicates whether the text should be centerd.
	- Type: bool
	- Default: True

</div>

<div class="FunctionDoc YAMLDoc" id="label-draw_frame" markdown="1">

## function __label\.draw\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

<div class="FunctionDoc YAMLDoc" id="label-draw_text" markdown="1">

## function __label\.draw\_text__\(text, html=True\)

Draws text inside the widget.

__Arguments:__

- `text` -- The text to draw.
	- Type: str, unicode

__Keywords:__

- `html` -- Indicates whether HTML should be parsed.
	- Type: bool
	- Default: True

</div>

<div class="FunctionDoc YAMLDoc" id="label-on_mouse_click" markdown="1">

## function __label\.on\_mouse\_click__\(pos\)

Is called whenever the user clicks on the widget.

__Arguments:__

- `pos` -- An (x, y) coordinates tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="label-render" markdown="1">

## function __label\.render__\(\)

Draws the widget.

</div>

<div class="FunctionDoc YAMLDoc" id="label-set_rect" markdown="1">

## function __label\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="label-set_var" markdown="1">

## function __label\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.

__Keywords:__

- `var` -- A variable name, or None to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

</div>

