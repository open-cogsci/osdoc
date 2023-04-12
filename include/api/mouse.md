<div class="ClassDoc YAMLDoc" markdown="1">

# class __Mouse__

The `Mouse` class is used to collect mouse input. You generally create a
`Mouse` object with the `Mouse()` factory function, as described in the
section [Creating a Mouse](#creating-a-mouse).

__Example__

~~~ .python
# Draw a 'fixation-dot mouse cursor' until a button is clicked
my_mouse = Mouse()
my_canvas = Canvas()
while True:
    button, position, timestamp = my_mouse.get_click(timeout=20)
    if button is not None:
        break
    (x,y), time = my_mouse.get_pos()
    my_canvas.clear()
    my_canvas.fixdot(x, y)
    my_canvas.show()
~~~

[TOC]

## Things to know

### Creating a Mouse

You generally create a `Mouse` with the `Mouse()` factory function:

~~~ .python
my_mouse = Mouse()
~~~

Optionally, you can pass [Response keywords](#response-keywords) to `Mouse()`
to set the default behavior:

~~~ .python
my_mouse = Mouse(timeout=2000)
~~~

### Coordinates

- When *Uniform coordinates* is set to 'yes', coordinates are relative to the
  center of the display. That is, (0,0) is the center. This is the default as
  of OpenSesame 3.0.0.
- When *Uniform coordinates* is set to 'no', coordinates are relative to the
  top-left of the display. That is, (0,0) is the top-left. This was the default
  in OpenSesame 2.9.X and earlier.

### Button numbers

Mouse buttons are numbered as follows:

1. Left button
2. Middle button
3. Right button
4. Scroll up
5. Scroll down

### Touch screens

When working with a touch screen, a touch is registered as button 1
(left button).

### Response keywords

Functions that accept `**resp_args` take the following keyword arguments:

- `timeout` specifies a timeout value in milliseconds, or is set to `None` to
  disable the timeout.
- `buttonlist` specifies a list of buttons that are accepted, or is set to
  `None` accept all buttons.
- `visible` indicates whether the mouse cursor becomes visible when a click is
  collected (`True` or `False`). To immediately change cursor visibility, use
  `Mouse.show_cursor()`.

~~~ .python
# Get a left or right button press with a timeout of 3000 ms
my_mouse = Mouse()
button, time = my_mouse.get_click(buttonlist=[1,3], timeout=3000)
~~~

Response keywords only affect the current operation (except when passed to
`Mouse()` when creating the object). To change the behavior for all subsequent
operations, set the response properties directly:

~~~ .python
# Get two left or right presses with a 5000 ms timeout
my_mouse = Mouse()
my_mouse.buttonlist = [1,3]
my_mouse.timeout = 5000
button1, time1 = my_mouse.get_click()
button2, time2 = my_mouse.get_click()
~~~

Or pass the response keywords to `Mouse()` when creating the object:

~~~ .python
# Get two left or right presses with a 5000 ms timeout
my_mouse = Mouse(buttonlist=[1,3], timeout=5000)
button1, time1 = my_mouse.get_click()
button2, time2 = my_mouse.get_click()
~~~

## flush(self)

Clears all pending input, not limited to the mouse.



__Returns__

- True if a button had been clicked (i.e., if there was something to
flush) and False otherwise.

__Example__

~~~ .python
my_mouse = Mouse()
my_mouse.flush()
button, position, timestamp = my_mouse.get_click()
~~~



## get_click(\*arglist, \*\*kwdict)

Collects a mouse click.


__Parameters__

- **\*\*resp_args**: Optional [response keywords](#response-keywords) that will be used
for this call to `Mouse.get_click()`. This does not affect
subsequent operations.

__Returns__

- A (button, position, timestamp) tuple. The button and position are
`None` if a timeout occurs. Position is an (x, y) tuple in screen
coordinates.

__Example__

~~~ .python
my_mouse = Mouse()
button, (x, y), timestamp = my_mouse.get_click(timeout=5000)
if button is None:
        print('A timeout occurred!')
~~~



## get_click_release(\*arglist, \*\*kwdict)

*New in v3.2.0*

Collects a mouse-click release.

*Important:* This
function is currently not implemented for the
*psycho* backend.

__Parameters__

- **\*\*resp_args**: Optional [response keywords](#response-keywords) that will be used
for this call to `Mouse.get_click_release()`. This does not affect
subsequent operations.

__Returns__

- A (button, position, timestamp) tuple. The button and position are
`None` if a timeout occurs. Position is an (x, y) tuple in screen
coordinates.

__Example__

~~~ .python
my_mouse = Mouse()
button, (x, y), timestamp = my_mouse.get_click_release(timeout=5000)
if button is None:
        print('A timeout occurred!')
~~~



## get_pos(self)

Returns the current position of the cursor.



__Returns__

- A (position, timestamp) tuple.

__Example__

~~~ .python
my_mouse = Mouse()
(x, y), timestamp = my_mouse.get_pos()
print('The cursor was at (%d, %d)' % (x, y))
~~~



## get_pressed(self)

Returns the current state of the mouse buttons. A True value means
the button is currently being pressed.



__Returns__

- A (button1, button2, button3) tuple of boolean values.

__Example__

~~~ .python
my_mouse = Mouse()
buttons = my_mouse.get_pressed()
b1, b2, b3 = buttons
print('Currently pressed mouse buttons: (%d,%d,%d)' % (b1,b2,b3))
~~~



## set_pos(pos=(0, 0))

Sets the position of the mouse cursor.

__Warning:__ `set_pos()` is
unreliable and will silently fail on
some systems.

__Parameters__

- **pos**: An (x,y) tuple for the new mouse coordinates.

__Example__

~~~ .python
my_mouse = Mouse()
my_mouse.set_pos(pos=(0,0))
~~~



## show_cursor(show=True)

Immediately changes the visibility of the mouse cursor.

__Note:__
In most cases, you will want to use the `visible`
keyword, which
changes the visibility during response collection,
that is, while
`mouse.get_click()` is called. Calling 
`show_cursor()` will not
implicitly change the value of `visible`, 
which can lead to the
somewhat unintuitive behavior that the cursor
is hidden as soon as
`get_click()` is called.

__Parameters__

- **show**: Indicates whether the cursor is shown (True) or hidden (False).


## synonyms(button)

Gives a list of synonyms for a mouse button. For example, 1 and
'left_button' are synonyms.


__Parameters__

- **button**: A button value.

__Returns__

- A list of synonyms.


</div>

