<div class="ClassDoc YAMLDoc" id="mouse" markdown="1">

# class __mouse__

The `mouse` class is used to collect mouse input.

__Example:__

~~~ .python
# Draw a 'fixation-dot mouse cursor' until a button is clicked
my_mouse = mouse()
my_canvas = canvas()
while True:
        button, position, timestamp = my_mouse.get_click(timeout=20)
        if button is not None:
                break
        (x,y), time = my_mouse.get_pos()
        my_canvas.clear()
        my_canvas.fixdot(x, y)
        my_canvas.show()
~~~

## Things to know

### Coordinates

- When *Uniform coordinates* is set to 'yes', coordinates are
  relative to the center of the display. That is, (0,0) is the center.
  This is the default as of OpenSesame 3.0.0.
- When *Uniform coordinates* is set to 'no', coordinates are relative to
  the top-left of the display. That is, (0,0) is the top-left. This was
  the default in OpenSesame 2.9.X and earlier.

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

Functions that accept `**resp_args` take the following keyword
arguments:

- `timeout` specifies a timeout value in milliseconds, or is set to
  `None` to disable the timeout.
- `buttonlist` specifies a list of buttons that are accepted, or is set
  to `None` accept all keys.
- `visible` indicates whether the mouse cursor becomes visible when a
  click is collected (`True` or `False`). To immediately change cursor
  visibility, use [mouse.show_cursor].

~~~ .python
# Get a left or right button press with a timeout of 3000 ms
my_mouse = mouse()
button, time = my_mouse.get_key(buttonlist=[1,3], timeout=3000)
~~~

Response keywords only affect the current operation (except when passed
to [mouse.\_\_init\_\_][__init__]). To change the behavior for all
subsequent operations, set the response properties directly:

~~~ .python
# Get two key left or right presses with a 5000 ms timeout
my_mouse = mouse()
my_mouse.keylist = [1,3]
my_mouse.timeout = 5000
button1, time1 = my_mouse.get_button()
button2, time2 = my_mouse.get_button()
~~~

Or pass the response keywords to [mouse.\_\_init\_\_][__init__]:

~~~ .python
# Get two key left or right presses with a 5000 ms timeout
my_mouse = mouse(keylist=[1,3], timeout=5000)
button1, time1 = my_mouse.get_button()
button2, time2 = my_mouse.get_button()
~~~

<div class="FunctionDoc YAMLDoc" id="mouse-__init__" markdown="1">

## function __mouse\.\_\_init\_\___\(experiment, \*\*resp\_args\)

Constructor to create a new `mouse` object. You do not generally
call this constructor directly, but use the `mouse()` function,
which is described here: [/python/common/]().

__Example:__

~~~ .python
my_mouse = mouse(buttonlist=[1, 2], timeout=2000)
~~~

__Arguments:__

- `experiment` -- The experiment object.
	- Type: experiment

__Keyword dict:__

- `**resp_args`: Optional [response keywords] that will be used as the default for this `mouse` object.

</div>

[mouse.__init__]: #mouse-__init__
[__init__]: #mouse-__init__

<div class="FunctionDoc YAMLDoc" id="mouse-flush" markdown="1">

## function __mouse\.flush__\(\)

Clears all pending input, not limited to the mouse.

__Example:__

~~~ .python
my_mouse = mouse()
my_mouse.flush()
button, position, timestamp = my_mouse.get_click()
~~~

__Returns:__

True if a button had been clicked (i.e., if there was something to flush) and False otherwise.

- Type: bool

</div>

[mouse.flush]: #mouse-flush
[flush]: #mouse-flush

<div class="FunctionDoc YAMLDoc" id="mouse-get_click" markdown="1">

## function __mouse\.get\_click__\(\*\*resp\_args\)

Collects a mouse click.

__Example:__

~~~ .python
my_mouse = mouse()
button, (x, y), timestamp = my_mouse.get_click(timeout=5000)
if button is None:
        print('A timeout occurred!')
~~~

__Keyword dict:__

- `**resp_args`: Optional [response keywords] that will be used for this call to [mouse.get_click]. This does not affect subsequent operations.

__Returns:__

A (button, position, timestamp) tuple. The button and position are `None` if a timeout occurs. Position is an (x, y) tuple in screen coordinates.

- Type: tuple

</div>

[mouse.get_click]: #mouse-get_click
[get_click]: #mouse-get_click

<div class="FunctionDoc YAMLDoc" id="mouse-get_pos" markdown="1">

## function __mouse\.get\_pos__\(\)

Returns the current position of the cursor.

__Example:__

~~~ .python
my_mouse = mouse()
(x, y), timestamp = my_mouse.get_pos()
print('The cursor was at (%d, %d)' % (x, y))
~~~

__Returns:__

A (position, timestamp) tuple.

- Type: tuple

</div>

[mouse.get_pos]: #mouse-get_pos
[get_pos]: #mouse-get_pos

<div class="FunctionDoc YAMLDoc" id="mouse-get_pressed" markdown="1">

## function __mouse\.get\_pressed__\(\)

Returns the current state of the mouse buttons. A True value means the button is currently being pressed.

__Example:__

~~~ .python
my_mouse = mouse()
buttons = my_mouse.get_pressed()
b1, b2, b3 = buttons
print('Currently pressed mouse buttons: (%d,%d,%d)' % (b1,b2,b3))
~~~

__Returns:__

A (button1, button2, button3) tuple of boolean values.

- Type: tuple.

</div>

[mouse.get_pressed]: #mouse-get_pressed
[get_pressed]: #mouse-get_pressed

<div class="FunctionDoc YAMLDoc" id="mouse-set_pos" markdown="1">

## function __mouse\.set\_pos__\(pos=\(0, 0\)\)

Sets the position of the mouse cursor.

__Warning:__ `set_pos()` is unreliable and will silently fail on
some systems.

__Example:__

~~~ .python
my_mouse = mouse()
my_mouse.set_pos(pos=(0,0))
~~~

__Keywords:__

- `pos` -- An (x,y) tuple for the new mouse coordinates.
	- Type: tuple
	- Default: (0, 0)

</div>

[mouse.set_pos]: #mouse-set_pos
[set_pos]: #mouse-set_pos

<div class="FunctionDoc YAMLDoc" id="mouse-show_cursor" markdown="1">

## function __mouse\.show\_cursor__\(show=True\)

Immediately changes the visibility of the mouse cursor.

__Note:__ In most cases, you will want to use the `visible`
[keyword][Response keywords], which changes the visibility during
response collection, that is, while `mouse.get_click()` is called.

__Keywords:__

- `show` -- Indicates whether the cursor is shown (True) or hidden (False).
	- Type: bool
	- Default: True

</div>

[mouse.show_cursor]: #mouse-show_cursor
[show_cursor]: #mouse-show_cursor

</div>

[mouse]: #mouse

