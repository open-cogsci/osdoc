<div class="ClassDoc YAMLDoc" markdown="1">

# class __Checkbox__

The `Checkbox` widget is a checkable box accompanied by a string of
text.

__Example (OpenSesame script):__

~~~
widget 0 0 1 1 checkbox
group="group" text="Option 1"
widget 0 1 1 1 checkbox group="group"
text="Option 2"
~~~

__Example (Python):__

~~~ .python
form = Form()
checkbox1 = Checkbox(text='Option 1', group='group')
checkbox2 =
Checkbox(text='Option 2', group='group')
form.set_widget(checkbox1, (0,0))
form.set_widget(checkbox2, (0,1))
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

Is called whenever the user clicks on the widget. Toggles the state
of the checkbox.


__Parameters__

- **pos**: An (x, y) coordinate tuple.


## set_checked(checked=True)

Sets the checked status of the checkbox.


__Parameters__

- **checked**: The checked status.


## set_rect(rect)

Sets the widget geometry.


__Parameters__

- **rect**: A (left, top, width, height) tuple.


## set_var(val, var=None)

Sets an experimental variable.


__Parameters__

- **val**: A value.
- **var**: A variable name, or `None` to use widget default.


</div>

