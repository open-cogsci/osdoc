<div class="ClassDoc YAMLDoc" id="image" markdown="1">

# class __image__

The image widget is used to display a non-interactive image.

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 image path='5.png'
~~~

__Example (Python):__

~~~ .python
from libopensesame import widgets
form = widgets.form(exp)
# The full path to the image needs to be provided.
# self.experiment.pool can be used to retrieve the full path
# to an image in the file pool.
image = widgets.image(form, path=pool['5.png'])
form.set_widget(image, (0,0))
form._exec()
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="image-__init__" markdown="1">

## function __image\.\_\_init\_\___\(form, path=None, adjust=True, frame=False\)

Constructor.

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

[image.__init__]: #image-__init__
[__init__]: #image-__init__

<div class="FunctionDoc YAMLDoc" id="image-draw_frame" markdown="1">

## function __image\.draw\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

[image.draw_frame]: #image-draw_frame
[draw_frame]: #image-draw_frame

<div class="FunctionDoc YAMLDoc" id="image-on_mouse_click" markdown="1">

## function __image\.on\_mouse\_click__\(pos\)

Is called whenever the user clicks on the widget.

__Arguments:__

- `pos` -- An (x, y) coordinates tuple.
	- Type: tuple

</div>

[image.on_mouse_click]: #image-on_mouse_click
[on_mouse_click]: #image-on_mouse_click

<div class="FunctionDoc YAMLDoc" id="image-render" markdown="1">

## function __image\.render__\(\)

Draws the widget.

</div>

[image.render]: #image-render
[render]: #image-render

<div class="FunctionDoc YAMLDoc" id="image-set_rect" markdown="1">

## function __image\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

[image.set_rect]: #image-set_rect
[set_rect]: #image-set_rect

<div class="FunctionDoc YAMLDoc" id="image-set_var" markdown="1">

## function __image\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.

__Keywords:__

- `var` -- A variable name, or None to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

[image.set_var]: #image-set_var
[set_var]: #image-set_var

</div>

[image]: #image

