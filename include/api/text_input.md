<div class="ClassDoc YAMLDoc" markdown="1">

# class __TextInput__

The text_input widget allows the participant to enter multi-character
responses. (This widget has no relation to the text_input plug-in, which
was created before forms where added to OpenSesame.)

__Example (OpenSesame
script):__

~~~
widget 0 0 1 1 text_input var='response'
return_accepts='yes'
~~~

__Example (Python):__

~~~ .python
form = Form()
text_input = TextInput(var='response', return_accepts=True)
form.set_widget(text_input, (0,0))
form._exec()
~~~

[TOC]

## coroutine(self)

Implements the interaction.




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

