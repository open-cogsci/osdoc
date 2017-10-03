<div class="ClassDoc YAMLDoc" id="Label" markdown="1">

# class __Label__

The `Label` widget is a non-interactive string of text.

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 label text='My text'
~~~

__Example (Python):__

~~~ .python
form = Form()
label = Label(text='My text')
form.set_widget(label, (0,0))
form._exec()
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="Label-__init__" markdown="1">

## function __Label\.\_\_init\_\___\(form, text=u'label', frame=False, center=True\)

Constructor to create a new `Label` object. You do not generally
call this constructor directly, but use the `Label()` factory
function, which is described here: [/python/common/]().

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

<div class="FunctionDoc YAMLDoc" id="Label-_init_canvas_elements" markdown="1">

## function __Label\.\_init\_canvas\_elements__\(\)

Initializes all canvas elements.

</div>

<div class="FunctionDoc YAMLDoc" id="Label-_update" markdown="1">

## function __Label\.\_update__\(\)

Draws the widget.

</div>

<div class="FunctionDoc YAMLDoc" id="Label-_update_frame" markdown="1">

## function __Label\.\_update\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

<div class="FunctionDoc YAMLDoc" id="Label-_update_text" markdown="1">

## function __Label\.\_update\_text__\(text\)

Draws text inside the widget.

__Arguments:__

- `text` -- The text to draw.
	- Type: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="Label-coroutine" markdown="1">

## function __Label\.coroutine__\(\)

Implements the interaction. This can be overridden to implement more complicated keyboard/ mouse interactions.

</div>

<div class="FunctionDoc YAMLDoc" id="Label-on_key_press" markdown="1">

## function __Label\.on\_key\_press__\(key\)

Is called whenever the widget is focused and the users enters a key.

__Arguments:__

- `key` -- A key
	- Type: str

</div>

<div class="FunctionDoc YAMLDoc" id="Label-on_mouse_click" markdown="1">

## function __Label\.on\_mouse\_click__\(pos\)

Is called whenever the user clicks on the widget.

__Arguments:__

- `pos` -- An (x, y) coordinates tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="Label-set_rect" markdown="1">

## function __Label\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="Label-set_var" markdown="1">

## function __Label\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.

__Keywords:__

- `var` -- A variable name, or None to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

</div>

