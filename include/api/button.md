<div class="ClassDoc YAMLDoc" id="Button" markdown="1">

# class __Button__

The `Button` widget is a clickable text string, by default surrounded by
a button-like frame.

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 button text='Click me!' center='yes' frame='yes' var='response'
~~~

Defining a button widget with Python inline code:

__Example (Python):__

~~~ .python
form = Form()
button = Button(text='Click me!', frame=True, center=True, var='response')
form.set_widget(button, (0,0))
form._exec()
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="Button-__init__" markdown="1">

## function __Button\.\_\_init\_\___\(form, text=u'button', frame=True, center=True, var=None\)

Constructor to create a new `Button` object. You do not generally
call this constructor directly, but use the `Button()` factory
function, which is described here: [/python/common/]().

__Arguments:__

- `form` -- The parent form.
	- Type: form

__Keywords:__

- `text` -- Button text.
	- Type: str, unicode
	- Default: 'button'
- `frame` -- Indicates whether a frame should be drawn around the widget.
	- Type: bool
	- Default: True
- `center` -- Indicates whether the text should be centered.
	- Type: bool
	- Default: True
- `var` -- The name of the experimental variable that should be used to log the widget status.
	- Type: str, unicode, NoneType
	- Default: None

</div>

<div class="FunctionDoc YAMLDoc" id="Button-_init_canvas_elements" markdown="1">

## function __Button\.\_init\_canvas\_elements__\(\)

Initializes all canvas elements.

</div>

<div class="FunctionDoc YAMLDoc" id="Button-_update" markdown="1">

## function __Button\.\_update__\(\)

Draws the widget.

</div>

<div class="FunctionDoc YAMLDoc" id="Button-_update_frame" markdown="1">

## function __Button\.\_update\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

<div class="FunctionDoc YAMLDoc" id="Button-_update_text" markdown="1">

## function __Button\.\_update\_text__\(text\)

Draws text inside the widget.

__Arguments:__

- `text` -- The text to draw.
	- Type: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="Button-coroutine" markdown="1">

## function __Button\.coroutine__\(\)

Implements the interaction. This can be overridden to implement more complicated keyboard/ mouse interactions.

</div>

<div class="FunctionDoc YAMLDoc" id="Button-on_key_press" markdown="1">

## function __Button\.on\_key\_press__\(key\)

Is called whenever the widget is focused and the users enters a key.

__Arguments:__

- `key` -- A key
	- Type: str

</div>

<div class="FunctionDoc YAMLDoc" id="Button-on_mouse_click" markdown="1">

## function __Button\.on\_mouse\_click__\(pos\)

Is called when the user clicks on the button. Returns the button text.

__Arguments:__

- `pos` -- An (x, y) coordinates tuple.
	- Type: tuple

__Returns:__

The button text.

- Type: unicode

</div>

<div class="FunctionDoc YAMLDoc" id="Button-set_rect" markdown="1">

## function __Button\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="Button-set_var" markdown="1">

## function __Button\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.

__Keywords:__

- `var` -- A variable name, or None to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

</div>

