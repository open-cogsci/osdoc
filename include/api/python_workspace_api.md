<div class=" YAMLDoc" id="" markdown="1">

 

<div class="FunctionDoc YAMLDoc" id="Canvas" markdown="1">

## function __Canvas__\(auto\_prepare=True, \*\*style\_args\)

A factory function that creates a new `Canvas` object. For a
description of possible keywords, see:

- %link:manual/python/canvas%

__Example:__

~~~ .python
my_canvas = Canvas(color=u'red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

__Keywords:__

- `auto_prepare` -- No description
	- Default: True

__Keyword dict:__

- `**style_args`: No description.

__Returns:__

A `Canvas` object.

- Type: canvas

</div>

<div class="FunctionDoc YAMLDoc" id="Form" markdown="1">

## function __Form__\(\*args, \*\*kwargs\)

A factory function that creates a new `Form` object. For a
description of possible keywords, see:

- %link:manual/forms/widgets%

__Example:__

~~~ .python
form = Form()
label = Label(text='label')
button = Button(text='Ok')
form.set_widget(label, (0,0))
form.set_widget(button, (0,1))
form._exec()
~~~

__Argument list:__

- `*args`: No description.

__Keyword dict:__

- `**kwargs`: No description.

__Returns:__

A `Form` object.

- Type: canvas

</div>

<div class="FunctionDoc YAMLDoc" id="Keyboard" markdown="1">

## function __Keyboard__\(\*\*resp\_args\)

A factory function that creates a new `Keyboard` object. For a
description of possible keywords, see:

- %link:manual/python/keyboard%

__Example:__

~~~ .python
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key, time = my_keyboard.get_key()
~~~

__Keyword dict:__

- `**resp_args`: No description.

__Returns:__

A `Keyboard` object.

- Type: keyboard

</div>

<div class="FunctionDoc YAMLDoc" id="Mouse" markdown="1">

## function __Mouse__\(\*\*resp\_args\)

A factory function that creates a new `Mouse` object. For a
description of possible keywords, see:

- %link:manual/python/mouse%

__Example:__

~~~ .python
my_mouse = Mouse(keylist=[1,3], timeout=5000)
button, time = my_mouse.get_button()
~~~

__Keyword dict:__

- `**resp_args`: No description.

__Returns:__

A `mouse` object.

- Type: mouse

</div>

<div class="FunctionDoc YAMLDoc" id="Sampler" markdown="1">

## function __Sampler__\(src, \*\*playback\_args\)

A factory function that creates a new `Sampler` object. For a
description of possible keywords, see:

- %link:manual/python/sampler%

__Example:__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~

__Arguments:__

- `src` -- No description

__Keyword dict:__

- `**playback_args`: No description.

__Returns:__

A SAMPLER object.

- Type: sampler

</div>

<div class="FunctionDoc YAMLDoc" id="Synth" markdown="1">

## function __Synth__\(osc=u'sine', freq=440, length=100, attack=0, decay=5\)

A factory function that synthesizes a sound and returns it as a `Sampler` object.

__Example:__

~~~ .python
my_sampler = Synth(freq=u'b2', length=500)
~~~

__Keywords:__

- `osc` -- Oscillator, can be "sine", "saw", "square" or "white_noise".
	- Type: str, unicode
	- Default: 'sine'
- `freq` -- Frequency, either an integer value (value in hertz) or a string ("A1", "eb2", etc.).
	- Type: str, unicode, int, float
	- Default: 440
- `length` -- The length of the sound in milliseconds.
	- Type: int, float
	- Default: 100
- `attack` -- The attack (fade-in) time in milliseconds.
	- Type: int, float
	- Default: 0
- `decay` -- The decay (fade-out) time in milliseconds.
	- Type: int, float
	- Default: 5

__Returns:__

A SAMPLER object.

- Type: sampler

</div>

<div class="FunctionDoc YAMLDoc" id="copy_sketchpad" markdown="1">

## function __copy\_sketchpad__\(name\)

Returns a copy of a `sketchpad`'s canvas.

__Example:__

~~~ .python
my_canvas = copy_sketchpad('my_sketchpad')
my_canvas.show()
~~~

__Arguments:__

- `name` -- The name of the `sketchpad`.
	- Type: str, unicode

__Returns:__

A copy of the `sketchpad`'s canvas.

- Type: canvas

</div>

<div class="FunctionDoc YAMLDoc" id="pause" markdown="1">

## function __pause__\(\)

Pauses the experiment.

</div>

<div class="FunctionDoc YAMLDoc" id="register_cleanup_function" markdown="1">

## function __register\_cleanup\_function__\(fnc\)

Registers a clean-up function, which is executed when the experiment ends. Clean-up functions are executed at the very end, after the display, sound device, and log file have been closed. Clean-up functions are also executed when the experiment crashes.

__Example:__

~~~ .python
def my_cleanup_function():
        print(u'The experiment is finished!')
register_cleanup_function(my_cleanup_function)
~~~

__Arguments:__

- `fnc` -- No description

</div>

<div class="FunctionDoc YAMLDoc" id="reset_feedback" markdown="1">

## function __reset\_feedback__\(\)

Resets all feedback variables to their initial state.

__Example:__

~~~ .python
reset_feedback()
~~~

</div>

<div class="FunctionDoc YAMLDoc" id="set_subject_nr" markdown="1">

## function __set\_subject\_nr__\(nr\)

Sets the subject number and parity (even/ odd). This function is called automatically when an experiment is started, so you only need to call it yourself if you overwrite the subject number that was specified when the experiment was launched.

__Example:__

~~~ .python
set_subject_nr(1)
print('Subject nr = %d' % var.subject_nr)
print('Subject parity = %s' % var.subject_parity)
~~~

__Arguments:__

- `nr` -- The subject nr.
	- Type: int

</div>

<div class="FunctionDoc YAMLDoc" id="sometimes" markdown="1">

## function __sometimes__\(p=0\.5\)

Returns True with a certain probability. (For more advanced
randomization, use the Python `random` module.)

__Example:__

~~~ .python
if sometimes():
        print('Sometimes you win')
else:
        print('Sometimes you loose')
~~~

__Keywords:__

- `p` -- The probability of returning True.
	- Type: float
	- Default: 0.5

__Returns:__

True or False

- Type: bool

</div>

<div class="FunctionDoc YAMLDoc" id="xy_circle" markdown="1">

## function __xy\_circle__\(n, rho, phi0=0, pole=\(0, 0\)\)

Generates a list of points (x,y coordinates) in a circle. This can be used to draw stimuli in a circular arrangement.

__Example:__

~~~ .python
# Draw 8 rectangles around a central fixation dot
c = Canvas()
c.fixdot()
for x, y in xy_circle(8, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~

__Arguments:__

- `n` -- The number of x,y coordinates to generate.
	- Type: int
- `rho` -- The radial coordinate, also distance or eccentricity, of the first point.
	- Type: float

__Keywords:__

- `phi0` -- The angular coordinate for the first coordinate. This is a counterclockwise rotation in degrees (i.e. not radians), where 0 is straight right.
	- Type: float
	- Default: 0
- `pole` -- The refence point.
	- Type: tuple
	- Default: (0, 0)

__Returns:__

A list of (x,y) coordinate tuples.

- Type: list

</div>

<div class="FunctionDoc YAMLDoc" id="xy_distance" markdown="1">

## function __xy\_distance__\(x1, y1, x2, y2\)

Gives the distance between two points.

__Arguments:__

- `x1` -- The x coordinate of the first point.
	- Type: float
- `y1` -- The y coordinate of the first point.
	- Type: float
- `x2` -- The x coordinate of the second point.
	- Type: float
- `y2` -- The y coordinate of the second point.
	- Type: float

__Returns:__

The distance between the two points.

- Type: float

</div>

<div class="FunctionDoc YAMLDoc" id="xy_from_polar" markdown="1">

## function __xy\_from\_polar__\(rho, phi, pole=\(0, 0\)\)

Converts polar coordinates (distance, angle) to Cartesian coordinates (x, y).

__Example:__

~~~ .python
# Draw a cross
x1, y1 = xy_from_polar(100, 45)
x2, y2 = xy_from_polar(100, -45)
c = Canvas()
c.line(x1, y1, -x1, -y1)
c.line(x2, y2, -x2, -y2)
c.show()
~~~

__Arguments:__

- `rho` -- The radial coordinate, also distance or eccentricity.
	- Type: float
- `phi` -- The angular coordinate. This reflects a clockwise rotation in degrees (i.e. not radians), where 0 is straight right.
	- Type: float

__Keywords:__

- `pole` -- The refence point.
	- Type: tuple
	- Default: (0, 0)

__Returns:__

An (x, y) coordinate tuple.

- Type: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="xy_grid" markdown="1">

## function __xy\_grid__\(n, spacing, pole=\(0, 0\)\)

Generates a list of points (x,y coordinates) in a grid. This can be used to draw stimuli in a grid arrangement.

__Example:__

~~~ .python
# Draw a 4x4 grid of rectangles
c = Canvas()
c.fixdot()
for x, y in xy_grid(4, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~

__Arguments:__

- `n` -- An `int` that indicates the number of columns and rows, so that `n=2` indicates a 2x2 grid, or a (n_col, n_row) `tuple`, so that `n=(2,3)` indicates a 2x3 grid.
	- Type: int, tuple
- `spacing` -- A numeric value that indicates the spacing between cells, or a (col_spacing, row_spacing) tuple.
	- Type: float

__Keywords:__

- `pole` -- The refence point.
	- Type: tuple
	- Default: (0, 0)

__Returns:__

A list of (x,y) coordinate tuples.

- Type: list

</div>

<div class="FunctionDoc YAMLDoc" id="xy_random" markdown="1">

## function __xy\_random__\(n, width, height, min\_dist=0, pole=\(0, 0\)\)

Generates a list of random points (x,y coordinates) with a minimum spacing between each pair of points. This function will raise an `osexception` when the coordinate list cannot be generated, typically because there are too many points, the min_dist is set too high, or the width or height are set too low.

__Example:__

~~~ .python
# Draw a 50 rectangles in a random grid
c = Canvas()
c.fixdot()
for x, y in xy_random(50, 500, 500, min_dist=40):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~

__Arguments:__

- `n` -- The number of points to generate.
	- Type: int
- `width` -- The width of the field with random points.
	- Type: float
- `height` -- The height of the field with random points.
	- Type: float

__Keywords:__

- `min_dist` -- The minimum distance between each point.
	- Type: float
	- Default: 0
- `pole` -- The refence point.
	- Type: tuple
	- Default: (0, 0)

__Returns:__

A list of (x,y) coordinate tuples.

- Type: list

</div>

<div class="FunctionDoc YAMLDoc" id="xy_to_polar" markdown="1">

## function __xy\_to\_polar__\(x, y, pole=\(0, 0\)\)

Converts Cartesian coordinates (x, y) to polar coordinates (distance, angle).

__Example:__

~~~ .python
rho, phi = xy_to_polar(100, 100)
~~~

__Arguments:__

- `x` -- The X coordinate.
	- Type: float
- `y` -- The Y coordinate.
	- Type: float

__Keywords:__

- `pole` -- The refence point.
	- Type: tuple
	- Default: (0, 0)

__Returns:__

An (rho, phi) coordinate tuple. Here, `rho` is the radial coordinate, also distance or eccentricity. `phi` is the angular coordinate in degrees (i.e. not radians), and reflects a counterclockwise rotation, where 0 is straight right.

- Type: tuple

</div>

</div>

