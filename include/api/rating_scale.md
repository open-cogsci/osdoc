<div class="ClassDoc YAMLDoc" markdown="1">

# class __RatingScale__

The rating_scale widget is a horizontally aligned series of checkable
boxes (nodes), optionally with a label attached to each node.

__Example
(OpenSesame script):__

~~~
widget 0 0 1 1 label text="I like fluffy
kittens"
widget 0 1 1 1 rating_scale var="response" nodes="Agree;Don't
know;Disagree"
~~~

__Example (OpenSesame script):__

~~~ .python
form =
Form()
label = Label(text='I like fluffy kittens')
rating_scale =
RatingScale(nodes=['Agree', "Don't know",
        'Disagree'],
var='response')
form.set_widget(label, (0,0))
form.set_widget(rating_scale,
(0,1))
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

Is called whenever the user clicks on the widget. Selects the
correct value from the scale and optionally closes the form.


__Parameters__

- **pos**: An (x, y) coordinates tuple.


## set_rect(rect)

Sets the widget geometry.


__Parameters__

- **rect**: A (left, top, width, height) tuple.


## set_value(val)

Sets the rating scale value.


__Parameters__

- **val**: The value.


## set_var(val, var=None)

Sets an experimental variable.


__Parameters__

- **val    A value.**: 
- **var**: A variable name, or None to use widget default.


</div>

