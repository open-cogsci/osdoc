<div class="ClassDoc YAMLDoc" id="rating_scale" markdown="1">

# class __rating_scale__

The rating_scale widget is a horizontally aligned series of checkable
boxes (nodes), optionally with a label attached to each node.

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 label text="I like fluffy kittens"
widget 0 1 1 1 rating_scale var="response" nodes="Agree;Don't know;Disagree"
~~~

__Example (OpenSesame script):__

~~~ .python
from libopensesame import widgets
form = widgets.form(exp)
label = widgets.label(form, text='I like fluffy kittens')
rating_scale = widgets.rating_scale(form, nodes=['Agree', "Don't know",
        'Disagree'], var='response')
form.set_widget(label, (0,0))
form.set_widget(rating_scale, (0,1))
form._exec()
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="rating_scale-__init__" markdown="1">

## function __rating\_scale\.\_\_init\_\___\(form, nodes=5, click\_accepts=False, orientation=u'horizontal', var=None, default=None\)

Constructor.

__Arguments:__

- `form` -- The parent form.
	- Type: form

__Keywords:__

- `nodes` -- The number of nodes or a list of node identifiers (e.g., ['yes', 'no', 'maybe']. If a list is passed the rating scale will have labels, otherwise it will just have boxes.
	- Type: int, list
	- Default: 5
- `click_accepts` -- Indicates whether the form should close when a value is selected.
	- Type: bool
	- Default: False
- `orientation` -- 'horizontal' indicates a horizontally oriented rating
scale, 'vertical' indicates a vertically oriented rating
scale.
	- Type: str, unicode
	- Default: 'horizontal'
- `var` -- The name of the experimental variable that should be used to log the widget status. The value that is logged is the number of the node that was selected, with the first node being 0. If no nodes were selected, the value is 'None'. For more information about the use of response variables in forms, see the form documentation page.
	- Type: str, unicode, NoneType
	- Default: None
- `default` -- The node that is selected by default, or `None` to select no node. The value corresponds to the node number, where 0 is the first node.
	- Type: int, NoneType
	- Default: None

</div>

<div class="FunctionDoc YAMLDoc" id="rating_scale-draw_frame" markdown="1">

## function __rating\_scale\.draw\_frame__\(rect=None, style=u'normal'\)

Draws a simple frame around the widget.

__Keywords:__

- `rect` -- A (left, top, width, height) tuple for the frame geometry or `None` to use the widget geometry.
	- Type: tuple, NoneType
	- Default: None
- `style` -- A visual style. Should be 'normal', 'active', or 'light'.
	- Type: str, unicode
	- Default: 'normal'

</div>

<div class="FunctionDoc YAMLDoc" id="rating_scale-on_mouse_click" markdown="1">

## function __rating\_scale\.on\_mouse\_click__\(pos\)

Is called whenever the user clicks on the widget. Selects the correct value from the scale and optionally closes the form.

__Arguments:__

- `pos` -- An (x, y) coordinates tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="rating_scale-render" markdown="1">

## function __rating\_scale\.render__\(\)

Draws the widget.

</div>

<div class="FunctionDoc YAMLDoc" id="rating_scale-set_rect" markdown="1">

## function __rating\_scale\.set\_rect__\(rect\)

Sets the widget geometry.

__Arguments:__

- `rect` -- A (left, top, width, height) tuple.
	- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="rating_scale-set_value" markdown="1">

## function __rating\_scale\.set\_value__\(val\)

Sets the rating scale value.

__Arguments:__

- `val` -- The value.
	- Type: int

</div>

<div class="FunctionDoc YAMLDoc" id="rating_scale-set_var" markdown="1">

## function __rating\_scale\.set\_var__\(val, var=None\)

Sets an experimental variable.

__Arguments:__

- `val` -- A value.

__Keywords:__

- `var` -- A variable name, or None to use widget default.
	- Type: str, unicode, NoneType
	- Default: None

</div>

</div>

