<div class="ClassDoc YAMLDoc" id="text_input" markdown="1">

# class __text_input__

The text_input widget allows the participant to enter multi-character
responses. (This widget has no relation to the text_input plug-in, which
was created before forms where added to OpenSesame.)

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 text_input var='response' return_accepts='yes'
~~~

__Example (Python):__

~~~ {.python}
from libopensesame import widgets
form = widgets.form(exp)
text_input = widgets.text_input(form, var='response',
        return_accepts=True)
form.set_widget(text_input, (0,0))
form._exec()
~~~

__Function list:__

%--
toc:
        mindepth: 2
        maxdepth: 2
--%

<div class="FunctionDoc YAMLDoc" id="text_input-__init__" markdown="1">

## function __text\_input\.\_\_init\_\___\(form, text=u'', frame=True, center=False, stub=u'Type here \.\.\.', return\_accepts=False, var=None\)

Constructor.

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

</div>

[text_input.__init__]: #text_input-__init__
[__init__]: #text_input-__init__

<div class="FunctionDoc YAMLDoc" id="text_input-draw_frame" markdown="1">

## function __text\_input\.draw\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

[text_input.draw_frame]: #text_input-draw_frame
[draw_frame]: #text_input-draw_frame

<div class="FunctionDoc YAMLDoc" id="text_input-draw_text" markdown="1">

## function __text\_input\.draw\_text__\(text, html=True\)

Draws text inside the widget.

__Arguments:__

- `text` -- The text to draw.
	- Type: str, unicode

__Keywords:__

- `html` -- Indicates whether HTML should be parsed.
	- Type: bool
	- Default: True

</div>

[text_input.draw_text]: #text_input-draw_text
[draw_text]: #text_input-draw_text

<div class="FunctionDoc YAMLDoc" id="text_input-on_mouse_click" markdown="1">

## function __text\_input\.on\_mouse\_click__\(pos\)

Is called whenever the user clicks on the widget. Activates the text input for typing text.

__Arguments:__

- `pos` -- An (x, y) coordinates tuple.
	- Type: tuple

</div>

[text_input.on_mouse_click]: #text_input-on_mouse_click
[on_mouse_click]: #text_input-on_mouse_click

<div class="FunctionDoc YAMLDoc" id="text_input-render" markdown="1">

## function __text\_input\.render__\(\)

Draws the widget.

</div>

[text_input.render]: #text_input-render
[render]: #text_input-render

<div class="FunctionDoc YAMLDoc" id="text_input-set_rect" markdown="1">

## function __text\_input\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

[text_input.set_rect]: #text_input-set_rect
[set_rect]: #text_input-set_rect

<div class="FunctionDoc YAMLDoc" id="text_input-set_var" markdown="1">

## function __text\_input\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.

__Keywords:__

- `var` -- A variable name, or None to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

[text_input.set_var]: #text_input-set_var
[set_var]: #text_input-set_var

</div>

[text_input]: #text_input

