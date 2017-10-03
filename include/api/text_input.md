<div class="ClassDoc YAMLDoc" id="TextInput" markdown="1">

# class __TextInput__

The text_input widget allows the participant to enter multi-character
responses. (This widget has no relation to the text_input plug-in, which
was created before forms where added to OpenSesame.)

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 text_input var='response' return_accepts='yes'
~~~

__Example (Python):__

~~~ .python
form = Form()
text_input = TextInput(var='response', return_accepts=True)
form.set_widget(text_input, (0,0))
form._exec()
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="TextInput-__init__" markdown="1">

## function __TextInput\.\_\_init\_\___\(form, text=u'', frame=True, center=False, stub=u'Type here \.\.\.', return\_accepts=False, var=None, key\_filter=None\)

Constructor to create a new `TextInput` object. You do not generally
call this constructor directly, but use the `TextInput()` factory
function, which is described here: [/python/common/]().

__Arguments:__

- `form` -- The parent form.
	- Type: form

__Keywords:__

- `text` -- The text to start with.
	- Type: str, unicode
	- Default: ''
- `frame` -- Indicates whether a frame should be drawn around the widget.
	- Type: bool
	- Default: True
- `center` -- Indicates whether the text should be centered.
	- Type: bool
	- Default: False
- `stub` -- A text string that should be shown whenever the user has not entered any text.
	- Type: str, unicode
	- Default: 'Type here ...'
- `return_accepts` -- Indicates whether a return press should accept and close the form.
	- Type: bool
	- Default: False
- `var` -- The name of the experimental variable that should be used to log the widget status.
	- Type: str, unicode, NoneType
	- Default: None
- `key_filter` -- A function that takes a key as a single argument and return True if the key should be accepted and False otherwise. This can also filter out keys such as return and backspace, but not Escape.
	- Type: FunctionType, NoneType
	- Default: None

</div>

<div class="FunctionDoc YAMLDoc" id="TextInput-_init_canvas_elements" markdown="1">

## function __TextInput\.\_init\_canvas\_elements__\(\)

Initializes all canvas elements.

</div>

<div class="FunctionDoc YAMLDoc" id="TextInput-_update" markdown="1">

## function __TextInput\.\_update__\(\)

Draws the widget.

</div>

<div class="FunctionDoc YAMLDoc" id="TextInput-_update_frame" markdown="1">

## function __TextInput\.\_update\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

<div class="FunctionDoc YAMLDoc" id="TextInput-_update_text" markdown="1">

## function __TextInput\.\_update\_text__\(text\)

Draws text inside the widget.

__Arguments:__

- `text` -- The text to draw.
	- Type: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="TextInput-coroutine" markdown="1">

## function __TextInput\.coroutine__\(\)

Implements the interaction.

</div>

<div class="FunctionDoc YAMLDoc" id="TextInput-on_key_press" markdown="1">

## function __TextInput\.on\_key\_press__\(key\)

Is called whenever the widget is focused and the users enters a key.

__Arguments:__

- `key` -- A key
	- Type: str

</div>

<div class="FunctionDoc YAMLDoc" id="TextInput-on_mouse_click" markdown="1">

## function __TextInput\.on\_mouse\_click__\(pos\)

Is called whenever the user clicks on the widget.

__Arguments:__

- `pos` -- An (x, y) coordinates tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="TextInput-set_rect" markdown="1">

## function __TextInput\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="TextInput-set_var" markdown="1">

## function __TextInput\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.

__Keywords:__

- `var` -- A variable name, or None to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

</div>

