<div class="ClassDoc YAMLDoc" id="ImageWidget" markdown="1">

# class __ImageWidget__

The `Image` widget is used to display a non-interactive image.

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 image path='5.png'
~~~

__Example (Python):__

~~~ .python
form = Form()
# The full path to the image needs to be provided.
# self.experiment.pool can be used to retrieve the full path
# to an image in the file pool.
image = ImageWidget(path=pool['5.png'])
form.set_widget(image, (0,0))
form._exec()
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="ImageWidget-__init__" markdown="1">

## function __ImageWidget\.\_\_init\_\___\(form, path=None, adjust=True, frame=False\)

Constructor to create a new `ImageWidget` object. You do not
generally call this constructor directly, but use the
`ImageWidget()` factory function, which is described here:
[/python/common/]().

__Arguments:__

- `form` -- The parent form.
	- Type: form

__Keywords:__

- `path` -- The full path to the image. To show an image from the file pool, you need to first use `experiment.get_file` to determine the full path to the image.
	- Type: str, unicode, NoneType
	- Default: None
- `adjust` -- Indicates whether the image should be scaled according to the size of the widget.
	- Type: bool
	- Default: True
- `frame` -- Indicates whether a frame should be drawn around the widget.
	- Type: bool
	- Default: False

</div>

<div class="FunctionDoc YAMLDoc" id="ImageWidget-_init_canvas_elements" markdown="1">

## function __ImageWidget\.\_init\_canvas\_elements__\(\)

Initializes all canvas elements.

</div>

<div class="FunctionDoc YAMLDoc" id="ImageWidget-_update" markdown="1">

## function __ImageWidget\.\_update__\(\)

Draws the widget.

</div>

<div class="FunctionDoc YAMLDoc" id="ImageWidget-_update_frame" markdown="1">

## function __ImageWidget\.\_update\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

<div class="FunctionDoc YAMLDoc" id="ImageWidget-coroutine" markdown="1">

## function __ImageWidget\.coroutine__\(\)

Implements the interaction. This can be overridden to implement more complicated keyboard/ mouse interactions.

</div>

<div class="FunctionDoc YAMLDoc" id="ImageWidget-on_key_press" markdown="1">

## function __ImageWidget\.on\_key\_press__\(key\)

Is called whenever the widget is focused and the users enters a key.

__Arguments:__

- `key` -- A key
	- Type: str

</div>

<div class="FunctionDoc YAMLDoc" id="ImageWidget-on_mouse_click" markdown="1">

## function __ImageWidget\.on\_mouse\_click__\(pos\)

Is called whenever the user clicks on the widget.

__Arguments:__

- `pos` -- An (x, y) coordinates tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="ImageWidget-set_rect" markdown="1">

## function __ImageWidget\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="ImageWidget-set_var" markdown="1">

## function __ImageWidget\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.

__Keywords:__

- `var` -- A variable name, or None to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

</div>

