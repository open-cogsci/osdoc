<div class="ClassDoc YAMLDoc" id="Mouse" markdown="1">

# class __Mouse__

The `Mouse` class is used to collect mouse input. You generally create a
`Mouse` object with the `Mouse()` factory function, as described in the
section [Creating a Mouse](#creating-a-mouse).

__Example:__

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

Optionally, you can pass [Response keywords](#response-keywords) to
`Mouse()` to set the default behavior:

~~~ .python
my_mouse = Mouse(timeout=2000)
~~~

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
  to `None` accept all buttons.
- `visible` indicates whether the mouse cursor becomes visible when a
  click is collected (`True` or `False`). To immediately change cursor
  visibility, use `Mouse.show_cursor()`.

~~~ .python
# Get a left or right button press with a timeout of 3000 ms
my_mouse = Mouse()
button, time = my_mouse.get_click(buttonlist=[1,3], timeout=3000)
~~~

Response keywords only affect the current operation (except when passed
to `Mouse()` when creating the object). To change the behavior for all
subsequent operations, set the response properties directly:

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

<div class="FunctionDoc YAMLDoc" id="Mouse-flush" markdown="1">

## function __Mouse\.flush__\(\)

Clears all pending input, not limited to the mouse.

__Example:__

~~~ .python
my_mouse = Mouse()
my_mouse.flush()
button, position, timestamp = my_mouse.get_click()
~~~

__Returns:__

True if a button had been clicked (i.e., if there was something to flush) and False otherwise.

- Type: bool

</div>

<div class="FunctionDoc YAMLDoc" id="Mouse-get_click" markdown="1">

## function __Mouse\.get\_click__\(\*\*resp\_args\)

Collects a mouse click.

__Example:__

~~~ .python
my_mouse = Mouse()
button, (x, y), timestamp = my_mouse.get_click(timeout=5000)
if button is None:
        print('A timeout occurred!')
~~~

__Keyword dict:__

- `**resp_args`: Optional [response keywords](#response-keywords) that will be used for this call to `Mouse.get_click()`. This does not affect subsequent operations.

__Returns:__

A (button, position, timestamp) tuple. The button and position are `None` if a timeout occurs. Position is an (x, y) tuple in screen coordinates.

- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="Mouse-get_click_release" markdown="1">

## function __Mouse\.get\_click\_release__\(\*\*resp\_args\)

*New in v3.2.0*

Collects a mouse-click release.

*Important:* This function is currently not implemented for the
*psycho* backend.

__Example:__

~~~ .python
my_mouse = Mouse()
button, (x, y), timestamp = my_mouse.get_click_release(timeout=5000)
if button is None:
        print('A timeout occurred!')
~~~

__Keyword dict:__

- `**resp_args`: Optional [response keywords](#response-keywords) that will be used for this call to `Mouse.get_click_release()`. This does not affect subsequent operations.

__Returns:__

A (button, position, timestamp) tuple. The button and position are `None` if a timeout occurs. Position is an (x, y) tuple in screen coordinates.

- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="Mouse-get_pos" markdown="1">

## function __Mouse\.get\_pos__\(\)

Returns the current position of the cursor.

__Example:__

~~~ .python
my_mouse = Mouse()
(x, y), timestamp = my_mouse.get_pos()
print('The cursor was at (%d, %d)' % (x, y))
~~~

__Returns:__

A (position, timestamp) tuple.

- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="Mouse-get_pressed" markdown="1">

## function __Mouse\.get\_pressed__\(\)

Returns the current state of the mouse buttons. A True value means the button is currently being pressed.

__Example:__

~~~ .python
my_mouse = Mouse()
buttons = my_mouse.get_pressed()
b1, b2, b3 = buttons
print('Currently pressed mouse buttons: (%d,%d,%d)' % (b1,b2,b3))
~~~

__Returns:__

A (button1, button2, button3) tuple of boolean values.

- Type: tuple.

</div>

<div class="FunctionDoc YAMLDoc" id="Mouse-set_pos" markdown="1">

## function __Mouse\.set\_pos__\(pos=\(0, 0\)\)

Sets the position of the mouse cursor.

__Warning:__ `set_pos()` is unreliable and will silently fail on
some systems.

__Example:__

~~~ .python
my_mouse = Mouse()
my_mouse.set_pos(pos=(0,0))
~~~

__Keywords:__

- `pos` -- An (x,y) tuple for the new mouse coordinates.
	- Type: tuple
	- Default: (0, 0)

</div>

<div class="FunctionDoc YAMLDoc" id="Mouse-show_cursor" markdown="1">

## function __Mouse\.show\_cursor__\(show=True\)

Immediately changes the visibility of the mouse cursor.

__Note:__ In most cases, you will want to use the `visible`
keyword, which changes the visibility during response collection,
that is, while `mouse.get_click()` is called. Calling 
`show_cursor()` will not implicitly change the value of `visible`, 
which can lead to the somewhat unintuitive behavior that the cursor
is hidden as soon as `get_click()` is called.

__Keywords:__

- `show` -- Indicates whether the cursor is shown (True) or hidden (False).
	- Type: bool
	- Default: True

</div>

</div>

