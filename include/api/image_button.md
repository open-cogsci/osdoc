<div class="ClassDoc YAMLDoc" markdown="1">

# class __ImageButton__

The image_button widget is a clickable image.

__Example (OpenSesame
script):__

~~~
widget 0 0 1 1 image_button path='5.png' var='response'
~~~
__Example (Python):__

~~~ .python
form = Form()
# The full path to the
image needs to be provided.
# self.experiment.pool can be used to retrieve
the full path
# to an image in the file pool.
image_button =
ImageButton(path=pool['5.png'], var='response')
form.set_widget(image_button, (0,0))
form._exec()
~~~

[TOC]

## coroutine(self)

Implements the interaction. This can be overridden to implement
more complicated keyboard/ mouse interactions.




## on_key_press(key)

Is called whenever the widget is focused and the users enters a
key.


__Parameters__

- **key**: A key


## on_mouse_click(pos)

Is called whenever the user clicks on the widget. Returns the
image_id or the path to the image if no image_id has been specified.


__Parameters__

- **pos**: An (x, y) coordinate tuple.


## set_rect(rect)

Sets the widget geometry.


__Parameters__

- **rect**: A (left, top, width, height) tuple.


## set_var(val, var=None)

Sets an experimental variable.


__Parameters__

- **val    A value.**: 
- **var**: A variable name, or None to use widget default.


</div>

