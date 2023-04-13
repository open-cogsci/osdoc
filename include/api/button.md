<div class="ClassDoc YAMLDoc" markdown="1">

# class __Button__

The `Button` widget is a clickable text string, by default surrounded
by
a button-like frame.

__Example (OpenSesame script):__

~~~
widget 0 0 1
1 button text='Click me!' center='yes' frame='yes' var='response'
~~~
Defining a button widget with Python inline code:

__Example (Python):__
~~~ .python
form = Form()
button = Button(text='Click me!', frame=True,
center=True, var='response')
form.set_widget(button, (0,0))
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

Is called when the user clicks on the button. Returns the button
text.


__Parameters__

- **pos**: An (x, y) coordinates tuple.

__Returns__

- The button text.


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

