<div class="ClassDoc YAMLDoc" markdown="1">

# class __Label__

The `Label` widget is a non-interactive string of text.

__Example
(OpenSesame script):__

~~~
widget 0 0 1 1 label text='My text'
~~~
__Example (Python):__

~~~ .python
form = Form()
label = Label(text='My
text')
form.set_widget(label, (0,0))
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

Is called whenever the user clicks on the widget.


__Parameters__

- **pos**: An (x, y) coordinates tuple.


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

